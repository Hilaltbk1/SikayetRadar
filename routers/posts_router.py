import os
from fastapi import APIRouter
import torch
from transformers import BertForSequenceClassification, BertTokenizer

from controller.controller import get_all_posts, get_a_post, create_post, update_post, delete_post
from models import Post

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.get('/allposts/')
async def all_posts():
    return await get_all_posts()

@router.get('/posts/{post_id}')
async def get_post_by_id(post_id: int):
    return await get_a_post(post_id)

@router.post('/create_post/{post_id}', response_model=Post)
async def create_post_endpoint(post: Post, user_id: int):
    return await create_post(post, user_id)

@router.put("/update_post/{post_id}", response_model=Post)
async def update_post_endpoint(post_id: int, post: Post):
    return await update_post(post_id, post)

@router.delete('/delete_post/{post_id}')
async def delete_user_endpoint(post_id: int):
    return await delete_post(post_id)



model_save_path = r"D:\fastApiProject\bert_model"

import os

model_save_path = r"D:\fastApiProject\bert_model"
print(f"Model save path: {model_save_path}")

if os.path.exists(model_save_path):
    try:
        with open(model_save_path, 'r') as file:
            print("Dosya erişilebilir ve okuma işlemi başarılı.")
    except PermissionError:
        print("Bu dosyaya okuma izniniz yok.")
else:
    print("Dosya mevcut değil.")




tokenizer = BertTokenizer.from_pretrained(model_save_path)
model = BertForSequenceClassification.from_pretrained(model_save_path)





device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

def infer_text(text):
    encoded_dict = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=142,
        padding='max_length',
        truncation=True,
        return_attention_mask=True,
        return_tensors='pt',
    )
    input_ids = encoded_dict['input_ids'].to(device)
    attention_mask = encoded_dict['attention_mask'].to(device)

    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)

    logits = outputs.logits
    prediction = torch.argmax(logits, dim=1).item()

    if prediction == 1:
        return "Şikayet"
    else:
        return "Şikayet değil"


@router.get('/post_predict/{post_id}')
async def predict(post_id: int):
    # Belirtilen post_id'ye göre gönderiyi al
    post = await get_a_post(post_id)  # get_a_post işlevi post'ları almak için
    if post is None:
        return {"error": "Gönderi bulunamadı."}

    text = post.post # Model içindeki Text alanını kullan

    # Tahmin yap
    prediction = infer_text(text)

    return {'prediction': prediction}

