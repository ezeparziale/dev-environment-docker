import pandas as pd

df = pd.read_json('https://raw.githubusercontent.com/ezeparziale/hello-docker/master/src/data/players.json')

print(df.head(1))