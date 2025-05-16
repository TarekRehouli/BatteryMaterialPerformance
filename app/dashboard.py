import streamlit as st
from src.ingest_data import ingest_csv
from src.process_data import extract_features
from src.visualize_data import plot_cycle_life, plot_dQdV

st.title("Battery Material Data Analysis")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    df = ingest_csv(uploaded_file)
    processed_df = extract_features(df)

    st.subheader("Cycle Life Plot")
    plot_cycle_life(processed_df)

    st.subheader("dQ/dV Plot")
    plot_dQdV(processed_df)

# --- requirements.txt ---
pandas
numpy
sqlalchemy
plotly
streamlit
psycopg2-binary

# --- Dockerfile ---
FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "app/dashboard.py"]
