import cv2
import face_recognition
import numpy as np


def main():
    vid = cv2.VideoCapture(0)
    face1 = cv2.imread("faces/face1.PNG")
    face1_encoding = face_recognition.face_encodings(face1)[0]

    while (True):

        ret, frame = vid.read()

        face_locations = face_recognition.face_locations(frame)

        for face_location in face_locations:
            top, right, bottom, left = face_location
            print(f"Top: {top}, Right: {right}, Bottom: {bottom}, Left: {left}")

        drawing = cv2.rectangle(frame, (right, top), (left, bottom), (0, 255, 0), 3)

        cv2.imshow('frame', drawing)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()