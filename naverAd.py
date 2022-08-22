import time
import random
import requests
import signaturehelper

def get_header(method, uri, api_key, secret_key, customer_id):
    timestamp = str(round(time.time()*1000))
    signature = signaturehelper.Signature.generate(timestamp, method, uri, secret_key)
    return {'Content-Type': 'application/json; charset=UTF-8',
            'X-Timestamp': timestamp,
            'X-API-KEY': API_KEY,
            'X-Customer': str(CUSTOMER_ID),
            'X-Signature': signature}

BASE_URL = 'https://api.naver.com'
API_KEY = '0100000000133ff8dd83d39366676de09a462d5ba13c5793bee0ca36811732626dbaca2f16'
SECRET_KEY = 'AQAAAAATP/jdg9OTZmdt4JpGLVuhcjuzbzF9nZYgkyDDLU4lxQ=='
CUSTOMER_ID = '2639773'


uri = '/keywordstool'
method = 'GET'
r = requests.get(BASE_URL + uri + '?hintKeywords={}&showDetail=1'.format(input('연관키워드를 조회할 키워드를 입력하세요\n')), headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))
