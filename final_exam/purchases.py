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
# Sample Script for Final Examination:
# Obtaining Data from a Database
# and Building Predictive Models
#
##################################################
"""

##################################################
# Import Required Modules
##################################################






##################################################
# Set up Workspace
##################################################







##################################################
# Question 1: Connect to a Database
#     and Obtain Applications Data
##################################################


#--------------------------------------------------
# a. Connect to the database called customers.db
#     and obtain a cursor object.
#--------------------------------------------------


con = None # Code goes here

cur = None # Code goes here


#--------------------------------------------------
# b. Submit a query to the database that obtains
#    the sales data.
#--------------------------------------------------

query_1 = """
            QUERY 
                GOES
            HERE
            """
print(query_1)
cur.execute(query_1)

#--------------------------------------------------
# c. Create a data frame and load the query
#     results into a dataframe.
#--------------------------------------------------

# Code goes here
purchase_app = None 

# Could use a loop with a pd.concat() command.


# Describe the contents of the dataframe to check the result.
purchase_app.describe()

purchase_app.columns



#--------------------------------------------------
# Fit a regression model to check progress.
#--------------------------------------------------

reg_model_app = sm.ols(formula = 
                           "model formula goes here", 
                           data = purchase_app).fit()


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
            QUERY 
                GOES
            HERE
            """
print(query_2)
cur.execute(query_2)




#--------------------------------------------------
# b. Create a data frame and load the query
#     results into a dataframe.
#--------------------------------------------------



# Code goes here
purchase_app_bureau = None 

# Could use a loop with a pd.concat() command.



# Describe the contents of the dataframe to check the result.
purchase_app_bureau.describe()
purchase_app_bureau.columns



#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

reg_model_app_bureau = sm.ols(formula = 
                           "model formula goes here", 
                           data = purchase_app_bureau).fit()


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
            QUERY 
                GOES
            HERE
            """
print(query_3)
cur.execute(query_3)




#--------------------------------------------------
# b. Create a data frame and load the query.
#--------------------------------------------------



# Code goes here
purchase_full = None 

# Could use a loop with a pd.concat() command.



# Check to see the columns in the result.
purchase_full.describe()

purchase_full.columns


#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

reg_model_full = sm.ols(formula = 
                           "model formula goes here", 
                           data = purchase_full).fit()


# Display a summary table of regression results.
print(reg_model_full.summary())



##################################################
# Question 4: Advanced Regression Modeling
##################################################

#--------------------------------------------------
# Parts a-c with utilization.
#--------------------------------------------------


# Create a variable for credit utilization.

# Code goes here.




#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------


# Code goes here.




#--------------------------------------------------
# Parts a-c with log_odds_util.
#--------------------------------------------------


# Create a variable for credit utilization.

# Code goes here.


#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------


# Code goes here.










##################################################
# Commit changes and close the connection
##################################################


# The commit method saves the changes. 
# con.commit()
# No changes were necessary -- only reading.

# Close the connection when finished. 
con.close()

# Then we can continue with this file when you have time
# to work on it later.



##################################################
# Extra code snippets
##################################################

# In case things go wrong, you can always drop the table
# and start over:
# cur.execute('DROP TABLE Applications')
# cur.execute('DROP TABLE CreditBureau')
# cur.execute('DROP TABLE Demographic')

# This can get the schema of the table,
# cur.execute("PRAGMA table_info('Applications')").fetchall()
# cur.execute("PRAGMA table_info('CreditBureau')").fetchall()
# cur.execute("PRAGMA table_info('Demographic')").fetchall()
# which states the names of the variables and the data types.


##################################################
# End
##################################################
