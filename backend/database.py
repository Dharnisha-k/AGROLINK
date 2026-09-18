"""
AGROLINK - Seeded Database & In-Memory Store
Provides realistic mock data for the demo scenario:
- Ramesh (Farmer in Coimbatore, 2,000 kg Tomato)
- ABC Foods (Enterprise Buyer in Coimbatore, 10,000 kg Tomato)
- Aggregated suppliers: Green Valley FPO, Ramesh, Anbu FPO, Kumar
- Order #AGL1024
"""

from typing import Dict, List, Any

# Market prices & 24h trends
MARKET_SNAPSHOT = [
    {
        "id": "tomato",
        "name": "Tomato",
        "local_name": "தக்காளி (Tamatar)",
        "variety": "Hybrid Roma / Shivam",
        "current_price": 28.0,
        "unit": "kg",
        "change_pct": 12.0,
        "trend": "up",
        "icon": "🍅",
        "image": "https://images.unsplash.com/photo-1592924357228-91a4daadcfea?w=500&auto=format&fit=crop&q=80",
        "modal_price": 27.5,
        "min_price": 24.0,
        "max_price": 34.0,
        "market_arrivals_tons": 142.5
    },
    {
        "id": "onion",
        "name": "Onion",
        "local_name": "வெங்காயம் (Pyaaz)",
        "variety": "Bellary Red",
        "current_price": 22.0,
        "unit": "kg",
        "change_pct": 5.0,
        "trend": "up",
        "icon": "🧅",
        "image": "https://images.unsplash.com/photo-1618512496248-a07fe83aa8cb?w=500&auto=format&fit=crop&q=80",
        "modal_price": 21.0,
        "min_price": 19.0,
        "max_price": 26.0,
        "market_arrivals_tons": 280.0
    },
    {
        "id": "potato",
        "name": "Potato",
        "local_name": "உருளைக்கிழங்கு (Aaloo)",
        "variety": "Kufri Jyoti",
        "current_price": 18.0,
        "unit": "kg",
        "change_pct": -3.0,
        "trend": "down",
        "icon": "🥔",
        "image": "https://images.unsplash.com/photo-1518977676601-b53f82aba655?w=500&auto=format&fit=crop&q=80",
        "modal_price": 18.5,
        "min_price": 16.0,
        "max_price": 22.0,
        "market_arrivals_tons": 310.0
    },
    {
        "id": "banana",
        "name": "Banana",
        "local_name": "வாழைப்பழம் (Kela)",
        "variety": "G9 Cavendish",
        "current_price": 24.0,
        "unit": "kg",
        "change_pct": 8.0,
        "trend": "up",
        "icon": "🍌",
        "image": "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?w=500&auto=format&fit=crop&q=80",
        "modal_price": 23.0,
        "min_price": 20.0,
        "max_price": 28.0,
        "market_arrivals_tons": 95.0
    }
]

# Buyer Demand Alerts (Advance procurement notifications)
BUYER_ALERTS = [
    {
        "id": "alert-1",
        "company_id": "comp-abc",
        "company_name": "ABC Foods",
        "logo": "🏢",
        "crop": "Tomato",
        "quantity_kg": 3000,
        "location": "Coimbatore (12 km)",
        "distance_km": 12,
        "required_by": "25 Sep 2024",
        "price_range": "₹30–₹34/kg",
        "min_price": 30,
        "max_price": 34,
        "quality_spec": "Firm ripe, visual grade A, min 5 days shelf life",
        "verified": True,
        "status": "active",
        "is_advance": True,
        "note": "Early procurement announcement for sauce and purée batch processing."
    },
    {
        "id": "alert-2",
        "company_id": "comp-freshmart",
        "company_name": "FreshMart",
        "logo": "🛒",
        "crop": "Onion",
        "quantity_kg": 5000,
        "location": "Tiruppur (28 km)",
        "distance_km": 28,
        "required_by": "28 Sep 2024",
        "price_range": "₹22–₹26/kg",
        "min_price": 22,
        "max_price": 26,
        "quality_spec": "Medium-large, dry skin, moisture < 14%",
        "verified": True,
        "status": "active",
        "is_advance": True,
        "note": "Advance regional retail stock planning."
    },
    {
        "id": "alert-3",
        "company_id": "comp-southindia",
        "company_name": "South India Retail",
        "logo": "🏬",
        "crop": "Potato",
        "quantity_kg": 2000,
        "location": "Erode (35 km)",
        "distance_km": 35,
        "required_by": "27 Sep 2024",
        "price_range": "₹18–₹22/kg",
        "min_price": 18,
        "max_price": 22,
        "quality_spec": "No sprouting, clean skin, Grade A",
        "verified": True,
        "status": "active",
        "is_advance": True,
        "note": "Bulk replenishment for weekly hypermarket dispatch."
    }
]

