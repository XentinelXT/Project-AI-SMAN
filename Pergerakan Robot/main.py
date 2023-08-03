import cv2
from Engine_Detection import *

# Pembentukan detec objek
tracker = EuclideanDistTracker()

#Opsional-CamVid

#cap = cv2.VideoCapture("test1.mp4")
cap = cv2.VideoCapture(0)

# Mendeteksi Objek
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

while True:
    ret,frame = cap.read()
    height,width, _ = frame.shape

    # Kunci wilayah (target)
    roi = frame[340: 1080,250: 1920]

    #  Deteksi Objek
    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []
    for cnt in contours:
        # Hitung luas dan menghapus elemen kecil / Binary
        area = cv2.contourArea(cnt)
        if area > 100:
            #cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(cnt)


            detections.append([x, y, w, h])

    #  Track Objek
    boxes_ids = tracker.update(detections)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        cv2.putText(roi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("roi", roi)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(30)
    if key == 27:
        break

#RUN
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)



