#!/bin/bash

# CementCycle Enhanced Setup Script
# Sets up the complete CementCycle platform with Gemini AI and Firestore

echo "🚀 CementCycle Enhanced Platform Setup"
echo "======================================="

# Check if gcloud is installed
if ! command -v gcloud &> /dev/null; then
    echo "❌ Google Cloud CLI is not installed. Please install it first."
    echo "📥 Download: https://cloud.google.com/sdk/docs/install"
    exit 1
fi

# Set project variables
read -p "Enter your Google Cloud Project ID: " PROJECT_ID
read -p "Enter your preferred region (default: us-central1): " REGION
REGION=${REGION:-us-central1}

echo "🔧 Setting up project: $PROJECT_ID in region: $REGION"

# Set default project
gcloud config set project $PROJECT_ID

echo "🌟 Enabling required APIs..."
gcloud services enable \
    cloudbuild.googleapis.com \
    cloudfunctions.googleapis.com \
    firestore.googleapis.com \
    run.googleapis.com \
    storage.googleapis.com \
    aiplatform.googleapis.com

echo "🔥 Setting up Firestore database..."
gcloud firestore databases create --region=$REGION --type=firestore-native

echo "👤 Creating service account for CementCycle..."
gcloud iam service-accounts create cementcycle-agent \
    --display-name="CementCycle AI Agent" \
    --description="Service account for CementCycle platform operations"

echo "🔑 Setting up IAM permissions..."
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:cementcycle-agent@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/cloudsql.client"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:cementcycle-agent@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/datastore.user"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:cementcycle-agent@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/aiplatform.user"

echo "📊 Setting up Cloud Storage for file uploads..."
gsutil mb -p $PROJECT_ID -c STANDARD -l $REGION gs://$PROJECT_ID-cementcycle-storage

echo "🔧 Creating configuration file..."
cat > config.json << EOF
{
  "projectId": "$PROJECT_ID",
  "region": "$REGION",
  "databaseUrl": "https://$PROJECT_ID.firebaseio.com",
  "geminiApiKey": "YOUR_GEMINI_API_KEY",
  "serviceAccountKeyPath": "./serviceAccountKey.json",
  "allowedOrigins": [
    "https://cementcycle-app-$PROJECT_ID.us-central1.run.app",
    "http://localhost:3000",
    "http://localhost:8080"
  ],
  "geminiModel": "gemini-1.5-pro",
  "geminiConfig": {
    "temperature": 0.7,
    "topK": 40,
    "topP": 0.8,
    "maxOutputTokens": 1024
  },
  "database": {
    "collections": {
      "waste_listings": "waste_listings",
      "cement_requirements": "cement_requirements", 
      "matches": "matches",
      "users": "users",
      "transactions": "transactions",
      "chat_logs": "chat_logs",
      "impact_metrics": "impact_metrics",
      "price_history": "price_history",
      "market_intelligence": "market_intelligence",
      "platform_metrics": "platform_metrics",
      "notification_templates": "notification_templates"
    }
  },
  "notifications": {
    "email": {
      "enabled": true,
      "provider": "sendgrid",
      "apiKey": "YOUR_SENDGRID_API_KEY"
    },
    "sms": {
      "enabled": true,
      "provider": "twilio",
      "accountSid": "YOUR_TWILIO_ACCOUNT_SID",
      "authToken": "YOUR_TWILIO_AUTH_TOKEN"
    }
  }
}
EOF

echo "🗃️ Initializing database with sample data..."
python3 init_data_enhanced.py

echo "☁️ Deploying Cloud Functions..."
cd functions

# Install dependencies
npm install

# Deploy all functions
echo "🚀 Deploying Gemini Chat function..."
gcloud functions deploy geminiChat \
    --runtime nodejs18 \
    --trigger-http \
    --allow-unauthenticated \
    --region $REGION \
    --source=. \
    --entry-point=geminiChat \
    --memory=1GB \
    --timeout=300s \
    --set-env-vars PROJECT_ID=$PROJECT_ID,GEMINI_API_KEY=YOUR_GEMINI_API_KEY

