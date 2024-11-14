# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a Dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    
    # Dropdown list to enable Launch Site selection
    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'All Sites', 'value': 'ALL'},
            {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'}, 
            {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
            {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'}
        ],
        value='ALL',
        placeholder="Select Launch Site",
        searchable=True
    ),
    html.Br(),

    # Pie chart to show the total successful launches count
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    # Slider to select payload range
    dcc.RangeSlider(
        id='payload-slider',
        min=0, max=10000, step=1000,
        marks={0: '0', 10000: '10000'},
        value=[min_payload, max_payload]
    ),

    # Scatter chart to show the correlation between payload and launch success
    html.Div(dcc.Graph(id='success-payload-scatter-chart'))
])

# Callback function for the pie chart
@app.callback(
    Output('success-pie-chart', 'figure'),
    [Input('site-dropdown', 'value')]
)
def update_pie_chart(site_dropdown):
    filtered_df = spacex_df
    if site_dropdown != 'ALL':
        filtered_df = spacex_df[spacex_df['Launch Site'] == site_dropdown]
        fig = px.pie(filtered_df, names='class', 
                     title=f'Total Launches for Site {site_dropdown}')
    else:
        fig = px.pie(filtered_df, values='class', 
                     names='Launch Site', 
                     title='Total Launches for All Sites')
    return fig

# Callback function for the scatter chart
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'),
     Input('payload-slider', 'value')]
)
def update_scatter_chart(site_dropdown, payload_slider):
    low, high = payload_slider
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)]
    if site_dropdown != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == site_dropdown]
    
    fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', 
                     color='Booster Version Category',
                     title=f'Payload vs. Launch Outcome for {site_dropdown if site_dropdown != "ALL" else "All Sites"}')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server()

