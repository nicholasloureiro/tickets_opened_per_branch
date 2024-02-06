import pandas as pd
import streamlit as st
import plotly.express as px

col1, col2 = st.columns([1,6])


col1.image('logo.png')


with col2:

    
    df = pd.read_csv('ticket.csv')

   
    request_counts = df.groupby('requester_name')['id'].count()

    
    request_counts_df = request_counts.reset_index()

    
    request_counts_df.columns = ['Solicitante', 'Número de tickets']

    
    request_counts_df = request_counts_df.sort_values('Número de tickets', ascending=False)

    
    requester_names = sorted(request_counts_df['Solicitante'].unique().tolist())

    
    requester_names.insert(0, 'Todos')

    
    selected_requester = st.selectbox('Selecione o(s) Solicitante', requester_names)

    
    if selected_requester == 'Todos':
        filtered_df = request_counts_df
    else:
        filtered_df = request_counts_df[request_counts_df['Solicitante'] == selected_requester]

    
    num_requesters = st.slider('Selecione a quantidade de Solicitantes a serem visualizados', 1, len(filtered_df), 10)

    
    filtered_df = filtered_df.head(num_requesters)

    
    fig = px.bar(filtered_df, y='Solicitante', x='Número de tickets', color='Número de tickets', orientation='h', title='Quantidade de tickets não resolvidos por Solicitante (01/01/2023-06/02/2024)', color_continuous_scale=['#E6056D', 'purple'])

    
    fig.update_layout(
        autosize=False,
        width=800,
        height=500,
        margin=dict(l=50, r=50, b=100, t=100, pad=4),
        font=dict(color="black"),  # Black font color
        xaxis=dict(title_font=dict(color="black")),  
        yaxis=dict(title_font=dict(color="black")), 
       
    )


  
    st.plotly_chart(fig)

