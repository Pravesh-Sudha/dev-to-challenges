import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'bhaiyokabhaipraveshbhai')
    AWS_REGION = 'us-east-1'
    DYNAMODB_TABLE = 'todo_tasks'
    SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")
    EMAIL = "programmerpravesh@gmail.com"
