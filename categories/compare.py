import streamlit as st
import pandas as pd


class Compare:
    def __init__(self):
        self.streamlit_app_view()

    def read_file(file):
        if (
            file.type
            == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ):
            df = pd.read_excel(file)
        elif file.type == "text/csv":
            df = pd.read_csv(file)
        else:
            st.error("Invalid file format. Please upload a CSV or Excel file.")
            df = pd.DataFrame()

        return df

    def display_df(self, df1, df2):
        col1, col2 = st.colummns(2)

        with col1:
            st.dataframe(df1)

        with col2:
            st.dataframe(df2)

    def streamlit_app_view(self):
        st.title("Compare 2 files")

        st.divider()

        st.write("Upload 2 csv or excel files")
        file1 = st.file_uploader(
            "Upload the first CSV or Excel file", type=["csv", "xlsx"]
        )
        file2 = st.file_uploader(
            "Upload the second CSV or Excel file", type=["csv", "xlsx"]
        )

        if file1 and file2:
            self.df1 = read_file(file1)
            self.df2 = read_file(file2)
