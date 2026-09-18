"""
AGROLINK Backend API - FastAPI Application
Provides endpoints for AI Analysis, Demand Forecasting, Buyer Alerts,
Company Matching, Supply Aggregation, Smart Logistics, Order Tracking,
Admin Oversight, and Multilingual Voice Processing.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any, List, Optional
import uvicorn

try:
    from .database import (
        MARKET_SNAPSHOT,
        BUYER_ALERTS,
        COMPANY_MATCHES,
        SUPPLY_AGGREGATION,
        ORDER_AGL1024,
        ADMIN_OVERVIEW
    )
    from .ai_engine import (
        forecast_crop_demand,
        analyze_produce_image,
        compute_company_matches
    )
    from .logistics import get_optimized_route
    from .nlp_voice import process_voice_query
except ImportError:
    from database import (
        MARKET_SNAPSHOT,
        BUYER_ALERTS,
        COMPANY_MATCHES,
        SUPPLY_AGGREGATION,
        ORDER_AGL1024,
        ADMIN_OVERVIEW
    )
    from ai_engine import (
        forecast_crop_demand,
        analyze_produce_image,
        compute_company_matches
    )
    from logistics import get_optimized_route
    from nlp_voice import process_voice_query

import os
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="AGROLINK API",
    description="Move Produce Where Demand Is. AI-powered direct procurement connecting farmers and FPOs with enterprise buyers.",
    version="1.0.0"
)

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request Models
class FreshnessRequest(BaseModel):
    crop: str = "Tomato"
    image_url: Optional[str] = None
    variety: Optional[str] = "Hybrid Roma"
    quantity_kg: Optional[float] = 2000.0

class VoiceQueryRequest(BaseModel):
    query: str
    language: str = "en"

class ProduceListingRequest(BaseModel):
    farmer_name: str = "Ramesh"
    crop: str = "Tomato"
    variety: str = "Hybrid Roma"
    quantity_kg: float = 2000.0
    expected_price: float = 32.0
    harvest_date: str = "2024-09-22"
    location: str = "Coimbatore"
    latitude: Optional[float] = 10.9850
    longitude: Optional[float] = 76.9200
    freshness_grade: Optional[str] = "High"

class RequirementPostRequest(BaseModel):
    company_name: str = "ABC Foods"
    crop: str = "Tomato"
    quantity_kg: float = 10000.0
    location: str = "Coimbatore"
    required_by: str = "25 Sep 2024"
    price_min: float = 30.0
    price_max: float = 34.0
    quality_spec: str = "Grade A, firm ripe"

# In-memory mutable state for live interactive demonstrations
live_orders = dict(ORDER_AGL1024)
live_alerts = list(BUYER_ALERTS)
live_listings: List[Dict[str, Any]] = [
    {
        "id": "list-1",
        "farmer_name": "Ramesh",
        "crop": "Tomato",
        "variety": "Hybrid Roma",
        "quantity_kg": 2000,
        "price_per_kg": 32,
        "freshness": "High (87% confidence)",
        "location": "Coimbatore (18 km)",
        "status": "Ready for Dispatch"
    }
]

@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AGROLINK Core Engine",
        "version": "1.0.0",
        "tagline": "Move Produce Where Demand Is."
    }

@app.get("/api/market-snapshot")
def get_market_snapshot():
    return MARKET_SNAPSHOT

@app.get("/api/buyer-alerts")
def get_buyer_alerts():
    return live_alerts

@app.get("/api/company-matches")
def get_company_matches(crop: str = "Tomato", location: str = "Coimbatore", quantity: float = 2000):
    return compute_company_matches(crop=crop, farmer_location=location, farmer_qty_kg=quantity)

@app.get("/api/demand-forecast/{crop}")
def get_demand_forecast(crop: str, weeks: int = 4):
    return forecast_crop_demand(crop=crop, horizon_weeks=weeks)

@app.post("/api/ai-freshness")
def analyze_freshness(payload: FreshnessRequest):
    return analyze_produce_image(crop=payload.crop)

@app.get("/api/supply-aggregation")
def get_supply_aggregation():
    return SUPPLY_AGGREGATION

@app.get("/api/logistics-route")
def get_logistics_route():
    return get_optimized_route()

@app.get("/api/order-tracking")
def get_order_tracking(order_id: str = "AGL1024"):
    return live_orders

@app.post("/api/order-tracking/advance")
def advance_order_status():
    """Simulates moving Order #AGL1024 to Delivered and then Payment settled."""
    curr_status = live_orders["status"]
    if curr_status == "In Transit":
        live_orders["status"] = "Delivered"
        live_orders["current_status_note"] = "Produce received at ABC Foods Sulur Hub. Digital weighbridge and QA approved."
        live_orders["estimated_arrival"] = "Completed at 01:15 PM"
        for item in live_orders["timeline"]:
            if item["stage"] == "DELIVERED":
                item["completed"] = True
    elif curr_status == "Delivered":
        live_orders["status"] = "Payment Released"
        live_orders["current_status_note"] = "₹3,20,000 paid to 4 suppliers via Instant Escrow UPI Settlement."
        live_orders["estimated_arrival"] = "Settled at 01:25 PM"
        for item in live_orders["timeline"]:
            if item["stage"] in ["DELIVERED", "PAYMENT"]:
                item["completed"] = True
    else:
        # Reset to In Transit for demo loop
        live_orders["status"] = "In Transit"
        live_orders["current_status_note"] = "On the way to ABC Foods"
        live_orders["estimated_arrival"] = "1 hr 20 mins"
        for item in live_orders["timeline"]:
            if item["stage"] in ["DELIVERED", "PAYMENT"]:
                item["completed"] = False

    return live_orders

@app.get("/api/admin-overview")
def get_admin_overview():
    return ADMIN_OVERVIEW

@app.post("/api/voice-query")
def voice_query(payload: VoiceQueryRequest):
    return process_voice_query(query=payload.query, language=payload.language)

@app.post("/api/post-requirement")
def post_requirement(req: RequirementPostRequest):
    new_alert = {
        "id": f"alert-{len(live_alerts) + 1}",
        "company_id": "comp-abc",
        "company_name": req.company_name,
        "logo": "🏢",
        "crop": req.crop,
        "quantity_kg": req.quantity_kg,
        "location": f"{req.location} (Hub)",
        "distance_km": 12,
        "required_by": req.required_by,
        "price_range": f"₹{int(req.price_min)}–₹{int(req.price_max)}/kg",
        "min_price": req.price_min,
        "max_price": req.price_max,
        "quality_spec": req.quality_spec,
        "verified": True,
        "status": "active",
        "is_advance": True,
        "note": "Immediate advance procurement requirement open for farmer cluster aggregation."
    }
    live_alerts.insert(0, new_alert)
    return {"status": "success", "alert": new_alert}

@app.post("/api/add-produce")
def add_produce(listing: ProduceListingRequest):
    new_item = {
        "id": f"list-{len(live_listings) + 1}",
        "farmer_name": listing.farmer_name,
        "crop": listing.crop,
        "variety": listing.variety,
        "quantity_kg": listing.quantity_kg,
        "price_per_kg": listing.expected_price,
        "freshness": f"{listing.freshness_grade} (87% confidence)",
        "location": f"{listing.location} (Auto-tagged)",
        "status": "Ready for Aggregation"
    }
    live_listings.insert(0, new_item)
    return {"status": "success", "listing": new_item}

frontend_dist = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend", "dist")
if os.path.exists(frontend_dist):
    app.mount("/", StaticFiles(directory=frontend_dist, html=True), name="static_frontend")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
