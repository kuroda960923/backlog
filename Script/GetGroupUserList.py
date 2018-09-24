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
OUTFILE = 'groupmemberlist.csv'
API_TARGET = 'api/v2/groups'

payload ={
	'count':'300'
}

url = HOST + API_TARGET + '?apiKey=' + API_KEY
print(url)

r = requests.get(url,params=payload,auth=(USER,PASS),verify=True, cert=PEM)
test = json.loads(r.text)

with open(OUTDIR + OUTFILE, 'w') as f:
	cols = test[0]["members"][0].keys()
	f.write(','.join(['group_id','group_name']))
	f.write(','.join(cols) + '\n')

	for line in test:
		group_id = line["id"]
		group_name = line["name"]

		for member in line["members"]:
			row = [str(member[col]) for col in cols]
			f.write(str(group_id) + "," + str(group_name)+ ",")
			f.write(','.join(row) + '\n')
			

"""
with open(DIR + 'projectlist.csv', 'w') as f:
	for line in test:
		group_id = [str(line["id"])]
		group_name = [str(line["name"])]


		row = [str(line["members"])]
		print(row)



		cols = row[0].keys()
		f.write(','.join(['group_id','group_name']))
		f.write(','.join(cols) + '\n')

		for line in row:
			row = [str(line[col]) for col in cols]
			f.write(','.join([group_id,group_name]))
			f.write(','.join(row) + '\n')

"""
"""
cols = test[0].keys()
with open(DIR + 'projectlist.csv', 'w') as f:
	f.write(','.join(cols) + '\n')

	for line in test:
		row = [str(line[col]) for col in cols]
		f.write(','.join(row) + '\n')
"""
