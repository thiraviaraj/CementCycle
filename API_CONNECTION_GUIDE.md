# 🔗 CementCycle API Connection Guide

## Quick Setup to Connect Frontend with Backend

### 1. **Update API Endpoints in Frontend**

In `index_new.html`, find the `apiEndpoints` object and update with your actual Cloud Functions URLs:

```javascript
this.apiEndpoints = {
    chat: 'https://us-central1-cementcycle-hackathon-2025.cloudfunctions.net/geminiChat',
    wasteMatcher: 'https://us-central1-cementcycle-hackathon-2025.cloudfunctions.net/wasteMatcherTool',
    co2Calculator: 'https://us-central1-cementcycle-hackathon-2025.cloudfunctions.net/co2CalculatorTool',
    priceEstimator: 'https://us-central1-cementcycle-hackathon-2025.cloudfunctions.net/priceEstimatorTool',
    createMatch: 'https://us-central1-cementcycle-hackathon-2025.cloudfunctions.net/createMatch'
};
```

### 2. **Deploy Cloud Functions**

```bash
cd functions
npm install
npm run deploy:all
```

### 3. **Configure API Keys**

Update `config.json` with your actual credentials:
```json
{
    "projectId": "your-actual-project-id",
    "geminiApiKey": "your-gemini-api-key",
    "region": "us-central1"
}
```

### 4. **Test Local Development**

For local testing, run each function:
```bash
# Terminal 1
npm run start:chat      # Port 8080

# Terminal 2  
npm run start:matcher   # Port 8081

# Terminal 3
npm run start:co2       # Port 8082

# Terminal 4
npm run start:price     # Port 8083

# Terminal 5
npm run start:match     # Port 8084
```

### 5. **Connection Status Indicators**

The frontend now shows:
- ✅ **Live API** - Connected to deployed Cloud Functions with Gemini AI
- 🟡 **Connecting...** - Attempting to connect to backend
- ⚪ **Demo Mode** - Using mock data (no backend connection)
- ❌ **Error** - Connection failed

### 6. **API Integration Features**

✅ **Real Gemini AI responses** instead of mock responses
✅ **Live waste matching** with Firestore data  
✅ **Actual CO2 calculations** and environmental impact
✅ **Real-time pricing** from market intelligence
✅ **Database-backed matches** with notifications

### 7. **Testing the Connection**

1. Open `index_new.html` in browser
2. Check the status indicator in chat header
3. Try asking: "I have fly ash to sell"
4. Should get Gemini AI-powered response with real data

### 8. **Troubleshooting**

**If seeing "Demo Mode":**
- Check Cloud Functions are deployed
- Verify API endpoints URLs
- Check CORS settings allow your domain

**If seeing "Error":**
- Check browser console for specific error
- Verify API keys in config.json
- Ensure Gemini API is enabled

**For 500 errors:**
- Check Cloud Functions logs: `gcloud functions logs read geminiChat`
- Verify Firestore database is initialized

### 9. **Next Steps**

1. Deploy to Cloud Run for production hosting
2. Set up custom domain
3. Configure production API keys  
4. Monitor usage and costs

🚀 **Your CementCycle platform is now fully connected with Google Gemini AI!**