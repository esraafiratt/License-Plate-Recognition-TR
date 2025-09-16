# Türk Plakaları Tanıma Sistemi (YOLOv8 + EasyOCR)

Bu proje, **YOLOv8** ile plaka tespiti ve **EasyOCR** ile karakter okuma (OCR) işlemlerini birleştirerek Türk plakalarının otomatik tanınmasını amaçlamaktadır.  

---

## Proje Amacı
- Araç plakalarının hızlı ve doğru şekilde tespit edilmesi  
- Karakterlerin OCR tabanlı okunması  
- Akıllı şehirler, güvenlik sistemleri ve trafik kontrolü için uygulanabilir bir çözüm sunmak  

---

## Kullanılan Teknolojiler
- **Programlama Dili:** Python  
- **Framework & Kütüphaneler:**  
  - YOLOv8 (Ultralytics)  
  - EasyOCR  
  - OpenCV  
  - PyTorch, TensorFlow, Keras  
  - Pandas, Numpy, Matplotlib, Seaborn  

---

##  Proje Yapısı
```
License-Plate-Recognition-TR/
│── Final_Report.docx
│── README.md
│── requirements.txt
│
├── plaka_tespit/
│ ├── plaka_tespit.ipynb
│ └── plaka_tanima.docx
│
├── karakter_okuma/
│ ├── karakter_tespiti.ipynb
│ └── bitirme_karaktertespiti.docx
│
└── ocr/
├── resim_okuma.py
├── videodan_okuma.py
├── Plaka Metni Tanıma Aşaması.docx
└── demo.jpg
```

---

##  Kurulum

1. Depoyu klonlayın:
   
```bash
git clone https://github.com/esraafiratt/License-Plate-Recognition-TR.git
cd License-Plate-Recognition-TR
```

2.Gerekli kütüphaneleri yükleyin:

```
pip install -r requirements.txt
```

3. Model ağırlıklarını indirin ve `ocr/` klasörüne yerleştirin:
   
- [Plaka Tespit Modeli (YOLOv8)](https://drive.google.com/file/d/1MarndN9XRqZAC9WdJjnasu1QkW9eLfLC/view?usp=share_link)  
- [Karakter Okuma Modeli (OCR)](https://drive.google.com/file/d/1x57K64kTtCipq4jiy7vaxiRc8UPsuiOI/view?usp=share_link)  

> Not: `.pt` dosyaları `requirements.txt` içinde değildir; lütfen bağlantılardan indirip `ocr/` klasörüne koyunuz.

## Kullanım

Görsel üzerinden plaka okuma:

```
python ocr/resim_okuma.py
```

Video üzerinden plaka okuma:

```
python ocr/videodan_okuma.py
```
