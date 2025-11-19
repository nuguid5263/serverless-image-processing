# serverless-image-processing

## Architecture
- S3 Buckets (source & destination)
- Lambda Function (processes images) 
- Step Functions (orchestrates workflow)
- API Gateway (triggers workflow)

## How to Test
1. Upload image to source S3 bucket
2. Trigger via API Gateway
3. Check destination bucket for resized image