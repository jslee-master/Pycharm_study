import json
import pandas as pd

data = pd.read_json('mytxt/database.json')

print(data[0:1])

