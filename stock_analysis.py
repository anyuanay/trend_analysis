from pandas.io.data import DataReader
from datetime import datetime

ibm = DataReader('IBM',  'yahoo', datetime(2016,1,8), datetime(2016,1,13))
print(ibm['Adj Close'])
