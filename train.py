from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolov8s.pt")
    data_path = "D:\pycharmWorkspace\squirrelDet\chonky2\data.yaml"
    model.train(data=data_path,epochs=10,workers=1,save_period = 2,save=True )
    metrics = model.val()
    results = model("chonky/test/images/1165cjve4jfa1-2-_jpg.rf.02e3c28e063fd51ca43fafb38d2e7d03.jpg")

