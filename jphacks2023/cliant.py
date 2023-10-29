import socket
import numpy
from ultralytics import YOLO
import cv2

# Load a model
model = YOLO("C:/Users/nanam/Desktop/workspaces/jphacks2023/runs/detect/train3/weights/best.pt")


HOST = "192.168.153.208"  # ここはRaspberryPiのIPアドレスを入力
PORT = 12345


def getimage():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    buf = []
    recvlen = 100

    while recvlen > 0:
        receivedstr = sock.recv(1024*8)
        recvlen = len(receivedstr)
        buf += receivedstr
    sock.close()
    recdata = numpy.array(buf, dtype='uint8')
    return cv2.imdecode(recdata, 1)

#while True:
for i in range(10):
    img = getimage()
    cv2.waitKey(5)  
    #result = model(img,show=True)#テスト用

result = model(img,exist_ok=True,save=True,save_txt=True)
