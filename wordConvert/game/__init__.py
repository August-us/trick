import pandas as pd

path=r'C:\Users\Administrator\Desktop\pcakage.csv'

data=pd.read_csv(path,sep='==')
data.to_csv(path,index=False)