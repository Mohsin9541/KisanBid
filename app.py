
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import plotly.express as px

# ==========================================
# 1. PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AgriSense | Smart Agriculture",
    page_icon="🌾",
    layout="wide"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR, "models", "kisanbid_model.pkl"
)

DATA_PATH = os.path.join(
    BASE_DIR, "dataset",
    "jk_farm_bidding_eda_dataset.csv"
)

# ==========================================
# 2. CUSTOM DESIGN
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #F5F7F2;
    color: #203B2B;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background: #153B2A;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

.main .block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1350px;
}

.hero {
    background: linear-gradient(120deg, #123B29, #347A48);
    padding: 38px;
    border-radius: 22px;
    margin-bottom: 28px;
    color: white;
    box-shadow: 0 10px 30px rgba(24,65,39,.12);
}

.hero h1 {
    font-size: 43px;
    color: white;
    font-weight: 800;
    margin-bottom: 8px;
}

.hero p {
    font-size: 16px;
    color: #DDEBDD;
}

.hero-tag {
    color: #F3D98B;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
}

.info-card {
    background: white;
    border: 1px solid #E4EADF;
    border-radius: 17px;
    padding: 22px;
    min-height: 125px;
    box-shadow: 0 4px 15px rgba(20,50,30,.04);
}

.info-card h3 {
    color: #28583A;
    font-size: 27px;
    margin: 8px 0 0 0;
}

.info-card p {
    color: #758576;
    font-size: 13px;
    margin: 0;
}

.section-card {
    background: white;
    border: 1px solid #E4EADF;
    border-radius: 18px;
    padding: 24px;
    margin-bottom: 18px;
}

.section-heading {
    color: #245638;
    font-size: 21px;
    font-weight: 800;
}

.result-card {
    background: linear-gradient(120deg, #17482E, #367C47);
    padding: 30px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin: 20px 0;
}

.result-card h1 {
    color: #F7E4A6;
    font-size: 43px;
}

.result-card p {
    color: #E1F0E2;
}

div.stButton > button,
div.stFormSubmitButton > button {
    background: linear-gradient(90deg, #286C3C, #4B9755);
    color: white;
    border: 0;
    border-radius: 11px;
    min-height: 48px;
    font-weight: 700;
}

div.stButton > button:hover,
div.stFormSubmitButton > button:hover {
    background: #17482E;
    color: white;
    border: 0;
}

[data-testid="stMetric"] {
    background: white;
    border: 1px solid #E1E9DC;
    border-radius: 14px;
    padding: 17px;
}

h1, h2, h3 {
    color: #214C31;
}

.footer {
    text-align: center;
    padding: 28px;
    color: #758576;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. LOAD FILES
# ==========================================

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

if not os.path.exists(MODEL_PATH):
    st.error("Model file missing. Check the models folder.")
    st.stop()

if not os.path.exists(DATA_PATH):
    st.error("Dataset missing. Check the dataset folder.")
    st.stop()

try:
    model = load_model()
    df = load_data()
except Exception as e:
    st.error(f"Loading error: {e}")
    st.stop()

# ==========================================
# 4. CLEAN DROPDOWN VALUES
# ==========================================

for col in ["district", "crop", "grade", "season"]:
    df[col] = df[col].astype("string").str.strip()

df["district"] = df["district"].str.title()
df["crop"] = df["crop"].str.title()
df["grade"] = df["grade"].str.upper()
df["season"] = df["season"].str.title()

df["variety"] = df["variety"].astype("string").str.strip()
df["storage_type"] = df["storage_type"].astype("string").str.strip()

districts = sorted(df["district"].dropna().unique())
crops = sorted(df["crop"].dropna().unique())
grades = sorted(df["grade"].dropna().unique())
seasons = sorted(df["season"].dropna().unique())
storage_types = sorted(df["storage_type"].dropna().unique())

# ==========================================
# 5. SIDEBAR NAVIGATION
# ==========================================

with st.sidebar:

    st.markdown("# 🌾 KisanBid")
    st.caption("SMART AGRICULTURAL MARKETPLACE")

    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "Dashboard",
            "Price Prediction",
            "Market Analytics",
            "About Us"
        ]
    )

    st.divider()

    st.markdown("### PLATFORM DETAILS")

    st.write("📍 Jammu & Kashmir")
    st.write("🤖 Random Forest ML")
    st.write("📊 Agricultural Analytics")

    st.divider()

    st.caption("Connecting farmers with opportunities.")

# ==========================================
# 6. HERO
# ==========================================

st.markdown("""
<div class="hero">
    <div class="hero-tag">SMART FARMING · SMARTER MARKETS</div>
    <h1>🌾 KisanBid</h1>
    <h3 style="color:#FFFFFF">
        Your harvest deserves a better market.
    </h3>
    <p>
        Empowering Jammu & Kashmir farmers with
        intelligent price predictions and wider
        market opportunities across India.
    </p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 7. DASHBOARD
# ==========================================

if page == "Dashboard":

    st.subheader("Welcome to KisanBid")
    st.write("Your agricultural intelligence dashboard.")

    total_listings = len(df)
    total_crops = df["crop"].nunique()
    total_districts = df["district"].nunique()

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="info-card">
            <p>DATASET RECORDS</p>
            <h3>{total_listings:,}</h3>
            <p>Agricultural listings</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="info-card">
            <p>CROP CATEGORIES</p>
            <h3>{total_crops}</h3>
            <p>Different crop types</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="info-card">
            <p>DISTRICTS</p>
            <h3>{total_districts}</h3>
            <p>Regional coverage in dataset</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.subheader("Explore Agricultural Markets")

    left, right = st.columns(2)

    with left:
        crop_counts = df["crop"].value_counts().reset_index()
        crop_counts.columns = ["Crop", "Listings"]

        fig = px.bar(
            crop_counts,
            x="Crop",
            y="Listings",
            title="Crop-wise Listings",
            color="Listings",
            color_continuous_scale=["#B7D9B0", "#23643A"]
        )

        fig.update_layout(
            plot_bgcolor="white",
            paper_bgcolor="white",
            font_color="#234A31"
        )

        st.plotly_chart(fig, use_container_width=True)

    with right:
        district_counts = df["district"].value_counts().reset_index()
        district_counts.columns = ["District", "Listings"]

        fig = px.pie(
            district_counts,
            names="District",
            values="Listings",
            title="District-wise Listings",
            hole=0.45
        )

        st.plotly_chart(fig, use_container_width=True)

    st.info(
        "Explore Price Prediction to estimate a starting "
        "price for an individual crop listing."
    )

# ==========================================
# 8. PRICE PREDICTION
# ==========================================

elif page == "Price Prediction":

    st.subheader("AI Agricultural Price Estimator")

    st.write(
        "Enter your crop details to generate "
        "an estimated starting bid price."
    )

    with st.form("prediction_form"):

        st.markdown(
            '<div class="section-heading">🌱 Crop Information</div>',
            unsafe_allow_html=True
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            district = st.selectbox("District", districts)
            crop = st.selectbox("Crop", crops)

        with c2:
            variety_list = sorted(
                df.loc[df["crop"] == crop, "variety"]
                .dropna().unique().tolist()
            )

            if not variety_list:
                variety_list = ["Unknown"]

            variety = st.selectbox("Variety", variety_list)
            grade = st.selectbox("Grade", grades)

        with c3:
            season = st.selectbox("Season", seasons)
            storage = st.selectbox("Storage Type", storage_types)

        st.divider()

        st.markdown(
            '<div class="section-heading">📦 Quantity & Quality</div>',
            unsafe_allow_html=True
        )

        c1, c2 = st.columns(2)

        with c1:
            quantity = st.number_input(
                "Quantity (Quintals)",
                min_value=1.0,
                value=100.0
            )

            quality = st.slider(
                "Quality Score",
                0, 100, 80
            )

        with c2:
            distance = st.number_input(
                "Distance to Mandi (KM)",
                min_value=0.0,
                value=25.0
            )

            transport_cost = st.number_input(
                "Transport Cost per Quintal (₹)",
                min_value=0.0,
                value=4.0
            )

        st.divider()

        st.markdown(
            '<div class="section-heading">📈 Market & Weather</div>',
            unsafe_allow_html=True
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            rainfall = st.number_input(
                "Rainfall (MM)",
                min_value=0.0,
                value=30.0
            )

            temperature = st.number_input(
                "Temperature (°C)",
                value=15.0
            )

        with c2:
            market_arrival = st.number_input(
                "Market Arrival (Quintals)",
                min_value=0.0,
                value=500.0
            )

            market_price = st.number_input(
                "Historical Modal Price (₹/Quintal)",
                min_value=1.0,
                value=12000.0
            )

        with c3:
            year = st.selectbox(
                "Listing Year",
                [2025, 2024, 2023, 2022]
            )

            month = st.selectbox(
                "Listing Month",
                list(range(1, 13)),
                index=9
            )

        st.write("")

        submitted = st.form_submit_button(
            "🌾 GENERATE PRICE PREDICTION",
            use_container_width=True
        )

    if submitted:

        input_data = pd.DataFrame([{
            "district": district,
            "crop": crop,
            "variety": variety,
            "grade": grade,
            "season": season,
            "quantity_quintals": quantity,
            "quality_score": quality,
            "storage_type": storage,
            "distance_to_major_mandi_km": distance,
            "transport_cost_per_quintal_inr": transport_cost,
            "rainfall_mm_30d": rainfall,
            "avg_temperature_c": temperature,
            "market_arrival_quintals": market_arrival,
            "historical_modal_price_inr_per_quintal": market_price,
            "year": year,
            "month": month
        }])

        try:
            prediction = float(model.predict(input_data)[0])

            if not np.isfinite(prediction) or prediction <= 0:
                st.error("Invalid prediction. Please check your inputs.")
            else:
                total_value = prediction * quantity

                st.markdown(f"""
                <div class="result-card">
                    <p>AI ESTIMATED STARTING BID PRICE</p>
                    <h1>₹{prediction:,.2f}</h1>
                    <p>PER QUINTAL</p>
                </div>
                """, unsafe_allow_html=True)

                c1, c2 = st.columns(2)

                c1.metric(
                    "Total Estimated Lot Value",
                    f"₹{total_value:,.2f}"
                )

                c2.metric(
                    "Available Quantity",
                    f"{quantity:,.1f} Quintals"
                )

                st.success("Your crop price estimate is ready!")

                with st.expander("View submitted crop details"):
                    st.dataframe(
                        input_data,
                        use_container_width=True
                    )

                st.warning(
                    "Experimental estimate based on synthetic "
                    "training data. It is not a verified market "
                    "quotation or guaranteed selling price."
                )

        except Exception as e:
            st.error(f"Prediction error: {e}")

# ==========================================
# 9. MARKET ANALYTICS
# ==========================================

elif page == "Market Analytics":

    st.subheader("📊 Agricultural Market Analytics")

    selected_crop = st.selectbox(
        "Select Crop for Analysis",
        sorted(df["crop"].dropna().unique())
    )

    crop_data = df[df["crop"] == selected_crop]

    average_price = crop_data[
        "starting_bid_price_inr_per_quintal"
    ].mean()

    highest_price = crop_data[
        "starting_bid_price_inr_per_quintal"
    ].max()

    lowest_price = crop_data[
        "starting_bid_price_inr_per_quintal"
    ].min()

    c1, c2, c3 = st.columns(3)

    c1.metric("Average Starting Price", f"₹{average_price:,.2f}")
    c2.metric("Highest Starting Price", f"₹{highest_price:,.2f}")
    c3.metric("Lowest Starting Price", f"₹{lowest_price:,.2f}")

    fig = px.histogram(
        crop_data,
        x="starting_bid_price_inr_per_quintal",
        nbins=35,
        title=f"{selected_crop} Price Distribution",
        color_discrete_sequence=["#36804B"]
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(fig, use_container_width=True)

    district_prices = (
        crop_data.groupby("district")
        ["starting_bid_price_inr_per_quintal"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        district_prices,
        x="district",
        y="starting_bid_price_inr_per_quintal",
        title="Average Starting Price by District",
        color="starting_bid_price_inr_per_quintal",
        color_continuous_scale="Greens"
    )

    st.plotly_chart(fig, use_container_width=True)

# ==========================================
# 10. ABOUT US
# ==========================================

elif page == "About Us":

    st.subheader("About KisanBid")

    st.markdown("""
    KisanBid is an agricultural marketplace concept
    designed to help farmers from Jammu & Kashmir
    reach buyers across India.

    The platform aims to combine machine learning,
    agricultural analytics and online bidding.
    """)

    st.markdown("### Our Objectives")

    st.markdown("""
    - Help farmers estimate crop starting prices.
    - Improve access to wider markets.
    - Encourage transparent agricultural trading.
    - Provide data-driven market insights.
    """)

    st.markdown("### Technologies")

    st.markdown("""
    - Python and Pandas
    - Scikit-learn
    - Random Forest Regression
    - Streamlit
    - Plotly
    """)

    st.info(
        "The current prediction model uses synthetic data "
        "and is an academic prototype."
    )

# ==========================================
# 11. FOOTER
# ==========================================

st.markdown("""
<div class="footer">
    <b>🌾 KisanBid</b>
    <br>
    Connecting Farmers · Empowering Agriculture ·
    Building Better Markets
    <br><br>
    Academic Project | Jammu & Kashmir, India
</div>
""", unsafe_allow_html=True)

