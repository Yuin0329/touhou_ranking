# 東方Project人氣投票歷年排名追蹤

網址：https://yuin0329.github.io/touhou_ranking/ <b>
用於爬取和視覺化東方Project人氣投票結果，支援第1回到第21回的完整數據分析


## 功能特色

- **自動爬取**：使用Selenium自動爬取toho-vote.info的投票結果
- **完整數據**：支援第1回到第21回的所有投票數據
- **互動圖表**：提供角色歷年排名變化的折線圖
-**角色選擇**：下拉選單選擇特定角色查看其排名變化
- **響應式設計**：支援桌面和移動設備
- **範圍選擇**：可以選擇特定回數範圍進行分析
- **詳細統計**：顯示角色的參與回數、最佳排名、平均排名等統計信息

## 專案結構

```
touhou_rank/
├── result20.py              # 主要爬蟲程式（支援1-21回）
├── index.html               # 網頁界面
├── data_processor.py        # 數據處理模組
├── crawler.py               # 爬蟲模組（可選）
├── README.md                # 說明文件
├── requirements.txt         # 依賴套件列表
├── data/                    # 數據文件目錄
│   ├── touhou_vote1.csv     # 第1回數據
│   ├── touhou_vote2.csv     # 第2回數據
│   ├── ...
│   ├── touhou_vote21.csv    # 第21回數據
│   ├── touhou_vote_all_rounds.csv  # 合併的所有數據
│   ├── characters_all.json  # 完整角色列表
│   └── statistics_all.json  # 統計信息
└── debug/                   # 調試文件目錄
    └── debug_*.html
```

## 安裝與使用

### 1. 安裝依賴套件

```bash
pip install -r requirements.txt
```

或手動安裝：

```bash
pip install requests beautifulsoup4 pandas selenium webdriver-manager
```

### 2. 爬取所有回數數據

```bash
# 爬取第1回到第21回的所有數據
python result20.py
```

- 爬取第1回到第21回的所有投票數據
- 生成每個回數的單獨CSV文件
- 合併所有數據到 `touhou_vote_all_rounds.csv`
- 生成完整的角色列表和統計信息

### 3. 啟動網頁服務器

```bash
python -m http.server 8000
```

### 4. 開啟網頁

訪問 `http://localhost:8000/index_all_rounds.html`


### 數據分析功能

```python
from data_processor import TouhouVoteDataProcessor

# 創建處理器
processor = TouhouVoteDataProcessor()

# 載入完整數據
processor.combined_data = processor.load_csv_data("touhou_vote_all_rounds.csv")

# 獲取角色排名歷史
history = processor.get_character_ranking_history("博麗 霊夢")

# 獲取排名變化
changes = processor.get_ranking_changes(19, 20, 10)

# 獲取統計信息
stats = processor.get_statistics()
```

## 數據欄位說明

- **回數**：投票回數（1-21）
- **名次**：角色在該回的排名
- **角色**：角色名稱
- **點數**：總點數
- **第一推**：第一推票數
- **評論**：評論票數
- **支援作品**：支援作品數量
- **上回排名**：上一回的排名
- **前前回排名**：前前回的排名

## 技術架構

- **爬蟲**：Python + Selenium + BeautifulSoup
- **數據處理**：Python + Pandas
- **前端**：HTML + CSS + JavaScript + Plotly.js
- **數據格式**：CSV + JSON

## 注意事項

- 需要安裝Chrome瀏覽器（Selenium會自動下載ChromeDriver）
- 爬取所有21回數據可能需要較長時間（約30-60分鐘）
- 網頁需要通過HTTP服務器訪問（不能直接打開HTML文件）
- 建議定期備份爬取的數據
- 某些早期回數的數據可能不完整或格式不同

## 未來功能

- 添加更多統計圖表（如點數變化趨勢）
- 實現角色比較功能
- 添加數據導出功能
- 創建API接口
- 添加數據庫支持
- 實現自動化定期爬取





