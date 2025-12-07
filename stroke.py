import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("/content/healthcare-dataset-stroke-data.csv")
print (data.head())

data.tail()
data.info()
print(data[['smoking_status','gender','ever_married','work_type','Residence_type']].dtypes)

data.describe()
data.shape
data.columns
data.isnull().sum()
data['bmi']=data['bmi'].fillna(data['bmi'].median())
data.isnull().sum()
data.dropna()

conditional_bmi=data[data['bmi']<=25.5]  
print(conditional_bmi.head())

conditional_smoking_status=data[data['smoking_status']!='never smoked']
print(conditional_smoking_status)

conditional_smokingstatus=data[data['smoking_status'].isin(['formerly smoked','smokes'])]
print(conditional_smokingstatus)

data["smoking_status"].value_counts().plot(kind="bar")
plt.title("Bar Plot")
plt.xlabel("smoking_status")
plt.ylabel("Count")
plt.show()

plt.hist(data["avg_glucose_level"],bins=20)
plt.title("Histogram")
plt.xlabel("avg_glucose_level")
plt.ylabel("Count")
plt.show()
