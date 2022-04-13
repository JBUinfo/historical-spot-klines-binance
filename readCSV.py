import pandas as pd
def readCSV_Normalize(coin, timeFrame):
    cols = ['OpenTime', 'Open', 'High', 'Low', 'Close', 'Volume', 'CloseTime', 'QuoteAssetVolume', 'NumberOfTrades', 'TakerBuyBaseAssetVolume', 'TakerBuyQuoteAssetVolume', 'Ignore']
    return pd.read_csv(f"./coins/{coin}/{timeFrame}/{timeFrame}.csv", names=cols, header=0)