# AI Company Matches for Farmer Ramesh (Tomato produce)
COMPANY_MATCHES = [
    {
        "id": "match-1",
        "company_id": "comp-abc",
        "company_name": "ABC Foods",
        "match_score": 94,
        "crop": "Tomato",
        "location": "Coimbatore (12 km)",
        "distance_km": 12,
        "requires_kg": 10000,
        "price_range": "₹30–₹34/kg",
        "reason": "High demand + nearby location + good price match",
        "tier": "Enterprise Premier",
        "fulfillment_type": "Direct Farmgate Pickup",
        "payment_terms": "Instant UPI upon digital dispatch verification"
    },
    {
        "id": "match-2",
        "company_id": "comp-freshmart",
        "company_name": "FreshMart",
        "match_score": 86,
        "crop": "Tomato",
        "location": "Tiruppur (28 km)",
        "distance_km": 28,
        "requires_kg": 5000,
        "price_range": "₹28–₹32/kg",
        "reason": "Good demand + location match",
        "tier": "Retail Chain",
        "fulfillment_type": "FPO Consolidation Point",
        "payment_terms": "T+1 Day Settlement"
    },
    {
        "id": "match-3",
        "company_id": "comp-agrofresh",
        "company_name": "AgroFresh Processing",
        "match_score": 78,
        "crop": "Tomato",
        "location": "Salem (65 km)",
        "distance_km": 65,
        "requires_kg": 8000,
        "price_range": "₹26–₹30/kg",
        "reason": "Matches quality requirement + bulk buyer",
        "tier": "Food Processor",
        "fulfillment_type": "Central Processing Hub",
        "payment_terms": "T+2 Days Settlement"
    }
]

# Supply Aggregation Details for 10,000 kg Tomato
SUPPLY_AGGREGATION = {
    "crop": "Tomato",
    "target_requirement_kg": 10000,
    "aggregated_kg": 10000,
    "remaining_kg": 0,
    "status": "Fully Aggregated",
    "buyer": "ABC Foods",
    "destination": "ABC Foods Processing Unit, Sulur / Coimbatore",
    "destination_coords": [11.0268, 77.1265],
    "suppliers": [
        {
            "id": "sup-1",
            "name": "Green Valley FPO",
            "type": "FPO (Consortium)",
            "quantity_kg": 4000,
            "location": "Coimbatore (12 km)",
            "lat": 11.0500,
            "lng": 76.9900,
            "status": "Ready for Dispatch",
            "contact": "+91 94432 10001"
        },
        {
            "id": "sup-2",
            "name": "Ramesh (Farmer)",
            "type": "Individual Farmer",
            "quantity_kg": 2000,
            "location": "Coimbatore (18 km)",
            "lat": 10.9850,
            "lng": 76.9200,
            "status": "Ready for Dispatch",
            "contact": "+91 98421 22334"
        },
        {
            "id": "sup-3",
            "name": "Anbu FPO",
            "type": "FPO (Consortium)",
            "quantity_kg": 3000,
            "location": "Tiruppur (28 km)",
            "lat": 11.1085,
            "lng": 77.3411,
            "status": "Ready for Dispatch",
            "contact": "+91 97890 33445"
        },
        {
            "id": "sup-4",
            "name": "Kumar (Farmer)",
            "type": "Individual Farmer",
            "quantity_kg": 1000,
            "location": "Tiruppur (32 km)",
            "lat": 11.1350,
            "lng": 77.3800,
            "status": "Ready for Dispatch",
            "contact": "+91 98940 55667"
        }
    ],
    "logistics": {
        "truck_assigned": "TN-37-BY-4512 (10-Ton Reefer Truck)",
        "driver": "Selvam Murugan (+91 94430 88990)",
        "total_distance_km": 68,
        "estimated_time": "2 hrs 15 mins",
        "route_order": [
            "Start: Kumar (Tiruppur)",
            "Stop 2: Anbu FPO (Tiruppur)",
            "Stop 3: Green Valley FPO (Coimbatore North)",
            "Stop 4: Ramesh (Coimbatore West)",
            "Destination: ABC Foods Hub (Sulur, Coimbatore)"
        ]
    }
}

