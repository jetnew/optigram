import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from info import *
import altair as alt
import numpy as np

# Import dataframes
df_electricity = pd.read_excel("electricity_by_area_and_building.xlsx", index_col="Area")
df_population_size = pd.read_excel("population_size.xlsx")
df_agg_elec = pd.read_excel("aggregated_electricity.xlsx")

def compute_usage(device, num, num_hours):
    if device == "aircon":
        unit = 0.8
    elif device == "fan":
        unit = 0.1
    elif device == "fluorescent":
        unit = 0.013
    elif device == "incandescent":
        unit = 0.06
    co2_monthly = unit * num * num_hours * 30 * 0.4085
    cost_monthly = unit * num * num_hours * 30 * 0.27
    car_distance = co2_monthly / 0.251087632
    return co2_monthly, cost_monthly, car_distance


st.title("Your Expensive Relationship With Energy")

st.caption("Authors: He Shiying and New Jun Jie")

# ========== Part 1: Introduction to the Climate Emergency ==========

st.header("We are aware of the climate emergency.")

st.markdown("51 billion tons of greenhouse gases are added to the atmosphere yearly. If we want to stop global warming and avoid the worst effects of climate change, [we need to work towards reducing our emissions down to zero](https://iea.blob.core.windows.net/assets/beceb956-0dcf-4d73-89fe-1310e3046d68/NetZeroby2050-ARoadmapfortheGlobalEnergySector_CORR.pdf).")
st.markdown("In case you didn’t already know, carbon emissions (CO2) are the #1 driver of global warming. And what is the greatest source of CO2 emissions? **Energy consumption**.")
st.markdown("In 2018, energy consumption from oil is the greatest by far, at 4M kilotonnes of oil equivalent (ktoe), more than *double* that of electricity (2ktoe).")

c1, c2 = st.columns(2)
c1.image('images/global_energy_consumption.png', caption="Figure 1: Global consumption of energy by source from 1990-2018.")

c2.image('images/global_co2_emissions.png', caption="Figure 2: Global CO2 emissions by source from 1990-2018")

st.markdown("The more energy we consume, the more CO2 we are adding to our atmosphere. Recently in 2019, global energy-related CO2 emissions reached [an all-time high and plateaued at 33 gigatonnes (Gt) of CO2](https://www.iea.org/articles/global-co2-emissions-in-2019), with global atmospheric carbon dioxide levels [averaging at 409.8 parts per million (ppm)](https://www.climate.gov/news-features/understanding-climate/climate-change-atmospheric-carbon-dioxide).")

st.image('images/co2_over_history.png', caption="Figure 3: The levels of CO2 in our atmosphere are higher than they have been at any time in the past 400,000 years")

st.markdown("The implications are immense. Researchers have shown that for hundreds of thousands of years, atmospheric CO2 has never been above 300ppm, while current levels have already reached above 400ppm.")

st.header("We are also aware that the globe is getting hotter.")

st.markdown("But why worry about skyrocketing CO2 emission levels? One huge reason remains: the abnormal amounts of carbon emissions in our atmosphere is *cooking us from the inside*. CO2 is a greenhouse gas, which traps heat in the atmosphere to keep the planet warm. And because of the greenhouse gas effect, our rising CO2 emissions are literally wrapping the earth around in a thick blanket, [trapping heat and preventing them from escaping into space](https://www.epa.gov/ghgemissions/overview-greenhouse-gases).")

st.image('images/greenhouse_effect.png', caption="Figure 4: The Greenhouse Gas Effect")

st.image('images/co2_temperature_over_history.png', caption="Figure 5: The relationship between rising CO2 levels and the earth’s temperature")
st.caption("")

st.markdown("Since energy consumption is the biggest driver of carbon emissions (27% of greenhouse gas emissions) which in turn causes global warming, cutting back on energy consumption  remains essential for us to achieve our collective climate goal of limiting global temperature increases to within 1.5 degrees Celsius.")

# ========== Part 2: Diving into Singapore's energy consumption landscape ==========

st.header("How much energy are Singaporeans consuming at home?")

