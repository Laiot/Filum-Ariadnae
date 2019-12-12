from ZODB import FileStorage, DB
import pandas as pd
storage = FileStorage.FileStorage('data/app.fs') 
db = DB(storage)
connection = db.open()
root = connection.root()
keys=root.keys()
#print root[keys[0]]
frames =[ pd.DataFrame(root[k], index=[k]) for k in keys ]
data=pd.concat(frames)
print(data)
data.to_csv('./export.csv')
