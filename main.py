import streamlit as st
import pandas as pd
import numpy as np
import time
from data.mock_data import column_text_data
from PIL import Image

# import matplotlib.pyplot as plt

pokemon = pd.read_csv("data/data.csv", index_col="Name")
mockdata = pd.read_csv("data/MOCK_DATA.csv")


# set page configuration
st.set_page_config(
    page_title="Demo App",
    initial_sidebar_state="collapsed",
    page_icon=None,
    layout="wide",
    menu_items=None,
)
st.title("Demo App")


# ------------------------------------------ Sidebar ---------------------------------------------------
# create and set sidebars
with st.sidebar:
    st.write("# Sidebar")

# ------------------------------------------ Tabs ---------------------------------------------------
# create and set tabs
(
    text_tab,
    visualization_tab,
    data_tab,
    controls_tab,
    status_tab,
    media_tab,
    messages_tab,
    layouts_tab,
    animations_tab,
    logic_tab,
) = st.tabs(
    [
        "Text",
        "Visualizations",
        "Data",
        "Controls",
        "Status",
        "Media",
        "Messages",
        "Layouts",
        "Animations",
        "Logic",
    ]
)


# ------------------------------------------ Text Tab ---------------------------------------------------
with text_tab:
    left_column, right_column = st.columns(2)

    with left_column:
        st.title("Title")
        st.header("Header", help="Optional tooltip")
        st.subheader("Subheader")
        st.text("Fixed width text")
        st.markdown("**Markdown**")
        st.write("**bold**")
        st.caption("Caption", help="Optional tooltip")
        "### Magic text rendering"
        "**Bold**"
        "*Italic*"

    with right_column:
        "### Metrics/KPI Widgets"
        col1, col2, col3 = st.columns(3)
        col1.metric("Temperature", "70 °F", "1.2 °F", help="Optional toolbar")
        col2.metric("Wind", "9 mph", "-8%")
        col3.metric("Humidity", "86%", "4%")
        st.divider()
        "### Display code"
        st.code("Code")
        with st.echo():
            st.write("This code will be printed")

# ------------------------------------------ Visualizations Tab ---------------------------------------------------

with visualization_tab:
    vis_left_column, vis_right_column = st.columns(2)
    with vis_left_column:
        "### Line chart"
        "#### One line"
        st.line_chart(pokemon.groupby(["Generation"])[["HP"]].mean())
        "#### Two lines"
        st.line_chart(
            pokemon.groupby(["Generation", "Legendary"])[["HP"]]
            .mean()
            .reset_index()
            .pivot(index="Generation", columns="Legendary", values="HP")
        )
        "### Area chart"
        st.area_chart(pokemon.groupby(["Generation"])[["HP"]].mean())
        "### Matplotlib chart"
        st.pyplot(
            pd.DataFrame(pokemon.groupby(["Type 1"]).size()).plot(kind="barh").figure
        )

    with vis_right_column:
        "### Bar chart"
        st.caption("Pokemon by Type")
        st.bar_chart(pd.DataFrame(pokemon.groupby(["Type 1"]).size()))
        map_data = pd.DataFrame(
            np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
            columns=["lat", "lon"],
        )

        st.map(map_data)

# ------------------------------------------ Data Tab ---------------------------------------------------
with data_tab:
    "#### Dataframe"
    st.dataframe(pokemon, use_container_width=True)

    "#### Dataframe Editor"
    st.data_editor(pokemon.head(), use_container_width=True)


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


# ------------------------------------------ Status Tab ---------------------------------------------------

with status_tab:
    if st.button("Spin me"):
        with st.spinner("Wait for it..."):
            time.sleep(5)
        st.success("Done!")

    if st.button("Progress me"):
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1, text=progress_text)

    if st.button("Error me"):
        st.error("This is an error", icon="🚨")

    if st.button("Warn me"):
        st.warning("This is a warning", icon="⚠️")

    if st.button("Info me"):
        st.info("This is a purely informational message", icon="ℹ️")

    if st.button("Success me"):
        st.success("This is a success message!", icon="✅")

    if st.button("Exception me"):
        e = RuntimeError("This is an exception of type RuntimeError")
        st.exception(e)


# ------------------------------------------ Media Tab ---------------------------------------------------
with media_tab:

    left_column, right_column = st.columns(2)
    with left_column:
        "#### Image"
        image = Image.open("media/hills.jpg")
        st.image(image, "Hills", width=600)

    with right_column:
        "#### Audio"
        audio_file = open("media/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg", "rb")
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format='audio/ogg')
        # sample_rate = 44100  # 44100 samples per second
        # seconds = 2  # Note duration of 2 seconds
        # frequency_la = 440  # Our played note will be 440 Hz
        # # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
        # t = np.linspace(0, seconds, seconds * sample_rate, False)
        # # Generate a 440 Hz sine wave
        # note_la = np.sin(frequency_la * t * 2 * np.pi)

        # st.audio(note_la, sample_rate=sample_rate)
        "#### Video"
        video_file = open("media/star_-_6962 (540p).mp4", 'rb')
        video_bytes = video_file.read()

        st.video(video_bytes)



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


# ------------------------------------------ Animations Tab ------------------  --------------------------------

with animations_tab:
    st.balloons()
    st.snow()


# ------------------------------------------ Logic Tab ---------------------------------------------------

with logic_tab:
    # Use checkboxes to show/hide data
    if st.checkbox("Show dataframe"):
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
        chart_data
