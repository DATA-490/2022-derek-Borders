# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
from plotly.figure_factory import create_distplot
import plotly.graph_objects as go
import plotly.io as pio



pio.templates.default = "plotly_dark"

app = Dash(__name__, )

###########################
# TODO: Add toggle to swap camera focal points
###########################
# a_cam_name = 'focus_on_center'
# a_camera = dict(
#     center=dict(x=0, y=0, z=0))
# fig.update_layout(scene_camera=a_camera, dragmode='orbit')

# b_cam_name = 'focus_on_my_stars'
b_camera = dict(
    center=dict(
        x=260, 
        y=20, 
        z=560))
# fig.update_layout(scene_camera=b_camera, dragmode='orbit')

# colors = {
#     'background': '#111111',
#     'text': '#7FDBFF'
# }

df = pd.read_csv('data/reddit_star_systems.csv')
df_mystars = pd.read_csv('data/my_star_systems.csv')
df_galaxy_center = pd.read_csv('data/galaxy_center.csv')

fig = make_subplots(
    rows=2, cols=3,
    specs=[
        [{'type':'scatter3d', "rowspan":2, "colspan":2}, None, {}],
        [None, None, {}],
        ],
    subplot_titles=(
        "No Man's Sky 'Euclid' Galaxy Map",
        "System Distances from Galactic Center", 
        "Number of Posts by Subject Count"))

# 3D Scatter Galaxy map
# Galaxy center 

gc_opacity = df_galaxy_center['opacity']
gc_color = df_galaxy_center['color']
gc_size = df_galaxy_center['size']


for i in range(len(gc_opacity)):
    fig.add_trace(go.Scatter3d(
        x=[0], y=[0], z=[0],
        # opacity=df_galaxy_center.opacity,
        name='Galaxy Center',
        opacity=gc_opacity[i],
        hovertext='Supermassive\nBlack Hole',
        mode='markers',
        marker=dict(
            size=gc_size[i],
            color=[gc_color[i]],              
            colorscale='hot',
            cmin=min(gc_color),
            cmax=max(gc_color),
        )
    ), row=1, col=1)

# Reddit Systems
fig.add_trace(go.Scatter3d(
    x=df.x, y=df.y, z=df.z,
    name='Reddit Systems',
    hovertext=df.address,
    opacity=0.8,
    mode='markers',
    marker=dict(
        size=2,
        color=df.k_ly_from_center,              
        colorscale='Inferno_r',   
    ),
    ), row=1, col=1)

# 3D Scatter Galaxy map
for i in range(15):
    fig.add_trace(go.Scatter3d(        
        x=df_mystars.x, y=df_mystars.y, z=df_mystars.z,
        hovertext=df_mystars.address,
        name='My Systems',
        opacity=1/(i*i) if i>0 else 1,
        mode='markers',
        marker=dict(
            size=i,
            color="red"
        ),
        ), row=1, col=1)

# Update camera for all scatter3d objects

# fig.update_scenes(camera=b_camera, dragmode='orbit')


# Density Plot
hist_data = [df.k_ly_from_center]
group_labels = ['ly to center/1000']
fig.add_histogram(
    name='',
    y=df.k_ly_from_center, 
    row=1, col=3)

# System Count by Subject
subject_counts = list(df.subject.value_counts().values)
subject_names = list(df.subject.value_counts().index)
subject_percentages = list(100*df.subject.value_counts().values/sum(df.subject.value_counts().values))
subject_percentage = ['{: .1f}%'.format(subject_percentage) for subject_percentage in subject_percentages]

fig.add_bar(
    x=subject_counts,
    y=subject_names,
    name='',
    hovertext= subject_percentage,
    orientation='h',
    marker=dict(color=subject_counts),
    row=2, col=3)

# Can't for the life of me figure out how to flip the order.
# fig.data[13].update(scene=dict(yaxis=dict(autorange="reversed")))



plot_range = [-2048,2048]
# fig.update_layout(showlegend=False, title_text="")
fig.update_layout(
    showlegend=False, 
    title_text="",
    scene = dict(
        xaxis = dict(
            range=plot_range,
            showline=False,            
            showbackground=False,            
            showgrid=False,            
            showticklabels=False,            
            showaxeslabels=False,            
            ),
        yaxis = dict(
            range=plot_range,
            showline=False,            
            showbackground=False,            
            showgrid=False,            
            showticklabels=False,            
            showaxeslabels=False
            ),
        zaxis = dict(
            range=plot_range,
            showline=False,            
            showbackground=False,            
            showgrid=False,            
            showticklabels=False,            
            showaxeslabels=False,
            ),
        ),
    height=800 , 
    margin=dict(l=50, r=50, b=50, t=50),
    margin_pad=50,
    )

# app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
app.layout = html.Div(style={"height":"100%", "backgroundColor":"#121212"},children=[
    # html.H1(
    #     children="Mapping the 'Euclid' Galaxy in No Man's Sky through Reddit Screenshots",
    #     style={
    #         'textAlign': 'center'#,
    #         # 'color': colors['text']
    #     }
    # ),

    # html.Div(children='', style={
    #     'textAlign': 'center',
    #     "height":"80%"
    #     # 'color': colors['text']
    # }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
