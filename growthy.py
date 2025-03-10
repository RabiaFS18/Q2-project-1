# import streamlit as st
# import pandas as pd
# import os
# from io import BytesIO

# st.set_page_config(page_title = "Data Sweeper" ,layout='wide' )

# # custom css
# st.markdown(
#     """
#     <style>
#     .stApp{
#         background-color: black;
#         color: white;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
# #title and dicription
# st.title("Data sweeper sterling Integrator By Rabia")
# st.write(" bn nb b   m m mb b b b b")

# #file uploader 
# uploaded_files = st.file_uploader("upload your files (accept CSV or Excel):" , type=["csv","xlsx"], accept_multiple_files=True) 
# if uploaded_files:
#     for file in uploaded_files:
#         file_ext = os.path.splitext(file.name)[-1].lower()

#         if file_ext == ".csv":
#             df = pd.read_csv(file)
#         elif file_ext == ".xlsx":
#             df = pd.read_excel(file)
#         else:
#             st.error(f"Unsupported file type: {file_ext}")
#         #file details
#         st.write("Preview the head of the Dataframe")
#         st.dataframe(df.head())

#         #dara cleaning options
#         st.subheader("data cleaning option")
#         if st.checkbox(f"clean data for {file.name}"):
#             col1, col2 = st.columns(2)

#             with col1:
#                 if st.button(f"Remove duplicates from the file: {file.name}"):
#                     df.drop_duplicates(inplace=True)
#                     st.write("Duplictes removed!")
            
#             with col2:
#                  if st.button(f"Fill missing values for {file.name}"):
#                     numeric_cols = df.select_dtypes(include=['number']).columns
#                     df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
#                     st.write("Mssing values have been filled!")
#         st.subheader("select column to keep")
#         columns = st.multiselect(f"choose columns for {file.name}", df.columns, default=df.columns)
#         df = df[columns]

#         #data visualization
#         st.subheader("Data Visualization")
#         if st.checkbox(f"Show visualization for {file.name} "):
#             st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])

#         #conversion Options

#         st.subheader("Conversion Options")
#         conversion_type = st.radio(f"Convert {file.name} to:", ["CVS" , "Excel"], key=file.name)
#         if st.button(f"Convert{file.name}"):
#           buffer = BytesIO()
#           if conversion_type == "CSV":
#               df.to_csv(buffer, index=False)
#               file_name = file.name.replace(file_ext, ".csv")
#               mime_type = "text/csv"
#         elif conversion_type == "Excel":
#             df.to.to_excel(buffer, index=False)
#             file_name = file.name.replace(file_ext, ".xlsx")
#             mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#         buffer.seek(0)

#         st.download_button(
#             label=f"Download {file.name} as {conversion_type}",
#             data=buffer,
#             file_name=file_name,
#             mime=mime_type
#         )
# st.success("All files processed successfully!")


import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="Data Sweeper", layout='wide')

# Custom CSS
st.markdown(
    """
    <style>
    .stApp{
        background-color: black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Description
st.title("Data Sweeper Sterling Integrator By Rabia")
st.write("bn nb b m m mb b b b b")

# File Uploader
uploaded_files = st.file_uploader("Upload your files (accept CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Try reading the file safely
        try:
            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file)
            else:
                st.error(f"Unsupported file type: {file_ext}")
                continue  # Skip this file if unsupported

        except Exception as e:
            st.error(f"Error reading file {file.name}: {e}")
            continue  # Skip to the next file

        # File details
        st.write(f"### Preview of {file.name}")
        st.dataframe(df.head())

        # Data Cleaning Options
        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Clean data for {file.name}", key=f"clean_{id(file)}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove duplicates from {file.name}", key=f"dup_{id(file)}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates removed!")

            with col2:
                if st.button(f"Fill missing values for {file.name}", key=f"fill_{id(file)}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing values have been filled!")

        # Column Selection
        st.subheader("Select Columns to Keep")
        columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns, key=f"cols_{id(file)}")
        df = df[columns]

        # Data Visualization
        st.subheader("Data Visualization")
        if st.checkbox(f"Show visualization for {file.name}", key=f"viz_{id(file)}"):
            st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])

        # Conversion Options
        st.subheader("Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=f"convert_{id(file)}")

        if st.button(f"Convert {file.name}", key=f"convert_btn_{id(file)}"):
            buffer = BytesIO()  # Ensure buffer is initialized

            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            buffer.seek(0)

            st.download_button(
                label=f"Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

    st.success("All files processed successfully!")

