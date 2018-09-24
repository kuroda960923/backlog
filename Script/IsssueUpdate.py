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
API_TARGET_1 = 'api/v2/issues/'
#API_TARGET_2 = '/users'
INFILE = 'issueupdatelist.csv'
OUTFILE = 'issueupdateresult.txt'

with open(OUTDIR + OUTFILE, 'w') as o:
	with open(INDIR + INFILE, 'r') as f:
		reader = csv.reader(f)
		#header = next(reader)

		for row in reader:
			issueId = row[0]
			
			if (row[1] != "" or row[2] != ""):
				payload = {}
				
				if row[1] != "":
					payload['statusId'] = row[1]
				if row[2] != "":
					payload['dueDate'] = row[2]

				url = HOST + API_TARGET_1 + issueId + '?apiKey=' + API_KEY
				print(url)
				r = requests.patch(url,params=payload,auth=(USER,PASS),verify=True, cert=PEM)
				test = json.loads(r.text)
				o.write(str(test) + '\n')
				
				del payload
			
