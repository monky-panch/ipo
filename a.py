# -*- coding: utf-8 -*-

import csv
import requests
from bs4 import BeautifulSoup
import os
import time

#とりあえず、tokyoipoの新規上場承認銘柄ページから情報を取り出す。
#あとで、リストからURL抽出して更新するようにできるといいな。

#requestsの使い方
#http://qiita.com/sqrtxx/items/49beaa3795925e7de666

url = "http://www.tokyoipo.com/ipo/detail.php?id=pre&seqid=2347" #euc-jpでした

#get
page_source = requests.get(url)
#print(page_source.content) #print(page_source)だけだとhttpのステータスが帰ってくる
bsObj = BeautifulSoup(page_source.content,"html.parser") #page_source.textだと文字化けしる

#テーブルを指定する
table = bsObj.findAll("table",{"class":"ipodatatable"})[0]
rows = table.findAll("tr")
print("-----------------------------")
print(rows)

table = bsObj.findAll("table",{"class":"ipodatatable"})[1]
rows = table.findAll("tr")
print("-----------------------------")
print(rows)

table = bsObj.findAll("table",{"class":"ipodatatable"})[5]
rows = table.findAll("tr")
print("-----------------------------")
print(rows)
