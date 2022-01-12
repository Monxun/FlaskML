import requests

# define the remote csv
csv_file = 'https://static.appseed.us/data/titanic.txt'

# dowload the file via requests
r = requests.get(csv_file)

# save content to new LOCAL file
f = open('titanic.csv', 'w')
f.write(r.content.decode('utf-8'))
f.close

############################
import pandas as pd

df = pd.read_csv('titanic.csv')
print(df.head())
