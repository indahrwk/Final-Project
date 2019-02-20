import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output, State
import pickle
from components.telcoTable import renderTable
from components.scatterPlot import renderScatterPlot
# from components.categorical import rendercategorical
from components.modelPredict import renderModelPredict
from sklearn.preprocessing import OneHotEncoder
from imblearn.under_sampling import RandomUnderSampler


loadModel = pickle.load(open('churnanalysis.sav', 'rb'))

app = dash.Dash(__name__)

server = app.server

dftelco = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

app.title = 'Dashboard Telco Customer Churn'

app.layout = html.Div(children=[
    html.H1(children='Dashboard Telco Customer Churn (by Indah R Kuniyo)',className='titleDashboard'),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Telco Customer Churn Dataset', value='tab-1',children=[
            renderTable(dftelco)
        ]),
        dcc.Tab(label='Scatter Plot', value='tab-2',children=[
            renderScatterPlot(dftelco)
        ]),    
        # dcc.Tab(label='Categorical Plot', value='tab-3',children=[
        #     rendercategorycal(dftelco)
        # ]),
        dcc.Tab(label='Test Predict', value='tab-3',children=[
            renderModelPredict()
        ]),
    ], style={
        'fontFamily': 'system-ui'
    }, content_style={
        'fontFamily': 'Arial',
        'borderBottom': '1px solid #d6d6d6',
        'borderLeft': '1px solid #d6d6d6',
        'borderRight': '1px solid #d6d6d6',
        'padding': '44px'
    })
], style={
    'maxWidth': '1200px',
    'margin': '0 auto'
})

@app.callback(
    Output('table-multicol-sorting', "data"),
    [Input('table-multicol-sorting', "pagination_settings"),
     Input('table-multicol-sorting', "sorting_settings")])
def update_graph(pagination_settings, sorting_settings):
    # print(sorting_settings)
    if len(sorting_settings):
        dff = dftelco.head(500).sort_values(
            [col['column_id'] for col in sorting_settings],
            ascending=[
                col['direction'] == 'asc'
                for col in sorting_settings
            ],
            inplace=False
        )
    else:
        # No sort is applied
        dff = dftelco.head(500)

    return dff.iloc[
        pagination_settings['current_page']*pagination_settings['page_size']:
        (pagination_settings['current_page'] + 1)*pagination_settings['page_size']
    ].to_dict('rows')

@app.callback(
    Output('outputPredict', 'children'),
    [Input('buttonPredict', 'n_clicks')],
    [State('inputgenderPredict', 'value'), 
    State('inputSeniorCitizenPredict', 'value'),
    State('inputPartnerPredict', 'value'),
    State('inputDependentsPredict', 'value'),
    State('inputtenurePredict', 'value'),
    State('inputPhoneServicePredict', 'value'),
    State('inputMultipleLinesPredict', 'value'),
    State('inputInternetServicePredict', 'value'),
    State('inputOnlineSecurityPredict', 'value'),
    State('inputOnlineBackupPredict', 'value'),
    State('inputDeviceProtectionPredict', 'value'),
    State('inputTechSupportPredict', 'value'),
    State('inputStreamingTVPredict', 'value'),
    State('inputStreamingMoviesPredict', 'value'),
    State('inputContractPredict', 'value'),
    State('inputPaperlessBillingPredict', 'value'),
    State('inputPaymentMethodPredict', 'value'),
    State('inputMonthlyChargesPredict', 'value'),
    State('inputTotalChargesPredict', 'value')
    ])
def update_output(n_clicks,gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges):
    # print(gender)
    data = np.array([[Partner,Dependents,tenure,PhoneService,MultipleLines,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,PaperlessBilling,MonthlyCharges,TotalCharges, gender, InternetService, Contract, PaymentMethod]])
    prediction = loadModel.predict(data)
    predictProba = loadModel.predict_proba(data)
    hasil = ''
    if(prediction[0] == 1) :
        hasil = 'Churn'
    else :
        hasil = 'No Churn'
    return 'Prediction : ' + hasil + ' | Probability : ' + str(predictProba[0,1])


if __name__ == '__main__':
    app.run_server(debug=True,port=1997)