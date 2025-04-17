# Şikayet Radar
 ### Projenin amacı, kullanıcıların yazdığı metinleri analiz ederek bunların şikayet içerip içermediğini otomatik olarak tespit etmektir. Bu sayede platform sahipleri ya da müşteri hizmetleri ekipleri, şikayet içerikli geri bildirimleri hızlıca ayıklayıp önceliklendirebilir.
### Model eğitimi için Trendyol’dan çektiğim veriler kullanılmış ve bu veriler "şikayet" ve "şikayet değil" olarak etiketlenmiştir. Bu sınıflandırma modeli, BERT mimarisi ile eğitilmiş ve FastAPI + React mimarisiyle servis edilmiştir.Kullanıcı ve gönderi bilgileri SQL tabanlı veritabanında tutulmakta, API üzerinden bu verilere erişim sağlanmaktadır.
---
### Özellikler
- 🔍 BERT ile metin sınıflandırma
- 🔄 Trendyol’dan veri çekme (web scraping)
- 🗃️ SQL veritabanı (kullanıcı & post modeli)
- ⚙️ FastAPI ile REST API
- 🌐 React ile görsel arayüz
---
### Backand Mimarisi
```log
├── controller/
│   ├── controller.py
│   ├── error.log
├── models/
│   ├── __init__/
│   └── Post.py
|   └── User.py
├── my-app/
│   ├── node_modules
│   └── public/
|   └── src
├── routers/
│   └── main.py
|   └── posts_router.py
|   └── users_router.py
|   └──test_main.py
├── myenv
└──database.py
```
---
### Kullanılan Teknolojiler
-`Python`: Model eğitimi, veri işleme ve backend geliştirme dili

-`BERT` :Şikayet/sikayet değil sınıflandırması için kullanılan transformer tabanlı dil modeli

-`Hugging Face Transformers`:BERT modelini fine-tune etmek ve kullanmak için

-`Trendyol Web Scraping`: Eğitim verilerini çekmek için kullanılan veri toplama yöntemi

-`SQL`: Kullanıcı ve post verilerini saklamak için kullanılan ilişkisel veritabanı

-`ORM` : Veritabanı işlemleri için

-`FastAPI`: RESTful API oluşturmak için modern ve hızlı Python framework

-`Uvicorn `:FastAPI uygulamasını çalıştırmak için ASGI server

-`React`: Web arayüzü geliştirme kütüphanesi

-`Axios`: React’ten API’ye veri alışverişi için HTTP istemcisi

---
### ⚙️ Kurulum
-`1.Projeyi Klonlayın`:
```bash
git clone https://github.com/Hilaltbk1/SikayetRadar.git
cd SikayetRadar
```
-`2.Sanal Ortam Oluşturun`:
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```
-`3.Gerekli Python Paketleri Kurun`:
```bash
pip install -r requirements.txt
```
-`4.Hugging Face Modelini İndirin`:
```bash
from transformers import BertForSequenceClassification

model = BertForSequenceClassification.from_pretrained("Hilaltbk1/bert_projeleri")
```
Eğer bir token gerekiyorsa Hugging Face hesabınızdan erişim anahtarınızı alıp terminalde şu şekilde tanımlayabilirsiniz:
```bash
export HUGGINGFACE_TOKEN=your_token_here  # Mac/Linux
set HUGGINGFACE_TOKEN=your_token_here     # Windows
```
-`5.Veritabanı Oluşturun`:
```bash
database..py
```
-`6.FastAPI Sunucusu Başlatın`:
```bash
uvicorn routers.main:app --reload
```
-`7.React Arayüzünü Başlatın`:
```bash
cd my-app
npm install
npm start
```
Arayüz şu adresten çalışır: **http://localhost:30000**
---
## 🧠 Model Eğitimi
Bu projede, kullanıcı gönderilerini "şikayet" ve "şikayet değil" olarak sınıflandırmak amacıyla BERT tabanlı bir dil modeli fine-tuning edilmiştir.
### Veri Seti
Veri Seti:Trendyol platformundan scraping yöntemiyle toplanmıstır.Veri setine ulaşmak için: ** https://huggingface.co/datasets/nanelimon/complaint-classification-dataset**
Her gönderi manuel olarak 0 veya 1 etiketiyle işaretlenmistir
Toplam Örnek Sayısı:6914
Veriler text ve label olmak üzere iki kolondan oluşmaktadır.
### Model Eğitimi
Kullanılan Tokenizer:dbmdz/bert-base-turkish-cased
HiperParametreler:
Max token length:142
Batch size:32
Epoch:15
Optimizer:AdamW
Eğitim boyunca train ve loss takip edilmiştir
Model tamamlandıktan sonra .p uzantısıyla kaydedilmiştir.
### Model Kaydı ve Kullanımı
Eğitilen model Hugging Face'e manuel olarak yüklenmiştir
Ulaşmak için : **https://huggingface.co/hilal1/my-awesome-bert**


