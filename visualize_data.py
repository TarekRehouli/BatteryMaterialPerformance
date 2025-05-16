import plotly.express as px

def plot_cycle_life(df):
    fig = px.line(df, x='Cycle', y='Capacity', title='Cycle Life')
    fig.show()

def plot_dQdV(df):
    fig = px.line(df, x='Voltage', y='dQdV', title='dQ/dV Plot')
    fig.show()
