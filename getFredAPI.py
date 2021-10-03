from fredapi import Fred
import configparser

config = configparser.ConfigParser()
config.sections()
config.read('setting.ini')


fredToken = config['DEFAULT']['FRED_API_KEY']

def getFredAPI(date):
    fred = Fred(api_key=fredToken)  # 替換成輸入你的api key
    #那斯達克少一天資料== 不知道為啥
    #邏輯 當天早上八點跑 now.date - 1天 去抓資料 抓地到就發 抓不到就不發 暫時先醬
    watchList = ['SP500','DJIA','NASDAQCOM']
    resultList = []
    for watch in watchList:
        result = dict()
        # watchInfo = fred.get_series_info(watch)
        watchLastIndex = fred.get_series(watch, date)
        if(len(watchLastIndex)!=0):
            result['title'] = watch
            result['value'] = watchLastIndex[0]
            resultList.append(result)
    
    return resultList

if __name__ == '__main__':
    getFredAPI('2021-10-01')