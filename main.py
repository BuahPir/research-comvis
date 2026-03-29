import requests
import supervision as sv
from PIL import Image
from rfdetr import RFDETRMedium
from rfdetr.assets.coco_classes import COCO_CLASSES

model = RFDETRMedium()

model.optimize_for_inference()

image = Image.open("dog.jpg")
detections = model.predict(image, threshold=0.5)

labels = [f"{COCO_CLASSES[class_id]}" for class_id in detections.class_id]

annotated_image = sv.BoxAnnotator().annotate(scene=image, detections=detections)
annotated_image = sv.LabelAnnotator().annotate(scene=annotated_image, detections=detections, labels=labels)

# 8. Convert back to PIL to view or save the result
annotated_image.show()
annotated_image.save("annotated_dog.jpg")