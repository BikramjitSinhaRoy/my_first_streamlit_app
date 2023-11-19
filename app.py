import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd


st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a dataframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)
x_limit = 100
x_axis = np.arange(0, x_limit ,1)

y_data = [random.random() for value in x_axis]

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)


st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)

scatter = alt.Chart(df).mark_point().encode(
    x= 'x',
    y= 'y'
)

st.altair_chart(scatter, use_container_width=True)




st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)

st.markdown("The five changes I made were.....")
st.markdown("""
The 5 changes I made were:
- Change 1: Added Tooltip
- Change 2: X axis label
- Change 3: Y axis label
- Change 4: Chart title
- Change 5,6,7,8: Size, Color, Opacity, Fill
""")

scatter = alt.Chart(df, title= "My new chart title").mark_point(size= 100, opacity= .2, fill= 'green', color='green').encode(
    alt.X('x', title = "My new x-axis title"),
    alt.Y('y', title = "My new y-axis title"),
    tooltip= ['x', 'y']
)

st.altair_chart(scatter, use_container_width=True)

st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)

st.markdown("""
The 2 changes I made were:
- Change 1: Color
- Change 2: Title
"""
)

source = pd.read_json('imdb.json')
st.write(source)

bar = alt.Chart(source).mark_bar(color ='#14a8c9').encode(
    alt.X("IMDB_Rating:Q", bin=True, title="IMDB Rating"), 
    alt.Y('count()',title="Records")
)

st.altair_chart(bar, use_container_width=True)
