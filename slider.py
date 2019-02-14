import dash
from dash.dependencies import Input,Output
import dash_core_components as dcc
import dash_html_components as html
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
import pandas as pd
import plotly.graph_objs as go
app=dash.Dash(external_stylesheets=external_stylesheets)
# simpel graph
# data=pd.read_csv('https://gist.githubusercontent.com/chriddyp/' +
#     '5d1ea79569ed194d432e56108a04d188/raw/' +
#     'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
#     'gdp-life-exp-2007.csv')
# #print(data.year.unique())
#
#
# app.layout=html.Div([html.H1('dash slider:'),
#             dcc.Graph(id='my-graph',
#                       figure={
#                           'data' :[
#                               go.Scatter(
#                                   x=data[data['continent']==i]['gdp per capita'],
#                                   y=data[data['continent']==i]['life expectancy'],
#                                   mode='markers',
#                                   name=i
#                               )for i in data.continent.unique()
#                           ],
#                           'layout':go.Layout(
#                               title="gdp per capita vs life expectancy",
#                               xaxis={'title':'gdp per capita'},
#                               yaxis={'title':'life expectancy'}
#                           )
#                       })
#                      ])


'''call back with sliders'''

# data=pd.read_csv(
#     'https://raw.githubusercontent.com/plotly/'
#     'datasets/master/gapminderDataFiveYear.csv')
#
#
# app.layout=html.Div([
#     dcc.Graph(id='graph-slider'),
#     dcc.Slider(
#         id='year-slider',
#         min=data.year.min(),
#         max=data.year.max(),
#         value=data.year.min(),
#         marks={str(year):str(year) for year in data.year.unique()}
#     )
# ])
#
# @app.callback(Output('graph-slider','figure'),[Input('year-slider','value')])
# def update_graph(selected_year):
#     filtered_df=data[data.year==selected_year]
#     traces=[]
#     for i in filtered_df.continent.unique():
#         df_by_continent=filtered_df[filtered_df.continent==i]
#         traces.append(
#             go.Scatter(
#                 x=df_by_continent['gdpPercap'],
#                 y=df_by_continent['lifeExp'],
#                 mode='markers',
#                 name=i
#             )
#         )
#     return {
#
#         'data':traces,
#         'layout':go.Layout(title='gdp per cap vs life exp',
#                            xaxis={'title':'gdp per capita'},
#                            yaxis={'title':'life exp'})
#
#     }

'''
calllback with multiple inputes'''

#app.layout=html.Div()
# data=df = pd.read_csv(
#     'https://gist.githubusercontent.com/chriddyp/'
#     'cb5392c35661370d95f300086accea51/raw/'
#     '8e0768211f6b747c0db42a9ce9a0937dafcbd8b2/'
#     'indicators.csv')
#
#
# app=dash.Dash()
# app.layout=html.Div([html.H1('indicatoar data'),
#                html.Div([
#                dcc.Dropdown(
#                    id='x-axis',
#                    options=[{'label':i,'value':i }for i in data['Indicator Name']],
#                    value='Fertility rate, total (births per woman)'
#                )
#                ],
#                    style={'width':'48%','display': 'inline-block'}),
# html.Div([
#                dcc.Dropdown(
#                    id='y-axis',
#                    options=[{'label':i,'value':i }for i in data['Indicator Name']],
#                    value='Life expectancy at birth, total (years)'
#                )
#                    ],
#                    style={'width':'48%','display': 'inline-block','float':'right'}
# ),
#                      dcc.Graph(id='graph'),
#                      dcc.Slider(id='slider',
#                         min=data.Year.min(),
#                         max=data.Year.max(),
#                         value=data.Year.min(),
#                         marks={str(year):str(year) for year in data.Year.unique()})
#                ])
#
# @app.callback(Output('graph','figure'),
#         [Input('x-axis','value'),
#          Input('y-axis','value'),
#          Input('slider','value')])
# def update_graph(xval,yval,slid):
#     dff=data[data['Year']==slid]
#     return {
#         'data':[go.Scatter(
#             x=dff[dff['Indicator Name'] ==xval]['Value'],
#             y=dff[dff['Indicator Name'] == yval]['Value'],
#             text=dff[dff['Indicator Name'] == yval]['Country Name'],
#             mode='markers'
#         ),
#         ],
#         'layout':go.Layout(
#             xaxis={
#                 'title':xval
#             },
#             yaxis={'title':yval}
#         )
#
#     }

'''
multiple
outputs
using check buttons:'''


# all_options = {
#     'America': ['New York City', 'San Francisco', 'Cincinnati'],
#     'Canada': ['Montréal', 'Toronto', 'Ottawa']
# }
#
# app=dash.Dash()
# app.layout=html.Div([
#     dcc.RadioItems(id='country',
#                  options=[{'label':i,'value':i}for i in all_options.keys()],
#                  value='America'),
#     html.Hr(),
#     dcc.RadioItems(id='city'),
#     html.Hr(),
#     html.Div(id='display')
# ])
#
# @app.callback(Output('city','options'),[Input('country','value')])
# def set_cities_options(selected_item):
#     return [{'label':i,'value':i}for i in all_options[selected_item]]
#
# @app.callback(
#     dash.dependencies.Output('city', 'value'),
#     [dash.dependencies.Input('city', 'options')])
# def set_cities_value(available_options):
#     return available_options[0]['value']
#
# @app.callback(Output('display','children'),[
#     Input('city','value'),Input('country','value')])
# def set_text(city,country):
#     return 'select city {} is the city of {}'.format(city,country)
#

'''
dash state using input box '''

# app.layout=html.Div([
#     dcc.Input(id='input1',value=10,type='number'),
#     dcc.Input(id='input2',type='number',value=20),
#     html.Div(id='sum1')
# ])
#
# @app.callback(Output('sum1','children'),
#               [Input('input1','value'),Input('input2','value')])
# def sum(value1,value2):
#     return 'sum of {} and {} is:{}'.format(value1,value2,(value1+value2))

"""
callback with to text input and one submit button with
number of clicks as property
"""

# app.layout=html.Div([
#     dcc.Input(id='input1',value=10,type='number'),
#     dcc.Input(id='input2',type='number',value=20),
#     html.Button(id='submit',children='submit',n_clicks=0),
#     html.Div(id='sum1')
# ])
#
# @app.callback(Output('sum1','children'),
#               [Input('input1','value'),Input('input2','value'),Input('submit','n_clicks')])
# def sum(value1,value2,n_clicks):
#     return 'sum of {} and {} is:{} . and the submit button is clicked {} times'.format(value1,value2,(value1+value2),n_clicks)




if __name__=='__main__':
    app.run_server(debug=True)
