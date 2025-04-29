# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 6315: Python for Business Analytics
#
# Name: Brian Carter
#
# Date: April 28, 2025
#
##################################################
"""

##################################################
# Import Required Modules
##################################################

import os
import sqlite3
import pandas as pd
import statsmodels.formula.api as sm


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






##################################################
# Question 1: Connect to a Database
#     and Obtain Applications Data
##################################################


#--------------------------------------------------
# a. Connect to the database called customers.db
#     and obtain a cursor object.
#--------------------------------------------------


con = sqlite3.connect('customers.db')
cur = con.cursor()


#--------------------------------------------------
# b. Submit a query to the database that obtains
#    the sales data.
#--------------------------------------------------

query_1 = """
SELECT *
FROM Applications
"""
print(query_1)
cur.execute(query_1)

#--------------------------------------------------
# c. Create a data frame and load the query
#     results into a dataframe.
#--------------------------------------------------


purchase_app = pd.DataFrame(cur.fetchall(), columns=[col[0] for col in cur.description])


# Describe the contents of the dataframe to check the result.

print(purchase_app.describe())
print(purchase_app.columns)



#--------------------------------------------------
# Fit a regression model to check progress.
#--------------------------------------------------

reg_model_app = sm.ols(
    formula = "purchases ~ income + homeownership + credit_limit",
    data = purchase_app
).fit()

# Display a summary table of regression results.
print(reg_model_app.summary())




##################################################
# Question 2: Obtain CreditBureau Data
##################################################




#--------------------------------------------------
# a. Submit a query to the database that obtains
#    the Application data joined with CreditBureau data.
#--------------------------------------------------

query_2 = """
SELECT Applications.*, CreditBureau.*
FROM Applications
INNER JOIN CreditBureau
ON Applications.ssn = CreditBureau.ssn
"""
print(query_2)
cur.execute(query_2)




#--------------------------------------------------
# b. Create a data frame and load the query
#     results into a dataframe.
#--------------------------------------------------




purchase_app_bureau = pd.DataFrame(cur.fetchall(), columns=[col[0] for col in cur.description])



# Describe the contents of the dataframe to check the result.

print(purchase_app_bureau.describe())
print(purchase_app_bureau.columns)



#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

reg_model_app_bureau = sm.ols(
    formula = "purchases ~ income + homeownership + credit_limit + fico + num_late + past_def + num_bankruptcy",
    data = purchase_app_bureau
).fit()

# Display a summary table of regression results.
print(reg_model_app_bureau.summary())




##################################################
# Question 3: Obtain Demographic Data
##################################################



#--------------------------------------------------
# a. Submit a query to the database that obtains
#    the Application data joined with CreditBureau data.
#    and then joined with the Demographic data.
#--------------------------------------------------

query_3 = """
SELECT Applications.*, CreditBureau.*, Demographic.*
FROM Applications
INNER JOIN CreditBureau
    ON Applications.ssn = CreditBureau.ssn
INNER JOIN Demographic
    ON Applications.zip_code = Demographic.zip_code
"""
print(query_3)
cur.execute(query_3)




#--------------------------------------------------
# b. Create a data frame and load the query.
#--------------------------------------------------




purchase_full = pd.DataFrame(cur.fetchall(), columns=[col[0] for col in cur.description])


# Check to see the columns in the result.
print(purchase_full.describe())
print(purchase_full.columns)


#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

reg_model_full = sm.ols(
    formula = "purchases ~ income + homeownership + credit_limit + fico + num_late + past_def + num_bankruptcy + avg_income + density",
    data = purchase_full
).fit()

# Display a summary table of regression results.
print(reg_model_full.summary())



##################################################
# Question 4: Advanced Regression Modeling
##################################################

#--------------------------------------------------
# Parts a-c with utilization.
#--------------------------------------------------




purchase_full["utilization"] = purchase_full["purchases"] / purchase_full["credit_limit"]

print(purchase_full["utilization"].describe())


#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------


reg_model_util = sm.ols(
    formula = "utilization ~ income + homeownership + fico + num_late + past_def + num_bankruptcy + avg_income + density",
    data = purchase_full
).fit()

print(reg_model_util.summary())




#--------------------------------------------------
# Parts a-c with log_odds_util.
#--------------------------------------------------




import math
purchase_full["log_odds_util"] = purchase_full["utilization"] / (1 - purchase_full["utilization"])
purchase_full["log_odds_util"] = purchase_full["log_odds_util"].apply(math.log)

print(purchase_full["log_odds_util"].describe())

#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------


reg_model_logodds = sm.ols(
    formula = "log_odds_util ~ income + homeownership + fico + num_late + past_def + num_bankruptcy + avg_income + density",
    data = purchase_full
).fit()

print(reg_model_logodds.summary())







##################################################
# Commit changes and close the connection
##################################################


# The commit method saves the changes. 
# con.commit()
# No changes were necessary -- only reading.

# Close the connection when finished. 
con.close()




##################################################
# End
##################################################
