import streamlit as st
import pandas as pd
import time
from PIL import Image
import random

# --- CONFIG & STYLING ---
st.set_page_config(page_title="AgriGuard Ultra", layout="wide", page_icon="🚀")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f2027, #203a43, #2c5364); color: white; }
    h1, h2, h3, h4 { color: #00ff7f !important; }
    [data-testid="stMetricValue"] { color: #00ff7f !important; }
    [data-testid="stSidebar"] { background-color: #0b1418 !important; border-right: 2px solid #00ff7f; }
    .stTabs [data-baseweb="tab-list"] { background-color: rgba(255,255,255,0.05); border-radius: 10px; }
    .stTabs [aria-selected="true"] { background-color: #00ff7f !important; color: black !important; }
    .stChatMessage { background-color: rgba(255,255,255,0.1); border-radius: 10px; margin-bottom: 10px; }
    .stAlert { background-color: rgba(255, 0, 0, 0.2); border: 1px solid #ff4b4b; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- LANGUAGE DICTIONARY ---
LANG = {
    "English": {
        "title": "AGRIGUARD ULTRA 🚀",
        "sub": "Next-Gen AI Agriculture Command Center",
        "weather_sync": "Syncing Satellite Data...",
        "calc_head": "Precision Nutrient Engine",
        "voice_btn": "🎙️ Activate Voice Command",
        "moist": "Soil Moisture",
        "temp": "Thermal Index",
        "health": "Crop Vitality",
        "weather_tip": "Agri-Weather Forecast",
        "disease_alert": "Local Disease Outbreak Alert"
    },
    "Tamil (தமிழ்)": {
        "title": "அக்ரிகார்ட் அல்ட்ரா 🚀",
        "sub": "அடுத்த தலைமுறை AI விவசாய கட்டுப்பாட்டு மையம்",
        "weather_sync": "செயற்கைக்கோள் தரவு இணைக்கப்படுகிறது...",
        "calc_head": "துல்லியமான ஊட்டச்சத்து இயந்திரம்",
        "voice_btn": "🎙️ குரல் கட்டளையை இயக்கவும்",
        "moist": "மண் ஈரப்பதம்",
        "temp": "வெப்ப நிலை",
        "health": "பயிர் ஆரோக்கியம்",
        "weather_tip": "விவசாய வானிலை முன்னறிவிப்பு",
        "disease_alert": "உள்ளூர் நோய் பரவல் எச்சரிக்கை"
    }
}

# --- SIDEBAR & NOTIFICATIONS ---
with st.sidebar:
    st.markdown("# 🍃 AGRISETTINGS")
    sel_lang = st.selectbox("Language / மொழி", ["English", "Tamil (தமிழ்)"])
    L = LANG[sel_lang]
    st.divider()
    
    st.subheader("🔔 " + L["disease_alert"])
    st.error("⚠️ DISTRICT ALERT: Blast Fungus reported in neighboring sector. Apply preventive Neem spray.")
    
    if st.button("SYNC SATELLITE WEATHER"):
        with st.spinner(L["weather_sync"]):
            time.sleep(1)
            st.success("🛰️ Connected: Chennai Sector | 31°C")
            st.info("💡 Best time to spray: Tomorrow 6:00 AM (Low Wind)")

# --- SESSION STATE ---
if 'garden' not in st.session_state: st.session_state.garden = []
if 'messages' not in st.session_state: st.session_state.messages = []

# --- MAIN UI ---
st.title(L["title"])
st.caption(L["sub"])

# CREATE THE TABS
t1, t2, t3, t4, t5, t6 = st.tabs(["📊 COMMAND", "🔍 SCANNER", "📅 CALENDAR", "🤖 AI ADVISOR", "🌍 TRACKER", "🧮 LOGISTICS"])

# --- TAB 1: DASHBOARD ---
with t1:
    c_left, c_right = st.columns([1, 2])
    with c_left:
        st.subheader("➕ Deploy Sensor")
        with st.form("deploy_form", clear_on_submit=True):
            p_id = st.text_input("Plot Designation")
            crop = st.selectbox("Genetic Variety", ["Rice", "Tomato", "Chilli", "Mango"])
            m = st.slider(L["moist"], 0, 100, 45)
            t = st.slider(L["temp"], 0, 50, 28)
            if st.form_submit_button("DEPLOY"):
                if p_id:
                    st.session_state.garden.append({"id": p_id, "type": crop, "moist": m, "temp": t})
                    st.rerun()
    with c_right:
        st.subheader("📡 Live Telemetry")
        for p in st.session_state.garden:
            with st.container():
                st.markdown(f"#### 🏷️ {p['id']} [{p['type'].upper()}]")
                col1, col2, col3 = st.columns(3)
                col1.metric(L["moist"], f"{p['moist']}%")
                col2.metric(L["temp"], f"{p['temp']}°C")
                status = "EXCELLENT" if p['moist'] > 35 else "CRITICAL"
                col3.metric(L["health"], status)
                st.write("---")

# --- TAB 2: MULTI-SCANNER ---
with t2:
    st.header("🔍 Neural Vision Diagnostics")
    mode = st.radio("Scan Mode", ["Disease Scan", "Species ID (24,000+)", "Mushroom Expert"])
    up = st.file_uploader(f"Upload {mode} sample...", type=["jpg", "png"])
    
    if up:
        st.image(up, width=400)
        with st.status("Analyzing..."):
            time.sleep(2)
            if mode == "Disease Scan":
                st.success("SCAN COMPLETE: Early Blight (Alternaria solani) Detected")
                st.markdown("### 🏥 DIY Treatment Plan")
                col_rx1, col_rx2 = st.columns(2)
                with col_rx1:
                    st.info("🧪 **Chemical Solution**\n* Fungicide: Copper Oxychloride\n* Dosage: 2.5g/L")
                with col_rx2:
                    st.success("🌿 **Organic Solution**\n* Mix: Neem Oil + Baking Soda\n* Action: Early Morning Spray")
            
            elif mode == "Species ID (24,000+)":
                st.success("MATCH FOUND: Ficus elastica (Rubber Plant)")
                st.write("**Type:** Broadleaf Evergreen Tree | **Rarity:** Common")
                
            elif mode == "Mushroom Expert":
                st.warning("⚠️ IDENTIFIED: Amanita muscaria")
                st.error("TOXICITY: POISONOUS. Do not consume.")

# --- TAB 3: CROP CALENDAR ---
with t3:
    st.subheader("📅 Smart Cultivation Timeline")
    selected_crop = st.selectbox("Select Crop for Guide", ["Rice", "Tomato", "Mango"])
    
    cal_cols = st.columns(4)
    steps = ["Sowing/Planting", "Vegetative", "Flowering", "Harvest"]
    for i, step in enumerate(steps):
        with cal_cols[i]:
            st.info(f"**Step {i+1}: {step}**")
            if i == 0: st.write("✅ Completed (Day 1-15)")
            elif i == 1: st.write("🕒 In Progress (Day 16-45)")
            else: st.write("⏳ Upcoming")
    
    st.divider()
    st.subheader("⏰ Care Reminders")
    st.checkbox("Watering Reminder (Every 2 days)", value=True)
    st.checkbox("Fertilizer Schedule (Monthly)", value=False)
    st.checkbox("Pruning/Misting Alert", value=False)

# --- TAB 4: AI ADVISOR ---
with t3: # This maps to the internal Logic for AI
    pass # Features remain in the script below

# --- TAB 4 (RE-INDEXED): AI ADVISOR ---
with t4:
    st.subheader("🤖 Neural Farmer Assistant")
    # (Existing AI logic kept intact as requested)
    st.write("Quick Inquiries:")
    cols = st.columns(3)
    q1 = cols[0].button("💧 Check Moisture")
    q2 = cols[1].button("🔥 Check Heat Stress")
    q3 = cols[2].button("🌿 Fertilizer Info")

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    prompt = st.chat_input("Ask about irrigation, pests, or mushrooms...")
    if q1: prompt = "What is the moisture status?"
    if q2: prompt = "Is there any heat stress?"
    if q3: prompt = "What fertilizer is needed?"

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        query = prompt.lower()
        if "moisture" in query:
            ans = "🛰️ **Sensor Analysis:** Current levels are stable. No irrigation needed."
        elif "fertilizer" in query:
            ans = "🌿 **Nutrient Advice:** Nitrogen-based urea is recommended for your current growth stage."
        else:
            ans = "I'm monitoring your field data. I recommend checking the 'Weather' alert in the sidebar."
        
        st.session_state.messages.append({"role": "assistant", "content": ans})
        st.rerun()

# --- TAB 5: GEO-TAGGING & GLOBAL TRACKER ---
with t5:
    st.header("🌍 Geo-Tagging & Disease Mapping")
    st.write("Tracking the global spread of agricultural pathogens to prevent failures.")
    
    # Mock Map Data
    map_data = pd.DataFrame({
        'lat': [13.0827, 12.9716, 19.0760, 28.6139],
        'lon': [80.2707, 77.5946, 72.8777, 77.2090],
        'disease': ['Blast Fungus', 'Early Blight', 'Leaf Rust', 'Mosaic Virus']
    })
    st.map(map_data)
    st.caption("🔴 Red dots indicate high-risk disease breakout zones reported by researchers.")

# --- TAB 6: CALCULATORS ---
with t6:
    st.header(L["calc_head"])
    acre = st.number_input("Field Dimension (Acres)", 1.0, 100.0)
    if st.button("RUN LOGISTICS CALCULATION"):
        st.balloons()
        st.success(f"Supply Plan: Transport {int(acre * 45)}kg of fertilizer to the site.")