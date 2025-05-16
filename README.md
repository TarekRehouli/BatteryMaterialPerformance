# BatteryMaterialPerformance
This project simulates a data engineering workflow for analyzing battery material performance.

## Features
- Ingests electrochemical test data (CSV format)
- Extracts cycle life and dQ/dV features
- Visualizes data using Plotly and Streamlit
- Stores processed data into a PostgreSQL database
- Dockerized for easy deployment

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/battery-data-pipeline.git
cd battery-data-pipeline
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App
```bash
streamlit run app/dashboard.py
```

### 4. Upload Dataset
Use the dashboard interface to upload a CSV file in the following format:

| Cycle | Voltage | Capacity |
|-------|---------|----------|
| 1     | 2.5     | 100.2    |
| 2     | 2.52    | 99.5     |
| ...   | ...     | ...      |

### 5. (Optional) Run with Docker
```bash
docker build -t battery-dashboard .
docker run -p 8501:8501 battery-dashboard
```

## Example Visualizations
- 📈 Cycle Life (Capacity vs. Cycle)
- 📉 dQ/dV Plot (Voltage Derivative)

## Technologies Used
- Python
- Pandas & NumPy
- Plotly
- Streamlit
- SQLAlchemy (PostgreSQL)
- Docker

## License
MIT License
