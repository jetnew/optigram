import pandas as pd
import streamlit as st
from texts import *

st.title(txt_title)

st.header(header1)
st.markdown(section1a)
st.image('images/global_energy_consumption.png')
st.image('images/global_co2_emissions.png')
st.markdown(section1b)

st.header(header2)
st.markdown(section2)

st.header(header3)
st.markdown(section3)

st.header("Monitoring Energy Consumption")
st.markdown(section4)

st.header("Interactive Energy Calculator")
residential_area = st.selectbox('Select your residential area:', area)
dwelling_type = st.selectbox('Select your housing type:', housing_type)


"""
Bargraph: Neighbourhood -> Housing type electricity consumption


Slider for no. aircon hours - no. fan hours
Default: User-specified

Bar Chart: CO2 emissions saved and cost savings 
"""


df_electricity = pd.read_excel("electricity_by_area_and_building.xlsx", index_col="Area")
if dwelling_type == "Condominiums and Other Apartments" or dwelling_type == "Landed Properties":
    residential_area = "Overall"
    st.info(f"Note: There is only available average data for {dwelling_type}.")
st.text(f"Average Electricty Consumed: {df_electricity[dwelling_type][residential_area]:.2f}")

st.text("Fan")
num_fan = st.number_input("No. of fans")
num_fan_hours = st.number_input("No. of fan hours used per day")
fan_co2_monthly = 0.1 * num_fan * num_fan_hours * 30 * 0.4085
fan_cost_monthly = 0.1 * num_fan * num_fan_hours * 30 * 0.27
fan_car_distance = fan_co2_monthly / 0.251087632
st.text(f"CO2 emitted per month (kg): {fan_co2_monthly:.2f}")
st.text(f"The amount of CO2 produced is equivalent to that of a car that drove {fan_car_distance:.2f} km!")
st.text(f"The monthly cost of your fan is: S${fan_cost_monthly:.2f}!")
st.text("Aircon")
num_aircon = st.number_input("No. of aircons")
num_aircon_hours = st.number_input("No. of aircon hours used per day")
aircon_co2_monthly = 0.8 * num_aircon * num_aircon_hours * 30 * 0.4085
aircon_cost_monthly = 0.1 * num_fan * num_fan_hours * 30 * 0.27
aircon_car_distance = aircon_co2_monthly / 0.251087632
st.text(f"CO2 emitted per month (kg): {aircon_co2_monthly:.2f}")
st.text(f"The amount of CO2 produced is equivalent to that of a car that drove {aircon_car_distance:.2f} km!")  # TODO: Include footnote
st.text(f"The monthly cost of your aircon is: S${aircon_cost_monthly:.2f}!")

st.text("Average Household Size")
household_size = [3.3, 3.3, 4.3, 2.9]
st.bar_chart(household_size)

df_population_size = pd.read_excel("population_size.xlsx")
