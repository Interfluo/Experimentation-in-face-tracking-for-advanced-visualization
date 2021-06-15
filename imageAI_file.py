from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path , "yolo.h5"))
detector.loadModel()
image_name = "21.jpg"  # """.join([str(i), '.jpg'])
new_image_name = "21_new.jpg"  # "".join([str(i), '_new.jpg'])
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, image_name),
                                             output_image_path=os.path.join(execution_path, new_image_name),
                                             minimum_percentage_probability=10)



for eachObject in detections:
    print(eachObject["name"], " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"])
    print("--------------------------------")
