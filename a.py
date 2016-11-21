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

#-------------------------------------------------------------
#ipodatatable[0]は企業名　コード、市場、主幹事、承認日、公開日
table0 = bsObj.findAll("table",{"class":"ipodatatable"})[0]

#企業名 テーブルの中から企業名を抜き出す
corp_name = table0.find("h1",class_="h1_title_ipodata")
print(corp_name.get_text())
#企業コード
corp_code = table0.findAll("td",class_="main_data aligncenter")[0]
print(corp_code.get_text())
#上場する市場
corp_market = table0.findAll("td",class_="main_data aligncenter")[2]
print(corp_market.get_text())
#認証日
ninshou_bi = table0.findAll("td",class_="main_data aligncenter")[3]
print(ninshou_bi.get_text())
#上場日
jyoujyou_bi = table0.findAll("td",class_="main_data aligncenter")[4]
print(jyoujyou_bi.get_text())

print("----------------------")
#-------------------------------------------------------------
#ipodatatable[1]はBB開始日、抽選日,購入申込日
table1 = bsObj.findAll("table",{"class":"ipodatatable"})[1]
#仮条件提示日
kari_bi = table1.findAll("td",class_="main_data")[8]
print(kari_bi.get_text())
#ブックビルディング（開始）
bb_kaishi_bi = table1.findAll("td",class_="main_data")[9]
print(bb_kaishi_bi.get_text())
#ブックビルディング（終了）
bb_shuryou_bi = table1.findAll("td",class_="main_data")[10]
print(bb_shuryou_bi.get_text())
#公募価格決定日
chusen_bi = table1.findAll("td",class_="main_data")[11]
print(chusen_bi.get_text())
#購入申込期間（開始）
kounyu_kaishi_bi = table1.findAll("td",class_="main_data")[12]
print(kounyu_kaishi_bi.get_text())
#購入申込期間（終了）
kounyu_shuryou_bi = table1.findAll("td",class_="main_data")[13]
print(kounyu_shuryou_bi.get_text())

print("----------------------")

#-------------------------------------------------------------
#ipodatatable[5]は幹事
table5 = bsObj.findAll("table",{"class":"ipodatatable"})[5]
kanji_index = [1,4,7,10,13,16,19,22,25,28,31,34,37,40,43,46,49,52,55,58,61,64,67,70,73,76,79]
kanji_list = []

for i in kanji_index:
    kanji_name = table5.findAll("td",class_="main_data")[i]
    kanji_list.append(kanji_name.get_text())

print(kanji_list)

#for row in kanjis_table:
#    csvRow = []
#    for cell in row.findAll():
#        csvRow.append(cell.get_text())

#kanjis_table = table5.findAll("td",class_="main_data")[1]

#print(kanjis_table.get_text())
