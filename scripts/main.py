# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 11:29:04 2025

@author: User
"""
import fetch_data as f
import clean_data as c
import visualize as v


data_path = "../data/data1.json"

fetch_data = f.read_data(data_path)

result = c.select_data(fetch_data)

filtered_data = c.adopt_data(result)

# 執行統計每個鄉鎮市區出現的次數並繪製成圖表
v.town_counts(filtered_data)
# 執行統計建物型態數量出現的次數並繪製成圖表
v.building_counts(filtered_data)

