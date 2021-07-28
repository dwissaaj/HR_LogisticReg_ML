import sys

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
import numpy as np

df = pd.read_csv("HR_comma_sep (2).csv")
class main():
    def __init__(self,satisfaction,evaluation,project,hours,timespend,accident,promotion,depart,salary):
        self.satisfaction = satisfaction
        self.evaluation = evaluation
        self.project = project
        self.hours = hours
        self.timespend = timespend
        self.accident = accident
        self.promotion = promotion
        self.depart = depart
        self.salary = salary

def check_promo():
    if prom > 1 or prom < 0:
        print("value salah")
        sys.exit()
    else:
        pass


def check_dep():
    if dep > 9 or dep < 0:
        print("Value salah ulangi")
        sys.exit()
    else:
         pass

def check_sal():
    if sal > 2 or sal < 0:
        print("Value salah ulangi")
        sys.exit()
    else:
         pass


lb = LabelEncoder()
depart = lb.fit_transform(df["Department"])
salary = lb.fit_transform(df["salary"])

df["new_depart"] = depart
df["new_salary"] = salary


X = df[["satisfaction_level","last_evaluation","number_project","average_montly_hours","time_spend_company"
        ,"Work_accident","promotion_last_5years","new_depart","new_salary"]]
y = df.left



X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=0.3)

lr = LogisticRegression(max_iter=1000)
lr.fit(X_train,y_train)

print("How Satisfaction?")
sat = input()
print("How lat evaluation score?")
eval = input()
print("How much Project worked?")
proj = input()
print("How much work hour?")
hour = input()
print("How years in company?")
year = input()
print("How much work accident happened?")
acc = input()
print("does worker get promotion?0 for false and 1 for true")
prom = int(input())

check_promo()
print("Where worker work?")
print("0 for IT,1 for R&D,2 for Accounting,3 for HR,4 for Management,5 for Marketing,6 for Product Management,7 for Sales,8 for Support,9 for Technical")
dep = int(input())
check_dep()
print("How about salary?")
print("0 for Hight,1 for Low and 2 for Medium")
sal = int(input())
check_sal()
reesult = lr.predict([[sat,eval,proj,hour,year,acc,prom,dep,sal]])
print(reesult)


