import React, { useState } from "react";
import axios from "axios";
import './App.css';
import {getAllUsers, createPost, updatePost, deletePost, getAllPosts} from './api.js';


const API_URL = "http://127.0.0.1:8000";  // Backend API URL'nizi buraya yazın

const App = () => {
    const [users, setUsers] = useState([]);
    const [userId, setUserId] = useState("");
    const [userIdToUpdate, setUserIdToUpdate] = useState("");
    const [userIdToDelete, setUserIdToDelete] = useState("");
    const [newUsername, setNewUsername] = useState("");
    const [newName, setNewName] = useState("");
    const [newPassword, setNewPassword] = useState("");
    const [userGetId, setUserGetId] = useState("");
     const [user, setUser] = useState({}); // user state'ini tanımladık
    const[selectedUserId, setSelectedUserId] = useState("");
    const [inputUserId, setInputUserId] = useState("");

    const[posts, setPosts] = useState([]);
      const [selectedPost, setSelectedPost] = useState(null);
    const[updatedContent, setUpdatedContent] = useState(null);
    const [content, setContent] = useState("");
     const[postGetId, setPostGetId] = useState("");
    const[postIdToUpdate, setPostIdToUpdate] = useState("");
    const[postIdToDelete, setPostIdToDelete] = useState("");
    const[postPredictId, setPostPredictId] = useState("");
    const[predict, setPredict] = useState(null);
    const[newPost, setNewPost] = useState(null);
    const[predictId, setPredictId] = useState("");



    // Kullanıcı oluşturma işlemi
    const handleCreateUser = async () => {
        const username = prompt("Kullanıcı Adınızı Girin:");
        const name = prompt("Adınızı Girin:");
        const password = prompt("Şifrenizi Girin:");

        if (!username || !name || !password) {
            alert("Tüm alanlar doldurulmalıdır.");
            return;
        }

        try {
            const response = await axios.post(`${API_URL}/users/users/users/`, {
                username,
                name,
                password
            });
            alert(`Kullanıcı oluşturuldu! ID: ${response.data.id}`);
        } catch (error) {
            console.error("Kullanıcı oluşturulurken hata oluştu:", error);
            alert("Kullanıcı oluşturulamadı!");
        }
    };
//CREATE POSTS
    const handleCreatePost = async () => {
        if (!userId  || !content) {
            alert("Kullanıcı ve post içeriği girilmelidir!");
            return;
        }
        try {
            const newPost = await createPost(userId, content);
            setPosts(prevPosts => Array.isArray(prevPosts) ? [...prevPosts, newPost] : [newPost]);  // Yeni postu state'e ekle
            setUsers(prevUsers =>
            prevUsers.map(user =>
                user.id === parseInt(userId) ? { ...user, posts: [...user.posts, newPost] } : user
                )
            );
            setContent("");  // Input alanını temizle
            alert("Gönderi başarıyla oluşturuldu!");
        } catch (error) {
            console.error("Gönderi oluşturulurken hata oluştu:", error);
            alert("Gönderi oluşturulamadı!");
        }
    };
//POST SİLME
const handleDeletePost = async () => {
    if (!postIdToDelete) {
        alert("Lütfen silmek istediğiniz post ID'sini girin!");
        return;
    }

    try {
        await axios.delete(`${API_URL}/posts/posts/delete_post/${postIdToDelete}`);

        // Post silindikten sonra posts state'ini güncelle
        setPosts(prevPosts => prevPosts.filter(post => post.id !== parseInt(postIdToDelete)));

        // Postu kullanıcıların posts listelerinden de çıkar
        setUsers(prevUsers =>
            prevUsers.map(user => ({
                ...user,
                posts: user.posts ? user.posts.filter(post => post.id !== parseInt(postIdToDelete)) : []
            }))
        );

        alert("Post başarıyla silindi!");
    } catch (error) {
        console.error("Post silinirken bir hata oluştu:", error);
        alert("Post silinemedi!");
    }
};
  const handleUpdatePost = async () => {
    if (!postIdToUpdate) {
        alert("Post ID'sini girin!");
        return;
    }
    const newPostContent = prompt("Lütfen yeni post içeriğini giriniz:");
    if (!newPostContent) {
        alert("Doldurmalısınız");
        return;
    }

    try {
        // Güncellenecek postu bul
        const postToUpdate = posts.find(post => post.id === parseInt(postIdToUpdate));

        if (!postToUpdate) {
            alert("Post bulunamadı!");
            return;
        }

        const response = await axios.put(`${API_URL}/posts/posts/update_post/${postIdToUpdate}`, {
            post: newPostContent,
            user_id: postToUpdate.user_id  // 🔥 Eksik olan user_id'yi ekledik
        });

        setPosts(prevPosts =>
            prevPosts.map(post =>
                post.id === parseInt(postIdToUpdate) ? response.data : post
            )
        );
        alert("Post başarıyla güncellendi!");
    } catch (error) {
        console.error("Post güncellenirken bir hata oluştu:", error);
        alert("Post güncellenemedi!");
    }
};
    const handleListPost = async () =>{
        try{
            const postData = await getAllPosts();
            setPosts(postData);
        }catch(error){
            console.log("Postlar listelenirken bir sorun oluştu")
            alert("Post alınamadı")
        }
    };



    // Kullanıcıyı güncelleme işlemi
    const handleUpdateUser = async () => {
        if (!userIdToUpdate) {
            alert("Lütfen güncellemek için kullanıcı ID'sini girin!");
            return;
        }

        const newUsername = prompt("Yeni kullanıcı adınızı giriniz");
        const newName = prompt("Yeni adınızı giriniz");
        const newPassword = prompt("Yeni şifrenizi giriniz");

        if (!newUsername || !newName || !newPassword) {
            alert("Tüm alanları doldurmalısınız.");
            return;
        }

        try {
            const response = await axios.put(`${API_URL}/users/users/update_user/${userIdToUpdate}`, {
                username: newUsername,
                name: newName,
                password: newPassword
            });
            setUsers(prevUsers =>
                prevUsers.map(user =>
                    user.id === parseInt(userIdToUpdate) ? response.data : user
                )
            );
                        alert("Kullanıcı güncellendi!");
        } catch (error) {
            console.error("Kullanıcı güncellenirken hata oluştu:", error);
            alert("Kullanıcı güncellenemedi!");
        }
    };
        // Kullanıcıları listeleme işlemi
    const handleListUser = async () => {
        try {
           const userData = await getAllUsers();
           setUsers(userData);

        } catch (error) {
            console.error("Kullanıcılar listelenirken hata oluştu:", error);
            alert("Kullanıcı listesi alınamadı!");
        }
    };

    // Kullanıcıyı silme işlemi
    const handleDeleteUser = async () => {
        if (!userIdToDelete) {
            alert("Lütfen silmek istediğiniz kullanıcı ID'sini girin!");
            return;
        }

        const confirmDelete = window.confirm(`Kullanıcı ID ${userIdToDelete} silinecek. Emin misiniz?`);
        if (!confirmDelete) return;

        try {
            await axios.delete(`${API_URL}/users/users/delete_user/${userIdToDelete}`);
            setUsers(prevUsers => prevUsers.filter(user => user.id !== parseInt(userIdToDelete)));
            alert("Kullanıcı başarıyla silindi!");
        } catch (error) {
            console.error("Kullanıcı silinirken hata oluştu:", error);
            alert("Kullanıcı silinemedi!");
        }
    };
    const handleGetUser = async () =>{
        if (!userGetId) {
            alert("Lütfen göruntulemek istediğiniz kullanıcı ID'sini girin!");
            return;
        }
        try{
            const response =await axios.get(`${API_URL}/users/users/users/${userGetId}`)
            setUser(response.data);
        } catch (error) {
            console.error("Kullanıcılar listelenirken hata oluştu:", error);
            alert("Kullanıcı  alınamadı!");
        }
    };
    const handleGetPost = async () => {
    if (!postGetId) {
        alert("Lütfen görmek istediğiniz postun ID'sini girin!");
        return;
    }
    try {
        const response = await axios.get(`${API_URL}/posts/posts/posts/${postGetId}`);
        console.log("Gelen post:", response.data); // Gelen veriyi kontrol et
        setSelectedPost(response.data);
    } catch (error) {
        console.log("Post görüntülenirken hata oluştu:", error);
        alert("Post alınamadı!");
    }
};



    const handlePredictPost = async () => {
      if (!postPredictId){
          alert("id girin")
          return;
      }
      try{
          const response = await axios.get(`${API_URL}/posts/posts/post_predict/${postPredictId}`);
          setPredict(response.data.prediction);
      }catch (error){
          console.log("hata");
          alert("alınamadı");
      }


    };



    return (
        <div className="main-container">
            {/* SOL BÖLÜM */}
            <div className="left-div">
                <div className="button-group">
                    <div className="action-container">
                        <button className="action-btn" onClick={handleCreateUser}>Kullanıcı Oluştur</button>
                    </div>
                    <div className="action-container">
                        <button className="action-btn" onClick={handleListUser}>Kullanıcıları Listele</button>
                    </div>
                    <div className="user-list">
                        <h3>Kullanıcılar:</h3>
                        <ul>
                            {users.map(user => (
                                <li key={user.id}>{user.username} - {user.name}</li>
                            ))}
                        </ul>
                    </div>
                    <div className="action-container">
                        <button className="action-btn" onClick={handleUpdateUser}>Kullanıcı Güncelle</button>
                        <input
                            type="number"
                            placeholder="Kullanıcı ID girin"
                            value={userIdToUpdate}
                            onChange={(e) => setUserIdToUpdate(e.target.value)}
                        />
                    </div>
                    <div className="action-container">
                        <button className="action-btn" onClick={handleDeleteUser}>Kullanıcı Sil</button>
                        <input type="number"
                               placeholder="Kullanıcı ID girin"
                               value={userIdToDelete}
                               onChange={(e) => setUserIdToDelete((e.target.value))}
                        />
                    </div>
                    <div className="action-container">
                        <button className="action-btn" onClick={handleGetUser}>Kullanıcıyı Görüntüle</button>
                        <input
                            type="number"
                            placeholder="Kullanıcı ID girin"
                            value={userGetId}
                            onChange={(e) => setUserGetId(e.target.value)}
                        />
                    </div>

                    <div className="user-details">
                        <h3>Kullanıcı Bilgisi:</h3>
                        <p>{user ? `${user.name} - ${user.username}` : ' '}</p>
                    </div>



                </div>
            </div>

            {/* SAĞ BÖLÜM */}
            <div className="right-div">
                <div className="button-group">
                    <div className="action-container">
                        <button className="action-btn" onClick={handleCreatePost}>Gönderi Oluştur</button>
                        <input
                            type="number"
                            placeholder="Kullanıcı ID girin"
                            value={userId}
                            onChange={(e) => setUserId(e.target.value)} // Kullanıcı ID'sini alıyoruz
                        />
                          <textarea
                        placeholder="Post içeriğini girin"
                        value={content}
                        onChange={(e) => setContent(e.target.value)}/>
                    </div>
                    <div className="action-container">
                        <button className="action-btn" onClick={handleListPost}>Postları Listele</button>
                    </div>

                    <div className="user-list">
                        <div className="post-list">
                            <h3>Postlar:</h3>
                            <ul>
                                {posts.length > 0 ? (
                                    posts.map(post => (
                                        <li key={post.id}>{post.post}</li>
                                    ))
                                ) : (
                                    <li></li>
                                )}
                            </ul>
                        </div>
                    </div>
                    <div className="action-container">
                        <button className="action-btn" onClick={handleUpdatePost}>Post Güncelle</button>
                        <input
                            type="number"
                            placeholder="Post ID girin"
                            value={postIdToUpdate}
                            onChange={(e) => setPostIdToUpdate(e.target.value)}
                        />
                    </div>
                    <div className="action-container">
                        <button className="action-btn" onClick={handleDeletePost}>Postu Sil</button>
                        <input type="number"
                               placeholder="Post ID girin"
                               value={postIdToDelete}
                               onChange={(e) => setPostIdToDelete(e.target.value)}
                        />
                    </div>
                    <div className="action-container">
                        <button className="action-btn" onClick={handleGetPost}>Postu Görüntüle</button>
                        <input type="number"
                               placeholder="Post ID girin"
                               value={postGetId}
                               onChange={(e) => setPostGetId(e.target.value)}
                        />
                    </div>
                    <div className="post-details">
                        <h3>Post Detayı:</h3>
                        <p>{selectedPost ? selectedPost.post : "Post bulunamadı"}</p>

                    </div>
                    <div className="action-container">
                    <button  className="action-btn" onClick={handlePredictPost}>Tahmin Et</button>
                        <input
                            type="number"
                            placeholder="Post ID girin"
                            value={postPredictId}
                            onChange={(e) => setPostPredictId(e.target.value)}
                        />

                    </div>
                    <div className="action-container" >
                        <button style={{width:"1000px" , height:"200px" ,backgroundColor:"lightgrey",fontSize:"50px",fontStyle:"bold"}}  >{predict !== null ? predict : "Tahmin Verisi Yok"}</button>
                    </div>

                </div>
            </div>
        </div>

    );
};


export default App;
