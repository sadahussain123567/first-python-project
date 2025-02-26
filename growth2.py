# import streamlit as st
# import pandas as pd
# import os 
# from io import BytesIO

# st.set_page_config(page_title="Data sweeper ",layout='wide')
# st.title ("Data sweeper")
# st.writer("transform")

# uploaded_files =st.file_uploader ("upload you files (csv or Excel):",type=["csv","xlsx"],
# accept_multiple_files =True)

# if uploaded_files:
#   for file in uploaded_files:
#     file_ext = os.path.splitext(file.name)[-1].lower()

#     if file_ext==".csv":
#       df=pd.read_csv(file)
#       elif file_ext ==".xlsx":
#         df = pd.read_excel(file)
#         else:st.error (f"unsupported file type:{file_exit}")
#         continue
# st.write(f"**File Name:**{file.name}")
# st.write(f"**File Size:**{file.size/1024}")

# #
# st.write ("Preview the Head of the Dataframe")
# st.dataframe(df.head())

# st.subheader("Data Cleaning Options")
# if st.checkbox(f"Clean Data for {file.name}"):
#   col1,col2=st.columns(2)

#   with col1:
#     if st.button(f"remove duplicates from {file.name}"):
#       df.drop_duplicates(inplace=True)
#       st.write("Duplicates Removed")

#       with col2:
#         if st.button(f"fill missing values for {file.name}"):
#           numeric_cols =df.select_dtypes(include=['number']).columns
#           df[numeric_cols]=df[numeric_cols].fillna(df[numeric_cols].mean())
# st.write("Missing Values have been Filled")

# st.subheader("Select Column to Convert")
# columns =st.multiselect(f"choose columns for {file.name}",df.columns,default=df.columns)
# df=df[columns]

# st.subheader("Data visualization")
# if st.checkbox(f"show visualization for {file.name}"):
#   st.checkbox (df.select_dtypes(include='number').iloc[:,:2])

#   st.subheader ("conversation options")
#   conversion_type=st.radio(f"convert {file.name}to:",["csv","excel"],key=file.name)
#   if st.button(f"convert {file.name}"):
#     buffer =BytesIO()
#     if conversion_type=="csv":
#       df.to_csv(buffer,index=False)
#       file.name= file.name.replace(file_ext,".csv")
#       mine_type="text/csv"

#       elif conversion_type== "Excel":
#         df.to_excel(buffer,index=False)
#         file_name =file.name.replace(file_ext,".xlsx")
#         mine_type= "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#         buffer.seek(0)

#         st.download.button(
#           label=f"Download {file.name}as {conversion_type}",
#           data=buffer,
#           file_name=file_name,
#           mine=mine_type
#         )
#         st.succes("All Files Processed")




import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="Data Sweeper", layout='wide')
st.title("Data Sweeper")
st.write("Transform")

uploaded_files = st.file_uploader(
    "Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_ext}")
            continue

        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.size / 1024:.2f} KB")

        # Display dataframe preview
        st.write("### Preview the Head of the DataFrame")
        st.dataframe(df.head())

        # Data Cleaning Options
        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates Removed")

            with col2:
                if st.button(f"Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing Values have been Filled")

        # Select Columns to Convert
        st.subheader("Select Columns to Convert")
        columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)
        df = df[columns]

        # Data Visualization
        st.subheader("Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
            st.line_chart(df.select_dtypes(include='number'))

        # Conversion Options
        st.subheader("Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ["csv", "excel"], key=file.name)

        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()

            if conversion_type == "csv":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mine_type = "text/csv"
            elif conversion_type == "excel":
                df.to_excel(buffer, index=False, engine='openpyxl')
                file_name = file.name.replace(file_ext, ".xlsx")
                mine_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            buffer.seek(0)

            st.download_button(
                label=f"Download {file_name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mine_type
            )

            st.success("All Files Processed")
