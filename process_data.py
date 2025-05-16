import numpy as np

def extract_features(df):
    """Extract battery performance metrics."""
    df['delta_capacity'] = df['Capacity'].diff()
    df['dQdV'] = df['delta_capacity'] / df['Voltage'].diff()
    return df.dropna()
