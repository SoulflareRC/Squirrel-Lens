# This is a sample Python script.
import hashlib
import http
import pathlib


# Press Ctrl+Shift+R to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from flask import *
from ultralytics import YOLO
from ultralytics.yolo.engine.results import *
import cv2
import urllib
import numpy as np
from skimage import io
from yolov8.dataset import *
from datetime import datetime
from PIL import  Image
import requests


def get_md5(img:np.ndarray):
    img = Image.fromarray(img)
    return hashlib.md5(img.tobytes()).hexdigest()
model = YOLO("last_chonky3.pt")
# model.train(data="")

threshold_x = 200
threshold_y = 200
app = Flask("Squirrel API")


@app.route("/img",methods=["GET","POST"])
def img():
    # print(request.method)
    # print(request.data)
    data = json.loads(request.data)
    # print(data)
    links = data['links']


    output_dir = "results"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    response_data = {
        "replace_links":[]
    }
    for link in links:
        replace_link = ""
        print(link)
        try:
            image:np.ndarray = io.imread(link)
            image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
            shape = image.shape
            if shape[0]>threshold_x and shape[1]>threshold_y:
                print(shape)
                pred = model.predict(source=image)
                boxes = get_boxes(pred)
                print(len(boxes))

                if len(boxes)>0:
                    imgd = draw_boxes(image,[box for box in boxes if box.conf>0.4])
                    imgd = highlight_box(imgd,boxes)
                    # print(pred)
                    # target_path = os.path.join(output_dir,datetime.time()+".jpg")
                    # print("Saving result to ",target_path)

                    md5 = get_md5(image)
                    # cv2.imshow(md5, imgd)
                    target_path = os.path.join(output_dir, str(md5)+".jpg")
                    print("target path:",target_path)
                    cv2.imwrite(target_path,imgd)
                    replace_link = f"/results/{md5}"
                # cv2.imshow(f"{link}",image)
                # cv2.waitKey(-1)
            cv2.waitKey(-1)
        except Exception as e:
            print(e)
            print(f"Failed to open image link {link}!")
        response_data['replace_links'].append(replace_link)

    print("Hey")
    # test = {
    #     "name":"chonks",
    #     "age":1
    # }
    # print(jsonify(test))
    response = jsonify(response_data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    print("Sending response:",response)
    return response,http.HTTPStatus.OK
@app.route("/results/<string:md5>",methods = ["GET","POST"])
def result(md5):
    # img_path = os.path.join("temp",md5+".jpg")
    return send_from_directory("results",md5+".jpg")

@app.route("/chonky",methods=["GET","POST"])
def chonky():

    images = list(pathlib.Path("images").iterdir())
    import random
    idx = random.randint(0,len(images)-1)
    file = images[idx]

    return send_file(file,mimetype="image/jpg")
app.run(port=8000,debug=True)
