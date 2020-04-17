import pandas as pd

dfHR = pd.read_csv("HR_Employee_Attrition_Data.csv")
#pd.set_option('display.max_columns', 500)

colNames = dfHR.columns
print(colNames)
print(dfHR.shape)
rows = dfHR.shape[0]

dfHR["AttritionNumber"] = pd.get_dummies(dfHR["Attrition"], drop_first=True)
impDFHR = dfHR[['Age', 'AttritionNumber']]
impDFHR["DerivedCol"] = dfHR["Age"] * 1.2
print(impDFHR.head())

dfDummyDept = pd.get_dummies(dfHR["Department"], drop_first=True)
dfHR[dfDummyDept.columns] = dfDummyDept
print(dfHR[dfDummyDept.columns.values])
dfHR[dfDummyDept.columns].to_csv("ModifiedHRData.csv")