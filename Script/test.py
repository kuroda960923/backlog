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
API_TARGET_1 = 'api/v2/issues'
#API_TARGET_2 = '/users'
INFILE = 'addissuelist.csv'
OUTFILE = 'addissueresult.txt'

with open(OUTDIR + OUTFILE, 'w') as o:
	with open(INDIR + INFILE, 'r') as f:
		reader = csv.reader(f)
		header = next(reader)

		for row in reader:
			payload = {
				'projectId':row[0],
				'summary':row[1],
				'startDate':row[2],
				'dueDate':row[3],
				'issueTypeId':row[4],
				'categoryId[]':row[5],
				'assigneeId':row[6],
				'priorityId':row[7]
			}
			url = HOST + API_TARGET_1 + '?apiKey=' + API_KEY
			print(url)
			print(payload)
			r = requests.post(url,params=payload,auth=(USER,PASS),verify=True, cert=PEM)
			print(r)
			test = json.loads(r.text)
			print(test)
			o.write(str(test) + '\n')
						