st.markdown("Did you know that households only accounted for 5.0% of energy consumption out of Singapore’s total energy consumption, primarily in the form of [electricity (i.e. 652.6 ktoe) and natural gas by way of town gas (i.e. 60.9 ktoe)](https://www.ema.gov.sg/cmsmedia/Publications_and_Statistics/Publications/SES18/Publication_Singapore_Energy_Statistics_2018.pdf)?")
st.markdown("However, when it comes to electricity consumption, our households contribute a much larger proportion of about [14.9% of all electricity consumption in Singapore in 2019](https://www.ema.gov.sg/singapore-energy-statistics/Ch03/index3). This figure is projected to rise.")
st.markdown("If we look at who’s consuming the most electricity, we see that generally, [public housing consumes more electricity than private housing](https://www.ema.gov.sg/cmsmedia/Publications_and_Statistics/Publications/SES18/Publication_Singapore_Energy_Statistics_2018.pdf). Here’s a breakdown by housing type across the years: about 58.8% (4,287.2 GWh) of total consumption was by public housing units, while another 41.1% (2,999.3 GWh) was attributed to private housing units.")

st.image('images/total_electricity_households.png', caption="Figure 6: Total electricity consumption by households based on housing type in 2017")

# ========== Part 3: Interactive Segment on Average Household Energy Use ==========

st.header("How much electricity is your neighbourhood using on average?")

st.warning("Find out how much electricity your neighbourhood is using on average.")

residential_area = st.selectbox('Select your residential area:', area)
dwelling_type = st.selectbox('Select your housing type:', housing_type)

avg_elec_consumed = df_electricity[dwelling_type][residential_area]
st.error(f"Average Electricity Consumed: {avg_elec_consumed:.2f} kWh")

with st.expander(f"Optional: Compare your monthly electricity usage with the average among {residential_area} {dwelling_type}!"):
    user_avg_elec = st.number_input("How much electricity do you use a month? (kWh)")

    if dwelling_type == "Condominiums and Other Apartments" or dwelling_type == "Landed Properties":
        residential_area = "Overall"
        st.info(f"Note: There is only available average data for {dwelling_type}.")

    avg_elec_consumed = df_electricity[dwelling_type][residential_area]
    st.markdown(f"Average Electricity Consumed: **{avg_elec_consumed:.2f} kWh**")
    c = alt.Chart(pd.DataFrame({
        'Electricity Consumed': [user_avg_elec, avg_elec_consumed],
        ' ': ["Your monthly electricity usage", "Average monthly electricity usage"],
    })).mark_bar().encode(x=' ', y='Electricity Consumed').properties(height=350)
    st.altair_chart(c, use_container_width=True)

st.markdown("This is the average electricty consumed by housing type:")
c = alt.Chart(df_agg_elec).mark_bar().encode(
    x='Housing', y='Usage').properties(height=500)
st.altair_chart(c, use_container_width=True)
st.caption("Figure 7: Average Monthly Electricity Consumption by Planning Area & Housing Type in 2015")


# ========== Part 4: Interactive Segment on Aircon vs Fan ==========

st.header("What’s contributing to all that electricity use?")

st.markdown("And if we dig deeper into the actual appliances we are using at home, the biggest electricity suckers tend to be our air-conditioners, water heaters and refrigerators. In 2012, the National Environment Agency (NEA) found that when energy consumption was weighted across all housing types, air-conditioners, water heaters, and refrigerators contribute to [more than 75% of the electricity consumed by a household](https://www.e2singapore.gov.sg/overview/households/saving-energy-at-home/HEA)!")

st.image('images/household_energy_profile.png', caption="Figure 8: Household energy consumption profile in 2016.")

st.header("Two tiny tricks to make immediate impact")
st.markdown("Our electricity use costs money and releases lots of CO2 into our already-cluttered atmosphere. Let’s visualise how two tricks we can practice at home will help us save our pockets and the environment at the same time.")

st.header("Tip 1: Swap out some aircon hours with fan hours.")
st.markdown("Did you know that an air conditioner (aircon for short) utilises up to 8 times more electricity than a floor fan? On average, Singaporeans turn on their aircons for 6 hours a day!")
st.warning("Let’s calculate how much you are currently spending.")

