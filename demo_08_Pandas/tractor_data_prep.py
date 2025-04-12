# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 6315: Python for Business Analytics
#
# Name:
#
# Date:
#
##################################################
#
# Sample Script for Assignment 2:
# Manipulating Data
#
##################################################
"""

##################################################
# Import Required Modules
##################################################

import pandas as pd
import os


# Import a module for estimating regression models.
import statsmodels.formula.api as sm # Another way to estimate linear regression
# This is a "light duty" modeling package designed to mimic the interface in R.


##################################################
# Set up Workspace
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
# Part a) Read Spreadsheet and Sales Data
##################################################


tractor_xlsx = pd.ExcelFile('tractor_data.xlsx')

# Read the data from the sheet with tractor sales data.
tractor_sales = pd.read_excel(tractor_xlsx,  'tractor_sales')


# Describe the contents of that file.
tractor_sales.describe()


#--------------------------------------------------
# Fit a regression model.
#--------------------------------------------------

reg_model_sales = sm.ols(formula = 
                           "saleprice ~ age + enghours + johndeere + spring + summer + winter", 
                           data = tractor_sales).fit()


# Display a summary table of regression results.
print(reg_model_sales.summary())




##################################################
# Part b) Read Specification Data
##################################################

# Read the data from the sheet with tractor sales data.
tractor_specs = pd.read_excel(tractor_xlsx,  'tractor_specs')


# Describe the contents of that file.
tractor_specs.describe()


#--------------------------------------------------
# Join the two datasets together.
#--------------------------------------------------


# The pd.concat command concatenates two data frames.
tractor_sales_specs = pd.concat([tractor_sales, tractor_specs], axis = 1)

# Check to see the columns in the result.
tractor_sales_specs.describe()

tractor_sales_specs.columns



#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

reg_model_sales_specs = sm.ols(formula = 
                           "saleprice ~ age + enghours + johndeere \
                               + spring + summer + winter \
                                   + horsepower + diesel + fwd + manual", 
                           data = tractor_sales_specs).fit()


# Display a summary table of regression results.
print(reg_model_sales_specs.summary())




##################################################
# Part c) Read Performance Data
##################################################

# Read the data from the sheet with tractor performance data.
tractors_w_cabs = pd.read_excel(tractor_xlsx,  'tractors_cabs')


# Describe the contents of that file.
tractors_w_cabs.describe()



#--------------------------------------------------
# Join the third dataset to the first two.
#--------------------------------------------------


# The pd.concat command concatenates two data frames.
tractor_full = pd.concat([tractor_sales_specs, tractors_w_cabs], axis = 1)

# Check to see the columns in the result.
tractor_full.describe()

tractor_full.columns


#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

reg_model_full = sm.ols(formula = 
                           "saleprice ~ age + enghours + johndeere \
                               + spring + summer + winter \
                                   + horsepower + diesel + fwd + manual + cab", 
                           data = tractor_full).fit()


# Display a summary table of regression results.
print(reg_model_full.summary())



##################################################
# End
##################################################
