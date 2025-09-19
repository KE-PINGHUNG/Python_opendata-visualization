# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 11:29:48 2025

@author: User
"""
#藉由篩選只取所有資料中的部份欄位
def select_data(fetch_data):
    return fetch_data[['鄉鎮市區','交易標的','主要用途','屋齡','建物型態','備註']]
    
#將篩選過後的欄位進行清洗
def adopt_data(result):
    # 去除任何一筆有包含NaN的row
    dp_data = result.dropna(axis=0, how='any')
    
    # 過濾備註含有任何字串（非正常交易） 與抓取主要用途為‘住家用’的資料
    filtered = dp_data[(dp_data['備註'] == "") & (dp_data['主要用途'] == '住家用')]
    print(filtered)
    
    return filtered 
     