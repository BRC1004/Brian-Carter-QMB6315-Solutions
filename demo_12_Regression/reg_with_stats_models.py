# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 6315: Python for Business Analytics
#
# Linear Regression with the statsmodels Module
#
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business
# University of Central Florida
#
# April 21, 2025
#
# This script outlies one approach to linear regression in python.
# It uses a sample dataset housing_data.csv with the following variables:
#     obsn_num an integer label for each observation
#     house_price (property values, in millions)
#     income (in millions)
#     in_cali (whether the property is in California)
#     earthquake (whether an earthquake had occurred)
# This example uses the statsmodels module for estimation.
#
##################################################
"""



##################################################
# Import Modules.
##################################################


import os # To set working directory
import pandas as pd # To read and inspect data
import statsmodels.formula.api as sm # Another way to estimate linear regression




##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
os.getcwd()

# Get the path where you saved this script.
# This only works when you run the entire script (with the green "Play" button or F5 key).
print(os.path.dirname(os.path.realpath(__file__)))
# It might be comverted to lower case, but it gives you an idea of the text of the path. 
# You could copy it directly or type it yourself, using your spelling conventions. 

# Change to a new directory.

# You could set it directly from the location of this file
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Check that the change was successful.
os.getcwd()
# I got lower case output, even though my folders have some upper case letters.
# But anyway, it works.



##################################################
# Load Data.
##################################################


housing = pd.read_csv('housing_data.csv')



##################################################
# Inspect Data.
##################################################


# What did we just read?
type(housing)

# Take a look at the individual types of columns in the data frame.
housing.dtypes


# Inspect a few rows of data.
housing.head(3)

housing.tail(3)

# Check the dimensions of the data.
housing.index

housing.columns


# Calculate summary statistics for your data.
housing.describe()


# Drop the observation numbers.
housing = housing.drop('obsn_num', axis = 1)


# Display the correlation matrix.
housing.corr()



##################################################
# Simple Regression.
##################################################


#--------------------------------------------------
# Fit the Regression Model.
#--------------------------------------------------

# Fit the regression model.
reg_model_full_sm = sm.ols(formula = 
                           "house_price ~ income + in_cali + earthquake", 
                           data = housing).fit()

# Display the parameters.
print(reg_model_full_sm.params)


# Display a summary table of regression results.
print(reg_model_full_sm.summary())



# Compare with a bivariate model.
reg_model_1_sm = sm.ols(formula = "house_price ~ income", data = housing).fit()
print(reg_model_1_sm.summary())




##################################################
# End
##################################################
