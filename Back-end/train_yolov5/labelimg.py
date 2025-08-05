import cv2
import glob
import os
import numpy as np

from time import sleep

# === 경로 설정 ===
BASE_PATH = r'C:/Users/LK/Desktop/test_entering'
CROP_PATH = r'C:/Users/LK/Desktop/circle_crop/'
IMAGE_PATH = os.path.join(BASE_PATH, '*.jpg')


def parse_image_name(path):
    """
    이미지 경로에서 파일 이름만 추출
    """
    return os.path.basename(path)


def save_image(original_path, image):
    """
    잘라낸 이미지 저장
    """
    image_name = parse_image_name(original_path)
    save_path = os.path.join(CROP_PATH, image_name)
    cv2.imwrite(save_path, image)
    print(f"[INFO] Saved cropped image: {save_path}")


def crop_image(path, param2):
    """
    원형을 감지하고, 감지된 원에 대해 일정 조건을 만족하면 해당 영역을 잘라 저장
    """
    if param2 > 100:
        print(f"[WARN] param2 > 100: Skipping {path}")
        return

    frame = cv2.imread(path)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(
        gray, 
        cv2.HOUGH_GRADIENT, 
        dp=1, 
        minDist=60,
        param1=40, 
        param2=param2, 
        minRadius=0, 
        maxRadius=0
    )

    if circles is None:
        return crop_image(path, param2 + 1)

    circles = np.uint16(np.around(circles))

    for circle in circles[0]:
        x, y, r = circle
        x1, x2 = max(0, x - r), min(gray.shape[1], x + r)
        y1, y2 = max(0, y - r), min(gray.shape[0], y + r)

        crop_frame = frame[y1:y2, x1:x2]

        if (crop_frame.shape[0] + crop_frame.shape[1]) <= 500:
            save_image(path, crop_frame)
            return  # 하나만 저장하고 종료


def main():
    image_paths = glob.glob(IMAGE_PATH)

    if not image_paths:
        print("[ERROR] No images found.")
        return

    for path in image_paths:
        crop_image(path, param2=1)


if __name__ == '__main__':
    main()