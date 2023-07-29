#Copyright Code By Zhen Xiong
import cv2

video = cv2.VideoCapture("LIL.mp4")
mg = cv2.imread("LIL.mp4")
thres = 0.5
cap = cv2.VideoCapture(0)
cap.set(4,480)

classNames= []
classFile = "data.names"
with open(classFile, "rt") as f:
   classNames = f.read().rstrip("\n").split("\n")

configPath = "dataset_base.pbtxt"
weightsPath = "graph.pb"

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(325,325)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
    success, img = cap.read()
    classIds, confs, bbox = net.detect(img, confThreshold=0.5)
    print(classIds,bbox)

    if len(classIds) != 0:
        for classIds, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            cv2.rectangle(img,box,color=(1,255,0),thickness=2)
            cv2.putText(img,classNames[classIds-1].upper(),(box[0]+10,box[1]+30),
                       cv2.FONT_HERSHEY_COMPLEX,1,(1,255,0),2)
            #cv2.putText(img,str(confidence),(box[0]+34,box[1]+30),
            #             cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)


    cv2.imshow("Deteksi",img)
    cv2.waitKey(1)






