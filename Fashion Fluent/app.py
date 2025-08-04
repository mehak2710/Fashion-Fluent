import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="TrendMuse – AI Trend Generator", layout="centered")
st.title("🧵 TrendMuse: Fashion Trend Generator")

st.markdown("Type in any fashion item below to view its simulated trend over the past year:")

# Input box
item = st.text_input("👗 Enter a fashion item:", placeholder="e.g. Maxi Dress, Crop Top, Sneakers")

# Generate date range for past 12 months
def generate_months():
    today = datetime.today()
    return [(today - timedelta(days=30 * i)).strftime("%b %Y") for i in range(11, -1, -1)]

# Create simulated trend pattern
def generate_trend(seed_word):
    random.seed(seed_word.lower())  # same word gives same trend
    trend = [random.randint(20, 50)]
    for _ in range(11):
        change = random.randint(-3, 5)
        next_val = max(10, min(100, trend[-1] + change))
        trend.append(next_val)
    return trend

if item:
    months = generate_months()
    values = generate_trend(item)
    
    df = pd.DataFrame({
        "Month": months,
        item.title(): values
    })

    st.subheader(f"📈 Simulated Trend for: *{item.title()}*")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df["Month"], df[item.title()], marker="o", linewidth=2, color="mediumvioletred")
    ax.set_xticks(df["Month"])
    ax.set_xticklabels(df["Month"], rotation=45)
    ax.set_ylabel("Trend Score")
    ax.set_ylim(0, 110)
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.set_title(f"Trend Analysis: {item.title()}")
    st.pyplot(fig)
else:
    st.info("Enter a fashion item above to generate trend insights.")

