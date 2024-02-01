import requests
import json
import pandas as pd
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()
SERVICE_KEY = os.getenv('SERVICE_KEY')

def fetch_data(start, end):
    URL = f'http://openapi.seoul.go.kr:8088/{SERVICE_KEY}/json/tbLnOpendataRtmsV/{start}/{end}/'
    req = requests.get(URL)
    content = req.json()
    return pd.DataFrame(content['tbLnOpendataRtmsV']['row'])

def main():
    st.title('Seoul Real Estate Transaction Information')

    N = st.slider('Select Range:', 0, 5000, step=1000)

    data = None
    for i in range(1, N + 1, 1000):
        result = fetch_data(i, i + 999)
        data = pd.concat([data, result], ignore_index=True)

    st.write('Data:')
    st.write(data)

if __name__ == '__main__':
    main()