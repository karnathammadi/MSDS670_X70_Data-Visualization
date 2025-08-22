# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Loading dataset
Data = pd.read_csv("C:/datasets/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Showing information about columns and basic statistics
print(Data.info())
print(Data.describe())

# Converting attrition values into numbers for analysis
Data['Attrition'] = Data['Attrition'].map({'Yes':1, 'No':0})

# 1. Plotting Attrition by Department using bar plot
# Getting department names
departments = Data['Department'].unique()
# Counting employees who stayed in each department
attr_0_counts = [len(Data[(Data['Department']==dept) & (Data['Attrition']==0)]) for dept in departments]
# Counting employees who left in each department
attr_1_counts = [len(Data[(Data['Department']==dept) & (Data['Attrition']==1)]) for dept in departments]
# Setting bar width and positions
bar_width = 0.35
x = np.arange(len(departments))
# Creating bar plot with side by side bars
plt.figure(figsize=(8,5))
plt.bar(x - bar_width/2, attr_0_counts, width=bar_width, color='skyblue', label='No')
plt.bar(x + bar_width/2, attr_1_counts, width=bar_width, color='red', label='Yes')
plt.xticks(x, departments)
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.title("Attrition by Department")
plt.legend(title='Attrition')
plt.show()


# 2. Plotting Age Distribution by Attrition using histogram
# Creating histogram for employees who stayed and who left
plt.figure(figsize=(8,5))
plt.hist(Data[Data['Attrition']==0]['Age'], bins=20, alpha=0.7, color='skyblue', label='No')
plt.hist(Data[Data['Attrition']==1]['Age'], bins=20, alpha=0.7, color='red', label='Yes')
plt.xlabel("Age")
plt.ylabel("Number of Employees")
plt.title("Age Distribution by Attrition")
plt.legend(title='Attrition')
plt.show()


# 3. Plotting Monthly Income vs Years at Company using scatter plot
# Drawing scatter points for employees who stayed
plt.figure(figsize=(8,5))
plt.scatter(Data[Data['Attrition']==0]['YearsAtCompany'], Data[Data['Attrition']==0]['MonthlyIncome'],
            color='skyblue', alpha=0.7, label='No')
# Drawing scatter points for employees who left
plt.scatter(Data[Data['Attrition']==1]['YearsAtCompany'], Data[Data['Attrition']==1]['MonthlyIncome'],
            color='red', alpha=0.7, label='Yes')
plt.xlabel("Years at Company")
plt.ylabel("Monthly Income")
plt.title("Monthly Income vs Years at Company")
plt.legend(title='Attrition')
plt.show()


# 4. Plotting Job Satisfaction by Job Role using box plot
# Preparing job roles for comparison
roles = Data['JobRole'].unique()
# Collecting job satisfaction values for each role
data_to_plot = [Data[Data['JobRole']==role]['JobSatisfaction'] for role in roles]
# Creating box plot for job satisfaction by role
plt.figure(figsize=(10,6))
bp = plt.boxplot(data_to_plot, patch_artist=True)
# Coloring boxes depending on attrition majority in each role
for i in range(len(roles)):
    colors = ['skyblue' if np.mean(Data[Data['JobRole']==roles[i]]['Attrition']==0) > 0.5 else 'red']
    bp['boxes'][i].set_facecolor(colors[0])
# Adding labels and title
plt.xticks(range(1,len(roles)+1), roles, rotation=45)
plt.ylabel("Job Satisfaction")
plt.title("Job Satisfaction by Job Role")
plt.show()