import streamlit as st
import requests
import datetime
import time

# from exception.exceptions import TradingBotException
import sys

BASE_URL = "http://localhost:8000"  # Backend endpoint

st.set_page_config(
    page_title="✈️ AI Travel Planner - Your Personal Travel Assistant",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for better styling
st.markdown("""
<style>
    /* Main header styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .main-header h1 {
        color: white;
        font-size: 3rem;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        color: #f0f0f0;
        font-size: 1.2rem;
        margin: 0.5rem 0 0 0;
    }
    
    /* Feature cards */
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        text-align: center;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    
    .feature-card h3 {
        color: #333;
        margin-bottom: 0.5rem;
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        border-radius: 25px;
        border: 2px solid #667eea;
        padding: 15px 20px;
        font-size: 16px;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #764ba2;
        box-shadow: 0 0 10px rgba(102, 126, 234, 0.3);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 15px 30px;
        font-size: 16px;
        font-weight: bold;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 7px 20px rgba(0,0,0,0.3);
    }
    
    /* Result container */
    .result-container {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Animation keyframes */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .animate-fade-in {
        animation: fadeIn 0.8s ease-out;
    }
    
    /* Stats cards */
    .stats-card {
        background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Main header with gradient background
st.markdown("""
<div class="main-header animate-fade-in">
    <h1>✈️ AI Travel Planner</h1>
    <p>Your Personal Intelligent Travel Assistant</p>
</div>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Create columns for layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Feature showcase
    st.markdown("""
    <div class="feature-card animate-fade-in">
        <h3>🎯 Smart Trip Planning</h3>
        <p>Get personalized travel recommendations based on your preferences, budget, and interests</p>
    </div>
    """, unsafe_allow_html=True)

# Stats row
stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)

with stats_col1:
    st.markdown("""
    <div class="stats-card">
        <h2>🌎</h2>
        <h4>200+</h4>
        <p>Destinations</p>
    </div>
    """, unsafe_allow_html=True)

with stats_col2:
    st.markdown("""
    <div class="stats-card">
        <h2>🏨</h2>
        <h4>50K+</h4>
        <p>Hotels</p>
    </div>
    """, unsafe_allow_html=True)

with stats_col3:
    st.markdown("""
    <div class="stats-card">
        <h2>✈️</h2>
        <h4>1000+</h4>
        <p>Airlines</p>
    </div>
    """, unsafe_allow_html=True)

with stats_col4:
    st.markdown("""
    <div class="stats-card">
        <h2>⭐</h2>
        <h4>4.9</h4>
        <p>Rating</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Sidebar with additional features
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 10px; margin-bottom: 1rem;">
        <h2 style="color: white;">🎒 Travel Tools</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🔧 Quick Actions")
    
    if st.button("🌤️ Weather Check", use_container_width=True):
        st.info("Weather checking feature coming soon!")
    
    if st.button("💱 Currency Converter", use_container_width=True):
        st.info("Currency conversion feature coming soon!")
    
    if st.button("📊 Budget Planner", use_container_width=True):
        st.info("Budget planning feature coming soon!")
    
    st.markdown("---")
    st.markdown("### 📋 Popular Destinations")
    
    popular_destinations = [
        "🏝️ Maldives", "🗼 Paris", "🍜 Tokyo", "🏛️ Rome", 
        "🕌 Istanbul", "🏖️ Bali", "🗽 New York", "🐨 Sydney"
    ]
    
    for dest in popular_destinations:
        if st.button(dest, use_container_width=True, key=f"dest_{dest}"):
            st.session_state.suggested_destination = dest.split(' ', 1)[1]

# Main content area
st.markdown("""
<div style="text-align: center; margin: 2rem 0;">
    <h2 style="color: #333; margin-bottom: 1rem;">🗨️ Chat with Your Travel Assistant</h2>
    <p style="color: #666; font-size: 1.1rem;">Tell me where you want to go and I'll create the perfect itinerary for you!</p>
</div>
""", unsafe_allow_html=True)

# Enhanced chat input with better styling
st.markdown("### 💬 Start Planning Your Adventure")

# Create input container
input_col1, input_col2, input_col3 = st.columns([1, 3, 1])

with input_col2:
    with st.form(key="query_form", clear_on_submit=True):
        # Check if there's a suggested destination from sidebar
        placeholder_text = "e.g. Plan a 5-day romantic trip to Paris with a budget of $3000"
        if "suggested_destination" in st.session_state:
            placeholder_text = f"Plan a trip to {st.session_state.suggested_destination}"
            
        user_input = st.text_input(
            "",
            placeholder=placeholder_text,
            help="💡 Be specific about your destination, duration, budget, and preferences for better results!"
        )
        
        # Submit button with custom styling
        submit_col1, submit_col2, submit_col3 = st.columns([1, 1, 1])
        with submit_col2:
            submit_button = st.form_submit_button("🚀 Plan My Trip", use_container_width=True)

# Example prompts
st.markdown("### 💡 Example Prompts")
example_col1, example_col2 = st.columns(2)

with example_col1:
    if st.button("🏖️ Beach Vacation in Australia", use_container_width=True):
        st.session_state.example_query = "Plan a 7-day beach vacation in Australia with water sports and local cuisine experiences"
        
    if st.button("🏔️ Adventure in Himalayas", use_container_width=True):
        st.session_state.example_query = "Plan a 10-day trekking adventure in the Himalayas with budget accommodation"

with example_col2:
    if st.button("🏛️ Cultural Tour of Berlin", use_container_width=True):
        st.session_state.example_query = "Plan a 14-day cultural tour of Berlin covering museums, historical sites, and local cuisine"
        
    if st.button("🌴 Backpacking in Turkey", use_container_width=True):
        st.session_state.example_query = "Plan a 8-day backpacking trip through Turkey covering historical sites, natural wonders, and local cuisine"

# Check for example query selection
if "example_query" in st.session_state:
    user_input = st.session_state.example_query
    submit_button = True
    del st.session_state.example_query

if submit_button and user_input.strip():
    try:
        # Create progress container
        progress_container = st.container()
        
        with progress_container:
            # Enhanced loading animation
            progress_col1, progress_col2, progress_col3 = st.columns([1, 2, 1])
            
            with progress_col2:
                st.markdown("""
                <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; margin: 1rem 0;">
                    <h3 style="color: white; margin: 0;">🤖 AI is crafting your perfect trip...</h3>
                    <p style="color: #f0f0f0; margin: 0.5rem 0 0 0;">Analyzing destinations, weather, and activities</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Animated progress bar
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                # Simulate processing steps
                steps = [
                    "🔍 Searching destinations...",
                    "🌤️ Checking weather conditions...",
                    "🏨 Finding best accommodations...",
                    "🍽️ Discovering local cuisine...",
                    "🎯 Creating personalized itinerary...",
                    "✨ Adding final touches..."
                ]
                
                for i, step in enumerate(steps):
                    status_text.text(step)
                    progress_bar.progress((i + 1) / len(steps))
                    time.sleep(0.3)  # Small delay for effect

        # Clear progress indicators
        progress_container.empty()
        
        # API call
        payload = {"question": user_input}
        response = requests.post(f"{BASE_URL}/query", json=payload)

        if response.status_code == 200:
            answer = response.json().get("answer", "No answer returned.")
            
            # Success animation and result display
            st.balloons()  # Celebration animation
            
            # Create result container with enhanced styling
            st.markdown("""
            <div class="result-container animate-fade-in">
                <div style="text-align: center; margin-bottom: 2rem;">
                    <h1 style="color: #333; margin: 0;">🎉 Your Perfect Trip Plan is Ready!</h1>
                    <p style="color: #666; font-size: 1.1rem; margin: 0.5rem 0 0 0;">Generated by AI • Personalized for You</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Trip details with enhanced formatting
            markdown_content = f"""
# 🌍 **AI-Generated Travel Itinerary**

> **📅 Generated:** {datetime.datetime.now().strftime('%B %d, %Y at %I:%M %p')}  
> **🤖 Created by:** Atriyo's AI Travel Assistant  
> **📝 Query:** "{user_input}"

---

{answer}

---

### 📋 **Important Notes**
- 🔍 **Verification Required:** Please verify all information including prices, operating hours, and travel requirements
- 📱 **Save This Plan:** Consider bookmarking or saving this itinerary for easy access
- 💬 **Need Changes?** Feel free to ask for modifications or additional information
- ⭐ **Enjoy Your Trip:** Have an amazing adventure!

---

*✨ This personalized travel plan was generated using advanced AI technology. For the most accurate and up-to-date information, please verify details with official sources before booking.*
            """
            
            st.markdown(markdown_content)
            
            # Action buttons after result
            action_col1, action_col2, action_col3, action_col4 = st.columns(4)
            
            with action_col1:
                if st.button("📧 Email Plan", use_container_width=True):
                    st.info("Email feature coming soon!")
                    
            with action_col2:
                if st.button("💾 Save Plan", use_container_width=True):
                    st.success("Plan saved to your account!")
                    
            with action_col3:
                if st.button("🔄 Modify Plan", use_container_width=True):
                    st.info("Ask me to modify any part of the plan!")
                    
            with action_col4:
                if st.button("⭐ Rate Plan", use_container_width=True):
                    st.info("Rating feature coming soon!")
                    
        else:
            st.error("🚨 Oops! Something went wrong. Please try again: " + response.text)

    except Exception as e:
        st.error(f"🚨 The response failed due to: {e}")
        st.info("💡 Please check your internet connection and try again.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); border-radius: 15px; margin-top: 3rem;">
    <h3 style="color: #333; margin-bottom: 1rem;">🌟 Why Choose Our AI Travel Planner?</h3>
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
        <div style="margin: 1rem; text-align: center;">
            <h2>🤖</h2>
            <h4>AI-Powered</h4>
            <p>Advanced algorithms for personalized recommendations</p>
        </div>
        <div style="margin: 1rem; text-align: center;">
            <h2>⚡</h2>
            <h4>Instant Results</h4>
            <p>Get your travel plan in seconds, not hours</p>
        </div>
        <div style="margin: 1rem; text-align: center;">
            <h2>🎯</h2>
            <h4>Personalized</h4>
            <p>Tailored to your budget, interests, and preferences</p>
        </div>
        <div style="margin: 1rem; text-align: center;">
            <h2>🔄</h2>
            <h4>Flexible</h4>
            <p>Easy to modify and adjust your plans anytime</p>
        </div>
    </div>
    <p style="color: #666; margin-top: 2rem;">Made with ❤️ by Rizwan Rizwan• Powered by Langgraph</p>
</div>
""", unsafe_allow_html=True)