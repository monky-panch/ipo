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
#print(bsObj.prettify()) #htmlデータ分析用

#テーブルを指定する
#ipodatatable[0]は企業名　コード、市場、主幹事、承認日、公開日
title = bsObj.findAll("h1",class_="h1_title_ipodata")
#aaa = title.findAll(title)
#aaa = title.get_text()
print(title)


table = bsObj.findAll("table",{"class":"ipodatatable"})[0]

#ipodatatable[1]はBB開始日、抽選日,購入申込日


#ipodatatable[5]は幹事
