import pandas as pd
import numpy as np
import streamlit as st
from Dropbox_Setup import *

#st.title("Apartment Ranking")

dbx = initializeToken('sl.BEMkL6aH-ohhGYv03y64H0fXNOT-RcjviwNWc04OC7lsRu01xqgDsCtgCKA9zMbgsfvxykg8Fverym8Vo_HO5MPp-trVUNn80Pm1VKA9_IdwpY1gaJQxWIPApbsOcm_x5bVb2WY')

filename = "/apartment.json"

file = fromDBX(dbx,filename)

init = {"Apartment Name":[],
        "Distance From School":[],
        "Distance From Mall":[],
        "Safety":[],
        "Internet":[],
        "Kitchen":[],
        "Water":[],
        "Condition":[],
        "Space":[],
        "Laundry":[],
        "Trash":[],
        "Mantenance":[],
        "Parking":[],
        "Pets":[],
        "Other Ammenities":[],
        "Price":[],
        "Ranking":[]}

name = st.text_input("Apartment Name:",key = 1)
school = st.slider("Distance to School:",0,10,key = 15)
mall = st.slider("Distance to Mall:",0,10,key = 16)
safety = st.slider("Safety Rating:",0,10,key = 2)
internet = st.slider("Internet Rating:",0,10,key = 3)
kitchen = st.slider("Kitchen Rating:",0,10,key = 4)
water = st.slider("Water Pressure Rating:",0,10,key = 5)
condition = st.slider("Condition Rating:",0,10,key = 6)
space = st.slider("Space Rating:",0,10,key = 7)
laundry = st.slider("Laundry Rating:",0,10,key = 8)
trash = st.slider("Trash Rating:",0,10,key = 9)
mantenance = st.slider("Mantenance Rating:",0,10,key = 10)
parking = st.slider("Parking Rating:",0,10,key = 11)
pets = st.slider("Pets Rating:",0,10,key = 12)
other = st.slider("Other Ammentities Rating:",0,10,key = 13)
price = st.slider("Price Rating:",0,10,key = 14)
values = [name,school,mall,safety,internet,kitchen,water,condition,space,laundry,
          trash,mantenance,parking,pets,other,price]

col1,col2 = st.columns(2)
action = 0
with col1:
    if st.button("Compile",key = 0):
        action = 1
with col2:
    if st.button("See Rankings",key = 17):
        action = 2

if action == 1:
    if name == "RESET ALL":
        toDBX(dbx,init,filename)
        st.text("Reset")
    else:
        for i in range(len(values)):
            file[list(file.keys())[i]].append(values[i])
        file['Ranking'].append(np.mean(values[1:]))
        toDBX(dbx,file,filename)
        st.text("Compiled")
elif action == 2:
    data = pd.DataFrame(file)
    data = data[['Apartment Name','Ranking']]
    data = data.sort_values("Ranking",ascending = False)
    st.dataframe(data)
