#!/usr/bin/env python3
"""
CementCycle Platform Test Suite
Comprehensive testing for the enhanced platform
"""

import requests
import json
import time
from datetime import datetime

class CementCycleTests:
    def __init__(self, base_url, project_id, region="us-central1"):
        self.base_url = base_url
        self.project_id = project_id
        self.region = region
        self.functions_base = f"https://{region}-{project_id}.cloudfunctions.net"
        
        print("🧪 CementCycle Platform Test Suite")
        print(f"🔗 Base URL: {base_url}")
        print(f"⚡ Functions: {self.functions_base}")
        print("=" * 50)

    def test_frontend(self):
        """Test frontend accessibility"""
        print("\n🌐 Testing Frontend...")
        try:
            response = requests.get(self.base_url, timeout=10)
            if response.status_code == 200:
                print("✅ Frontend is accessible")
                if "CementCycle" in response.text:
                    print("✅ Content loads correctly")
                else:
                    print("⚠️  Content may not be loading properly")
            else:
                print(f"❌ Frontend returned status code: {response.status_code}")
        except Exception as e:
            print(f"❌ Frontend test failed: {str(e)}")

    def test_gemini_chat(self):
        """Test Gemini AI chat functionality"""
        print("\n🤖 Testing Gemini Chat Function...")
        
        test_cases = [
            {
                "message": "I have 500 tons of fly ash to sell",
                "context": {"location": "Mumbai"}
            },
            {
                "message": "Calculate CO2 impact for 300 tons steel slag",
                "context": {"location": "Chennai"}
            },
            {
                "message": "Show current market prices",
                "context": {}
            }
        ]
        
        for i, test_case in enumerate(test_cases, 1):
            try:
                print(f"  Test {i}: {test_case['message'][:30]}...")
                response = requests.post(
                    f"{self.functions_base}/geminiChat",
                    json=test_case,
                    timeout=30,
                    headers={"Content-Type": "application/json"}
                )
                
                if response.status_code == 200:
                    data = response.json()
                    if "response" in data:
                        print(f"  ✅ Test {i} passed - Got AI response")
                    else:
                        print(f"  ⚠️  Test {i} - Unexpected response format")
                else:
                    print(f"  ❌ Test {i} failed - Status: {response.status_code}")
                    
            except Exception as e:
                print(f"  ❌ Test {i} failed: {str(e)}")
            
            time.sleep(1)  # Rate limiting

    def test_waste_matcher(self):
        """Test waste matching functionality"""
        print("\n🔍 Testing Waste Matcher Function...")
        
        test_data = {
            "parameters": {
                "waste_type": "fly_ash",
                "quantity": 500,
                "location": "Mumbai",
                "quality_grade": "grade_a"
            }
        }
        
        try:
            response = requests.post(
                f"{self.functions_base}/wasteMatcherTool",
                json=test_data,
                timeout=15,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                data = response.json()
                if "fulfillmentResponse" in data:
                    print("✅ Waste matcher is working")
                    messages = data.get("fulfillmentResponse", {}).get("messages", [])
                    if messages:
                        print(f"✅ Found match recommendations")
                else:
                    print("⚠️  Unexpected response format")
            else:
                print(f"❌ Waste matcher failed - Status: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Waste matcher test failed: {str(e)}")

    def test_co2_calculator(self):
        """Test CO2 calculation functionality"""
        print("\n🌍 Testing CO2 Calculator Function...")
        
        test_data = {
            "parameters": {
                "waste_type": "steel_slag",
                "quantity": 300,
                "location": "Chennai"
            }
        }
        
        try:
            response = requests.post(
                f"{self.functions_base}/co2CalculatorTool",
                json=test_data,
                timeout=15,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                data = response.json()
                if "fulfillmentResponse" in data:
                    print("✅ CO2 calculator is working")
                    messages = data.get("fulfillmentResponse", {}).get("messages", [])
                    if messages and "CO2" in str(messages):
                        print("✅ CO2 calculations are being performed")
                else:
                    print("⚠️  Unexpected response format")
            else:
                print(f"❌ CO2 calculator failed - Status: {response.status_code}")
                
        except Exception as e:
            print(f"❌ CO2 calculator test failed: {str(e)}")

    def test_price_estimator(self):
        """Test price estimation functionality"""
        print("\n💰 Testing Price Estimator Function...")
        
        test_data = {
            "parameters": {
                "waste_type": "silica_fume",
                "location": "Bangalore",
                "quantity": 150,
                "quality_grade": "premium"
            }
        }
        
        try:
            response = requests.post(
                f"{self.functions_base}/priceEstimatorTool",
                json=test_data,
                timeout=15,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                data = response.json()
                if "fulfillmentResponse" in data:
                    print("✅ Price estimator is working")
                    messages = data.get("fulfillmentResponse", {}).get("messages", [])
                    if messages and ("₹" in str(messages) or "price" in str(messages).lower()):
                        print("✅ Price calculations are being performed")
                else:
                    print("⚠️  Unexpected response format")
            else:
                print(f"❌ Price estimator failed - Status: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Price estimator test failed: {str(e)}")

    def test_match_creation(self):
        """Test match creation functionality"""
        print("\n🔗 Testing Match Creation Function...")
        
        test_data = {
            "wasteId": "w001",
            "requirementId": "c001",
            "userInfo": {
                "name": "Test User",
                "email": "test@example.com"
            },
            "contactPreference": "email"
        }
        
        try:
            response = requests.post(
                f"{self.functions_base}/createMatch",
                json=test_data,
                timeout=15,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    print("✅ Match creation is working")
                    if "matchId" in data:
                        print(f"✅ Match ID generated: {data['matchId']}")
                else:
                    print("⚠️  Match creation may have issues")
            else:
                print(f"❌ Match creation failed - Status: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Match creation test failed: {str(e)}")

    def run_all_tests(self):
        """Run comprehensive test suite"""
        print(f"\n🚀 Starting comprehensive tests at {datetime.now()}")
        print("=" * 60)
        
        # Run all tests
        self.test_frontend()
        self.test_gemini_chat()
        self.test_waste_matcher()
        self.test_co2_calculator()
        self.test_price_estimator()
        self.test_match_creation()
        
        print("\n" + "=" * 60)
        print("🎯 Test Suite Complete!")
        print("\n📋 Next Steps:")
        print("• Review any failed tests above")
        print("• Check Cloud Function logs for errors")
        print("• Verify Gemini API key is configured")
        print("• Test the web interface manually")
        print("\n📊 For monitoring:")
        print("• Cloud Console: https://console.cloud.google.com")
        print("• Firebase Console: https://console.firebase.google.com")

if __name__ == "__main__":
    # Configuration - Update these values
    PROJECT_ID = input("Enter your Google Cloud Project ID: ").strip()
    
    # Construct URLs
    REGION = "us-central1"
    CLOUD_RUN_URL = f"https://cementcycle-app-{PROJECT_ID}.run.app"
    
    # Ask user for custom URL if needed
    custom_url = input(f"Frontend URL (press Enter for default: {CLOUD_RUN_URL}): ").strip()
    if custom_url:
        CLOUD_RUN_URL = custom_url
    
    # Run tests
    tester = CementCycleTests(CLOUD_RUN_URL, PROJECT_ID, REGION)
    tester.run_all_tests()