c1, c2 = st.columns(2)
num_fans = int(c1.number_input("No. of fans:", value=2))
unit_fan_hours = int(c2.number_input("Hours of daily usage per fan:", value=3))
curr_fan_hours = num_fans * unit_fan_hours
c1, c2 = st.columns(2)
num_aircon = int(c1.number_input("No. of aircons:", value=2))
unit_aircon_hours = int(c2.number_input("Hours of daily usage per aircon:", value=3))
curr_aircon_hours = num_aircon * unit_aircon_hours
fan_co2_monthly, fan_cost_monthly, fan_car_distance = compute_usage("fan", 1, curr_fan_hours)
aircon_co2_monthly, aircon_cost_monthly, aircon_car_distance = compute_usage("aircon", 1, curr_aircon_hours)
monthly_cost = fan_cost_monthly + aircon_cost_monthly
monthly_co2 = fan_co2_monthly + aircon_co2_monthly
st.error(f"You currently spend: **${monthly_cost:.2f}** a month!")

st.markdown("Let’s now decide to swap out some aircon hours and replace them with fan hours.")

hours_diff = st.slider("No. of aircon hours to switch to fan hours", 0, curr_aircon_hours, value=0)
fan_co2_monthly, fan_cost_monthly, fan_car_distance = compute_usage("fan", 1, hours_diff)
aircon_co2_monthly, aircon_cost_monthly, aircon_car_distance = compute_usage("aircon", 1, hours_diff)
cost_savings = abs(fan_cost_monthly - aircon_cost_monthly)
new_monthly_cost = monthly_cost - cost_savings
new_monthly_co2 = monthly_co2 - fan_co2_monthly - aircon_co2_monthly
st.success(f"You now spend ${new_monthly_cost:.2f}, and save a total of **${cost_savings:.2f}** every month! That's equivalent to {cost_savings/4:.0f} cup(s) of bubble tea! :) (per month!)")

c1, c2 = st.columns(2)
df_monthly_cost = pd.DataFrame({
    'Before & After': ["Monthly Cost", "Monthly Cost (After)"],
    'Monthly Cost ($)': [monthly_cost, new_monthly_cost]})
c = alt.Chart(df_monthly_cost).mark_bar().encode(
    x='Before & After', y='Monthly Cost ($)')
c1.altair_chart(c, use_container_width=True)
st.caption("Figure 9: Monthly Savings in Electricity Cost")

df_monthly_co2 = pd.DataFrame({
    'Before & After': ["Monthly CO2", "Monthly CO2 (After)"],
    'Monthly CO2': [monthly_co2, new_monthly_co2]})
c = alt.Chart(df_monthly_co2).mark_bar().encode(
    x='Before & After', y='Monthly CO2')
c2.altair_chart(c, use_container_width=True)
st.caption("Figure 10: Monthly Reduction in CO2 emissions")

# What happens if every household in Singapore swaps out some aircon hours for fan hours?
st.markdown("What happens if every household in Singapore swaps out some aircon hours for fan hours?")
sg_population_size = 1_225_300
reduction_co2 = monthly_co2 - new_monthly_co2
st.success(f"If everyone was as honourable as you, the whole of Singapore would save: **${cost_savings * sg_population_size:,.2f}** and cut down **{reduction_co2 * sg_population_size:,.2f} kg** of CO2 emissions per month!")

# ========== Part 5: Interactive segment on Fluorescent vs Incandescent ==========

st.header("Tip 2: Switch out your bulbs.")
st.markdown("How you choose to light up your home matters. Did you know that a fluorescent lamp uses only 13W of electricity while an incandescent bulb uses 60W? Choosing energy-efficient light bulbs to save up to [$30 per bulb per year](https://www.cgs.gov.sg/what-we-do/programmes/eco-music-challenge/let%27s-go-green/nea%27s-go-green-tips).")
st.warning("Let’s calculate how much you are currently spending.")

c1, c2 = st.columns(2)
num_f = int(c1.number_input("No. of fluorescent bulbs:", value=5))
f_hours = int(c2.number_input("Hours of usage per fluorescent bulb:", value=10))
curr_f_hours = num_f * f_hours
c1, c2 = st.columns(2)
num_i = int(c1.number_input("No. of incandescent bulbs:", value=5))
i_hours = int(c2.number_input("Hours of usage per incandescent bulb:", value=10))
curr_i_hours = num_i * i_hours
f_co2_monthly, f_cost_monthly, f_car_distance = compute_usage("fluorescent", 1, curr_f_hours)
i_co2_monthly, i_cost_monthly, i_car_distance = compute_usage("incandescent", 1, curr_i_hours)
monthly_cost = f_cost_monthly + i_cost_monthly
monthly_co2 = f_co2_monthly + i_co2_monthly
st.error(f"You currently spend: **${monthly_cost:.2f}** a month!")

