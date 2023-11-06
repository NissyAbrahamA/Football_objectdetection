from ultralytics import YOLO

model = YOLO("yolov8n.yaml")
results = model.train(data="config.yml", epochs=50)
