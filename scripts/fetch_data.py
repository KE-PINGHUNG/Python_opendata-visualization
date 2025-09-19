# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 11:29:33 2025

@author: User
"""

import pandas as pd

#讀取路徑的資料
def read_data(data_path):
    try:
        fetch_data = pd.read_json(data_path)
        print(fetch_data.head())
        return fetch_data
        
    except:
        print('資料讀取錯誤！')



