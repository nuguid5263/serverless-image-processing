import json
import boto3
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print(" Image processing workflow started")
    print("Event received:", json.dumps(event, indent=2))
    
    try:
        # Get input parameters
        source_bucket = event['sourceBucket']
        source_key = event['sourceKey'] 
        destination_bucket = event['destinationBucket']
        
        print(f" Downloading: {source_key} from {source_bucket}")
        
        # Download the image
        response = s3.get_object(Bucket=source_bucket, Key=source_key)
        image_data = response['Body'].read()
        content_type = response['ContentType']
        
        print(f" Downloaded successfully. Type: {content_type}, Size: {len(image_data)} bytes")
        
        # Create destination path
        filename = os.path.basename(source_key)
        name, ext = os.path.splitext(filename)
        destination_key = f"resized/{name}_thumbnail{ext}"
        
        print(f" Uploading to: {destination_bucket}/{destination_key}")
        
        # Upload to destination
        s3.put_object(
            Bucket=destination_bucket,
            Key=destination_key,
            Body=image_data,
            ContentType=content_type,
            Metadata={
                'original-file': source_key,
                'processed-by': 'serverless-image-processor',
                'workflow-completed': 'true'
            }
        )
        
        print(" Success! File processed and saved")
        
        return {
            'statusCode': 200,
            'message': 'Image processing completed successfully',
            'sourceBucket': source_bucket,
            'sourceKey': source_key,
            'destinationBucket': destination_bucket,
            'destinationKey': destination_key,
            'fileSize': len(image_data),
            'contentType': content_type
        }
        
    except Exception as e:
        error_msg = f" Error processing image: {str(e)}"
        print(error_msg)
        return {
            'statusCode': 500,
            'error': error_msg,
            'sourceBucket': event.get('sourceBucket', 'unknown'),
            'sourceKey': event.get('sourceKey', 'unknown')
        }