st.markdown("Let’s now decide to swap out some incandescent bulbs and replace them with fluorescent bulbs.")

hours_diff = st.slider("No. of incandescent bulbs to switch to fluorescent bulbs", 0, num_i, value=0)
f_co2_monthly, f_cost_monthly, f_car_distance = compute_usage("fluorescent", 1, hours_diff)
i_co2_monthly, i_cost_monthly, i_car_distance = compute_usage("incandescent", 1, hours_diff)
cost_savings = abs(f_cost_monthly - i_cost_monthly)
new_monthly_cost = monthly_cost - cost_savings
new_monthly_co2 = monthly_co2 + f_co2_monthly - i_co2_monthly
st.success(f"You now spend ${new_monthly_cost:.2f}, and save a total of **${cost_savings:.2f}** every month!")
st.success(f"You also reduce CO2 emissions from {monthly_co2:.2f} kg to **{new_monthly_co2:.2f} kg** of CO2 emissions per month!")

st.success(f"If everyone was as honourable as you, the whole of Singapore would save **${cost_savings * sg_population_size:,.2f}** and cut down **{(monthly_co2 - new_monthly_co2) * sg_population_size:,.2f} kg** of CO2 emissions per month!")


# ========== Part 6: Conclusion ==========

st.header("Conclusion: Don’t stop here.")

st.markdown("We have shared two nifty tricks you can adopt to mitigate your own personal impact on climate change: switching out your aircon hours for fan hours, and replacing your incandescent bulbs with fluorescent ones. There is, of course, more you can do. ")

st.subheader("Write to your leaders.")
st.markdown("Make phone calls to your [local government representatives](https://www.gatesnotes.com/Energy/What-you-can-do-to-fight-climate-change)- ask them about their stance on climate change and what they are doing about it. Raise your concerns about current policies in place and let them know that their actions will influence your voting decisions.")

st.subheader("Support climate initiatives.")
st.markdown("Adopt a tree as part of [WWF India’s Adopt a Tree programme](https://join.wwfindia.org/adopt-a-tree/), offset your carbon footprint by removing carbon dioxide from the atmosphere with [Climeworks](​​https://climeworks.com/subscriptions) or destroying refrigerants in the air with [Tradewater](https://tradewater.us/offsetnow).")

st.subheader("Vote with your dollar.")
st.markdown("The market is ruled by supply and demand. As a consumer, you have the power to influence what brands produce. Opt for a [plant-based burger next time](https://www.globalcitizen.org/en/content/which-vegan-burger-best-environment/),  buy energy-efficient appliances, and purchase from sustainable brands. Supporting sustainable products goes a long way to signal to brands that there is a market for them.")

st.header("Footnotes")

st.caption("Monthly cost savings are based on an electricity tariff of $0.27 per kWh, assuming a 0.8kWh  air-conditioner and  0.1kWh floor fan used for 30 days a month.")
st.caption("CO2 emissions are based on Singapore’s 2019 average Operating Margin (OD) Grid Emission Factor (GEF) of 0.4085 kg CO2/kWh.")
st.caption("Monthly cost savings are based on an electricity tariff of $0.27 per kWh, assuming a 0.013kWh fluorescent lamp and 0.06 kWh incandescent bulb used for 30 days a month.")

st.header("References")

