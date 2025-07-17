import json
import boto3

glue_client = boto3.client('glue')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])

        job_name = body.get('jobName')
        start_date = body.get('startDate')
        end_date = body.get('endDate')

        if not all([job_name, start_date, end_date]):
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing jobName, startDate or endDate'})
            }

        response = glue_client.start_job_run(
            JobName=job_name,
            Arguments={
                '--startDate': start_date,
                '--endDate': end_date
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Glue job started successfully',
                'jobName': job_name,
                'jobRunId': response['JobRunId']
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
