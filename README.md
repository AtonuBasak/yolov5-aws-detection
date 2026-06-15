# yolov5-aws-detection

# YOLOv5 Image Object Identification System on AWS

## Student Information
- **Name:** Atonu Basak
- **Student Number:** 379197597141
- **Unit:** BIS202 — Business Information Systems
- **Institution:** Apex Australia Higher Education
- **Submission:** Assignment 2

---

## Project Description
A serverless image object detection system built on Amazon Web Services 
using YOLOv5, AWS Lambda, API Gateway, and Amazon S3. Users upload images 
to an S3 bucket and call the REST API to receive object detection results 
including class labels, confidence scores, and bounding box coordinates.

---

## Live API URL

POST https://lp9ktv3ri8.execute-api.ap-southeast-1.amazonaws.com/prod/detect

## How to Test

curl -X POST https://lp9ktv3ri8.execute-api.ap-southeast-1.amazonaws.com/prod/detect 

-H "Content-Type: application/json" 

-d '{"image_key": "images/images.jpg"}'

---

## Technology Stack
- **Object Detection:** YOLOv5s (Ultralytics)
- **Cloud Platform:** Amazon Web Services (AWS)
- **Serverless Function:** AWS Lambda (Python 3.11)
- **API Layer:** AWS API Gateway (REST)
- **Storage:** Amazon S3
- **Compute:** EC2 t3.micro (Ubuntu 26.04 LTS)
- **Region:** Asia Pacific — Singapore (ap-southeast-1)

---

## Project Structure
- `lambda_function.py` — Main Lambda function code
- `images/` — Input images stored in S3
- `results/` — Detection results stored in S3

---

## Dataset
- COCO Dataset (via YOLOv5s pre-trained weights)
- Link: https://cocodataset.org

---

## References
- Jocher et al. (2022). Ultralytics YOLOv5. https://github.com/ultralytics/yolov5
- Amazon Web Services. (2024). AWS Lambda. https://docs.aws.amazon.com/lambda
- Amazon Web Services. (2024). Amazon S3. https://docs.aws.amazon.com/s3
