# 113年度臺中市房屋買賣趨勢與分析

本專案以 **Python** 進行113年度臺中市不動產交易資料分析與圖表繪製。

藉由此專案快速了解臺中市**各區交易量**與**住宅用之建物型態**分布，以作為人口居住分析與居住型態趨勢之基石。


## 安裝 Installation 
python 3.12

pandas // pip install pandas 

matplotlib // pip install matplotlib

**使用前**
- 須將main.py中data_path的路徑改為目前檔案儲存路徑。

- 生成圖檔要先將visualize.py裡matplotlib的文字參數修改為：
  *plt.rcParams['font.family'] = 'Microsoft JhengHei'*

## 文件 Documentation



📝 資料來源：[ 政府開放資料平台 ](https://data.gov.tw/)

### 資料目錄結構

- open-data-visualization/
    - data /                     **資料原始檔**
        - data1.json
        - 113年1月1日至113年12月31日買賣案件.csv
    - charts /                  **視覺化圖片輸出**
        - district_diagram.png
        - building_diagram.png
    - scripts /                 **程式碼主體**
        - main.py               *主程式*
        - fetch_data.py         *資料擷取模組*
        - clean_data.py         *資料清理模組*
        - visualize.py          *視覺化模組*
    - requirements.txt          **所需安裝的 Python 套件**
    - README.md                 **專案說明**
---

### 📌 各模組功能概述：

  **scripts/fetch_data.py → import pandas**  
  - 使用pandas讀取路徑中data1.json資料。
  - 利用try except語法確認是否讀取資料成功。

  **scripts/clean_data.py → 過濾＆清洗**
  - 將所有以DataFrame結構讀取的資料，藉由select_data()過濾、取部分欄位資料。
  - 定義adopt_data()，使用**dropna函式**去除掉這些欄位中含有NaN值的列(row)。
  - 篩選剩下的列裡，對應的**備註欄位等於空字串**(*因為備註有字串的情況為非正常。例如：交易政府機關標讓售、親友、員工、共有人或其他特殊關係間之交易*)與**主要用途為住家用**之資料。(*其他作為營登商業用、空字串為農地、辦公用等不在本專題探討之樣本數據*)

  **scripts/visualize.py → import matplotlib.pyplot**
  
   圖表_**district_diagram.png 各區交易統計長條圖**
  - 藉由town_counts()將過濾清洗後的資料以欄位**鄉鎮市區**做統計。
  - 設定長條圖參數，並將X軸標籤設定為行政區名，Y軸標籤設定為交易數。
  - 設定matplotlib圖片儲存路徑並生成圖檔。

  圖表_**building_diagram.png 交易建物型態圓餅圖**
  - 藉由building_counts將過濾清洗後的資料以欄位**建物型態**做統計。
  - 設定圓餅圖參數，並將標籤設定為資料之表頭、90度開始繪製。
  - 設定matplotlib圖片儲存路徑並生成圖檔。

### 故障排除
- pandas.read_json(data_path)讀取資料時，將DataFrame結構全部讀取後，取部分欄位時，未理解.column[ ]只是單取表頭名稱，造成return因結構欄位長度不一出現 pandas錯誤。
- 各模組導入主程式之變數設定、各模組function與主程式參數錯誤之修正。

### 專題結果
本專題將台中市113年度五萬多筆交易房屋買賣數據，經由python讀取、清洗、篩選後，並使用matplotlib套件生成兩筆圖表。

藉由數據圖像化的方式，快速地了解113年房市熱度持續時，台中市的房屋買賣交易最熱區為北屯區，其次是西屯再者南屯區。並以電梯住宅大樓約60%壓倒性的居住型態為主，次之為21%的華夏(含電梯)高於透天厝的12.8%，由此可見高房價影響下，現代購屋換房會以單層樓並附有電梯型態居住方式為主。

(備註：因取得數據僅為113年度，未能深度分析購屋買賣趨勢，期望後續能以近十年數據資料作延伸，分析並洞悉未來居住型態趨勢。)


