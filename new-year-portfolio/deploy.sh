#!/bin/bash

# Configuration
PROJECT_ID=$(gcloud config get-value project)
SERVICE_NAME="portfolio-website"
REGION="us-central1" # You can change this to your preferred region

echo "🚀 Starting Deployment to Google Cloud Run..."
echo "Project ID: $PROJECT_ID"
echo "Service Name: $SERVICE_NAME"

# Check if Project ID is set
if [ -z "$PROJECT_ID" ]; then
    echo "❌ Error: No Google Cloud Project ID found."
    echo "👉 Please run: gcloud config set project [YOUR_PROJECT_ID]"
    exit 1
fi

# Enable required services
echo "🔄 Enabling Cloud Build and Cloud Run services..."
gcloud services enable cloudbuild.googleapis.com run.googleapis.com

# Build and Deploy
echo "🔨 Building and Deploying..."
gcloud run deploy $SERVICE_NAME \
    --source . \
    --platform managed \
    --region $REGION \
    --labels dev-tutorial=blog-devcommunity2026 \
    --allow-unauthenticated

echo "✅ Deployment Complete!"
