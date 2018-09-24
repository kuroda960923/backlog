#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

HOST = 'https://tss-otc.com/backlog/'
API_KEY= 'cSOrCzMHqO6Kbs2xoXJTs0kTmI9Qvlb1QiqDr4PzcJOke9SEFmzdCuJk6SrcyBjL'
OUTDIR = '/home/kuroda960923/Desktop/backlog/Output/'
INDIR = '/home/kuroda960923/Desktop/backlog/Input/'
PEM = '/home/kuroda960923/Desktop/backlog/kuroda2.pem'
USER = 'y-kuroda'
PASS = 'kuroda96'
OUTFILE = 'issuelist.csv'
API_TARGET = 'api/v2/issues'

url = HOST + API_TARGET + '?apiKey=' + API_KEY
print(url)

payload ={
	'projectId[]':31,
	'statusId[]':[1,2,3],
	'count':100,
	'sort':'duteDate',
	'order':'asc'
}

r = requests.get(url,params=payload,auth=(USER,PASS),verify=True, cert=PEM)
test = json.loads(r.text)
#cols = test[0].keys()
#print(test)

with open(OUTDIR + OUTFILE, 'w') as f:
	for line in test:		
		f.write(str(line["id"]) + "," + str(line["status"]["id"]) + "," +line["dueDate"][0:10]+ ","+ str(line["projectId"])  + "," + line["issueKey"]  + "," + line["summary"] + "," + line["priority"]["name"] + "," + line["status"]["name"] + "," + str(line["issueType"]["id"]) + "," + str(line["category"]) + "," + str(line["priority"])  
		+ '\n')
