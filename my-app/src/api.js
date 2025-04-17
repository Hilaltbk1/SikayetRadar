import axios from 'axios';



const API_URL = 'http://localhost:8000';

export const createUser = async (userData) => {
  try {
    const response = await axios.post(`${API_URL}/users/users/users/`, userData);
    return response.data;
  } catch (error) {
    console.error('Error creating user:', error.response?.data || error.message);
    throw error;
  }
};

export const getUser = async (userId) => {
  try {
    const response = await axios.get(`${API_URL}/users/users/users/${userId}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching user:', error.response?.data || error.message);
    throw error;
  }
};

export const getAllUsers = async () => {
  try {
    const response = await axios.get(`${API_URL}/users/users/allusers/`);
    return response.data;
  } catch (error) {
    console.error('Error fetching users:', error.response?.data || error.message);
    throw error;
  }
};

export const updateUser = async (userId, userData) => {
  try {
    const response = await axios.put(`${API_URL}/users/users/update_user/${userId}`, userData);
    return response.data;
  } catch (error) {
    console.error('Error updating user:', error.response?.data || error.message);
    throw error;
  }
};

export const deleteUser = async (userId) => {
  try {
    const response = await axios.delete(`${API_URL}/users/users/delete_user/${userId}`);
    return response.data;
  } catch (error) {
    console.error('Error deleting user:', error.response?.data || error.message);
    throw error;
  }
};

export const createPost = async (userId,content) => {
  if (!userId || !content) {
    throw new Error("userId ve content gereklidir.");
  }

 try {
    // Burada params kullanarak user_id'yi query string olarak gönderiyoruz
      const response = await axios.post(`${API_URL}/posts/posts/create_post/${userId}`, {
            post: content  // content'i post olarak gönderiyoruz
        });
    return response.data;
  } catch (error) {
    console.error('Error creating post:', error.response?.data || error.message);
    throw error;
  }
};

export const updatePost = async (postId,content) =>{
  try{
    const response = await axios.put(`${API_URL}/posts/update_post/${postId}`,{
      post: content
    });
    return response.data;
  }catch (error){
    console.error('Error updating post:', error.response?.data || error.message);
    throw error;
  }
};

export const deletePost = async (postId) => {
  try {
    const response = await axios.delete(`${API_URL}/posts/delete_post/${postId}`);
    return response.data;
  } catch (error) {
    console.error('Error deleting post:', error);
    throw error;
  }
};
export const getAllPosts = async () => {
  try{
    const response = await axios.get(`${API_URL}/posts/posts/allposts/`);
    return response.data;
  }catch(error){
    console.log("error");
    throw error;
  }
};

export const getPost = async (postId) => {
  try{
    const response = await axios.get(`${API_URL}/posts/posts/${postId}`);
    return response.data;
  }catch(error){
    console.error('Error  post:', error.response?.data || error.message);
    throw error;
  }
}
export const getPredict = async (postId) => {
  try{
    const response = await axios.get(`${API_URL}/posts/posts/post_predict/${postId}`);
    return response.data.prediction;
  } catch (error){
    console.error('Error :', error.response?.data || error.message);
    throw error;
  }
}
