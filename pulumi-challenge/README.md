# Pulumi Challenge Dev Community

This is a simple Flask-based To-Do List application that allows users to add, complete, and delete tasks. The tasks are stored in AWS DynamoDB, notifications are managed through AWS SNS, and infrastructure is provisioned using Pulumi. A video demo of this project is available on YouTube in which I have used Terraform to deploy the project.

## Video Demo

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/ZLRv0rVifL8/0.jpg)](https://www.youtube.com/watch?v=ZLRv0rVifL8) 

## Features

- Add new tasks
- Mark tasks as completed
- Delete tasks
- Flash messages for task actions
- SNS notifications for task updates

## Prerequisites

1. **AWS Account**: You’ll need an AWS account to set up DynamoDB, SNS, and configure the AWS CLI.
2. **Python 3.10+**: This project uses Python for its backend logic.
3. **Flask**: A lightweight web framework to create the app.
4. **Boto3**: AWS SDK for Python to interact with DynamoDB and SNS.
5. **AWS CLI**: Command line tool for configuring AWS services.
6. **Pulumi**: Infrastructure as Code tool for provisioning AWS resources.

---

## Table of Contents

1. [Installation](#installation)
2. [Configuring AWS CLI](#configuring-aws-cli)
3. [Pulumi Integration](#pulumi-integration)
4. [Setting up DynamoDB and SNS](#setting-up-dynamodb-and-sns)
5. [Running the Application](#running-the-application)
6. [File Structure](#file-structure)
7. [Contributing](#contributing)

---

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Pravesh-Sudha/pulumi-challenge.git
   cd pulumi-challenge
   ```

2. **Create a Python virtual environment**:

   ```bash
   python3 -m venv flask-env
   ```

3. **Activate the virtual environment**:

   - On Windows:
     ```bash
     flask-env\Scripts\activate
     ```
   - On MacOS/Linux:
     ```bash
     source flask-env/bin/activate
     ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## Configuring AWS CLI

1. **Install AWS CLI** (if not already installed):

   Follow the instructions from the [AWS CLI Documentation](https://aws.amazon.com/cli/).

2. **Configure AWS CLI**:

   Run the following command to configure your AWS CLI:

   ```bash
   aws configure
   ```

   You'll need to provide your:
   - AWS Access Key ID
   - AWS Secret Access Key
   - Default region name (e.g., `us-east-1`)
   - Default output format (e.g., `json`)

3. **Ensure permissions**:
   - DynamoDB permissions for table operations
   - SNS permissions for topic and subscription management

---

## Pulumi Integration

This project uses Pulumi to manage AWS infrastructure (DynamoDB table and SNS topic/subscription).

1. **Install Pulumi using Homebrew** (MacOS/Linux):

   ```bash
   brew install pulumi
   ```

   For other platforms, follow the [official Pulumi installation guide](https://www.pulumi.com/docs/get-started/install/).

2. **Create the Pulumi Project**:

   Initialize a new Pulumi project with the AWS Python template:

   ```bash
   pulumi new aws-python
   ```

   Follow the prompts to set up the project. Replace the default `__main__.py` with the provided Pulumi script.

3. **Deploy Infrastructure**:

   Apply the Pulumi changes to create the AWS resources:

   ```bash
   pulumi up
   ```

   This will provision:
   - A DynamoDB table named `todo_tasks`
   - An SNS topic named `todo_notifications`
   - An email subscription to the SNS topic

   ![Pulumi-Up](<Screenshot 2025-04-05 at 3.45.07 PM.png>)


---

## Setting up DynamoDB and SNS

The Pulumi script automatically creates:
- **DynamoDB Table**: `todo_tasks`
  - Partition key: `task_id` (String)
  - Attributes: `task_name` (String), `completed` (Boolean)
- **SNS Topic**: `todo_notifications`
- **SNS Subscription**: Email endpoint (configured in `__main__.py`)

After running `pulumi up`:
1. Check your email to confirm the SNS subscription.
2. Verify resources in the AWS Console.

![Subs-msg](<Screenshot 2025-04-05 at 3.45.35 PM.png>) 

![subs-confirm](<Screenshot 2025-04-05 at 3.45.48 PM.png>)

---



## Configuring the Application

1. **Update `config.py`**:

   In the `config.py` file, update the following values:

   ```python
   class Config:
       # AWS DynamoDB Configuration
       SECRET_KEY = os.getenv('SECRET_KEY', 'KEY')
       AWS_REGION = 'us-east-1'
       DYNAMODB_TABLE = 'todo_tasks'
       SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")
       EMAIL = "Your-Email"
   ```

![alt text](<Screenshot 2025-04-05 at 4.19.44 PM.png>)

   Retrieve the SNS Topic ARN from the `pulumi up` output.

---

## Running the Application

1. **Run the Flask app**:

   Start the Flask development server:

   ```bash
   flask run
   ```

   The application will run on `http://127.0.0.1:5000/`.

2. **Access the To-Do List App**:

   Open your browser and navigate to `http://127.0.0.1:5000/`. You should be able to see the app's user interface.

![alt text](<Screenshot 2025-04-05 at 3.51.33 PM-1.png>)

![alt text](<Screenshot 2025-04-05 at 4.21.16 PM.png>)

---

## File Structure

```
flask-todo-app/
│
├── __main__.py          # Pulumi infrastructure script
├── app.py               # Flask app entry point
├── db.py                # DynamoDB connection setup
├── routes.py            # Main routes for task management
├── static/
│   └── style.css        # CSS for styling the UI
├── templates/
│   ├── dashboard.html   # Dashboard (Task Management) page
├── config.py            # Configuration for AWS and app settings
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation (this file)
```

---

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Make changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request to the main repository.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