st.subheader("Figures")
st.caption("Figure 1 Source: International Energy Agency. (2020). Total final consumption of energy by source, World 1990-2018. IEA. https://www.iea.org/data-and-statistics/data-tables")
st.caption("Figure 2 Source: International Energy Agency. (2020). CO2 emissions by energy source, World 1990-2018. IEA. https://www.iea.org/data-and-statistics/data-tables")
st.caption("Figure 3 Source: NASA. (2013). Graphic: The relentless rise of carbon dioxide. Climate Change: Vital Signs of the Planet. https://climate.nasa.gov/climate_resources/24/graphic-the-relentless-rise-of-carbon-dioxide")
st.caption("Figure 4 Source: NRDC, & Denchak, M. (2019). Greenhouse Effect 101. NRDC. https://www.nrdc.org/stories/greenhouse-effect-101")
st.caption("Figure 5 Source: Bhatia, A. (2020). Your Personal Carbon History. Parametric Press: The Climate Issue. https://parametric.press/issue-02/carbon-history/")
st.caption("Figure 6 Source: The Energy Market Authority. (2018). Singapore Energy Statistics 2018. https://www.ema.gov.sg/cmsmedia/Publications_and_Statistics/Publications/SES18/Publication_Singapore_Energy_Statistics_2018.pdf")
st.caption("Figure 7 Source: Enterprise Singapore and Energy Market Authority (EMA) (2020). Singapore Energy Statistics. https://www.ema.gov.sg/Singapore_Energy_Statistics.aspx")
st.caption("Figure 8 Source: Energy Efficient Singapore. (2019). Home Energy Audit. Energy Efficient Singapore. https://www.e2singapore.gov.sg/overview/households/saving-energy-at-home/HEA")

st.subheader("Datasets and Other Information")
st.caption("Bhatia, A. (2020). Your Personal Carbon History. Parametric Press: The Climate Issue. https://parametric.press/issue-02/carbon-history/")
st.caption("Energy Efficient Singapore. (2019). Home Energy Audit. Energy Efficient Singapore. https://www.e2singapore.gov.sg/overview/households/saving-energy-at-home/HEA")
st.caption("Energy Market Authority. (2019a). Energy Consumption Chapter 03. Singapore Energy Statistics. https://www.ema.gov.sg/singapore-energy-statistics/Ch03/index3")
st.caption("Energy Market Authority. (2019b). Energy Transformation Chapter 02. Singapore Energy Statistics. https://www.ema.gov.sg/singapore-energy-statistics/Ch02/index2")
st.caption("International Energy Agency. (2020a). CO2 emissions by energy source, World 1990-2018. IEA. https://www.iea.org/data-and-statistics/data-tables")
st.caption("International Energy Agency. (2020b). Total final consumption of energy by source, World 1990-2018. IEA. https://www.iea.org/data-and-statistics/data-tables")
st.caption("International Energy Agency. (2020c, February 11). Global CO2 emissions in 2019 – Analysis. IEA. https://www.iea.org/articles/global-co2-emissions-in-2019")
st.caption("International Energy Agency. (2021). Net Zero by 2050—A Roadmap for the Global Energy Sector (p. 224). IEA. https://iea.blob.core.windows.net/assets/beceb956-0dcf-4d73-89fe-1310e3046d68/NetZeroby2050-ARoadmapfortheGlobalEnergySector_CORR.pdf")
st.caption("Lindsey, R. (2020, August 14). Climate Change: Atmospheric Carbon Dioxide. Climate.Gov. https://www.climate.gov/news-features/understanding-climate/climate-change-atmospheric-carbon-dioxide")
st.caption("NASA. (2013). Graphic: The relentless rise of carbon dioxide. Climate Change: Vital Signs of the Planet. https://climate.nasa.gov/climate_resources/24/graphic-the-relentless-rise-of-carbon-dioxide")
st.caption("National Environment Agency. (2020, November). NEA’s Go Green Tips. Clean & Green Singapore. https://www.cgs.gov.sg/what-we-do/programmes/eco-music-challenge/let%27s-go-green/nea%27s-go-green-tips")
st.caption("NRDC, & Denchak, M. (2019, July). Greenhouse Effect 101. NRDC. https://www.nrdc.org/stories/greenhouse-effect-101")
st.caption("The Energy Market Authority. (2018). Singapore Energy Statistics 2018. https://www.ema.gov.sg/cmsmedia/Publications_and_Statistics/Publications/SES18/Publication_Singapore_Energy_Statistics_2018.pdf")
st.caption("United States Environmental Protection Agency. (2015, December 12). Overview of Greenhouse Gases [Overviews and Factsheets]. https://www.epa.gov/ghgemissions/overview-greenhouse-gases")
