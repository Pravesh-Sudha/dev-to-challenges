import boto3
from config import Config

sns = boto3.client('sns', region_name=Config.AWS_REGION)

def send_task_completion_email(email, task_description):
    message = f'Task completed: {task_description}'
    sns.publish(
        TopicArn=Config.SNS_TOPIC_ARN,  # Replace with direct email ARN
        Message=message,
        Subject= "Task Completion Notification"
    )