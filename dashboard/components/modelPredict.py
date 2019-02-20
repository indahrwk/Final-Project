import dash_core_components as dcc
import dash_html_components as html

def renderModelPredict() :
    return html.Div([
                html.H1('Test Predict Churn', className='h1'),
                html.Div(children=[
                    html.Div([
                        html.P('gender : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(
                            id='inputgenderPredict',
                            options=[
                                {'label': 'Female', 'value': 'Female'},
                                {'label': 'Male', 'value': 'Male'},
                            ],
                            value='Female'
                        ),
                    ],className='col-4'),
                    html.Div([
                        html.P('SeniorCitizen : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(
                            id='inputSeniorCitizenPredict',
                            options=[
                                {'label': '0', 'value': '0'},
                                {'label': '1', 'value': '1'},
                            ],
                            value='0'
                        ),
                    ],className='col-4'),
                    html.Div([
                        html.P('Partner : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(
                            id='inputPartnerPredict',
                            options=[
                                {'label': 'Yes', 'value': 1},
                                {'label': 'No', 'value': 0},
                            ],
                            value=1
                        ),
                    ],className='col-4'),
                    html.Div([
                        html.P('Dependents : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(
                            id='inputDependentsPredict',
                            options=[
                                {'label': 'Yes', 'value': 1},
                                {'label': 'No', 'value': 0},
                            ],
                            value=1
                        ),
                    ],className='col-4'),
                     html.Div([
                        html.P('tenure : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputtenurePredict', type='number', value='0')
                   
                    ],className='col-4'),
                    html.Div([
                        html.P('PhoneService : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(
                            id='inputPhoneServicePredict',
                            options=[
                                {'label': 'Yes', 'value': 1},
                                {'label': 'No', 'value': 0},
                            ],
                            value=1
                        ),
                    ],className='col-4'),
                    html.Div([
                        html.P('MultipleLines : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(
                            id='inputMultipleLinesPredict',
                            options=[
                                {'label': 'Yes', 'value': 1},
                                {'label': 'No', 'value': 0},
                            ],
                            value=1
                        ),
                    ],className='col-4'),
                    html.Div([
                        html.P('InternetService : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(
                            id='inputInternetServicePredict',
                            options=[
                                {'label': 'DSL', 'value': 'DSL'},
                                {'label': 'Fiber optic', 'value': 'Fiber optic'},
                            ],
                            value='Fiber optic'
                        ),
                    ],className='col-4'),
                    html.Div([
                        html.P('OnlineSecurity : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(
                            id='inputOnlineSecurityPredict',
                            options=[
                                {'label': 'Yes', 'value': 1},
                                {'label': 'No', 'value': 0},
                            ],
                            value=1
                        ),
                    ],className='col-4'),
                    html.Div([
                        html.P('OnlineBackup : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(
                            id='inputOnlineBackupPredict',
                            options=[
                                {'label': 'Yes', 'value': 1},
                                {'label': 'No', 'value': 0},
                            ],
                            value=1
                        ),
                    ],className='col-4'),
                    html.Div([
                        html.P('DeviceProtection : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(
                            id='inputDeviceProtectionPredict',
                            options=[
                                {'label': 'Yes', 'value': 1},
                                {'label': 'No', 'value': 0},
                            ],
                            value=1
                        ),
                    ],className='col-4'),
                    html.Div([
                        html.P('TechSupport : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(
                            id='inputTechSupportPredict',
                            options=[
                                {'label': 'Yes', 'value': 1},
                                {'label': 'No', 'value': 0},
                            ],
                            value=1
                        ),
                    ],className='col-4'),
                    html.Div([
                        html.P('StreamingTV : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(
                            id='inputStreamingTVPredict',
                            options=[
                                {'label': 'Yes', 'value': 1},
                                {'label': 'No', 'value': 0},
                            ],
                            value=1
                        ),
                    ],className='col-4'),
                    html.Div([
                        html.P('StreamingMovies : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(
                            id='inputStreamingMoviesPredict',
                            options=[
                                {'label': 'Yes', 'value': 1},
                                {'label': 'No', 'value': 0},
                            ],
                            value=1
                        ),
                    ],className='col-4'),
                    html.Div([
                        html.P('Contract : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(
                            id='inputContractPredict',
                            options=[
                                {'label': 'Month-to-month', 'value': 'Month-to-month'},
                                {'label': 'One year', 'value': 'One year'},
                                {'label': 'Two year', 'value': 'Two year'},
                            ],
                            value='Month-to-month'
                        ),
                    ],className='col-4'),
                    html.Div([
                        html.P('PaperlessBilling : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(
                            id='inputPaperlessBillingPredict',
                            options=[
                                {'label': 'Yes', 'value': 1},
                                {'label': 'No', 'value': 0},
                                
                            ],
                            value=1
                        ),
                    ],className='col-4'),
                    html.Div([
                        html.P('PaymentMethod : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Dropdown(
                            id='inputPaymentMethodPredict',
                            options=[
                                {'label': 'Electronic check', 'value': 'Electronic check'},
                                {'label': 'Mailed check', 'value': 'Mailed check'},
                                {'label': 'Bank transfer (automatic)', 'value': 'Bank transfer (automatic)'},
                                {'label': 'Credit card (automatic)', 'value': 'Credit card (automatic)'},
                            ],
                            value='Mailed check'
                        ),
                    ],className='col-4'),
                     html.Div([
                        html.P('MonthlyCharges : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputMonthlyChargesPredict', type='number', value='0')
                        
                    ],className='col-4'),
                     html.Div([
                        html.P('TotalCharges : ')
                    ],className='col-2'),
                    html.Div([
                        dcc.Input(id='inputTotalChargesPredict', type='number', value='0')
                        
                    ],className='col-4'),
                    html.Div([
                        html.Button('Predict', id='buttonPredict', className='btn btn-primary')
                    ],className='mx-auto', style={ 'paddingTop': '20px', 'paddingBottom': '20px' })
                ],className='row'),
                html.Div([
                    html.H2('', id='outputPredict', className='mx-auto')
                ], className='row')
            ])