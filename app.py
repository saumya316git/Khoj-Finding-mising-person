import streamlit as st
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import cv2
import re
import os
import csv
from csv import writer
import glob
import face_recognition
import re
import pandas as pd
import numpy as np
from datetime import datetime
import streamlit as st 
from tkinter import filedialog
from enum import Enum
from io import BytesIO, StringIO
from typing import Union
import pathlib
import hashlib
import sqlite3 
import base64
from livefeed import livefeed
from facialsearch import facial_search
import login_signup
from login_signup import create_usertable
from login_signup import make_hashes
from login_signup import check_hashes
from login_signup import add_userdata
from login_signup import login_user
from login_signup import view_all_users
from details import details
import requests
from search_by_filter import search_by_filter
from details_upload import upload
import time
def main():
	"""Simple Login App"""
	my_bar = st.progress(0)
	for percent_complete in range(100):

		time.sleep(0.01)
		my_bar.progress(percent_complete + 1)

	menu = ["Home","Login","SignUp","Contact Us"]
	choice = st.sidebar.selectbox("Menu",menu)
 #Playing It In The Whole Device
	if choice == "Home":



		main_bg = "hope2.png"
		main_bg_ext = "png"



		st.markdown(
		    f"""
		    <style>
		    .reportview-container {{
		        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})

		    }}
		    </style>
		    """,
		    unsafe_allow_html=True
)




	elif choice == "Login":
			
#Loading File Into Mixer


		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):

			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))
				st.write('')
				task = st.selectbox("Choose",["Search by image","Search by filter","Search by live camera","Upload image"])
				
				if task == "Search by image":
					user_input = st.text_input("SELECT IMAGE FROM YOUR LOCAL SYSTEM",'C:\\Users\\User\\OneDrive\\Desktop\\LocalDirectoryPictures\\')	
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
					st.write('')
					st.write('')
					st.write('')
					st.write('')
					st.write('')
					st.write('')
					st.write('')
					n,s=facial_search(user_input)
					st.write('')
				
						

				
					stt=details(n,s,user_input)
				

				elif task== 'Search by filter':

					stt=search_by_filter()

				elif task == "Search by live camera":

					feed=livefeed()
					feed.map()
				

				elif task=="Upload image":
					upload()







			else:
				st.warning("Incorrect Username/Password")





	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a New Account")
			st.info("Go to login from the main menu")

	else:
		st.success("MADE BY: ")

		for i in range(1): # number of rows in your table! = 2 
			cols=st.beta_columns(3) # number of columns in each row! = 2 # first column of the ith row 
			cols[0].image('SA1.jpg',use_column_width=True)
			cols[1].image('SG3.png',use_column_width=True)
			cols[2].image('RT1.jpg',use_column_width=True)

		for i in range(1): # number of rows in your table! = 2 
			cols=st.beta_columns(3) # number of columns in each row! = 2 # first column of the ith row 
			cols[0].write('__SAUMYA ACHANTANI__',use_column_width=True)
			cols[1].write('__SAUMYA GUPTA__',use_column_width=True)
			cols[2].write('__RUPALI TANEJA__',use_column_width=True)


		linkrt = '[LinkedIn](https://www.linkedin.com/in/saumyaachantani-2000/)'
		linksg = '[LinkedIn](https://www.linkedin.com/in/saumya-gupta-60a9481a9)'
		linksa = '[LinkedIn](https://www.linkedin.com/in/rupali-taneja-ba2619169)'

		for i in range(1): # number of rows in your table! = 2 
			cols=st.beta_columns(3) # number of columns in each row! = 2 # first column of the ith row 
			cols[0].markdown(linkrt, unsafe_allow_html=True)
			cols[1].markdown(linksg, unsafe_allow_html=True)
			cols[2].markdown(linksa, unsafe_allow_html=True)
		mailrt = '[Mail](saumya18csu194@ncuindia.edu)'
		mailsg = '[Mail](saumya18csu195@ncuindia.edu)'
		mailsa = '[Mail](rupali18csu182@ncuindia.edu)'

		for i in range(1): # number of rows in your table! = 2 
			cols=st.beta_columns(3) # number of columns in each row! = 2 # first column of the ith row 
	
			cols[0].markdown('<a href="mailto:saumya18csu194@ncuindia.edu">Mail</a>', unsafe_allow_html=True)
			cols[1].markdown('<a href="mailto:saumya18csu195@ncuindia.edu">Mail</a>', unsafe_allow_html=True)
			cols[2].markdown('<a href="mailto:rupali18csu182@ncuindia.edu">Mail</a>', unsafe_allow_html=True)
		

if __name__ == '__main__':
	main()