# Order #AGL1024 Tracking State
ORDER_AGL1024 = {
    "order_id": "AGL1024",
    "crop": "Tomato",
    "total_quantity_kg": 10000,
    "buyer": "ABC Foods",
    "seller_group": "Coimbatore & Tiruppur Farmer Cluster",
    "total_amount": 320000,
    "rate_per_kg": 32.0,
    "status": "In Transit",
    "current_status_note": "On the way to ABC Foods",
    "estimated_arrival": "1 hr 20 mins",
    "truck_number": "TN-37-BY-4512",
    "driver_name": "Selvam Murugan",
    "driver_phone": "+91 94430 88990",
    "timeline": [
        {
            "stage": "CONFIRMED",
            "title": "Order Confirmed",
            "date": "20 Sep 2024",
            "time": "10:00 AM",
            "completed": True,
            "description": "ABC Foods verified 10,000 kg aggregation contract."
        },
        {
            "stage": "COLLECTION",
            "title": "Produce Collected",
            "date": "21 Sep 2024",
            "time": "09:00 AM",
            "completed": True,
            "description": "Multi-stop pickup completed across 4 farmgate locations."
        },
        {
            "stage": "IN TRANSIT",
            "title": "In Transit",
            "date": "21 Sep 2024",
            "time": "11:30 AM",
            "completed": True,
            "description": "Reefer vehicle on NH544 toward ABC Foods Sulur Hub."
        },
        {
            "stage": "DELIVERED",
            "title": "Delivered to Hub",
            "date": "21 Sep 2024",
            "time": "01:15 PM (Est.)",
            "completed": False,
            "description": "Weighbridge confirmation and digital QA inspection."
        },
        {
            "stage": "PAYMENT",
            "title": "Payment Released",
            "date": "21 Sep 2024",
            "time": "01:30 PM (Est.)",
            "completed": False,
            "description": "₹3,20,000 released directly to farmer/FPO bank accounts via smart escrow."
        }
    ]
}

# Admin Overview Analytics Data
ADMIN_OVERVIEW = {
    "stats": {
        "farmers_fpos": 1248,
        "companies": 86,
        "produce_listings": 5320,
        "orders": 1102,
        "total_tons_traded": 52400,
        "avg_farmer_income_gain": "+31.4%"
    },
    "monthly_trade_tons": [
        {"month": "Jun", "tons": 3200},
        {"month": "Jul", "tons": 4100},
        {"month": "Aug", "tons": 4800},
        {"month": "Sep", "tons": 5400}
    ],
    "crop_distribution": [
        {"name": "Tomato", "percentage": 35, "color": "#ef4444"},
        {"name": "Onion", "percentage": 20, "color": "#f97316"},
        {"name": "Potato", "percentage": 15, "color": "#eab308"},
        {"name": "Banana", "percentage": 10, "color": "#22c55e"},
        {"name": "Others", "percentage": 20, "color": "#065f46"}
    ],
    "recent_activities": [
        {
            "id": "act-1",
            "time": "5 mins ago",
            "action": "New Requirement Posted",
            "details": "ABC Foods posted a new requirement for 10,000 kg Tomato",
            "type": "requirement"
        },
        {
            "id": "act-2",
            "time": "22 mins ago",
            "action": "Produce Listing Verified",
            "details": "Ramesh (Coimbatore) listed 2,000 kg Grade-A Tomato",
            "type": "listing"
        },
        {
            "id": "act-3",
            "time": "45 mins ago",
            "action": "Supply Aggregated",
            "details": "Cluster AGL-TN-102 completed 10,000 kg Tomato aggregation",
            "type": "aggregation"
        },
        {
            "id": "act-4",
            "time": "1 hour ago",
            "action": "Logistics Dispatched",
            "details": "Order #AGL1024 vehicle TN-37-BY-4512 departed Tiruppur",
            "type": "order"
        },
        {
            "id": "act-5",
            "time": "3 hours ago",
            "action": "FPO Onboarding",
            "details": "Anbu FPO verified with 45 member farmers",
            "type": "verification"
        }
    ]
}
