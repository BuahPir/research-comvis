import requests
import supervision as sv
from PIL import Image
from inference import get_model

model = get_model("rfdetr-medium")

image = Image.open("dog.jpg")
predictions = model.infer(image, confidence=0.5)[0]
detections = sv.Detections.from_inference(predictions)

annotated_image = sv.BoxAnnotator().annotate(image, detections)
annotated_image = sv.LabelAnnotator().annotate(annotated_image, detections)