import pandas as pd

df = pd.DataFrame({'name': ['Olivia','Olivia','Alex','Alex','Tom','Tom','Tom'],
           'age': [32,23,45,35,20,28,55],
           'sex':['female11', 'male22','ma3le','ma4le','ma77le','fem8al9e','fem3ale'],
            'num': [1111,2222,45,5555,3333,228,51115]})


# 1
for x in df.index:
    if df.loc[x, "num"] < 1000:
        df.drop(x, inplace=True)

# 2
for x in df.index:
    df.loc[x, "sex"] = ''.join(filter(str.isdigit, df.loc[x, "sex"]))

# 3
myList = []

for x in df.index:
    myList.append(int(df.loc[x, "age"])+int(df.loc[x, "sex"]))

df['Address'] = myList


df = df.sort_values(by=['Address'], ascending=False)
df = df.drop_duplicates('name')
df = df.sort_values(by=['name'], ascending=True)


print(df)
