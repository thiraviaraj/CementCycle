"""
Enhanced CementCycle Database Initialization Script
Initializes Firestore with comprehensive sample data for the circular economy platform
"""

from google.cloud import firestore
import datetime
import random
import json
import os
from typing import Dict, List, Any

class CementCycleDataInitializer:
    """Initialize comprehensive sample data for CementCycle platform"""
    
    def __init__(self):
        """Initialize Firestore client and configuration"""
        self.db = firestore.Client()
        self.timestamp = datetime.datetime.now()
        
        # Load configuration
        self.config = self.load_config()
        
        print("🚀 CementCycle Database Initializer v2.0")
        print(f"📅 Timestamp: {self.timestamp}")
        print(f"🔗 Project: {self.config.get('projectId', 'default')}")
    
    def load_config(self) -> Dict[str, Any]:
        """Load configuration from config.json"""
        try:
            with open('config.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("⚠️  config.json not found, using default configuration")
            return {
                "database": {
                    "collections": {
                        "waste_listings": "waste_listings",
                        "cement_requirements": "cement_requirements",
                        "matches": "matches",
                        "users": "users",
                        "transactions": "transactions"
                    }
                }
            }
    
    def initialize_all_data(self):
        """Initialize all sample data collections"""
        print("\n🏗️  Initializing comprehensive sample data...")
        
        try:
            # Initialize core data
            self.initialize_waste_listings()
            self.initialize_cement_requirements()
            self.initialize_users()
            self.initialize_impact_metrics()
            self.initialize_price_history()
            self.initialize_market_intelligence()
            
            # Initialize derived data
            self.initialize_sample_matches()
            self.initialize_platform_metrics()
            self.initialize_notification_templates()
            
            print("\n✅ All sample data initialized successfully!")
            print("🌍 CementCycle platform ready for circular economy operations")
            
        except Exception as e:
            print(f"❌ Error during initialization: {str(e)}")
            raise

    def initialize_waste_listings(self):
        """Initialize comprehensive waste listings with enhanced metadata"""
        print("\n📦 Initializing enhanced waste listings...")
        
        waste_listings = [
            {
                "id": "w001",
                "type": "fly_ash",
                "type_display": "Fly Ash (Grade A)",
                "quantity": 500,
                "unit": "tons",
                "location": "Mumbai",
                "state": "Maharashtra",
                "company": "ABC Power Plant Ltd",
                "contact_person": "Rajesh Kumar",
                "email": "waste@abcpower.com",
                "phone": "+91-9876543210",
                "quality_grade": "grade_a",
                "quality_certifications": ["ASTM C618", "IS 3812"],
                "chemical_composition": {
                    "sio2": 55.2,
                    "al2o3": 28.4,
                    "fe2o3": 6.8,
                    "cao": 3.1,
                    "loss_on_ignition": 2.8
                },
                "physical_properties": {
                    "fineness": 320,
                    "specific_gravity": 2.24,
                    "moisture_content": 0.5
                },
                "price_expected": 3200,
                "price_negotiable": True,
                "available_date": self.timestamp,
                "expiry_date": self.timestamp + datetime.timedelta(days=90),
                "co2_savings_potential": 400,
                "status": "available",
                "storage_location": "Covered warehouse, Port connectivity",
                "transportation": "Rail/Road accessible",
                "pickup_preference": "bulk_only",
                "minimum_order": 50,
                "packaging": "Bulk/Pneumatic tankers",
                "testing_reports_available": True,
                "environmental_clearance": True,
                "created_at": self.timestamp,
                "updated_at": self.timestamp,
                "tags": ["power_plant", "thermal", "grade_a", "high_quality"],
                "seasonal_availability": "year_round",
                "production_rate": "100 tons/day"
            },
            {
                "id": "w002", 
                "type": "steel_slag",
                "type_display": "Steel Slag (Grade 1)",
                "quantity": 300,
                "unit": "tons",
                "location": "Chennai",
                "state": "Tamil Nadu",
                "company": "XYZ Steel Mills Pvt Ltd",
                "contact_person": "Priya Sharma",
                "email": "sales@xyzsteel.com",
                "phone": "+91-9876543211",
                "quality_grade": "grade_1",
                "quality_certifications": ["IS 383", "ASTM C989"],
                "chemical_composition": {
                    "sio2": 35.8,
                    "al2o3": 12.4,
                    "fe2o3": 1.2,
                    "cao": 42.6,
                    "mgo": 6.8
                },
                "physical_properties": {
                    "fineness": 280,
                    "specific_gravity": 2.85,
                    "moisture_content": 1.0
                },
                "price_expected": 2800,
                "price_negotiable": True,
                "available_date": self.timestamp,
                "expiry_date": self.timestamp + datetime.timedelta(days=60),
                "co2_savings_potential": 210,
                "status": "available",
                "storage_location": "Open yard, covered storage available",
                "transportation": "Truck loading facility",
                "pickup_preference": "flexible",
                "minimum_order": 25,
                "packaging": "Loose bulk",
                "testing_reports_available": True,
                "environmental_clearance": True,
                "created_at": self.timestamp,
                "updated_at": self.timestamp,
                "tags": ["steel_mill", "blast_furnace", "grade_1", "infrastructure"],
                "seasonal_availability": "year_round",
                "production_rate": "150 tons/day"
            },
            {
                "id": "w003",
                "type": "silica_fume",
                "type_display": "Silica Fume (Premium)",
                "quantity": 150,
                "unit": "tons",
                "location": "Bangalore",
                "state": "Karnataka", 
                "company": "Tech Industries Corp",
                "contact_person": "Amit Patel",
                "email": "waste@techindustries.com",
                "phone": "+91-9876543212",
                "quality_grade": "premium",
                "quality_certifications": ["ASTM C1240", "IS 15388"],
                "chemical_composition": {
                    "sio2": 92.8,
                    "al2o3": 1.2,
                    "fe2o3": 0.8,
                    "cao": 0.4,
                    "loss_on_ignition": 2.1
                },
                "physical_properties": {
                    "fineness": 15000,
                    "specific_gravity": 2.22,
                    "moisture_content": 0.3
                },
                "price_expected": 5200,
                "price_negotiable": False,
                "available_date": self.timestamp,
                "expiry_date": self.timestamp + datetime.timedelta(days=45),
                "co2_savings_potential": 180,
                "status": "limited_stock",
                "storage_location": "Climate controlled warehouse",
                "transportation": "Specialized pneumatic handling",
                "pickup_preference": "scheduled_only",
                "minimum_order": 10,
                "packaging": "Sealed bags/Silos",
                "testing_reports_available": True,
                "environmental_clearance": True,
                "created_at": self.timestamp,
                "updated_at": self.timestamp,
                "tags": ["silicon_industry", "premium", "high_performance", "concrete"],
                "seasonal_availability": "limited",
                "production_rate": "20 tons/day"
            },
            {
                "id": "w004",
                "type": "bottom_ash",
                "type_display": "Bottom Ash (Standard)",
                "quantity": 800,
                "unit": "tons",
                "location": "Pune",
                "state": "Maharashtra",
                "company": "Green Energy Solutions",
                "contact_person": "Sunita Reddy",
                "email": "materials@greenenergy.com",
                "phone": "+91-9876543213",
                "quality_grade": "standard",
                "quality_certifications": ["IS 383", "Local pollution board clearance"],
                "chemical_composition": {
                    "sio2": 48.5,
                    "al2o3": 22.1,
                    "fe2o3": 8.9,
                    "cao": 4.2,
                    "loss_on_ignition": 3.8
                },
                "physical_properties": {
                    "fineness": 150,
                    "specific_gravity": 2.15,
                    "moisture_content": 2.0
                },
                "price_expected": 2000,
                "price_negotiable": True,
                "available_date": self.timestamp,
                "expiry_date": self.timestamp + datetime.timedelta(days=120),
                "co2_savings_potential": 480,
                "status": "available",
                "storage_location": "Large open stockyard",
                "transportation": "Conveyor/Truck loading",
                "pickup_preference": "bulk_preferred",
                "minimum_order": 100,
                "packaging": "Bulk transport",
                "testing_reports_available": True,
                "environmental_clearance": True,
                "created_at": self.timestamp,
                "updated_at": self.timestamp,
                "tags": ["power_plant", "thermal", "aggregate", "road_construction"],
                "seasonal_availability": "year_round",
                "production_rate": "200 tons/day"
            }
        ]
        
        collection_name = self.config['database']['collections']['waste_listings']
        for waste in waste_listings:
            doc_ref = self.db.collection(collection_name).document(waste['id'])
            doc_ref.set(waste)
            print(f"  ✓ Added {waste['type_display']} - {waste['quantity']} tons")
        
        print(f"📦 Initialized {len(waste_listings)} waste listings")

    def initialize_cement_requirements(self):
        """Initialize cement plant requirements with detailed specifications"""
        print("\n🏭 Initializing cement plant requirements...")
        
        cement_requirements = [
            {
                "id": "c001",
                "company": "PQR Cement Industries Ltd",
                "plant_name": "Mumbai Manufacturing Unit",
                "location": "Mumbai",
                "state": "Maharashtra",
                "contact_person": "Vikram Singh",
                "email": "procurement@pqrcement.com",
                "phone": "+91-9876543220",
                "materials_needed": ["fly_ash", "bottom_ash"],
                "primary_material": "fly_ash",
                "monthly_capacity": 1000,
                "current_inventory": 150,
                "urgency": "high",
                "price_offered": 3200,
                "price_range": {
                    "min": 3000,
                    "max": 3400
                },
                "quality_requirements": {
                    "grade": "grade_a",
                    "certifications_required": ["ASTM C618", "IS 3812"],
                    "chemical_specs": {
                        "sio2_min": 50,
                        "al2o3_min": 25,
                        "loss_on_ignition_max": 5
                    }
                },
                "delivery_preferences": {
                    "method": "bulk_pneumatic",
                    "frequency": "weekly",
                    "lead_time_days": 7,
                    "storage_capacity": 500
                },
                "logistics_support": {
                    "pickup_available": True,
                    "transport_provided": True,
                    "loading_facilities": "pneumatic_systems"
                },
                "payment_terms": {
                    "method": "bank_transfer",
                    "days": 30,
                    "advance_percentage": 0
                },
                "active": True,
                "contract_type": "spot_purchase",
                "rating": 4.8,
                "total_purchases_ytd": 8500,
                "preferred_suppliers": ["ABC Power Plant Ltd"],
                "compliance_requirements": ["environmental_clearance", "quality_certificates"],
                "created_at": self.timestamp,
                "updated_at": self.timestamp,
                "last_purchase_date": self.timestamp - datetime.timedelta(days=15),
                "sustainability_goals": {
                    "co2_reduction_target": 2000,
                    "waste_utilization_target": 80,
                    "circular_economy_certified": True
                }
            },
            {
                "id": "c002",
                "company": "LMN Cement Corporation",
                "plant_name": "Chennai Coastal Plant",
                "location": "Chennai",
                "state": "Tamil Nadu",
                "contact_person": "Meera Nair",
                "email": "sourcing@lmnindustries.com",
                "phone": "+91-9876543221",
                "materials_needed": ["steel_slag", "silica_fume"],
                "primary_material": "steel_slag",
                "monthly_capacity": 800,
                "current_inventory": 80,
                "urgency": "medium",
                "price_offered": 2750,
                "price_range": {
                    "min": 2500,
                    "max": 2900
                },
                "quality_requirements": {
                    "grade": "grade_1",
                    "certifications_required": ["IS 383", "ASTM C989"],
                    "chemical_specs": {
                        "cao_min": 35,
                        "sio2_min": 30,
                        "fineness_min": 250
                    }
                },
                "delivery_preferences": {
                    "method": "truck_bulk",
                    "frequency": "bi_weekly",
                    "lead_time_days": 10,
                    "storage_capacity": 400
                },
                "logistics_support": {
                    "pickup_available": True,
                    "transport_provided": False,
                    "loading_facilities": "conveyor_belt"
                },
                "payment_terms": {
                    "method": "bank_transfer",
                    "days": 45,
                    "advance_percentage": 10
                },
                "active": True,
                "contract_type": "annual_contract",
                "rating": 4.6,
                "total_purchases_ytd": 6200,
                "preferred_suppliers": ["XYZ Steel Mills Pvt Ltd"],
                "compliance_requirements": ["quality_certificates", "transport_permits"],
                "created_at": self.timestamp,
                "updated_at": self.timestamp,
                "last_purchase_date": self.timestamp - datetime.timedelta(days=22),
                "sustainability_goals": {
                    "co2_reduction_target": 1500,
                    "waste_utilization_target": 75,
                    "circular_economy_certified": True
                }
            }
        ]
        
        collection_name = self.config['database']['collections']['cement_requirements']
        for requirement in cement_requirements:
            doc_ref = self.db.collection(collection_name).document(requirement['id'])
            doc_ref.set(requirement)
            print(f"  ✓ Added {requirement['company']} - {requirement['monthly_capacity']} tons/month capacity")
        
        print(f"🏭 Initialized {len(cement_requirements)} cement plant requirements")

    def initialize_users(self):
        """Initialize user profiles with role-based access"""
        print("\n👥 Initializing user profiles...")
        
        users = [
            {
                "id": "u001",
                "email": "rajesh.kumar@abcpower.com",
                "name": "Rajesh Kumar",
                "role": "waste_supplier",
                "company": "ABC Power Plant Ltd",
                "phone": "+91-9876543210",
                "location": "Mumbai",
                "verification_status": "verified",
                "profile_completeness": 95,
                "joined_date": self.timestamp - datetime.timedelta(days=180),
                "last_active": self.timestamp - datetime.timedelta(hours=2),
                "preferences": {
                    "notification_channels": ["email", "sms", "platform"],
                    "language": "english",
                    "currency": "INR",
                    "time_zone": "Asia/Kolkata"
                },
                "business_details": {
                    "industry": "power_generation",
                    "company_size": "large",
                    "annual_waste_volume": 6000,
                    "waste_types": ["fly_ash", "bottom_ash"],
                    "certifications": ["ISO 14001", "Pollution Control Board"]
                },
                "performance_metrics": {
                    "total_transactions": 15,
                    "total_revenue": 1800000,
                    "average_rating": 4.8,
                    "co2_impact": 1200
                },
                "subscription": {
                    "plan": "premium",
                    "started": self.timestamp - datetime.timedelta(days=90),
                    "expires": self.timestamp + datetime.timedelta(days=275)
                }
            }
        ]
        
        collection_name = self.config['database']['collections']['users']
        for user in users:
            doc_ref = self.db.collection(collection_name).document(user['id'])
            doc_ref.set(user)
            print(f"  ✓ Added user {user['name']} ({user['role']})")
        
        print(f"👥 Initialized {len(users)} user profiles")

    def initialize_impact_metrics(self):
        """Initialize environmental impact tracking"""
        print("\n🌍 Initializing impact metrics...")
        
        impact_data = {
            "id": "current_impact",
            "total_co2_saved": 12500,
            "total_waste_processed": 8750,
            "total_revenue_generated": 2300000,
            "total_matches_created": 156,
            "active_suppliers": 45,
            "active_buyers": 32,
            "monthly_growth": {
                "co2_savings": 8.5,
                "waste_volume": 12.3,
                "revenue": 15.7
            },
            "quarterly_targets": {
                "co2_savings": 15000,
                "waste_volume": 12000,
                "new_suppliers": 60
            },
            "timestamp": self.timestamp,
            "last_updated": self.timestamp
        }
        
        self.db.collection('impact_metrics').document('current').set(impact_data)
        print("🌍 Impact metrics initialized")

    def initialize_price_history(self):
        """Initialize historical pricing data"""
        print("\n💰 Initializing price history...")
        
        materials = ['fly_ash', 'steel_slag', 'silica_fume', 'bottom_ash']
        
        for material in materials:
            for i in range(6):  # 6 months of data
                date = self.timestamp - datetime.timedelta(days=30*i)
                
                # Simulate price variations
                base_prices = {
                    'fly_ash': 2800,
                    'steel_slag': 2200,
                    'silica_fume': 4500,
                    'bottom_ash': 1800
                }
                
                variation = random.uniform(0.85, 1.15)
                price = int(base_prices[material] * variation)
                
                price_record = {
                    "material": material,
                    "price_per_ton": price,
                    "region": "national_average",
                    "quality_grade": "standard",
                    "timestamp": date,
                    "market_conditions": random.choice(["high_demand", "stable", "low_demand"])
                }
                
                self.db.collection('price_history').add(price_record)
        
        print(f"💰 Price history initialized for {len(materials)} materials")

    def initialize_market_intelligence(self):
        """Initialize market intelligence data"""
        print("\n📊 Initializing market intelligence...")
        
        market_data = {
            "id": "current_market",
            "overall_market": {
                "growth_rate": 12.5,
                "market_sentiment": "positive",
                "demand_level": "high",
                "supply_constraints": "moderate"
            },
            "timestamp": self.timestamp,
            "last_updated": self.timestamp
        }
        
        self.db.collection('market_intelligence').document('current').set(market_data)
        print("📊 Market intelligence initialized")

    def initialize_sample_matches(self):
        """Initialize sample successful matches"""
        print("\n🔗 Initializing sample matches...")
        
        matches = [
            {
                "id": "m001",
                "waste_id": "w001",
                "requirement_id": "c001",
                "status": "completed",
                "match_score": 92,
                "quantity_agreed": 400,
                "price_agreed": 3200,
                "total_value": 1280000,
                "created_at": self.timestamp - datetime.timedelta(days=30),
                "completed_at": self.timestamp - datetime.timedelta(days=20),
                "co2_savings_achieved": 320
            }
        ]
        
        collection_name = self.config['database']['collections']['matches']
        for match in matches:
            doc_ref = self.db.collection(collection_name).document(match['id'])
            doc_ref.set(match)
            print(f"  ✓ Added match {match['id']} ({match['status']})")
        
        print(f"🔗 Initialized {len(matches)} sample matches")

    def initialize_platform_metrics(self):
        """Initialize platform performance metrics"""
        print("\n📈 Initializing platform metrics...")
        
        metrics = {
            "id": "platform_performance",
            "operational_metrics": {
                "uptime_percentage": 99.8,
                "avg_response_time_ms": 450,
                "successful_matches_rate": 98.5,
                "user_satisfaction": 4.7
            },
            "timestamp": self.timestamp,
            "last_calculated": self.timestamp
        }
        
        self.db.collection('platform_metrics').document('current').set(metrics)
        print("📈 Platform metrics initialized")

    def initialize_notification_templates(self):
        """Initialize notification templates"""
        print("\n📧 Initializing notification templates...")
        
        templates = [
            {
                "id": "match_created",
                "type": "email",
                "subject": "🎉 New Match Found - CementCycle",
                "template": "A new match has been found for your {material_type}. Match score: {match_score}%",
                "variables": ["material_type", "match_score", "company_name"],
                "active": True
            }
        ]
        
        for template in templates:
            self.db.collection('notification_templates').document(template['id']).set(template)
        
        print(f"📧 Initialized {len(templates)} notification templates")

if __name__ == "__main__":
    try:
        initializer = CementCycleDataInitializer()
        initializer.initialize_all_data()
        
        print("\n🎊 CementCycle Database Initialization Complete!")
        print("=" * 60)
        print("✅ All collections created with comprehensive sample data")
        print("🔄 Platform ready for circular economy operations")
        print("🌍 Environmental impact tracking enabled")
        print("💰 Price intelligence and market data available")
        print("🤖 AI-powered matching system initialized")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Initialization failed: {str(e)}")
        exit(1)