# AWS Lambda + API Gateway + Glue Job Trigger

## 📌 What it does
- Exposes a REST API via API Gateway
- Triggers an AWS Glue job with 3 parameters: `jobName`, `startDate`, `endDate`

## 📦 Contents
- `lambda_function.py`: AWS Lambda code
- `glue_script.py`: Sample Glue job that accepts parameters
- `iam_policy.json`: Permissions needed for the Lambda role
- `postman_collection.json`: Import into Postman to test the API

## 🧪 Sample API Request

### POST /trigger-glue-job
```
{
  "jobName": "daily-job",
  "startDate": "2025-07-01",
  "endDate": "2025-07-17"
}
```

## ✅ Response
```
{
  "message": "Glue job started successfully",
  "jobName": "daily-job",
  "jobRunId": "jr_xxx"
}
```

## 🛠 Setup
1. Create Glue job that accepts --startDate and --endDate
2. Deploy `lambda_function.py` in Lambda
3. Set IAM policy from `iam_policy.json`
4. Create HTTP API Gateway and connect to Lambda
5. Use Postman or CURL to test

