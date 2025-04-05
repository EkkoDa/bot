from vision.object_detector import ObjectDetector
import cv2
import os

# Пути к ассетам и скриншотам
assets_path = "first_run_bot/assets"
screenshots_path = "first_run_bot/screenshots"

# Инициализация детектора
detector = ObjectDetector(assets_path, threshold=0.75)

# Обработка всех скриншотов
for filename in os.listdir(screenshots_path):
    if filename.endswith((".png", ".jpg")):
        image_path = os.path.join(screenshots_path, filename)
        result = detector.detect(image_path)

        # Показываем результат
        cv2.imshow(f"Detection: {filename}", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()