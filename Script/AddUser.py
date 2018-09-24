#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import csv

HOST = 'https://tss-otc.com/backlog/'
API_KEY= 'cSOrCzMHqO6Kbs2xoXJTs0kTmI9Qvlb1QiqDr4PzcJOke9SEFmzdCuJk6SrcyBjL'
OUTDIR = '/home/kuroda960923/Desktop/backlog/Output/'
INDIR = '/home/kuroda960923/Desktop/backlog/Input/'
PEM = '/home/kuroda960923/Desktop/backlog/kuroda2.pem'
USER = 'y-kuroda'
PASS = 'kuroda96'
API_TARGET = 'api/v2/users'
INFILE = 'useraddlist.csv'
OUTFILE = 'useraddresult.txt'

url = HOST + API_TARGET + '?apiKey=' + API_KEY
print(url)

with open(OUTDIR + OUTFILE, 'w') as o:
	with open(INDIR + INFILE, 'r') as f:
		reader = csv.reader(f)
		header = next(reader)

		for row in reader:
			payload = {
				'userId':row[0],
				'password':row[1],
				'name':row[2],
				'mailAddress':row[3],
				'roleType':row[4]
			}
			r = requests.post(url,params=payload,auth=(USER,PASS),verify=True, cert=PEM)
			test = json.loads(r.text)
			o.write(str(test) + '\n')
			
