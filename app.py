from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales_data.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Create app
app = Dash(__name__)

# App layout
app.layout = html.Div(

    style={
        "backgroundColor": "#f4f4f4",
        "padding": "20px",
        "fontFamily": "Arial"
    },

    children=[

        html.H1(
            "Pink Morsel Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#ff1493",
                "marginBottom": "30px"
            }
        ),

        html.Div([
            
            html.Label(
                "Select Region:",
                style={
                    "fontSize": "20px",
                    "fontWeight": "bold"
                }
            ),

            dcc.RadioItems(
                id="region-filter",

                options=[
                    {"label": "All", "value": "all"},
                    {"label": "North", "value": "north"},
                    {"label": "East", "value": "east"},
                    {"label": "South", "value": "south"},
                    {"label": "West", "value": "west"},
                ],

                value="all",

                inline=True,

                style={
                    "marginTop": "10px",
                    "marginBottom": "20px"
                }
            )

        ]),

        dcc.Graph(id="sales-chart")

    ]
)

# Callback
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)

def update_chart(selected_region):

    # Filter data
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    # Group by date
    sales_by_date = (
        filtered_df.groupby("date")["sales"]
        .sum()
        .reset_index()
    )

    # Create figure
    fig = px.line(
        sales_by_date,
        x="date",
        y="sales",
        title=f"Sales Trend - {selected_region.title()} Region"
    )

    # Styling chart
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(size=14)
    )

    return fig

# Run app
if __name__ == "__main__":
    app.run(debug=False)