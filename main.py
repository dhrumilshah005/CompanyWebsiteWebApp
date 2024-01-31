import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Raghuvir Synthetics Ltd")
var_content = """Raghuvir group was established in 1968 to meet the local demand and it became one of the largest Textile Processing Company covering variety of products which enjoyed excellent reputation amongst its clientele. The company achieved a great success in local market by supplying fabrics to leading Garment and Made Ups exporters. In view of the Continuous Export demand, Management brought the notion of their own exports, and the mission was accomplished in 1991.
The Raghuvir group's corporate vision sensed the trend and strengthened itself to compete by strategic investments in putting Wider Processing plant, Dyeing, Printing and finishing. The Company has its own stitching unit equipped with latest Japanese machines with the capacity to stitch/deliver 2,50,000 bed sets a month. RAGHUVIR SYNTHETICS LIMITED is one of the major contenders in the Textile field, commanding loyalty from its wide customers base & enviable respect from the trade"""
st.write(var_content)
st.header("Our team")

col1, col2, col3 = st.columns(3)

with open("data.csv") as csv_file:
    df = pd.read_csv("data.csv",sep=",")

with col1:
    for index, row in df[0:4].iterrows():
        full_name = row["first name"] +" "+ row["last name"]
        st.header(full_name.title())
        st.write(row["role"])
        st.image(f"images/{int(index)+1}.png")
        st.write("")
        st.write("")

with col2:
    for index, row in df[4:8].iterrows():
        full_name = row["first name"] +" "+ row["last name"]
        st.header(full_name.title())
        st.write(row["role"])
        st.image(f"images/{int(index)+1}.png")
        st.write("")
        st.write("")

with col3:
    for index, row in df[8:13].iterrows():
        full_name = row["first name"] +" "+ row["last name"]
        st.header(full_name.title())
        st.write(row["role"])
        st.image(f"images/{int(index)+1}.png")
        st.write("")
        st.write("")