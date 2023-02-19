# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from flask import *
from ultralytics import YOLO
from ultralytics.yolo.engine.results import *
import cv2
import urllib
import numpy as np
from skimage import io
import os
from yolov8.dataset import *
from datetime import datetime
import gradio as gr

class ui_wrapper(object):
    def __init__(self):
        self.model:YOLO = YOLO("last_chonky3.pt")

        pass
    def infer_img(self,img):
        # print(type(img))
        pred = self.model.predict(img)
        boxes = get_boxes(pred)
        # boxes = [box for box in boxes if box.conf>0.3]
        imgd = draw_boxes(img,boxes)
        imgd = highlight_box(imgd,boxes)
        num = len(boxes)
        hint = f"{num} chonky squirrels are detected in this image🐿️🐿️🐿️"
        if num==0:
            hint = "No chonky squirrels is detected in this image😔."
        cropped = crop_boxes(img,boxes)

        gallery_out = []
        for idx,crop in enumerate(cropped):
            elem = (crop,"Confidence:" +str(float(boxes[idx].conf[0])))
            gallery_out.append(elem)
        return imgd,hint,gallery_out
    def infer_vid(self,vid):
        vid_run_dir = "runs/detect"
        if os.path.exists(vid_run_dir):
            shutil.rmtree(vid_run_dir)
        pred = self.model.predict(source=vid,save=True)
        p = pathlib.Path(vid_run_dir).joinpath("predict")
        vid =list(p.iterdir())[0].resolve()
        return str(vid)



    def interface(self):

        hint = gr.Markdown(value="")
        image_input = gr.Image(label="Image input")
        submit_btn = gr.Button(value="Submit Image!")
        squirrels_gallery = gr.Gallery(label="🐿️")
        # save_btn = gr.Button(value="Save Result")


        video_opt = gr.Radio(choices=["upload","webcam"],value="upload")
        video_input = gr.Video(label="Video Input",source="upload")
        video_submit_btn = gr.Button("Submit Video!")

        with gr.Blocks() as demo:
            with gr.Column():
                hint.render()
                image_input.render()
                with gr.Row():
                    submit_btn.render()
                    # save_btn.render()
                squirrels_gallery.render()
                video_opt.render()
                video_input.render()
                video_submit_btn.render()
            submit_btn.click(fn=self.infer_img,inputs=image_input,outputs=[image_input,hint,squirrels_gallery])
            video_submit_btn.click(fn=self.infer_vid,inputs=video_input,outputs=video_input)
        return demo
gui = ui_wrapper()
gui.interface().launch(share=True)