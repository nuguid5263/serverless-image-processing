import json
import boto3
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print("Image processing function started")
    
    # Get bucket and file info from Step Functions
    source_bucket = event['sourceBucket']
    source_key = event['sourceKey'] 
    destination_bucket = event['destinationBucket']
    
    print(f"Processing: {source_key} from {source_bucket}")
    
    try:
        # Download image
        image_response = s3.get_object(Bucket=source_bucket, Key=source_key)
        image_data = image_response['Body'].read()
        
        # In a real project, we'd resize here
        # For now, just copy to show it works
        resized_key = f"resized/{os.path.basename(source_key)}"
        
        s3.put_object(
            Bucket=destination_bucket,
            Key=resized_key,
            Body=image_data,
            ContentType='image/jpeg'
        )
        
        return {
            'statusCode': 200,
            'message': 'Success! Image processed',
            'sourceKey': source_key,
            'resizedKey': resized_key
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'error': str(e)
        }