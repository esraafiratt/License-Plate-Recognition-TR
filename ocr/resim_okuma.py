import cv2
import easyocr
from ultralytics import YOLO

# Modelleri yükle
plate_model = YOLO("/Users/esranurfirat/PycharmProjects/12mart_sunum/plaka_tespit.pt")
char_model = YOLO("/Users/esranurfirat/PycharmProjects/12mart_sunum/karakter_okuma.pt")
ocr_reader = easyocr.Reader(['tr'])

# Görüntüyü yükle
image_path = "/Users/esranurfirat/PycharmProjects/12mart_sunum/110000434058310.jpg"
image = cv2.imread(image_path)

# Plaka tespiti
plate_results = plate_model.predict(source=image, conf=0.5)

for r in plate_results:
    for box in r.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        plate_crop = image[y1:y2, x1:x2]

        # Karakter modeli opsiyonel
        char_results = char_model.predict(source=plate_crop, conf=0.5)

        # OCR ile oku
        plate_text_raw = ocr_reader.readtext(plate_crop, detail=0)

        # Hepsi birleştirilsin (listeyi metne çevir)
        full_text = " ".join(plate_text_raw).upper()

        # "06" gibi şehir koduyla başlayan kısmı bul
        import re
        match = re.search(r'\b\d{2}\s?[A-Z]{1,3}\s?\d{2,4}\b', full_text)
        if match:
            filtered_plate = match.group(0)
        else:
            filtered_plate = full_text  # Yine de bir şey göster

        # Ekrana yaz
        print(f"📌 Tespit Edilen Plaka Numarası: {filtered_plate}")

        # Görüntü üzerine yaz
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, filtered_plate, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

# Göster
cv2.imshow("Plate Detection & OCR", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
