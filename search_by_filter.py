import streamlit as st 
import requests
import pandas as pd
import numpy as np
from io import BytesIO, StringIO
def search_by_filter():


    r = requests.get('https://docs.google.com/spreadsheets/d/181BSppIG1Y6vukLJDU-Ksdw4xcRnmfKhO8poBNmkJaw/export?format=csv&id=181BSppIG1Y6vukLJDU-Ksdw4xcRnmfKhO8poBNmkJaw&gid=2120383827')
    data = r.content
    rslt_df = pd.read_csv(BytesIO(data),error_bad_lines=False)
    search=st.radio("Filter by ",('1. Name','2. Age group','3. Location','4. Location and Age Groups','5. Name and Age Groups'))
    if search=='1. Name':
        enter_name=st.text_input("Enter name of the missing person")
        if st.button('Click'):
            rslt_df2=rslt_df.loc[(rslt_df['Name']==enter_name)]
            st.write(rslt_df2)
            a=rslt_df2['GeoCode']
            number_of_index = rslt_df2.index
            number_of_rows = len(number_of_index)
            b=rslt_df2['Timestamp']
            c=rslt_df2['GeoAddress']
            if number_of_rows==1:
                st.write('Track the location of missing person  :')
                st.write('Last seen at  :')
                st.write('Time: ')
                st.write(b)
                st.write('Location: ')
                st.write(c)
                data=a.str.split(",", n = 2, expand = True)
                data.rename(columns= {0: 'lat', 1:'lon'}, inplace = True)
                data['lat']=data['lat'].astype(float)
                data['lon']=data['lon'].astype(float)
                st.write(data)
                st.map(data)
            else:
                st.warning("Either search manually or through other filters from dropdown menu")
    if search=='2. Age group':
        
        st.write("Enter age group of the missing person .")
        age_grp=st.slider('Age range', min_value=1, max_value=90, value=(10,20), step=2)
        if st.button("Click here to check records from this age group"):
            lrange=age_grp[0]
            hrange=age_grp[1]
            rslt_df1=rslt_df.loc[(rslt_df['Age']>=lrange) & (rslt_df['Age']<=hrange)]
            st.write(rslt_df1)
            a=rslt_df1['GeoCode']
            number_of_index = rslt_df1.index
            number_of_rows = len(number_of_index)
            if number_of_rows==1:
                b=rslt_df1['Timestamp']
                c=rslt_df1['GeoAddress']
                st.write('Track the location of missing person  :')
                st.write('Last seen at  :')
                st.write('Time: ')
                st.write(b)
                st.write('Location: ')
                st.write(c)
                data=a.str.split(",", n = 2, expand = True)
                data.rename(columns= {0: 'lat', 1:'lon'}, inplace = True)
                data['lat']=data['lat'].astype(float)
                data['lon']=data['lon'].astype(float)
                st.write(data)
                st.map(data)
            else:
                st.warning("Either search manually or through other filters from dropdown menu")

    if search=='3. Location':

        enter_state=st.text_input("Enter state of the missing person")
        if st.button('Click'):
            rslt_df2=rslt_df.loc[(rslt_df['State']==enter_state)]
            st.write(rslt_df2)
            a=rslt_df2['GeoCode']
            number_of_index = rslt_df2.index
            number_of_rows = len(number_of_index)
            b=rslt_df2['Timestamp']
            c=rslt_df2['GeoAddress']
            if number_of_rows==1:
                st.write('Track the location of missing person  :')
                st.write('Last seen at  :')
                st.write('Time: ')
                st.write(b)
                st.write('Location: ')
                st.write(c)
                data=a.str.split(",", n = 2, expand = True)
                data.rename(columns= {0: 'lat', 1:'lon'}, inplace = True)
                data['lat']=data['lat'].astype(float)
                data['lon']=data['lon'].astype(float)
                st.write(data)
                st.map(data)

    if search=='4. Location and Age Groups':
        enter_state=st.text_input("Enter state of the missing person")
        age_grp=st.slider('Age range', min_value=1, max_value=90, value=(10,20), step=2)
        lrange=age_grp[0]
        hrange=age_grp[1]
        if st.button("Click here to check records"):
            rslt_df3=rslt_df.loc[(rslt_df['State']==enter_state) &(rslt_df['Age']>=lrange) & (rslt_df['Age']<=hrange)]
            st.write(rslt_df3)
            a=rslt_df3['GeoCode']
            number_of_index = rslt_df3.index
            number_of_rows = len(number_of_index)
            if number_of_rows==1:
                b=rslt_df3['Timestamp']
                c=rslt_df3['GeoAddress']
                st.write('Track the location of missing person  :')
                st.write('Last seen at  :')
                st.write('Time: ')
                st.write(b)
                st.write('Location: ')
                st.write(c)
                data=a.str.split(",", n = 2, expand = True)
                data.rename(columns= {0: 'lat', 1:'lon'}, inplace = True)
                data['lat']=data['lat'].astype(float)
                data['lon']=data['lon'].astype(float)
                st.write(data)
                st.map(data)

    if search=='5. Name and Age Groups':
        enter_name=st.text_input("Enter name of the missing person")
        age_grp=st.slider('Age range', min_value=1, max_value=90, value=(10,20), step=2)
        lrange=age_grp[0]
        hrange=age_grp[1]
        if st.button("Click here to check records"):
            rslt_df3=rslt_df.loc[(rslt_df['Name']==enter_name) &(rslt_df['Age']>=lrange) & (rslt_df['Age']<=hrange)]
            st.write(rslt_df3)
            a=rslt_df3['GeoCode']
            number_of_index = rslt_df3.index
            number_of_rows = len(number_of_index)
            if number_of_rows==1:
                b=rslt_df3['Timestamp']
                c=rslt_df3['GeoAddress']
                st.write('Track the location of missing person  :')
                st.write('Last seen at  :')
                st.write('Time: ')
                st.write(b)
                st.write('Location: ')
                st.write(c)
                data=a.str.split(",", n = 2, expand = True)
                data.rename(columns= {0: 'lat', 1:'lon'}, inplace = True)
                data['lat']=data['lat'].astype(float)
                data['lon']=data['lon'].astype(float)
                st.write(data)
                st.map(data)

