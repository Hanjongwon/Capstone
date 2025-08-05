# 🧪 ELISA 기반 객체 인식 진단 자동화 플랫폼

> Raspberry Pi 기반의 IP 카메라와 YOLOv5를 이용하여 ELISA 장비의 유체 상태를 자동으로 인식하고, 색상 분석 및 서보모터 제어를 통해 진단 과정을 자동화한 시스템입니다.

---

## 📌 프로젝트 개요

본 프로젝트는 ELISA 진단 장비의 시약 주입 및 반응 과정을 자동화하여 진단 정확도와 작업 효율성을 높이는 것을 목표로 합니다.  
YOLOv5 기반 객체 인식과 색상 기반 Hue 분석을 통해 챔버 내 유체 상태를 판별하고, 각 단계에 맞는 제어 시퀀스를 자동으로 실행합니다.

---

## 🛠️ 주요 기능

- ✅ **객체 인식 기반 챔버 상태 판별**  
  YOLOv5 모델을 통해 EMPTY, FILLED, ENTERING, LEAVING 등의 상태를 실시간 인식

- 🎨 **Hue 색상 분석을 통한 농도 추정**  
  인식된 챔버의 RGB 영역을 분석하여 평균 Hue 값을 계산 → 양성/음성 판정 및 정량 농도 예측

- 🔄 **자동 모터 제어 시퀀스 (Auto Mode)**  
  FSM 방식으로 단계별 모터 제어 (1단계 180초 → 2단계 2400초 → 3단계 600초)

- 💾 **진단 결과 DB 저장**  
  진단 결과(`id`, `name`, `location`, `concentration`, `result`)를 MySQL에 저장

- 🖥️ **PyQt5 기반 GUI**  
  4개 서버(IP 카메라) 관리, 영상 모니터링, 제어 및 저장 기능 제공

---

## ⚙️ 기술 스택

| 범주        | 사용 기술 |
|-------------|-----------|
| 언어        | Python 3.x |
| 영상처리    | OpenCV |
| 딥러닝      | PyTorch, YOLOv5 |
| GUI         | PyQt5 |
| DB 연동     | PyMySQL |
| 하드웨어 제어 | gpiozero, pigpio |
| 병렬 처리   | QThread (PyQt) |
| 기타        | argparse, pathlib, math 등 |

---
