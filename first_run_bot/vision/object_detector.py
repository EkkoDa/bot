import cv2
import numpy as np
import os

class ObjectDetector:
    def __init__(self, assets_dir, threshold=0.7):
        self.assets_dir = assets_dir
        self.templates = {}
        self.threshold = threshold

        self._load_templates()

    def _load_templates(self):
        for filename in os.listdir(self.assets_dir):
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                key = os.path.splitext(filename)[0]
                path = os.path.join(self.assets_dir, filename)
                self.templates[key] = cv2.imread(path, cv2.IMREAD_UNCHANGED)

    def detect(self, image_path):
        image = cv2.imread(image_path)
        result_img = image.copy()

        for name, template in self.templates.items():
            if template is None:
                continue

            h, w = template.shape[:2]
            res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
            loc = np.where(res >= self.threshold)

            for pt in zip(*loc[::-1]):
                cv2.rectangle(result_img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
                cv2.putText(result_img, name, (pt[0], pt[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        return result_img