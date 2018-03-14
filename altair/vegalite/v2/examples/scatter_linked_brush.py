"""
Faceted Scatter Plot with Linked Brushing
-----------------------------------------
This is an example of using an interval selection to control the color of
points across multiple facets.
"""
# category: interactive

import altair as alt
from vega_datasets import data

cars = data.cars()

brush = alt.selection(type='interval', resolve='global')

base = alt.Chart(cars).mark_point().encode(
    y='Miles_per_Gallon',
    color=alt.condition(brush, 'Origin', alt.ColorValue('gray'))
).properties(
    selection=brush,
    width=250,
    height=250
)

chart = base.encode(x='Horsepower') | base.encode(x='Acceleration')