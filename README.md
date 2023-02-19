# Squirrel-Lens
### [MHacks 15] An object detection chrome extension that detects CHONKY squirrels in your browser.<br>
![val_batch2_pred](https://user-images.githubusercontent.com/107384280/219932642-adc78b97-20ef-4e68-835c-41f746e1baa1.jpg)

This project aims to find out chonky squirrels, which the UofM is known for, in images. 
This project uses [YOLOv8](https://github.com/ultralytics/ultralytics) as the base model, fined tuned for 10 epochs with 220+ handpicked chonky squirrel images from various sources including UofM reddit, instagram, twitter, and 200+ non-chonky squirrel images from [squirrel data dataset](https://www.kaggle.com/datasets/sheldenshi/squirrel-data). The total dataset size is 1122 images after augmentation. Base model used for this project is yolov8s, and it achieved a mAP50-95 of 45.0. 

##  Install
Clone the whole repository using ```git clone https://github.com/SoulflareRC/Squirrel-Lens.git``` 

### Requirements
- ultralytics
- flask
- opencv
- PyTorch
- gradio

### Usage

#### Use the extension
1. Run the api server with ```python main.py```
2. Open chrome extension tab by typing ```chrome://extensions/``` in your browser
3. Turn on the developer mode on the upper right <br>![image](https://user-images.githubusercontent.com/107384280/219932991-1d36926d-afa6-4566-bbe3-d20eb3288d2e.png)
4. Find the ```extension``` folder in the repo, drag it into the extension tab
5. The extension is successfully installed when you see this<br>![image](https://user-images.githubusercontent.com/107384280/219933041-2c1b5eff-62c7-42cf-81f1-3bd9e8463c2d.png)
<br>

#### Only use inference
1. Run the gradio app with ```python gradio_ui.py```
2. You should see two links, one starts with ```127.0.0.1 ...```, another ends with ```gradio.live```. You can use the former on your own machine, and you can share the latter with your friend!
3. Enjoy!


Confusion matrix of the model:
![confusion_matrix](https://user-images.githubusercontent.com/107384280/219932626-4df4ff90-fe07-40a0-b34c-37d0a4315e0a.png)

