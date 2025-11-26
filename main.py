import streamlit as st
import pandas as pd
from collectors.amazon import get_amazon_trending
from collectors.flipkart import get_flipkart_trending

st.set_page_config(page_title="Trend Explorer", layout="wide")

st.title("🔥 Trend Explorer – Trending Products Web App")

tab1, tab2, tab3 = st.tabs(["Trending Products", "Upload CSV", "About"])

# -------------------------- TAB 1 --------------------------
with tab1:
    st.header("📈 Trending Products")

    platform = st.selectbox("Select Platform", ["Amazon", "Flipkart"])
    
    if st.button("Fetch Trending Products"):
        with st.spinner("Fetching..."):
            if platform == "Amazon":
                df = get_amazon_trending()
            else:
                df = get_flipkart_trending()
        
        st.success("Fetched Successfully!")
        st.dataframe(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", csv, "trending_products.csv", "text/csv")

# -------------------------- TAB 2 --------------------------
with tab2:
    st.header("📤 Upload Your CSV")
    
    uploaded_file = st.file_uploader("Upload product CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

# -------------------------- TAB 3 --------------------------
with tab3:
    st.header("ℹ️ About Project")
    st.write("""
    **Trend Explorer** shows trending products from popular e-commerce websites.
    - Amazon Trending Products  
    - Flipkart Trending Products  
    - CSV Upload  
    - Easy Export  
    """)

