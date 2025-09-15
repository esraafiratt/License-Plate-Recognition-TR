import cv2
import easyocr
from ultralytics import YOLO

# YOLO Modellerini Yükle
plate_model = YOLO("/Users/esranurfirat/PycharmProjects/12mart_sunum/plaka_tespit.pt")
char_model = YOLO("/Users/esranurfirat/PycharmProjects/12mart_sunum/karakter_okuma.pt")
ocr_reader = easyocr.Reader(['en'])

# Video aç (0 -> Webcam veya "video.mp4" -> Video dosyası)
cap = cv2.VideoCapture("/Users/esranurfirat/PycharmProjects/12mart_sunum/demo.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO ile plaka tespiti yap
    plate_results = plate_model.predict(source=frame, conf=0.5)

    for r in plate_results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Plaka koordinatları
            plate_crop = frame[y1:y2, x1:x2]  # Plaka bölgesini kırp

            # OCR ile plakayı oku
            plate_text = ocr_reader.readtext(plate_crop, detail=0)

            # Sonucu ekrana yazdır
            print(f"📌 Tespit Edilen Plaka Numarası: {' '.join(plate_text)}")

            # Görüntü üzerine yazdır
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, " ".join(plate_text), (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Sonucu göster
    cv2.imshow("Plate Detection & OCR", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
