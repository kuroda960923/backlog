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
OUTFILE = 'projectlist.csv'
API_TARGET = 'api/v2/projects'

payload ={
	'all':'true'
}

url = HOST + API_TARGET + '?apiKey=' + API_KEY
print(url)

r = requests.get(url,params=payload,auth=(USER,PASS),verify=True, cert=PEM)
test = json.loads(r.text)

cols = test[0].keys()
with open(OUTDIR + OUTFILE, 'w') as f:
	f.write(','.join(cols) + '\n')

	for line in test:
		row = [str(line[col]) for col in cols]
		f.write(','.join(row) + '\n')
