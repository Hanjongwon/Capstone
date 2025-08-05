import cv2
import uuid
import glob
import os

# === 설정 ===
VIDEO_DIR = 'C:/Users/LK/Desktop/2022_kwix/2022_data_video/taewon-20220320T194508Z-001/taewon/empty_video'
OUTPUT_DIR = 'C:/Users/LK/Desktop/2022_kwix/2022_data_video/taewon-20220320T194508Z-001/taewon'
VIDEO_PATTERN = os.path.join(VIDEO_DIR, 'empty_1_taewon.mp4')

video_list = glob.glob(VIDEO_PATTERN)
frame_global_index = 0

for video_path in video_list:
    cap = cv2.VideoCapture(video_path)
    frame_local_index = 0

    while True:
        ret, frame = cap.read()
        frame_local_index += 1

        if not ret:
            cap.release()
            os.remove(video_path)
            print(f"[INFO] Removed corrupted video: {video_path}")
            break

        frame_global_index += 1
        if frame_local_index % 2 == 0:
            filename = f"{frame_global_index}_taewon_{uuid.uuid1()}.jpg"
            save_path = os.path.join(OUTPUT_DIR, filename)
            cv2.imwrite(save_path, frame)

    cap.release()

print("Finished processing all videos.")
