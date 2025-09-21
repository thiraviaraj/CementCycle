# CementCycle Enhanced Platform - Deployment Guide

## 🚀 Quick Start

This enhanced CementCycle platform integrates Google Gemini AI, Firestore database, and modern UI for a complete circular economy solution.

### Prerequisites

1. **Google Cloud Account** with billing enabled
2. **Google Cloud CLI** installed
3. **Node.js 18+** and **Python 3.8+**
4. **Gemini API Key** from Google AI Studio

### 🏗️ Architecture Overview

```
Frontend (Cloud Run) → Cloud Functions → Firestore Database
                              ↓
                         Google Gemini AI
```

## 📦 Installation Steps

### 1. Clone and Setup

```bash
# Make setup script executable
chmod +x setup_enhanced.sh

# Run the setup script
./setup_enhanced.sh
```

### 2. Configure Gemini API

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create an API key
3. Update your Cloud Functions:

```bash
# Update Gemini Chat function
gcloud functions deploy geminiChat \
    --update-env-vars GEMINI_API_KEY=your_actual_api_key_here
```

### 3. Test the Platform

Visit your Cloud Run URL to test the enhanced interface.

## 🔧 Manual Setup (Alternative)

### 1. Enable APIs

```bash
gcloud services enable \
    cloudbuild.googleapis.com \
    cloudfunctions.googleapis.com \
    firestore.googleapis.com \
    run.googleapis.com \
    aiplatform.googleapis.com
```

### 2. Setup Firestore

```bash
gcloud firestore databases create --region=us-central1 --type=firestore-native
```

### 3. Initialize Database

```bash
python3 init_data_enhanced.py
```

### 4. Deploy Functions

```bash
cd functions
npm install

# Deploy all functions
npm run deploy:all
```

### 5. Deploy Frontend

```bash
# Build and deploy to Cloud Run
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/cementcycle-frontend
gcloud run deploy cementcycle-app --image gcr.io/YOUR_PROJECT_ID/cementcycle-frontend
```

## 🔧 Configuration

### Environment Variables

Update `config.json` with your specific values:

```json
{
  "projectId": "your-project-id",
  "geminiApiKey": "your-gemini-api-key",
  "allowedOrigins": ["your-frontend-url"]
}
```

### Cloud Functions Environment

```bash
# Set environment variables for all functions
gcloud functions deploy FUNCTION_NAME \
    --set-env-vars PROJECT_ID=your-project-id,GEMINI_API_KEY=your-key
```

## 🌟 New Features

### Enhanced UI
- Modern design with glassmorphism effects
- Real-time metrics dashboard
- Interactive chat interface
- Mobile-responsive layout

### Google Gemini Integration
- Advanced natural language processing
- Context-aware responses
- Real-time market intelligence
- Intelligent waste matching

### Database Enhancements
- Comprehensive waste listings with chemical analysis
- Detailed cement plant requirements
- User profiles and preferences
- Impact tracking and analytics
- Price history and market intelligence

### API Enhancements
- Advanced matching algorithms
- CO2 impact calculations
- Dynamic pricing analysis
- Real-time notifications

## 🧪 Testing

### Test Chat Interface
```bash
curl -X POST \
  https://REGION-PROJECT_ID.cloudfunctions.net/geminiChat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "I have 500 tons of fly ash to sell",
    "context": {"location": "Mumbai"}
  }'
```

### Test Waste Matching
```bash
curl -X POST \
  https://REGION-PROJECT_ID.cloudfunctions.net/wasteMatcherTool \
  -H "Content-Type: application/json" \
  -d '{
    "parameters": {
      "waste_type": "fly_ash",
      "quantity": 500,
      "location": "Mumbai"
    }
  }'
```

## 📊 Monitoring

### View Logs
```bash
# Function logs
gcloud functions logs read geminiChat --limit 50

# Cloud Run logs
gcloud logging read "resource.type=cloud_run_revision"
```

### Monitor Database
Visit [Firebase Console](https://console.firebase.google.com) to monitor Firestore usage.

## 🚨 Troubleshooting

### Common Issues

1. **Gemini API Quota Exceeded**
   - Check your API usage in Google Cloud Console
   - Consider upgrading your quota

2. **CORS Issues**
   - Update `allowedOrigins` in config.json
   - Redeploy functions with updated CORS settings

3. **Database Connection Issues**
   - Verify Firestore is enabled
   - Check service account permissions

4. **Function Timeout**
   - Increase timeout for complex operations
   - Optimize database queries

### Debug Commands

```bash
# Check function status
gcloud functions describe FUNCTION_NAME

# Test function locally
functions-framework --target=geminiChat --port=8080

# Check Cloud Run status
gcloud run services describe cementcycle-app
```

## 🔄 Updates and Maintenance

### Update Functions
```bash
cd functions
npm run deploy:all
```

### Update Frontend
```bash
gcloud run deploy cementcycle-app --image gcr.io/PROJECT_ID/cementcycle-frontend
```

### Database Maintenance
```bash
# Backup Firestore
gcloud firestore export gs://PROJECT_ID-backup/$(date +%Y%m%d)

# Update sample data
python3 init_data_enhanced.py
```

## 🌍 Production Considerations

### Security
- Enable IAM authentication for production
- Use Secret Manager for API keys
- Implement rate limiting
- Add input validation

### Performance
- Enable Cloud CDN for static assets
- Use Cloud Load Balancer for high availability
- Monitor function performance
- Optimize database queries

### Scaling
- Configure auto-scaling for Cloud Run
- Use Cloud Functions concurrency settings
- Monitor Firestore usage and quotas

## 📞 Support

For technical support or questions:
- Check the logs first
- Review the troubleshooting section
- Open an issue in the repository
- Contact the development team

## 📝 License

This project is licensed under the MIT License. See LICENSE file for details.