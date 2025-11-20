Project Overview
This project implements a serverless image processing pipeline that automatically processes images uploaded to an S3 bucket. The application uses AWS Lambda for image processing, Step Functions for workflow orchestration, and API Gateway for external triggers.

Live API Endpoint
POST https://9qza7nca15.execute-api.us-east-1.amazonaws.com/prod/process


How to Test the API

Request Format
Method: POST
Content-Type: application/json
Endpoint: https://9qza7nca15.execute-api.us-east-1.amazonaws.com/prod/process

Request Body
{
  "sourceBucket": "original-image-nuguidpauljohn",
  "sourceKey": "myphoto.jpg",
  "destinationBucket": "resized-imaged-nuguidpauljohn"
}


Architecture Diagram

+-------------+     +----------------+     +-------------------+     +-------------+
| API Gateway | --> | Step Functions | --> | Lambda Function   | --> | S3 Bucket   |
| (Trigger)   |     | (Orchestration)|     | (Image Processor) |     | (Resized)   |
+-------------+     +----------------+     +-------------------+     +-------------+
                                                         |
                                                         v
                                                +-------------+
                                                | S3 Bucket   |
                                                | (Original)  |
                                                +-------------+


AWS Services Used
Amazon S3 - File storage (source and destination buckets)
AWS Lambda - Image processing function
AWS Step Functions - Workflow orchestration with success/failure states
Amazon API Gateway - REST API endpoint


Project Requirements Met 

Two S3 buckets for original and resized images
Lambda function for image processing
Step Functions state machine with success/failure states
API Gateway endpoint to trigger workflow
Complete serverless architecture
Working demonstration


Implementation Notes

Lambda function processes images and copies them between S3 buckets
Step Functions orchestrates the workflow with proper error handling
API Gateway provides external access to trigger the image processing pipeline
The architecture is fully serverless and scalable

Project Structure
serverless-image-processing/
├── lambda_functions/
│   └── image_processor.py
├── README.md
├── .gitignore
└── LICENSE


Workflow Process

Trigger: API Gateway receives POST request
Orchestration: Step Functions starts execution
Processing: Lambda function processes the image
Decision: Step Functions checks success/failure
Storage: Processed image saved to destination S3 bucket
Completion: Success or failure response returned

Implementation Details

Runtime: Python 3.11
Function: ImageProcessor
Purpose: Downloads images from source S3 bucket, processes them, and uploads to destination bucket
Error Handling: Comprehensive try-catch with proper error responses


Step Functions Workflow

State Machine: ImageProcessingWorkflow
States:
ProcessImage: Invokes Lambda function
CheckResult: Validates processing outcome
Success: Final state for successful executions
Fail: Final state for failed executions


API Gateway

API: ImageProcessingAPI
Endpoint: /process (POST method)
Integration: Direct integration with Step Functions


Testing Results
Successful Execution
{
  "statusCode": 200,
  "message": "Image processing completed successfully",
  "sourceBucket": "original-image-nuguidpauljohn",
  "sourceKey": "myphoto.jpg",
  "destinationBucket": "resized-imaged-nuguidpauljohn",
  "destinationKey": "resized/myphoto_thumbnail.jpg",
  "fileSize": 134187,
  "contentType": "image/jpeg"
}


Scalability & Performance

Serverless Architecture: Automatically scales with load
Cost Effective: Pay-per-use pricing model
High Availability: AWS managed services with built-in redundancy
Performance: Parallel processing capabilities through Step Functions

Developer Notes
This project demonstrates a complete serverless application using core AWS services. The architecture can be extended with additional features like:

Image format conversion
Multiple resize dimensions
Image metadata extraction
CloudFront distribution for resized images

Support
For questions or issues related to this project, please refer to the AWS documentation for each service or consult the instructor.


Submission Details:

GitHub Repository: (https://github.com/nuguid5263/serverless-image-processing.git)
Student: Paul John Nuguid
Date: 11/20/2025