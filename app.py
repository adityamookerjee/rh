import base64
import datetime
import io

import random
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import sd_material_ui
import pandas as pd
import brawl

external_stylesheets = [
    "https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"
]


def return_func_content():
    return html.Div(
        [
            # sd_material_ui.Stepper(
            #     id='input-stepper',
            #     activeStep=0,
            #     stepCount=2,
            #     stepLabels=['Upload Data', 'Select Fighters'],
            # ),
            html.Div(
                id="upload_div",
                children=[
                    dcc.Upload(
                        id='upload-data',
                        children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
                        style={
                            'width': '100%',
                            'height': '60px',
                            'lineHeight': '60px',
                            'borderWidth': '1px',
                            'borderStyle': 'dashed',
                            'borderRadius': '5px',
                            'textAlign': 'center',
                            'margin': '10px',
                        },
                        # Allow multiple files to be uploaded
                        multiple=True,
                    )
                ],
            ),
            # html.Div(
            #     id="selection_div",
            #     children=[dcc.Dropdown(id="dropdown_1"), dcc.Dropdown(id="dropdown_2")],
            # ),
            html.Div(id='output-data-upload'),
        ]
    )


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.title = "Adi Mookerjee RH Assignment"
app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Nav(
                            children=[
                                html.Div(
                                    [
                                        html.A(
                                            ["Adi - RH Coding Challenge"],
                                            className="brand-logo center",
                                        )
                                    ],
                                    className="nav-wrapper",
                                )
                            ],
                            className="light-blue accent-2",
                        )
                    ],
                    className="col s12",
                )
            ],
            className="row",
        ),
        return_func_content(),
    ]
)


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    results = pd.DataFrame()
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            df.set_index('Name', inplace=True)
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div(['There was an error processing this file.'])
    applicants = brawl.pick_applicants(df)
    applicant_pairing = list()
    for applicant in applicants:
        applicant_pairing.append(brawl.Applicant(df, applicant))
    applicant_1 = applicant_pairing[0]
    applicant_2 = applicant_pairing[1]

    round_num = 1
    while applicant_1.health > 0 and applicant_2.health > 0:
        log = brawl.fight(round_num, [applicant_1, applicant_2])
        round_num += 1
        results = results.append(log)
    winner = brawl.determine_winner([applicant_1, applicant_2])
    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(["Upload Info"], className="card-title"),
                                    html.Div(
                                        [
                                            html.H5(f"Filename : {filename}"),
                                            html.H6(
                                                f"Date : {datetime.datetime.fromtimestamp(date)}"
                                            ),
                                            html.Label("Upload Data"),
                                            dash_table.DataTable(
                                                data=df.reset_index().to_dict('records'),
                                                columns=[
                                                    {'name': i, 'id': i}
                                                    for i in df.reset_index().columns
                                                ],
                                                style_table={'overflowX': 'scroll'},
                                            ),
                                        ],
                                        className="card-content",
                                    ),
                                ],
                                className="card",
                            )
                        ],
                        className="col s5",
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(["Matchup"], className="card-title"),
                                    html.Div(
                                        [
                                            html.H4(f"{applicants[0]} VS {applicants[1]}"),
                                            html.H5(f"Winner : {winner}"),
                                            html.H6(
                                                f"Number of Rounds : {int(max(results.Round.values))}"
                                            ),
                                            html.Label("Results"),
                                            dash_table.DataTable(
                                                data=results.to_dict('records'),
                                                columns=[
                                                    {'name': i, 'id': i} for i in results.columns
                                                ],
                                                style_table={'overflowX': 'scroll'},
                                            ),
                                        ],
                                        className="card-content",
                                    ),
                                ],
                                className="card",
                            )
                        ],
                        className="col s7",
                    ),
                ],
                className="row",
            )
        ]
    )


# # Callback for Stepper
# @app.callback(Output('upload_div', 'style'), [Input('input-stepper', 'activeStep')])
# def stepper_callback(activeStep: int):
#     print(activeStep)
#     if activeStep == 0:
#         return {'display': 'block'}
#     else:
#         return {'display': 'none'}


# @app.callback(Output('dropdown_1', 'options'), [Input('upload-data', 'contents')])
# def update_output(contents):
#     content_type, content_string = contents.split(',')

#     decoded = base64.b64decode(content_string)
#     # Assume that the user uploaded a CSV file
#     df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
#     df.set_index('Name', inplace=True)
#     options = list()
#     for name in list(df.index):
#         options.append({"label": name, "value": name})
#     print(options)
#     return options


@app.callback(
    Output('output-data-upload', 'children'),
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename'), State('upload-data', 'last_modified')],
)
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d)
            for c, n, d in zip(list_of_contents, list_of_names, list_of_dates)
        ]
        return children


if __name__ == '__main__':
    app.run_server(debug=True)
