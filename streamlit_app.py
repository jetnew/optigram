import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from texts import *

def compute_usage(device, num, num_hours):
    if device == "aircon":
        unit = 0.8
    elif device == "fan":
        unit = 0.1
    co2_monthly = unit * num * num_hours * 30 * 0.4085
    cost_monthly = unit * num * num_hours * 30 * 0.27
    car_distance = co2_monthly / 0.251087632
    return co2_monthly, cost_monthly, car_distance

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


# Bargraph: Neighbourhood -> Housing type electricity consumption
agg_elec = pd.read_excel("aggregated_electricity.xlsx", index_col='Type')
st.bar_chart(agg_elec['Usage'])

# Slider for no. aircon hours - no. fan hours
# Default: User-specified

curr_fan_hours = int(st.number_input("No. of fan hours used per day (No. of hours x No. of fans)", value=8))
curr_aircon_hours = int(st.number_input("No. of aircon hours used per day (No. of hours x No. of aircons)", value=10))
fan_co2_monthly, fan_cost_monthly, fan_car_distance = compute_usage("fan", 1, curr_fan_hours)
aircon_co2_monthly, aircon_cost_monthly, aircon_car_distance = compute_usage("aircon", 1, curr_aircon_hours)
monthly_cost = fan_cost_monthly + aircon_cost_monthly
monthly_co2 = fan_co2_monthly + aircon_co2_monthly
st.text(f"YOU CURRENTLY SPEND: ${monthly_cost:.2f} A MONTH!")
hours_diff = st.slider("No. of aircon hours to switch to fan hours", 0, curr_aircon_hours, value=4)
fan_co2_monthly, fan_cost_monthly, fan_car_distance = compute_usage("fan", 1, hours_diff)
aircon_co2_monthly, aircon_cost_monthly, aircon_car_distance = compute_usage("aircon", 1, hours_diff)
cost_savings = abs(fan_cost_monthly - aircon_cost_monthly)
new_monthly_cost = monthly_cost - cost_savings
new_monthly_co2 = fan_co2_monthly + aircon_co2_monthly
st.text(f"YOU NOW SPEND: ${new_monthly_cost:.2f}")
st.text(f"YOU SAVE A GRAND TOTAL OF: ${cost_savings:.2f} A MONTH!")
st.text(f"THAT'S EQUIVALENT TO {cost_savings/4} BUBBLE TEAS! :) (PER MONTH!!!)")

st.bar_chart(pd.DataFrame(
    data={'data': [monthly_cost, new_monthly_cost]},
    index=["Monthly Cost", "Monthly Cost (New)"]))

st.bar_chart(pd.DataFrame(
    data={'data': [monthly_co2, new_monthly_co2]},
    index=["Monthly CO2", "Monthly CO2 (New)"]))


"""
Bar Chart: CO2 emissions saved and cost savings

Bar graph - Aggregated statistics - If everyone changes from AC hours to fan hours per household
By housing type
"""

df_electricity = pd.read_excel("electricity_by_area_and_building.xlsx", index_col="Area")
if dwelling_type == "Condominiums and Other Apartments" or dwelling_type == "Landed Properties":
    residential_area = "Overall"
    st.info(f"Note: There is only available average data for {dwelling_type}.")
st.text(f"Average Electricty Consumed: {df_electricity[dwelling_type][residential_area]:.2f}")

st.text("Fan")


num_fans = st.number_input("No. of fans")
num_fan_hours = st.number_input("No. of fan hours used per day")
fan_co2_monthly, fan_cost_monthly, fan_car_distance = compute_usage("fan", num_fans, num_fan_hours)
st.text(f"CO2 emitted per month (kg): {fan_co2_monthly:.2f}")
st.text(f"The amount of CO2 produced is equivalent to that of a car that drove {fan_car_distance:.2f} km!")
st.text(f"The monthly cost of your fan is: S${fan_cost_monthly:.2f}!")
st.text("Aircon")
num_aircon = st.number_input("No. of aircons")
num_aircon_hours = st.number_input("No. of aircon hours used per day")
aircon_co2_monthly, aircon_cost_monthly, aircon_car_distance = compute_usage("aircon", num_aircon, num_aircon_hours)
st.text(f"CO2 emitted per month (kg): {aircon_co2_monthly:.2f}")
st.text(f"The amount of CO2 produced is equivalent to that of a car that drove {aircon_car_distance:.2f} km!")  # TODO: Include footnote
st.text(f"The monthly cost of your aircon is: S${aircon_cost_monthly:.2f}!")

st.text("Average Household Size")
household_size = [3.3, 3.3, 4.3, 2.9]
st.bar_chart(household_size)

df_population_size = pd.read_excel("population_size.xlsx")
