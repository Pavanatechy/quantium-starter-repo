from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

# Read cleaned data
df = pd.read_csv("formatted_sales_data.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Group sales by date
sales_by_date = df.groupby("date")["sales"].sum().reset_index()

# Create line chart
fig = px.line(
    sales_by_date,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)

# Create Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    
    html.H1(
        "Pink Morsel Sales Visualizer",
        style={"textAlign": "center"}
    ),

    dcc.Graph(figure=fig)

])

# Run app
app.run(debug=True)