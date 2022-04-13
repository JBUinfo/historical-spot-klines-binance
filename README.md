# historical-spot-klines-binance
Download and merge CSVs from historical spot candles.

# DownloadAndMergeCSV_Binance.py
Write the pairs you want in "coins" array and it will create pair-folders.
Example:

    coins = ['TRXUSDT', 'XMRUSDT', 'FILUSDT', 'EOSUSDT', 'DASHUSDT']
    
![alt text](https://github.com/JBUinfo/historical-spot-klines-binance/blob/main/Images/CoinsFolder.png?raw=true)

Each temporality has his own folder and csv.

![alt text](https://github.com/JBUinfo/historical-spot-klines-binance/blob/main/Images/TempFolders.png?raw=true)

Execute:
![alt text](https://github.com/JBUinfo/historical-spot-klines-binance/blob/main/Images/ExecuteDownload.png?raw=true)

# readCSV.py
Just a function that returns a pandas dataframe with the CSV you choose.
Example:

    from readCSV import readCSV_Normalize
    trx_1d = readCSV_Normalize("TRXUSDT", "1d")
    
# Install
DownloadAndMergeCSV_Binance.py:

    pip install xmltodict
    
readCSV.py:

    pip install pandas
    
