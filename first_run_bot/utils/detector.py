
import cv2
import numpy as np

# Цвета монет и препятствий можно откалибровать по примеру
COIN_COLOR_RANGE = ([120, 0, 120], [180, 60, 255])  # Пример для фиолетовых колец
OBSTACLE_COLOR_RANGE = ([30, 30, 30], [80, 80, 80])  # Пример для серых объектов (автобусы)

def detect_elements(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Монеты
    lower_coin = np.array(COIN_COLOR_RANGE[0], dtype=np.uint8)
    upper_coin = np.array(COIN_COLOR_RANGE[1], dtype=np.uint8)
    mask_coin = cv2.inRange(hsv, lower_coin, upper_coin)
    contours_coin, _ = cv2.findContours(mask_coin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    coins = [cv2.boundingRect(cnt) for cnt in contours_coin if cv2.contourArea(cnt) > 100]

    # Препятствия
    lower_obs = np.array(OBSTACLE_COLOR_RANGE[0], dtype=np.uint8)
    upper_obs = np.array(OBSTACLE_COLOR_RANGE[1], dtype=np.uint8)
    mask_obs = cv2.inRange(hsv, lower_obs, upper_obs)
    contours_obs, _ = cv2.findContours(mask_obs, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    obstacles = [cv2.boundingRect(cnt) for cnt in contours_obs if cv2.contourArea(cnt) > 200]

    return {"coins": coins, "obstacles": obstacles}
