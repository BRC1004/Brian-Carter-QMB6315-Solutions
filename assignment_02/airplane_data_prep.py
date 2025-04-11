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




#--------------------------------------------------
# Fit a regression model.
#--------------------------------------------------




##################################################
# Part b) Read Specification Data
##################################################



#--------------------------------------------------
# Join the two datasets together.
#--------------------------------------------------




#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------




##################################################
# Part c) Read Performance Data
##################################################



#--------------------------------------------------
# Join the third dataset to the first two.
#--------------------------------------------------




#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------



##################################################
# End
##################################################
