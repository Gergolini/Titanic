# import matplotlib.pyplot as plt # for plotting
import pandas as pd # for data manipulation

# Importing the dataset
df = pd.read_csv('train.csv')


# write a line to check the name of the columns of df
df.columns

# check the number of rows and columns of df

# change the index to 'PassengerId', save the result to df (or you can explore the 'inplace' option)

# select the 'Age' column and save it to a Series named s1

# What is the percentage of passengers younger than 15?

# check the statistical summary of s1 (using the describe() function)

# what is the percentage of the passengers who survived?

# drop the 'Cabin' column and save the result to df1

# check the mean value of the 'Age' column

# filter the rows to get all the passengers with 'Age' from 10 to 15

# check how many missing values (null) are there in each column

# for the Age column, fill all the missing values with the mean value

# select the ['Age','SibSp', 'Parch', 'Fare', 'Pclass','Sex'] columns, and save it to a
# numpy array (using .values), save the result to variable "X"

# select the ['Survived'] column from the original df, and save it to a numpy array named as "y"

# X, y will be the starting point for our scikit learn part next week
