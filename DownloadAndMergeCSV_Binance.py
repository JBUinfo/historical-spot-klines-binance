import urllib.request
import xmltodict
from zipfile import ZipFile
import glob
import os

times = ["12h","15m","1d","1h","1m","1mo","1w","2h","30m","3d","3m","4h","5m","6h","8h"]
coins = ['TRXUSDT', 'XMRUSDT', 'FILUSDT', 'EOSUSDT', 'DASHUSDT']
folderCoins = 'coins'
if not os.path.isdir(folderCoins):
    os.mkdir(folderCoins)
for coin in coins:
    if not os.path.isdir(f"{folderCoins}/{coin}"):
        os.mkdir(f"{folderCoins}/{coin}")
    for time in times:
        if not os.path.isdir(f"{folderCoins}/{coin}/{time}"):
            os.mkdir(f"{folderCoins}/{coin}/{time}")
        if os.path.exists(f"{folderCoins}/{coin}/{time}/{time}.csv"):
            continue
        url = f'https://s3-ap-northeast-1.amazonaws.com/data.binance.vision?delimiter=/&prefix=data/spot/monthly/klines/{coin}/{time}/'
        print("Getting URLs from: "+ url)
        with urllib.request.urlopen(url) as response:
            data = response.read()
            data = xmltodict.parse(data)
            for link in data['ListBucketResult']['Contents']:
                link = link['Key']
                if "CHECKSUM" not in link:
                    nameZIP = link[link.index(time)+len(time)+1:]
                    print(f"Downloading ZIP: https://data.binance.vision/{link}")
                    urllib.request.urlretrieve(f'https://data.binance.vision/{link}', nameZIP)
                    with ZipFile(nameZIP, 'r') as zipObj:
                       zipObj.extractall()
                    os.remove(nameZIP)
            all_filenames = [i for i in glob.glob('*.{}'.format('csv'))]
            fout=open(f"{folderCoins}/{coin}/{time}/{time}.csv","a")
            print(f"Compressing CSVs and removing ZIPs...")
            for file in all_filenames:
               f = open(file)
               for line in f:
                    fout.write(line)
               f.close()
               os.remove(file)
            fout.close()
            print('Done: '+ time)
