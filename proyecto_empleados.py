import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Encabezados, títulos, 
st.title('Hackathon HackerEarth 2020')
st.header('Employee Attrition Data')

# Leer datos de la fuente
employees_link = 'Employees.csv'

# Funciones para cargar datos
@st.cache
def load_data(nrows):
    employees_data = pd.read_csv(employees_link, nrows=nrows)
    return employees_data

def load_employee_id(id):
    id_data = data[data['Employee_ID'].str.upper().str.contains(id)]
    return id_data

def load_education_level(education):
    education_data = data[data['Education_Level']==education]
    return education_data

def load_hometown(hometown):
    hometown_data = data[data['Hometown']==hometown]
    return hometown_data

def load_unit(unit):
    unit_data = data[data['Unit']==unit]
    return unit_data

# Llamar funciones
data = load_data(500)

# Sidebar
sidebar = st.sidebar

# Checkbox para mostrar todos los datos del dataframe
if sidebar.checkbox('Show all employee data'):
    st.subheader('All Employee Data')
    st.write(data)

# FILTROS
#Inputbox Employee ID
employeeid = sidebar.text_input('Employee ID:')
btn_filter_employeeid = sidebar.button('Filter by Employee ID')

if (btn_filter_employeeid):
    filter_id = load_employee_id(employeeid.upper())
    st.write(filter_id)

# Selectbox Nivel Educativo
selected_education = sidebar.selectbox('Select Education Level', data['Education_Level'].unique())
btn_selected_education = sidebar.button('Filter by Education Level')

if(btn_selected_education):
    filter_education = load_education_level(selected_education)
    count_row = filter_education.shape[0]
    st.write(f'Total Employees by Education Level: {count_row}')
    st.write(filter_education)

# Selectbox Hometown
selected_hometown = sidebar.selectbox('Select Hometown', data['Hometown'].unique())
btn_selected_hometown = sidebar.button('Filter by Hometown')

if (btn_selected_hometown):
    filter_hometown = load_hometown(selected_hometown)
    count_row = filter_hometown.shape[0]
    st.write(f'Total Employees by Hometown: {count_row}')
    st.write(filter_hometown)

# Selectbox Unidad Funcional
selected_unit = sidebar.selectbox('Select Unit', data['Unit'].unique())
btn_selected_unit = sidebar.button('Filter by Unit')

if(btn_selected_unit):
    filter_unit = load_unit(selected_unit)
    count_row = filter_unit.shape[0]
    st.write(f'Total Employees by Unit: {count_row}')
    st.write(filter_unit)

st.markdown("_____")
st.header('Employee Attrition Analysis')

# Histograma (Edad)
age = data['Age']

fig_hist_age = px.histogram(data, x='Age', title='Employee Age Distribution')
fig_hist_age.update_layout(bargap=0.2)
st.plotly_chart(fig_hist_age)

#Gráfico de Frecuencias (Unidad)
fig_hist_unit = px.histogram(data, x='Unit', title='Functional Unit Employee Distribution', color_discrete_sequence=['indianred'])
fig_hist_unit.update_layout(bargap=0.2)
st.plotly_chart(fig_hist_unit)

# Gráfico de Dispersión (Tiempo de servicio, Deserción)
fig_scatter_service_attrition = px.scatter(data, x='Time_of_service', y='Attrition_rate', title='Relationship between Time of Service and Attrition Rate', color_discrete_sequence=['orchid'])
st.plotly_chart(fig_scatter_service_attrition)
st.write('There no relation between these 2 variables.')

#Gráfico de barras (Deserción por Ciudad)
avg_attrition_hometown = data[['Hometown', 'Attrition_rate']].groupby('Hometown').mean().sort_values('Attrition_rate').reset_index()
fig_hometown_attrition = px.bar(avg_attrition_hometown, x='Hometown', y='Attrition_rate', title='Attrition rate by Hometown', color_discrete_sequence=['cornflowerblue'])
st.plotly_chart(fig_hometown_attrition)

#Gráfico de Dispersión (Edad, Deserción)
fig_scatter_age_attrition = px.scatter(data, x='Age', y='Attrition_rate', title='Relationship between Age and Attrition')
st.plotly_chart(fig_scatter_service_attrition)
st.write('There no relation between these 2 variables.')