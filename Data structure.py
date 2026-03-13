
#Data structure
#1.Series
#2.DataFrame
#3 pd.Series
#4 pd.DataFrame

#Create a dictionary
dict_var={"Name":["Alice","Bob","Charlie"],
          "Age":[25,30,35],
          "Score":[88.5,92.3,79.1]
          }
print(type(dict_var))

#Create a Data frame
import pandas as pd 
df=pd.DataFrame(dict_var)

#Series(single column)
ages=df["Age"]
print(ages[1])

#quick inspection
print(df.shape)          #(3,3)
print(df.dtypes)         #COLUMN TYPE
print(df.describe())     #statistics

#another dataframe

df=pd.DataFrame({"Name":["Alice","Bob","Charlie","Diana"],
                 "Dept":["IT","HR","IT","HR"],
                 "Salary":[70000,65000,80000,72000]})

#Filtering 
df[df["Dept"]=="HR"]
df[df["Dept"]=="IT"]
it_team=df[df["Dept"]=="IT"]
print(it_team)
high_pay=df[df["Salary"]>70000]
print(high_pay)

#Sorting
sorted_df=df.sort_values("Salary",ascending=False)
print(sorted_df)

#New column
df["Bonus"]=df["Salary"]*0.1

#groupby -aggregate
dept_avg=df.groupby("Dept")["Salary"].mean()
print(dept_avg)

#Drop and rename
df=df.drop(columns=["Bonus"])
df= df.rename(columns={"Dept":"Department"})
