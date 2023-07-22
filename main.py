import streamlit as st
import pandas as pd
import numpy as np
from mock_data import column_text_data
# import matplotlib.pyplot as plt

# set page configuration
st.set_page_config(page_title="Exercise App")
st.title("Exercise App")


# ------------------------------------------ Sidebar ---------------------------------------------------
# create and set sidebars
with st.sidebar:
    st.write("# Sidebar")


# ------------------------------------------ Tabs ---------------------------------------------------
# create and set tabs
(
    text_tab,
    controls_tab,
    messages_tab,
    layouts_tab,
    data_tab,
    visualization_tab,
    animations_tab,
    logic_tab,
) = st.tabs(
    ["Text", "Controls", "Messages", "Layouts", "Data", "Visualizations", "Animations", "Logic"]
)




# ------------------------------------------ Text Tab ---------------------------------------------------
with text_tab:
    "# Title"
    st.title("Title")
    st.header("Header")
    st.subheader("Subheader")
    st.text("Fixed width text")
    st.markdown("**Markdown**")
    st.write("**bold**")
    st.caption("Caption")
    st.code("a = 1234")
    st.divider()
    "### Magic text rendering"
    "**Non-Markdown**"
    "# 1 Text"
    "## 2"
    "### 3"
    "#### 4"
    "#### 5"
    "##### 6"
    st.divider()
    "### Metrics/KPI Widgets"
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")
    st.divider()
    "### Display code"
    with st.echo():
        st.write("This code will be printed")

# ------------------------------------------ Controls Tab ---------------------------------------------------

with controls_tab:
    st.write("## User widgets")
    st.text_input("Text Input", key="name")
    # You can access the value at any point with:
    print(st.session_state.name)
    st.checkbox("Checkbox", help="This is a help toolbar")
    st.selectbox("Select Box", ("A", "B", "C"), index=0)
    st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
    st.button("Hit me")
    # st.download_button('On the dl', df)
    st.checkbox("Check me out")
    st.radio("Radio", [1, 2, 3])
    st.selectbox("Select", [1, 2, 3])
    st.selectbox("Select", [1, 2, 3])
    st.multiselect("Multiselect", [1, 2, 3])
    st.slider("Slide me", min_value=0, max_value=10)
    st.select_slider("Slide to select", options=range(10))
    st.text_input("Enter some text")
    st.number_input("Enter a number")
    st.text_area("Area for textual entry")
    st.date_input("Date input")
    st.time_input("Time entry")
    st.file_uploader("File uploader")
    # st.camera_input("一二三,茄子!")
    st.color_picker("Pick a color")


# ------------------------------------------ Messages Tab ---------------------------------------------------
with messages_tab:
    st.error("Error message")
    st.warning("Warning message")
    st.info("Info message")
    st.success(
        "Success message",
    )

# ------------------------------------------ Layout Tab ---------------------------------------------------
with layouts_tab:
    # create layouts with columns
    left_column, middle_column, right_column = st.columns(3)

    # you can use a column just like st.sidebar:
    left_column.write(column_text_data[0])

    # or even better, call Streamlit functions inside a "with" block:
    with middle_column:
        st.write(column_text_data[1])

    with right_column:
        st.write(column_text_data[2])

# ------------------------------------------ Data Tab ---------------------------------------------------
with data_tab:
    pokemon = pd.read_csv("data.csv", index_col="Name")
    mockdata = pd.read_csv("MOCK_DATA.csv")
    pokemon
    mockdata

# ------------------------------------------ Visualizations Tab ---------------------------------------------------

with visualization_tab:
    vis_left_column, vis_right_column = st.columns(2)
    with vis_left_column:
        "### Line chart"
        st.line_chart(pokemon.groupby(["Generation"])[["HP"]].mean())
        st.line_chart(
            pokemon.groupby(["Generation", "Legendary"])[["HP"]]
            .mean()
            .reset_index()
            .pivot(index="Generation", columns="Legendary", values="HP")
        )
        "### Area chart"
        st.area_chart(pokemon.groupby(["Generation"])[["HP"]].mean())

    with vis_right_column:
        "### Bar chart"
        st.caption("Pokemon by Type")
        st.bar_chart(pd.DataFrame(pokemon.groupby(["Type 1"]).size()))

# ------------------------------------------ Animations Tab ------------------  --------------------------------

with animations_tab:
    "test"

# ------------------------------------------ Logic Tab ---------------------------------------------------

with logic_tab:
    "Logic"

# # st.balloons()
# # st.snow()

# # st.exception()


# # Use checkboxes to show/hide data
# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])

#     chart_data


# # use a selectbox for options
# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })

# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected: ', option


# st.title("Practice App")

# # st.write(df)
# # st.table(df.head(10))
# # df_widget = st.dataframe(df)
# # df_widget.add_rows(df.head())

# # use dataframe methods in order to change it
# dataframe = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))

# st.dataframe(dataframe.style.highlight_max(axis=0))

# # create charts
# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)
# st.line_chart(df.groupby("Generation")[["HP", "Attack", "Defense"]].mean())

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)
# # st.write(plt.scatter(df["HP"], df["Attack"]))
# st.write(df[["HP", "Attack"]].plot.scatter("HP", "Attack"))

# st.slider("Label")
