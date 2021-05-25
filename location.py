import streamlit as st
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
import time
import reverse_geocoder as rg 
import pprint 
import requests
import pandas as pd
def main():

	phone_no=8860009833   #pre defined number assumed to be given by the person
	options = Options()
	options.add_argument("--use--fake-ui-for-media-stream")
	driver = webdriver.Chrome(executable_path = 'C:\\Users\\User\\Downloads\\tech_girls_imagine_cup_2021\\chromedriver.exe',options=options) 
	#Edit path of chromedriver accordingly
	timeout = 20
	driver.get("https://mycurrentlocation.net/")
	wait = WebDriverWait(driver, timeout)
	time.sleep(3)
	longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')   
	longitude = [x.text for x in longitude]    
	longitude = str(longitude[0])    
	latitude = driver.find_elements_by_xpath('//*[@id="latitude"]') 
	latitude = [x.text for x in latitude]    
	latitude = str(latitude[0])    
	driver.quit()    
	coordinates =(latitude,longitude)
	d1 = rg.search(coordinates)
	pprint.pprint(d1)
	st.write(coordinates)
	d3=str(d1)
	st.write(d3)
	data=[coordinates]
	df=pd.DataFrame.from_records(data, columns = ['lat', 'lon'])
	df['lat']=df['lat'].astype(float)
	df['lon']=df['lon'].astype(float)
	st.write(df)
	st.success('Your current location has been sent to your SOS contacts')
	st.map(df)

if __name__ == '__main__':
	main()