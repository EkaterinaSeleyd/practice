#оценка правильности осанки
import cv2
import mediapipe as mp
import numpy as np
import os
import sys
import keyboard

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

bad_time = 300 #примерно 20 секунд

cap = cv2.VideoCapture(1)  #импорт видеопотока

counter = 0  #счётчик
stage = None #состояние сгибания (нейтральное)
bad_frames = 0
good_frames = 0

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

            # определяем координаты частей тела
            shoulderL = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            shoulderR = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]

            wristL = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            wristR = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

            elbowL = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            elbowR = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]

            earL = [landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].x, landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].y]
            earR = [landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].y]

            hipL = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            hipR = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]

            kneeL = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            kneeR = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]

            ankleL = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
            ankleR = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
            # отрисовка средней точки плечевого пояса
            avg_point_shoulder = ((shoulderL[0] + shoulderR[0]) / 2, (shoulderL[1] + shoulderR[1]) / 2)
            cv2.circle(image,(int(avg_point_shoulder[0] * frame.shape[1]), int(avg_point_shoulder[1] * frame.shape[0])), 5,(0, 0, 255), -1)
            # отрисовка средней точки тазового пояса
            avg_point_hip = ((hipL[0] + hipR[0]) / 2, (hipL[1] + hipR[1]) / 2)
            cv2.circle(image, (int(avg_point_hip[0] * frame.shape[1]), int(avg_point_hip[1] * frame.shape[0])), 5,(0, 0, 255), -1)

            #вычисление угла подъема рук
            angleEL = calculate_angle(shoulderL, elbowL, wristL)
            #cv2.putText(image, str(angleEL), tuple(np.multiply(elbowL, [640, 480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            angleER = calculate_angle(shoulderR, elbowR, wristR)
            #cv2.putText(image, str(angleER), tuple(np.multiply(shoulderR, [640, 480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            # угол наклона ног
            angleLL = calculate_angle(ankleL, kneeL, hipL)
            #cv2.putText(image, str(angleLL), tuple(np.multiply(kneeL, [640, 480]).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            angleLR = calculate_angle(ankleR, kneeR, hipR)
            #cv2.putText(image, str(angleLR), tuple(np.multiply(ankleR, [640, 480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            # угол наклона торса
            avg_point_kneel = ((kneeL[0] + kneeR[0]) / 2, (kneeL[1] + kneeR[1]) / 2)
            angleHL = calculate_angle(avg_point_kneel, avg_point_hip, avg_point_shoulder)
            #cv2.putText(image, str(angleHL), tuple(np.multiply(hipL, [640, 480]).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            #cv2.line(image, (int(avg_point_shoulder[0] * frame.shape[1]), int(avg_point_shoulder[1] * frame.shape[0])),
             #        (int(avg_point_hip[0] * frame.shape[1]), int(avg_point_hip[1] * frame.shape[0])), (255, 0, 0), 2)

            avg_point_ear = ((earL[0] + earR[0]) / 2, (earL[1] + earR[1]) / 2)
            cv2.circle(image, (int(avg_point_ear[0] * frame.shape[1]), int(avg_point_ear[1] * frame.shape[0])), 5, (0, 0, 255), -1)
            #угол наклона шеи
            angleL = calculate_angle(avg_point_ear, avg_point_shoulder, avg_point_hip)
            #cv2.putText(image, str(angleL), tuple(np.multiply(avg_point_shoulder, [640, 480]).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            if angleL > 155 and (angleHL > 85 and angleHL < 115) and (angleLL > 80 and angleLL < 120) and (angleLR > 80 and angleLR < 120) and angleEL > 25 and angleER > 25:
                stage = "good"
                bad_frames = 0
                good_frames += 1
            if angleL < 155 or (angleHL < 85 or angleHL > 110) or (angleLL < 80 or angleLL > 120) or (angleLR < 80 or angleLR > 120) or angleEL < 25 or angleER < 25 and stage == 'good':
                stage = "bad"
                bad_frames += 1
                good_frames = 0

            if bad_frames > bad_time:
                os.system("start osanka.mp3")
                bad_frames = 0


        except:
            pass
        #прямоугольник состояния: начальные координаты, размер, цвет, заполнение цветом (-1))
        cv2.rectangle(image, (0, 0), (225, 73), (250, 250, 250), -1)

        #вывод состояния сгибания (вверх, вниз)
        cv2.putText(image, 'POSE', (80, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1, cv2.LINE_AA)
        if stage == 'good':
            cv2.putText(image, stage, (70, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(image, stage, (70, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2, cv2.LINE_AA)

        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                  )  # отрисовка линий, соединяющих опорные точки позы человека
        cv2.imshow('Mediapipe Feed', image)  # всплывающее окно с кадром

        if cv2.waitKey(10) & keyboard.is_pressed('Esc'):  # выход из программы
             #sys.exit(0)
            break

    cap.release()  #закрытие камеры
    cv2.destroyAllWindows()  #закрытие всех окон
