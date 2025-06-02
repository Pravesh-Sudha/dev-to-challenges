import pulumi
import pulumi_aws as aws

# Configure AWS region
aws_provider = aws.Provider("aws", region="us-east-1")

# Create DynamoDB table
todo_tasks_table = aws.dynamodb.Table("todo_tasks",
    name="todo_tasks",
    billing_mode="PAY_PER_REQUEST",
    hash_key="task_id",
    attributes=[aws.dynamodb.TableAttributeArgs(
        name="task_id",
        type="S",
    )],
    tags={
        "Name": "dynamodb-table-1",
        "Environment": "production"
    },
    opts=pulumi.ResourceOptions(provider=aws_provider)
)

# Create SNS Topic with corrected delivery policy
todo_notifications_topic = aws.sns.Topic("todo_notifications",
    name="todo_notifications",
    delivery_policy="""{
        "http": {
            "defaultHealthyRetryPolicy": {
                "minDelayTarget": 20,
                "maxDelayTarget": 20,
                "numRetries": 3,
                "numMaxDelayRetries": 0,
                "numNoDelayRetries": 0,
                "numMinDelayRetries": 3,
                "backoffFunction": "linear"
            }
        }
    }""",
    opts=pulumi.ResourceOptions(provider=aws_provider)
)

# Create SNS Topic Subscription
todo_subscription = aws.sns.TopicSubscription("user_updates_sqs_target",
    topic=todo_notifications_topic.arn,
    protocol="email",
    endpoint="programmerpravesh@gmail.com",  # Change this to your email
    confirmation_timeout_in_minutes=5,
    endpoint_auto_confirms=False,
    opts=pulumi.ResourceOptions(
        provider=aws_provider,
        depends_on=[todo_notifications_topic]
    )
)
# Export SNS Topic ARN
pulumi.export("sns_topic_arn", todo_notifications_topic.arn)