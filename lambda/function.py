import json
import boto3

def lambda_handler(event, context):
    # Initialize the Glue client
    glue = boto3.client('glue')
    
    # Extract the S3 bucket and file name from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    
    # Log the event for debugging
    print(f"New file uploaded: {file_key} in bucket {bucket}")
    
    # Define Glue Job name (replace with your Glue Job name)
    glue_job_name = 'ETL-for-S3'
    
    # Check the current job runs for the Glue job
    job_runs = glue.get_job_runs(JobName=glue_job_name, MaxResults=1)
    
    # If a job is already running, do not start a new one
    if job_runs['JobRuns'] and job_runs['JobRuns'][0]['JobRunState'] == 'RUNNING':
        print("Job is already running. Skipping this trigger.")
        return {
            'statusCode': 200,
            'body': json.dumps('Job is already running, skipping trigger.')
        }
    
    # If no job is running, start the Glue job
    response = glue.start_job_run(JobName=glue_job_name)
    
    # Log the response (optional for debugging)
    print("Glue job triggered:", response)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Glue job triggered successfully')
    }
