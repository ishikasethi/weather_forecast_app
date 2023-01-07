import streamlit as st
import plotly.express as px
from backend import get_data

# st.set_page_config(layout="wide")

# Add the title, text input, slider, selection, and subhead
st.title("Weather Forecast for next few days")

st.write("<b>Note: </b>The data shown here is being rendered from this [API](https://openweathermap.org/forecast5)",
         unsafe_allow_html=True)

place = st.text_input("Type in a Place: ")
days = st.slider("Days to Forecast", min_value=1, max_value=5,
                 help="Select the number of days to forecast.")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        # Get the temperature/sky data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            # Create a temperature plot
            temperatures = [(dict['main']['temp'] / 10) for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]

            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
    except KeyError:
        st.error("Oh! You entered a non-existed place. Enter again")

