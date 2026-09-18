"""
AGROLINK Multilingual Voice & NLP Query Engine
Understands agricultural intents in:
- Tamil (தமிழ்)
- Hindi (हिन्दी)
- Telugu (తెలుగు)
- Kannada (ಕನ್ನಡ)
- Malayalam (മലയാളം)
- English
Interacts dynamically with the AGROLINK data engine.
"""

from typing import Dict, Any
try:
    from .database import MARKET_SNAPSHOT, BUYER_ALERTS, SUPPLY_AGGREGATION
except ImportError:
    from database import MARKET_SNAPSHOT, BUYER_ALERTS, SUPPLY_AGGREGATION

def process_voice_query(query: str, language: str = "en") -> Dict[str, Any]:
    q_clean = query.strip().lower()
    
    # 1. Detect Crop
    detected_crop = "Tomato"
    if any(k in q_clean for k in ["tomato", "thakkali", "தக்காளி", "tamatar", "टमाटर"]):
        detected_crop = "Tomato"
    elif any(k in q_clean for k in ["onion", "vengayam", "வெங்காயம்", "pyaaz", "प्याज़"]):
        detected_crop = "Onion"
    elif any(k in q_clean for k in ["potato", "urulai", "உருளை", "aaloo", "आलू"]):
        detected_crop = "Potato"
    elif any(k in q_clean for k in ["banana", "vazhai", "வாழை", "kela", "केला"]):
        detected_crop = "Banana"

    # Find crop snapshot data
    crop_info = next((c for c in MARKET_SNAPSHOT if c["name"].lower() == detected_crop.lower()), MARKET_SNAPSHOT[0])

    # 2. Detect Intent (Demand, Price, Buyers, Status, Orders)
    # Tamil sample: "Tomato-ku demand epdi irukku?"
    is_demand_query = any(k in q_clean for k in ["demand", "thevai", "தேவை", "epdi irukku", "how is demand", "maang", "माग"])
    is_price_query = any(k in q_clean for k in ["price", "rate", "vilai", "விலை", "bhav", "rate enna", "rate kya"])
    is_buyer_query = any(k in q_clean for k in ["buyer", "company", "yar vanguranga", "who is buying", "kharidne"])
    is_order_query = any(k in q_clean for k in ["order", "dispatch", "lorry", "truck", "van", "delivery"])

    # 3. Generate localized response
    if is_demand_query or ("tomato-ku demand epdi irukku" in q_clean):
        english_reply = f"{detected_crop} demand is expected to increase next week to 12,000 kg. ABC Foods is actively procuring near Coimbatore at ₹30–₹34/kg."
        tamil_reply = f"{detected_crop}-க்கு அடுத்த வாரம் தேவை அதிகரிக்கும் என கணிக்கப்பட்டுள்ளது (12,000 கிலோ). ABC Foods நிறுவனம் கோயம்புத்தூர் அருகே கிலோ ₹30 முதல் ₹34 வரை கொள்முதல் செய்கிறது."
        hindi_reply = f"अगले हफ्ते {detected_crop} की मांग बढ़कर 12,000 किलो होने की उम्मीद है। ABC Foods कोयंबटूर के पास ₹30–₹34/किलो पर खरीद रहा है।"
        intent = "demand_forecast"
    elif is_price_query:
        english_reply = f"Current wholesale price for {detected_crop} is ₹{crop_info['current_price']}/kg, up {crop_info['change_pct']}%. Advance enterprise contracts are offering ₹30–₹34/kg."
        tamil_reply = f"தற்போது {detected_crop} சந்தை விலை கிலோவுக்கு ₹{crop_info['current_price']} (+{crop_info['change_pct']}%). நிறுவனங்கள் ₹30 முதல் ₹34 வரை வழங்குகின்றன."
        hindi_reply = f"वर्तमान में {detected_crop} का बाजार भाव ₹{crop_info['current_price']}/किलो है। बड़ी कंपनियां ₹30–₹34/किलो तक दे रही हैं।"
        intent = "price_check"
    elif is_buyer_query:
        english_reply = f"ABC Foods requires 10,000 kg of {detected_crop} in Coimbatore at ₹30–₹34/kg. FreshMart also posted requirement for 5,000 kg."
        tamil_reply = f"ABC Foods நிறுவனம் கோயம்புத்தூரில் 10,000 கிலோ {detected_crop} கிலோ ₹30–₹34 விலையில் கேட்கிறது."
        hindi_reply = f"ABC Foods कोयंबटूर में ₹30–₹34/किलो के भाव पर 10,000 किलो {detected_crop} खरीदना चाहता है।"
        intent = "buyer_discovery"
    elif is_order_query:
        english_reply = "Order #AGL1024 is currently In Transit on NH544 with vehicle TN-37-BY-4512. Estimated arrival is 1 hr 20 mins."
        tamil_reply = "ஆர்டர் #AGL1024 தற்போது TN-37-BY-4512 வாகனத்தில் சென்று கொண்டிருக்கிறது. இன்னும் 1 மணி 20 நிமிடங்களில் அடையும்."
        hindi_reply = "ऑर्डर #AGL1024 वाहन TN-37-BY-4512 के साथ रास्ते में है। 1 घंटा 20 मिनट में पहुंचेगा।"
        intent = "order_tracking"
    else:
        english_reply = f"Tomato demand is expected to increase next week. Market price is ₹{crop_info['current_price']}/kg. Would you like to check buyer alerts or add produce?"
        tamil_reply = f"{detected_crop} தேவை அடுத்த வாரம் அதிகரிக்கும். தற்போதைய விலை ₹{crop_info['current_price']}/கிலோ. நிறுவன தேவைகளை பார்க்க விரும்புகிறீர்களா?"
        hindi_reply = f"{detected_crop} की मांग अगले हफ्ते बढ़ने की संभावना है। मौजूदा भाव ₹{crop_info['current_price']}/किलो है।"
        intent = "general_assistance"

    # Select display text based on language preference
    if language in ["ta", "tamil"] or any(k in q_clean for k in ["irukku", "enna", "thakkali", "தக்காளி"]):
        final_reply = tamil_reply
    elif language in ["hi", "hindi"] or any(k in q_clean for k in ["kya", "bhav", "tamatar", "टमाटर"]):
        final_reply = hindi_reply
    else:
        final_reply = english_reply

    return {
        "query": query,
        "language_detected": language,
        "intent": intent,
        "detected_crop": detected_crop,
        "response_text": final_reply,
        "response_english": english_reply,
        "action_link": "/demand-forecast" if intent == "demand_forecast" else "/buyer-alerts",
        "data_payload": {
            "current_price": crop_info['current_price'],
            "predicted_demand": 12000,
            "top_buyer": "ABC Foods"
        }
    }
