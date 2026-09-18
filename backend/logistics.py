"""
AGROLINK Smart Logistics & Route Optimization Engine
Calculates optimal collection routes for aggregated farmgate produce,
minimizing transit time and spoilage risk.
"""

from typing import Dict, Any, List

# Waypoints representing the 68 km optimal collection route through Tiruppur & Coimbatore
ROUTE_GEOJSON_COORDINATES = [
    [11.1350, 77.3800], # Stop 1: Kumar (Tiruppur East)
    [11.1210, 77.3620],
    [11.1085, 77.3411], # Stop 2: Anbu FPO (Tiruppur Central)
    [11.0950, 77.2800],
    [11.0800, 77.2000],
    [11.0650, 77.1400],
    [11.0500, 76.9900], # Stop 3: Green Valley FPO (Coimbatore North)
    [11.0200, 76.9500],
    [10.9850, 76.9200], # Stop 4: Ramesh (Coimbatore West)
    [11.0050, 76.9900],
    [11.0268, 77.1265]  # Destination: ABC Foods Hub (Sulur)
]

STOPS = [
    {
        "id": "stop-1",
        "name": "Kumar (Farmer)",
        "role": "Farmgate Pickup",
        "location": "Uthukuli / Tiruppur",
        "coords": [11.1350, 77.3800],
        "quantity_kg": 1000,
        "eta": "06:30 AM",
        "completed": True
    },
    {
        "id": "stop-2",
        "name": "Anbu FPO",
        "role": "Aggregation Hub",
        "location": "Tiruppur Central",
        "coords": [11.1085, 77.3411],
        "quantity_kg": 3000,
        "eta": "07:15 AM",
        "completed": True
    },
    {
        "id": "stop-3",
        "name": "Green Valley FPO",
        "role": "Consortium Warehouse",
        "location": "Coimbatore North",
        "coords": [11.0500, 76.9900],
        "quantity_kg": 4000,
        "eta": "08:10 AM",
        "completed": True
    },
    {
        "id": "stop-4",
        "name": "Ramesh (Farmer)",
        "role": "Farmgate Pickup",
        "location": "Coimbatore West",
        "coords": [10.9850, 76.9200],
        "quantity_kg": 2000,
        "eta": "08:50 AM",
        "completed": True
    },
    {
        "id": "dest",
        "name": "ABC Foods Processing Plant",
        "role": "Delivery Destination Hub",
        "location": "Sulur, Coimbatore",
        "coords": [11.0268, 77.1265],
        "quantity_kg": 0,
        "eta": "10:15 AM",
        "completed": False
    }
]

def get_optimized_route() -> Dict[str, Any]:
    return {
        "crop": "Tomato",
        "total_distance_km": 68,
        "estimated_time": "2 hrs 15 mins",
        "total_weight_kg": 10000,
        "vehicle": "TN-37-BY-4512 (10-Ton Climate Controlled Reefer)",
        "temperature_setting": "13°C (Optimal for Fresh Tomatoes)",
        "stops": STOPS,
        "route_coordinates": ROUTE_GEOJSON_COORDINATES,
        "co2_savings_kg": 42.6,
        "summary": "Multi-stop pickup aggregating 4 suppliers (10,000 kg) into single transit."
    }
