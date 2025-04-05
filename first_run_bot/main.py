
import cv2
import numpy as np
from utils.detector import detect_elements
from utils.visualize import draw_detections

def main():
    image = cv2.imread("test_assets/frame1.jpg")
    if image is None:
        print("❌ Не удалось загрузить test_assets/frame1.jpg")
        return

    detections = detect_elements(image)
    image_with_boxes = draw_detections(image, detections)

    print(f"[INFO] Обнаружено: {len(detections['coins'])} монет, {len(detections['obstacles'])} препятствий")
    cv2.imshow("First Run Bot - Detection", image_with_boxes)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
