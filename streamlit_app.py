import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from texts import *
import altair as alt


# Import dataframes
df_electricity = pd.read_excel("electricity_by_area_and_building.xlsx", index_col="Area")
df_population_size = pd.read_excel("population_size.xlsx")
agg_elec = pd.read_excel("aggregated_electricity.xlsx", index_col='Type')


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

# Part 1: Introduction to the Climate Emergency
st.header(header1a)  # We are aware...
st.markdown(section1a)  # 51 billion tons...
st.image('images/global_energy_consumption.png')
st.caption(caption1)
st.caption(citation1)
st.image('images/global_co2_emissions.png')
st.caption(caption2)
st.caption(citation2)
st.markdown(section1b)
st.image('images/co2_over_history.png')
st.caption(caption3)
st.caption(citation3)
st.markdown(section1c)

st.header(header1b)
st.markdown(section1d)
st.image('images/greenhouse_effect.png')
st.caption(caption4)
st.caption(citation4)
st.image('images/co2_temperature_over_history.png')
st.caption(caption5)
st.caption(citation5)
st.markdown(section1e)

# Part 2: Diving into Singapore's energy consumption landscape

st.header(header2)
st.markdown(section2)
st.image('images/total_electricity_households.png')
st.caption(caption6)
st.caption(citation6)

# Part 3: Interactive Segment on Average Household Energy Use

st.header(header3)
st.markdown(section3)

residential_area = st.selectbox('Select your residential area:', area)
dwelling_type = st.selectbox('Select your housing type:', housing_type)

avg_elec_consumed = df_electricity[dwelling_type][residential_area]
st.text(f"Average Electricty Consumed: {avg_elec_consumed:.2f} kWh")

with st.beta_expander(f"Optional: Compare your monthly electricity usage with the average among {residential_area} {dwelling_type}!"):
    user_avg_elec = st.number_input("How much electricity do you use a month? (kWh)")

    if dwelling_type == "Condominiums and Other Apartments" or dwelling_type == "Landed Properties":
        residential_area = "Overall"
        st.info(f"Note: There is only available average data for {dwelling_type}.")

    avg_elec_consumed = df_electricity[dwelling_type][residential_area]
    st.text(f"Average Electricty Consumed: {avg_elec_consumed:.2f} kWh")

    st.bar_chart(pd.DataFrame({
        'data': [user_avg_elec, avg_elec_consumed],
        'index': ["Your monthly electricity usage", "Average monthly electricity usage"]
    }))




# Bargraph: Neighbourhood -> Housing type electricity consumption
# Note: Use of wrong excel sheet
st.markdown("This is the average electricty consumed by housing type:")
st.bar_chart(agg_elec['Usage'])

st.caption(caption7)
st.caption(citation7)

# Part 4: Interactive Segment on Aircon vs Fan

st.header(header4)
st.markdown(section4)
st.image('images/household_energy_profile.png')
st.caption(caption8)
st.caption(citation8)

st.subheader(header4a)
st.markdown(section4a)

st.header(header4b)
st.markdown(section4b)

# Slider for no. aircon hours - no. fan hours
# Default: User-specified

curr_fan_hours = int(st.number_input("No. of fan hours used per day (No. of hours x No. of fans)", value=8))
curr_aircon_hours = int(st.number_input("No. of aircon hours used per day (No. of hours x No. of aircons)", value=10))
fan_co2_monthly, fan_cost_monthly, fan_car_distance = compute_usage("fan", 1, curr_fan_hours)
aircon_co2_monthly, aircon_cost_monthly, aircon_car_distance = compute_usage("aircon", 1, curr_aircon_hours)
monthly_cost = fan_cost_monthly + aircon_cost_monthly
monthly_co2 = fan_co2_monthly + aircon_co2_monthly
st.text(f"YOU CURRENTLY SPEND: ${monthly_cost:.2f} A MONTH!")

st.markdown(section4c)
hours_diff = st.slider("No. of aircon hours to switch to fan hours", 0, curr_aircon_hours, value=4)
fan_co2_monthly, fan_cost_monthly, fan_car_distance = compute_usage("fan", 1, hours_diff)
aircon_co2_monthly, aircon_cost_monthly, aircon_car_distance = compute_usage("aircon", 1, hours_diff)
cost_savings = abs(fan_cost_monthly - aircon_cost_monthly)
new_monthly_cost = monthly_cost - cost_savings
new_monthly_co2 = fan_co2_monthly + aircon_co2_monthly
st.markdown(f"You now spend ${new_monthly_cost:.2f}, and save a total of ${cost_savings:.2f} every month!")
st.markdown(f"That's equivalent to {cost_savings/4:.0f} cups of bubble tea! :) (per month!)")


st.bar_chart(pd.DataFrame(
    data={'data': [monthly_cost, new_monthly_cost]},
    index=["Monthly Cost", "Monthly Cost (New)"]))

st.caption(caption9)


st.bar_chart(pd.DataFrame(
    data={'data': [monthly_co2, new_monthly_co2]},
    index=["Monthly CO2", "Monthly CO2 (New)"]))

st.caption(caption10)

# What happens if every household in Singapore swaps out some aircon hours for fan hours?
st.subheader(header4c)
sg_population_size = 1_225_300
st.markdown(f"If everyone was as honourable as you we would save: ${cost_savings * sg_population_size:,.2f} per month!")

reduction_co2 = monthly_co2 - new_monthly_co2
st.markdown(f"If everyone was as honourable as you we would cut down: {reduction_co2 * sg_population_size:,} kg of CO2 emissions per month!")


# Part 5: Interactive segment on Fluorescent vs Incandescent

st.header(header5)
st.markdown(section5)

# Part 6: References

st.header(header6)
st.markdown(section6)

st.caption(footnotes1)
st.caption(footnotes2)
st.caption(footnotes3)