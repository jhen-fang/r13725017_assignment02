# Countdown CLI Tool 

這是一個 Python Command-line tool，能夠計算距離指定日期還有多少天，非常適合用來追蹤報告截止日、假期、人生目標等重要時刻。

## Features

- 計算距離未來日期**還有幾天**
- 自動判斷輸入日期是**今天**還是**已經過去**
- 使用顏色區分輸出結果，提升可讀性
- 日期格式自動檢查與提示
- 命令列介面操作簡單直覺

## Quick Start

### 1. Clone the repository

```
git clone https://github.com/jhen-fang/r13725017_assignment02.git
cd r13725017_assignment02
```

### 2. Set up a virtual environment

```
python -m venv venv
source venv/bin/activate      # or venv\Scripts\activate on Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the script

```
python countdown.py 2025-12-31
```

### Example Output

```
$ python countdown.py 2025-12-31
距離 2025-12-31 還有 268 天 ✨
```

如果目標日期是今天:

```
今天就是 2025-04-06！🎉
```

如果目標日期已經過去:

```
2024-12-31 已經過了 96 天 🕒
```

### Notes

- 日期格式必須為 `YYYY-MM-DD`（例如：2025-12-31）
- 程式會使用目前電腦系統的時間作為「今天」的依據

### Dependencies

- Python 3.6+
- colorama
