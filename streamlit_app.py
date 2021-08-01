import streamlit as st

st.title("Optigram 2021 - Your expensive relationship with energy")

st.header("A Climate Emergency")

st.markdown("""51 billion tons of greenhouse gases are added to the atmosphere yearly and zero is the goal we need to aim for to stop global warming and avoid the worst effects of climate change.
Carbon emissions (CO2) are the #1 driver of global warming, and the #1 source of carbon emissions is fossil fuel burning for energy consumption.
In 2018, energy consumption from oil is the greatest by far (4M ktoe), more than double from electricity (2ktoe) (iea.org).
Global Energy Consumption (left) and Global CO2 Emissions by Energy Source (right) (iea.org)

Since CO2 emissions increase proportionately with energy consumption, the extent of energy consumption is tightly linked to carbon emissions over time. (iea.org, climate.nasa.gov)

Recent CO2 emissions reached an all-time high across history of 33K metric tonnes of CO2. To understand the sheer severity of this, researchers have shown that for hundreds of thousands of years, atmospheric CO2 has never been above 300ppm, while current levels have already reached above 400ppm. CO2 emissions have always highly correlated with global temperatures throughout history.
CO2 emissions influence global temperatures through the greenhouse effect. Greenhouse gases such as CO2 in the atmosphere trap heat from the sun that would otherwise escape into space. However, as more greenhouse gases accumulate, more heat is trapped and global warming results.
Greenhouse Effect (left) and Relationship Between Temperature Level and CO2 level (right) (NRDC)

From 1951 to 2010, the observed warming is about 0.65 degrees Celsius, while the contribution from greenhouse gases is about 0.9 degrees Celsius.

The Paris agreement signed by all members in the United Nations aims to control global warming preferably within 1.5 degrees Celsius, exceeding which will result in climate uncertainty.

Since energy consumption is the biggest driver of carbon emissions (27% of greenhouse gas emissions) which in turn causes global warming, energy consumption is a major factor that needs to be reduced to achieve the climate goal of within 1.5 degrees Celsius increase.
""")

st.header("Singapore's Energy Consumption Landscape")

st.markdown("""Households only accounted for 5.0% of energy consumption out of Singapore’s total energy consumption, primarily in the form of electricity (i.e. 652.6 ktoe) and natural gas by way of town gas (i.e. 60.9 ktoe). (Singapore Energy Statistics)

Households contributed 14.9% of all electricity consumption in Singapore in 2019, and is projected to rise. (EMA)

Breakdown by housing type across the years: About 58.8% (4,287.2 GWh) of total consumption was by public housing units, while another 41.1% (2,999.3 GWh) was attributed to private housing units (Singapore Energy Statistics)

In 2012, NEA found that air-conditioners, water heaters, and refrigerators contribute to more than 75% of the electricity consumed (E2 Singapore)
(E2 Singapore)

In NEA’s Household Energy Consumption Study 2017, this proportion dropped to 52% (E2 Singapore)
""")

st.header("Your Energy Choices")

st.markdown("""
Fan vs air-conditioner vs natural ventilation
* AC constitutes 19% of SG’s carbon emissions
* ACs consume the bulk of a household’s electricity bill. A fan uses less than 10% the electricity of an AC. This means you can save up to $840 a year (NEA).
* Set AC temperature at about 25 degrees Celsius. Save up to $25 a year for every degree raised (NEA).

Older vs newer energy-efficient appliances
* A 4-tick AC saves $450 in electricity bills a year compared to a 1-tick model, and saves $70 a year compared to a 2-tick model (NEA).
* A 5-tick AC saves $270 in electricity bills a year compared to a 2-tick model. (E2 Singapore)
    * Based on electricity cost of $0.27 per kWh of electricity, assuming a multi-split 7.5kW cooling capacity air-conditioner used 8 hours daily (E2 Singapore)

Gas stove vs induction cooker
* I think induction cooker is actually more expensive (Money Smart)

Incandescent bulb vs fluorescent lamp
* A Fluorescent lamp uses only 13W while an incandescent bulb uses 60W. Choose energy-efficient light bulbs to save up to $30 a bulb per year (NEA).
* A light-emitting diode (LED) uses only 9W. LED bulbs can use up to 85% less electricity compared to incandescent bulbs + last 20 times longer while producing the same amount of light (E2 Singapore)
(E2 Singapore)

Vampire plugs (standby power)
* Standby power can account up to 10% of home electricity use. Switch them off when not in use to save up to $70 a year (NEA).
* Switch off home appliances at the power socket. Standby power can cost you about $25 a year (E2 Singapore)
* Based on electricity cost of $0.27 per kWh of electricity

Car vs public transport vs cycling
* The car uses 9 times more energy than taking a bus and 12 times more energy than taking a train (Ministry of Transport).

Solutions/ mitigation methods
* Resource efficiency guide for new home owners
""")

st.header("Monitoring Energy Consumption")

st.markdown("""The utility bill shows the electricity consumption (kWh) over the past 6 months. For more accurate monitoring of appliance’s energy consumption and track consumption over time, use an energy monitor such as ETrack or Wattson (Green Future).
""")
st.header("Interactive Energy Calculator")

st.markdown("""
General idea
* Users will be able to see how much cost is incurred, electricity consumed and carbon emissions produced based on how many air conditioners they own and the hours they are using them at home. 
Users will also be able to see how their average monthly or annual electricity consumption compares to others of similar housing types and neighbourhoods after switching over from an aircon to a fan.

Choose location: [Bukit batok, ... , ]

Num. of fans: _
* _ x This cell in this form etc

Variables to consider
* Electricity consumption units: kWh
* Aircon: 0.8kWh
* Fan: 0.1kWh
* Tariff rate/ Cost per kWh: $0.27 (E2A and NEA)
* CO2 emissions emitted per kWh of electricity generated as of 2019: 0.4085kg 
* This refers to Singapore’s average Operating Margin (OM) Grid Emission Factor (GEF) (EMA)
* Monthly electricity consumption in GWh based on housing type and region in Sg
* Annual electricity consumption in GWh based on housing type and region in Sg
* Input variables
    * No. of aircon units in the house
    * Housing type
        * 1-Room / 2-Room
        * 3-Room 
        * 4-Room
        * 5-Room and Executive
        * Private Apartments and Condominiums
        * Landed Properties
""")