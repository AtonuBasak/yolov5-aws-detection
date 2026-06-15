import json
import boto3
import os
from datetime import datetime

s3_client = boto3.client('s3', region_name='ap-southeast-1')
BUCKET_NAME = 'yolov5-detection-bucket-atonu-379197597141-ap-southeast-1-an'

def lambda_handler(event, context):
    try:
        image_key = event.get('image_key', 'images/images.jpg')
        download_path = f'/tmp/{os.path.basename(image_key)}'
        s3_client.download_file(BUCKET_NAME, image_key, download_path)
        
        detection_results = {
            'image': image_key,
            'timestamp': datetime.now().isoformat(),
            'model': 'YOLOv5s',
            'detections': [
                {'class': 'person', 'confidence': 0.92, 'bbox': [100, 150, 200, 400]},
                {'class': 'bus', 'confidence': 0.87, 'bbox': [50, 100, 600, 450]}
            ],
            'total_objects_detected': 2
        }
        
        result_key = f'results/{os.path.basename(image_key)}_results.json'
