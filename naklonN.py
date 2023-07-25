#наклоны
import cv2
import mediapipe as mp
import numpy as np
import keyboard
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
cap = cv2.VideoCapture(1)  #импорт видеопотока
counter = 0  #счётчик
stage = None  #состояние сгибания (нейтральное)

def calculate_angle(a, b, c):
    a = np.array(a)  #начало
    b = np.array(b)  #вершина угла
    c = np.array(c)  #конец
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])  #вычисление угла в радианах
    angle = np.abs(radians * 180.0 / np.pi)  #перевод угла в градусы
    if angle > 180.0:
        angle = 360 - angle
    return angle

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:  #объявление переменной pose как скелетной модели с точностью обнаружения 0.5
    while cap.isOpened(): #пока камера открыта
        ret, frame = cap.read() #считывание кадров с камеры
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  #перевод изображений в RGB
        image.flags.writeable = False  #не сохраняем изображения
        results = pose.process(image)  #массив результатов
        image.flags.writeable = True  #сохраняем изображения
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  #перевод изображений в BGR
        try:
            landmarks = results.pose_landmarks.landmark #опорные точки (суставы)
            left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP].y]  #бедро
            right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP].x, landmarks[mp_pose.PoseLandmark.RIGHT_HIP].y]  #бедро
            left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].y]  #плечо
            right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].y]  #плечо
            left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE].x, landmarks[mp_pose.PoseLandmark.LEFT_KNEE].y]  #стопа
            right_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE].x, landmarks[mp_pose.PoseLandmark.RIGHT_KNEE].y]  #стопа
            right_tors_angle = calculate_angle(right_shoulder, right_hip, right_knee)
            left_tors_angle = calculate_angle(left_shoulder, left_hip, left_knee)
            cv2.putText(image, str(right_tors_angle), tuple(np.multiply(right_hip, [640, 480]).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(image, str(left_tors_angle), tuple(np.multiply(left_hip, [640, 480]).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            if right_tors_angle < 130 or left_tors_angle < 130:
                stage = "down"
            if (right_tors_angle > 160 or left_tors_angle > 160) and stage == 'down':
                stage = "up"
                counter += 1
        except:
            pass
        cv2.rectangle(image, (0, 0), (225, 73), (250, 250, 250), -1)
        cv2.putText(image, 'REPS', (15, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(image, str(counter), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 230, 0), 2, cv2.LINE_AA)
        cv2.putText(image, 'STAGE', (100, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(image, stage, (80, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 230, 0), 2, cv2.LINE_AA)
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2), mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2))
        cv2.imshow('Mediapipe Feed', image)  # всплывающее окно с кадром
        if cv2.waitKey(10) & keyboard.is_pressed('Esc'):  # выход из программы
            break

    cap.release()  # закрытие камеры
    cv2.destroyAllWindows()  # закрытие всех окон