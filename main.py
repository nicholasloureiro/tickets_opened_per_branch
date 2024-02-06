import pandas as pd
import streamlit as st
import plotly.express as px

col1, col2 = st.columns([1,6])

# Add the image to the first column
col1.image('logo.png')

# The rest of your code goes into the second column
with col2:

    # Load the data from the CSV file
    df = pd.read_csv('ticket.csv')

    # Group by 'requester_name' and count the number of 'id's
    request_counts = df.groupby('requester_name')['id'].count()

    # Convert the Series to a DataFrame and reset the index
    request_counts_df = request_counts.reset_index()

    # Rename the columns
    request_counts_df.columns = ['Solicitante', 'Número de tickets']

    # Order the DataFrame by 'Número de tickets' from most to least
    request_counts_df = request_counts_df.sort_values('Número de tickets', ascending=False)

    # Get a list of 'Solicitantes' in alphabetical order
    requester_names = sorted(request_counts_df['Solicitante'].unique().tolist())

    # Add 'Todos' to the beginning of the list
    requester_names.insert(0, 'Todos')

    # Create a dropdown menu for the user to select a 'Solicitante'
    selected_requester = st.selectbox('Selecione o(s) Solicitante', requester_names)

    # Filter the DataFrame based on the selected 'Solicitante'
    if selected_requester == 'Todos':
        filtered_df = request_counts_df
    else:
        filtered_df = request_counts_df[request_counts_df['Solicitante'] == selected_requester]

    # Add a slider to select the number of 'Solicitantes' to display
    num_requesters = st.slider('Selecione a quantidade de Solicitantes a serem visualizados', 1, len(filtered_df), 10)

    # Limit the number of 'Solicitantes' displayed
    filtered_df = filtered_df.head(num_requesters)

    # Create a horizontal bar chart
    fig = px.bar(filtered_df, y='Solicitante', x='Número de tickets', color='Número de tickets', orientation='h', title='Quantidade de tickets não resolvidos por Solicitante (01/01/2023-06/02/2024)', color_continuous_scale=['#E6056D', 'purple'])

    # Update the layout to make it more corporate
    fig.update_layout(
        autosize=False,
        width=800,
        height=500,
        margin=dict(l=50, r=50, b=100, t=100, pad=4),
        font=dict(color="black"),  # Black font color
        xaxis=dict(title_font=dict(color="white")),  # Black font color for x axis title
        yaxis=dict(title_font=dict(color="white")), 
        
        # Black font color for y axis title
    )


    # Display the chart
    st.plotly_chart(fig)

