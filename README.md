# Boto3 Python Layer Test

This is an example of how a Lambda utilising Boto3 >=1.36.0 with DataDog instrumented via layers fails to initialise when the Python Powertools logger is imported. When the logger is imported, the Lambda immediately fails with the following error:

```
{
  "errorMessage": "Unable to import module 'datadog_lambda.handler': No module named 'aws_lambda_powertools'",
  "errorType": "Runtime.ImportModuleError",
  "requestId": "",
  "stackTrace": []
}
```

## Getting Started

1. Clone the repository
2. Run `npm install`
3. Specify a Serverless organisation in the `serverless.yml` file.
4. Run `npm run deploy`
5. Invoke the Lambda function in question to see the error.
