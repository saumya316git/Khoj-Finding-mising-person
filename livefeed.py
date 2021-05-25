import os
import face_recognition
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
class livefeed():
    def __init__(self):
        self.path = 'C:\\Users\\User\\OneDrive\\Desktop\\data'
        self.images = []
        self.classNames = []
        self.myList = os.listdir(self.path)
        print(self.myList)
        for cl in self.myList:
            self.curImg = cv2.imread(f'{self.path}/{cl}')
            self.images.append(self.curImg)
            self.classNames.append(os.path.splitext(cl)[0])
        print(self.classNames)


    def findEncodings(self):
        self.encodeList = []


        for self.img in self.images:
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            self.encode = face_recognition.face_encodings(self.img)[0]
            self.encodeList.append(self.encode)
        return self.encodeList






                    
                    
    def video_capture(self):
        self.encodeListKnown = self.findEncodings()
        print('Encoding Complete')

        self.cap = cv2.VideoCapture(0)

        while True:
            self.success, self.img = self.cap.read()

            self.imgS = cv2.resize(self.img, (0, 0), None, 0.25, 0.25)
            self.imgS = cv2.cvtColor(self.imgS, cv2.COLOR_BGR2RGB)

            self.facesCurFrame = face_recognition.face_locations(self.imgS)
            self.encodesCurFrame = face_recognition.face_encodings(self.imgS, self.facesCurFrame)

            for self.encodeFace, self.faceLoc in zip(self.encodesCurFrame, self.facesCurFrame):
                self.matches = face_recognition.compare_faces(self.encodeListKnown,self.encodeFace)
                self.faceDis = face_recognition.face_distance(self.encodeListKnown,self.encodeFace)

                self.matchIndex = np.argmin(self.faceDis)

                if self.matches[self.matchIndex]:
                    self.name = self.classNames[self.matchIndex].upper()
                    self.y1, self.x2, self.y2, self.x1 = self.faceLoc
                    self.y1, self.x2, self.y2, self.x1 = self.y1 * 4, self.x2 * 4, self.y2 * 4, self.x1 * 4
                    cv2.rectangle(self.img, (self.x1, self.y1), (self.x2, self.y2), (0, 255, 0), 2)
                    cv2.rectangle(self.img, (self.x1, self.y2 - 35), (self.x2, self.y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(self.img,self.name, (self.x1 + 6, self.y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            cv2.imshow('Webcam', self.img)
            self.c = cv2.waitKey(1)

            if self.c == 27:
                break
        self.cap.release()
        cv2.destroyAllWindows()
    def map(self):

        st.warning('Please wait ⏳ till the camera turns on')
        self.video_capture()
        self.name=self.name.lower()
        if self.name!='unidentified':


            lst=self.name.split('_',2)
            uid=lst[1]
            r = requests.get('https://docs.google.com/spreadsheets/d/181BSppIG1Y6vukLJDU-Ksdw4xcRnmfKhO8poBNmkJaw/export?format=csv&id=181BSppIG1Y6vukLJDU-Ksdw4xcRnmfKhO8poBNmkJaw&gid=2120383827')
            data = r.content
            df = pd.read_csv(BytesIO(data),error_bad_lines=False)    
            rslt_df= df.loc[df['ID']==uid]
            #st.write(self.name)
            #st.write(uid)
            st.write(rslt_df)
            #number_of_index = rslt_df.index
            #number_of_rows = len(number_of_index)
            abc=rslt_df['Related'].item()
            if abc=='Yes':
                st.info('Below is the house location of missing person')
            else:
                st.info('Below is the location where missing person was last found')
            a=rslt_df['GeoCode']
            data=a.str.split(",", n = 2, expand = True)
            data.rename(columns= {0: 'lat', 1:'lon'}, inplace = True)
            data['lat']=data['lat'].astype(float)
            data['lon']=data['lon'].astype(float)
            b=rslt_df['Timestamp']
            c=rslt_df['GeoAddress']
            st.write('Time of reporting: ')
            st.write(b)
            st.write('Location: ')
            st.write(c)
            st.map(data)
        else:
            st.error("Return Back to menu to Upload a new record")


    
    
            