import os
import csv
from csv import writer
import cv2
import re
import pandas as pd
import numpy as np
from datetime import datetime
import streamlit as st
from details import details
import csv
from csv import writer
import streamlit as st
import pandas as pd
import re
import cv2
import os
import time
import requests
from io import BytesIO, StringIO
def upload():
    googleform = '[Click here to create a new record](https://forms.gle/C9gqQDu5HPuFtfj8A)'
    st.markdown(googleform, unsafe_allow_html=True)
    r = requests.get('https://docs.google.com/spreadsheets/d/181BSppIG1Y6vukLJDU-Ksdw4xcRnmfKhO8poBNmkJaw/export?format=csv&id=181BSppIG1Y6vukLJDU-Ksdw4xcRnmfKhO8poBNmkJaw&gid=2120383827')
    data = r.content
    df = pd.read_csv(BytesIO(data),error_bad_lines=False) 
    path1="C:\\Users\\User\\OneDrive\\Desktop\\data\\"
    if st.checkbox('Click here after submitting the form'):
        path=st.text_input("UPLOAD IMAGE ",'C:\\Users\\User\\OneDrive\\Desktop\\LocalDirectoryPictures\\')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        img = cv2.imread(path,1)
        name=df['Name'].iloc[-1]
        i_d=df['ID'].iloc[-1]
        conc=name+'_'+i_d

        cv2.imwrite(os.path.join(path1,conc+".png"), img)
        st.success("Record saved!!")
        st.info('We will notify you as soon as update is available')