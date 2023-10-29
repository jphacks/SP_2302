from ultralytics import YOLO
model = YOLO("yolov8s.pt")
model.train(data="syokuhin.yaml", epochs=10, batch=8, workers=4, degrees=90.0)