# conda activate csv_xlsx_streamlit
from categories.compare import Compare
import streamlit as st

st.set_page_config(layout="wide")
st.set_option("deprecation.showPyplotGlobalUse", False)


def main():
    select_box = st.sidebar.selectbox("Select Category", ["Home", "Compare"])

    option_functions = {
        "Home": "home",
        "Compare": Compare,
    }

    if option_functions[select_box] != "home":
        option_functions[select_box]()
    else:
        st.title("Excel and CSV File Processing")


if __name__ == "__main__":
    main()
