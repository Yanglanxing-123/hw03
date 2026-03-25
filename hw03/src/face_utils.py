import face_recognition
import cv2
import numpy as np

# 检测人脸位置
def detect_faces(image):
    face_locations = face_recognition.face_locations(image)
    return face_locations

# 给人脸画框
def draw_face_boxes(image, face_locations):
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
    return image