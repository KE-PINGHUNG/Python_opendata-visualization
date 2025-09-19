# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 11:30:01 2025

@author: User
"""

import matplotlib.pyplot as plt

# 計算每個鄉鎮市區出現的次數
def town_counts(filtered_data):
    district =  filtered_data['鄉鎮市區'].value_counts()
    print(district)
    
    plt.rcParams['font.family'] = 'Heiti TC' ,# 黑體 for mac
    #plt.rcParams['font.family'] = 'Microsoft JhengHei'  # 微軟正黑體 for window

# 113年台中市房屋買賣“住家用途”交易熱區分析
# 繪製長條圖
    plt.figure(figsize=(12,7)) , # 圖片大小
    plt.bar(district.index, district.values),

# 標題與標籤
    plt.title('113年台中市房屋買賣“住家用途”交易分布'),
    plt.xlabel('行政區名',labelpad=10),
    plt.ylabel('交易數',rotation=0,labelpad=30),

# 旋轉 X 軸標籤避免重疊
    plt.xticks(rotation=45),
    
# 儲存圖表
    plt.savefig("../charts/district_diagram.png")
    
# 顯示圖表
    plt.show()



#----------------------------------------------------------------------------
# 計算建物型態數量
def building_counts(filtered_data):
    building = filtered_data['建物型態'].value_counts()
    print(building)
# 113年台中市房屋買賣“ 住家用途 ” 之建物型態分析

# 繪製圓餅圖
    plt.rcParams['font.family'] = 'Heiti TC' ,# 黑體 for mac
    #plt.rcParams['font.family'] = 'Microsoft JhengHei'  # 微軟正黑體 for window
    plt.figure(figsize=(10,8)),
    plt.pie(
        building.values,
        labels=building.index,
        autopct='%1.1f%%',
        startangle=90,
        counterclock=False
        ),
    plt.title('113年房屋買賣“ 住家用途 ” 之建物型態分布')
# 儲存圖表
    plt.savefig("../charts/building_diagram.png")
        
# 顯示圖表
    plt.show()
