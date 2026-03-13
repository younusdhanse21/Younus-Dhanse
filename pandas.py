
# Dictionary
dict_var={
    "Name": ["Alice", "Bob", "Charlie","Sharad"],
    "Age": [25, 30, 35, None],
    "Score": [88.5, 92.3, 79.1, 59.2]
}


import pandas as pd
#convert to DataFrame
df = pd.DataFrame(dict_var)

#save to excel,csv, json format
save = df.to_excel("DATAfile.xlsx")
save1 = df.to_csv("DATAfile.csv")
save2 = df.to_json(orient="index")

# read json files in Pandas
df1_json = pd.read_json("rows.json")


import json
with open('rows.json', 'r') as fileobj:
    data = json.load(fileobj)
print(json.dumps(data, indent = 4))




