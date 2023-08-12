cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')


# Initialize the Dash app
app = dash.Dash(__name__)


# Set the title of the dashboard
#app.title = "Automobile Statistics Dashboard"
app.title= "Automobile Sales Statistics Dashboard"


#---------------------------------------------------------------------------------
# Create the dropdown menu options
dropdown_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]
# List of years
year_list = [i for i in range(1980, 2024, 1)]
#---------------------------------------------------------------------------------------
# Create the layout of the app
app.layout = html.Div([
    #TASK 2.1 Add title to the dashboard
    html.H1("Automobile Sales Statistics Dashboard", style={'textAlign':'left', 'color':'#503D36', 'font-size':24}),#May include style for title
    html.Div([#TASK 2.2: Add two dropdown menus
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=[{'label': 'Yearly Statistics', 'value': 'Yearly Statistics'}, {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}],
            value='Select Statistics',
            placeholder='Select a report type'
        )
    ]),
    html.Div(dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            value='Select Statistics',
            style={
            'width': '80%',
            'padding': '3px',
            'font-size': '20px',
            'text-align-last': 'center'
        }'
        )),
    html.Div([#TASK 2.3: Add a division for output display
    html.Div(id='output-container', className='chart-grid', style={flex}),])
])
#TASK 2.4: Creating Callbacks
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='select year', component_property='figure'),
    Input(component_id='dropdown-statistics',component_property='figure'))


def update_input_container(selected_statistics):
    if selected_statistics =='Yearly Statistics':
        return False
    else:
        return True


#Callback for plotting
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='selected-statistics-output'', component_property='children'),
    [Input(component_id='dropdown-statistics', component_property='value'), Input(component_id='...', component_property='...')])




def update_output_container(selected_statistics, .....):
    if selected_statistics == 'Recession Period Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]
       
#TASK 2.5: Create and display graphs for Recession Report Statistics


#Plot 1 Automobile sales fluctuate over Recession Period (year wise)
        # use groupby to create relevant data for plotting
        yearly_rec=recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec,
                x='Year',
                y='Sales',
                title="Average Automobile Sales fluctuation over Recession Period"))


#Plot 2 Calculate the average number of vehicles sold by vehicle type      
        # use groupby to create relevant data for plotting
        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()                          
        R_chart2  = dcc.Graph(figure=px.bar(average_sales,
        x='vehicle type'
        y='sales'
        title="average number of vehicles sold by vehicle type")
       
# Plot 3 Pie chart for total expenditure share by vehicle type during recessions
        # use groupby to create relevant data for plotting
        exp_rec= recession_data.groupby('Vehicle_Type')['Automobile_Sales'].sum().reset_index
        R_chart3 = dcc.Graph(
                    figure=px.pie(exp_rec,
                    values='Total expenditure',
                 names='Vehicle Type',
                 title="Pie chart for total expenditure share by vehicle type during recessions"
                )


# Plot 4 bar chart for the effect of unemployment rate on vehicle type and sales
       




        return [
            html.Div(className='chart-item', children=[html.Div(children=R_chart1),html.Div(children=R_chart2)],style={.....}),
            html.Div(className='chart-item', children=[html.Div(children=R_chart3),html.Div(.............)],style={....})
            ]


# TASK 2.6: Create and display graphs for Yearly Report Statistics
 # Yearly Statistic Report Plots                            
    elif (input_year and selected_statistics=='...............') :
        yearly_data = data[data['Year'] == ......]
                             
#TASK 2.5: Creating Graphs Yearly data
                             
#plot 1 Yearly Automobile sales using line chart for the whole period.
        yas= data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1  = dcc.Graph(figure=px.line(yas, x='Year', y='Automobile_Sales', title='Yearly Automobile Sales'))
           
# Plot 2 Total Monthly Automobile sales using line chart.
        total_monthly_sales= recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()                        
        Y_chart2 = dcc.Graph(figure=px.line(total_monthly_sales, x='Month', y='Automobile_Sales', title='Total Monthly Automobile Sales'))


            # Plot bar chart for average number of vehicles sold during the given year
        avr_vdata = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        chart3 = dcc.Graph(figure=px.bar(avr_vdata, x='Vehicle_Type', y='Automobile_Sales', title=f'Average Vehicles Sold by Vehicle Type in the year {input_year}'))


            # Total Advertisement Expenditure for each vehicle using pie chart
        exp_data=yearly_data.groupby('Vehicle_Type')['Advertisement_Expenditure'].sum().reset_index()
        Y_chart4 = dcc.Graph(figure=px.pie(pie_chart_data, values='Advertisement_Expenditure', names='Vehicle_Type', title='Total Advertisement Expenditure by Vehicle Type'))


#TASK 2.6: Returning the graphs for displaying Yearly data
        return [
                html.Div(className='chart-item', children=[chart1]),
                html.Div(className='chart-item', children=[chart2]),
                html.Div(className='chart-item', children=[chart3]),
                html.Div(className='chart-item', children=[chart4])
                ]
       
    else:
        return None


# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
   
