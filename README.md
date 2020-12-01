# pythonTelegramBot

### python Telegram Bot

__功能:發送圖片給加入bot的會員(目前訊息OK)__

```bash
pip install python-telegram-bot --upgrade
pip install configparser
pip install dataframe-image
pip install tabulate
```

------------

### 需新建 setting.ini 內容為

```bash
[DEFAULT]
TOKEN = YOUR BOT TOKEN

```

------------

### 若部屬至heroku

token改為這樣取 然後heroku要設定
Settings -> Config Vars -> 新增一個**key = TOKEN ,value = 你的TOKEN** 填寫自己bot的TOKEN

`token = os.environ['TOKEN']`

------------

### 設定排程

heroku Scheduled 
*是使用UTC時間 記得要轉換*  
| name | 說明  | 時間 |   |   |
|---|---|---|---|---|
| sendStockDayPrice.py  | 個股收盤價  | 設定下午兩點  |   |   |
| sendThree.py  | 三大法人買賣超  | 設定下午三點  |   |   |
| sendStockBuySell.py  |  三大法人個股買賣超 | 設定下午四點半  |   |   |

