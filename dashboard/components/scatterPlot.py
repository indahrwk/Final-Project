import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

color_set = ['#80aaff','#cc0000']

def legendChurn(val) :
    if(val == 1) :
        return 'Churn'
    elif(val == 0) :
        return 'Not Churn'

def renderScatterPlot(df) :
    return html.Div([
                html.H1('Scatter Plot telco', className='h1'),
                dcc.Graph(
                    id='scatterPlot',
                    figure={
                        'data': [
                            go.Scatter(
                                x=df[df['Churn'] == col].head(500)['MonthlyCharges'],
                                y=df[df['Churn'] == col].head(500)['TotalCharges'],
                                mode='markers',
                                marker=dict(color=color_set[i], size=10, line=dict(width=0.5, color='white')),
                                name=legendChurn(col)
                            ) for col, i in zip(df['Churn'].unique(), range(2))
                        ],
                        'layout': go.Layout(
                            xaxis= dict(title='MonthlyCharges'),
                            yaxis={'title': 'TotalCharges'},
                            margin={ 'l': 40, 'b': 40, 't': 10, 'r': 10 },
                            hovermode='closest'
                        )
                    }
                )
            ])