echo "🔍 Deploying Waste Matcher function..."
gcloud functions deploy wasteMatcherTool \
    --runtime nodejs18 \
    --trigger-http \
    --allow-unauthenticated \
    --region $REGION \
    --source=. \
    --entry-point=wasteMatcherTool \
    --memory=512MB \
    --timeout=60s \
    --set-env-vars PROJECT_ID=$PROJECT_ID

echo "🌍 Deploying CO2 Calculator function..."
gcloud functions deploy co2CalculatorTool \
    --runtime nodejs18 \
    --trigger-http \
    --allow-unauthenticated \
    --region $REGION \
    --source=. \
    --entry-point=co2CalculatorTool \
    --memory=512MB \
    --timeout=60s \
    --set-env-vars PROJECT_ID=$PROJECT_ID

echo "💰 Deploying Price Estimator function..."
gcloud functions deploy priceEstimatorTool \
    --runtime nodejs18 \
    --trigger-http \
    --allow-unauthenticated \
    --region $REGION \
    --source=. \
    --entry-point=priceEstimatorTool \
    --memory=512MB \
    --timeout=60s \
    --set-env-vars PROJECT_ID=$PROJECT_ID

echo "🔗 Deploying Match Creator function..."
gcloud functions deploy createMatch \
    --runtime nodejs18 \
    --trigger-http \
    --allow-unauthenticated \
    --region $REGION \
    --source=. \
    --entry-point=createMatch \
    --memory=512MB \
    --timeout=60s \
    --set-env-vars PROJECT_ID=$PROJECT_ID

cd ..

echo "🌐 Deploying frontend to Cloud Run..."
cat > Dockerfile << EOF
FROM nginx:alpine
COPY index_new.html /usr/share/nginx/html/index.html
COPY config.json /usr/share/nginx/html/config.json
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
EOF

# Build and deploy
gcloud builds submit --tag gcr.io/$PROJECT_ID/cementcycle-frontend
gcloud run deploy cementcycle-app \
    --image gcr.io/$PROJECT_ID/cementcycle-frontend \
    --platform managed \
    --region $REGION \
    --allow-unauthenticated \
    --port 8080

echo ""
echo "🎉 CementCycle Platform Setup Complete!"
echo "======================================="
echo ""
echo "📋 Next Steps:"
echo "1. Get your Gemini API key from Google AI Studio"
echo "2. Update the GEMINI_API_KEY in your Cloud Functions"
echo "3. Configure notification services (SendGrid, Twilio) if needed"
echo "4. Test the platform at your Cloud Run URL"
echo ""
echo "📊 Platform Components:"
echo "✅ Firestore Database with sample data"
echo "✅ Cloud Functions for AI and matching"
echo "✅ Cloud Run frontend application"
echo "✅ Google Gemini AI integration"
echo "✅ Environmental impact tracking"
echo "✅ Real-time market intelligence"
echo ""
echo "🔗 Useful Commands:"
echo "• View logs: gcloud functions logs read [FUNCTION_NAME]"
echo "• Update function: gcloud functions deploy [FUNCTION_NAME] ..."
echo "• Monitor Firestore: Visit Firebase Console"
echo ""
echo "📧 Support: For issues, check the logs or contact the development team"
echo ""

# Get the deployed URLs
echo "🌐 Your Platform URLs:"
echo "Frontend: $(gcloud run services describe cementcycle-app --region=$REGION --format='value(status.url)')"
echo "Gemini Chat API: https://$REGION-$PROJECT_ID.cloudfunctions.net/geminiChat"
echo "Waste Matcher API: https://$REGION-$PROJECT_ID.cloudfunctions.net/wasteMatcherTool"
echo ""