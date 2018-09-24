


#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import requests
import json
 
HOST = 'https://tss-otc.com'
API_KEY = 'apiKey=cSOrCzMHqO6Kbs2xoXJTs0kTmI9Qvlb1QiqDr4PzcJOke9SEFmzdCuJk6SrcyBjL'
#PROJECT_KEY = '#####YOUR_PROJECT_KEY#####'
 
def main():
    # ユーザ情報の取得
    # GET ${HOST}/api/v2/users/myself?${API_KEY}
    print(HOST + '/api/v2/users/?' + API_KEY)
    r = requests.get(HOST + '/api/v2/users/?' + API_KEY)
    print(r.text)
#    print(r.json())

if __name__ == '__main__':
    main()
