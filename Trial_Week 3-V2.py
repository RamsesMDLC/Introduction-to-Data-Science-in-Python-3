# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 14:08:16 2021

@author: USUARIO
"""

import pandas as pd
import numpy as np
import re


#MORE DATA PROCESSING WITH PANDAS

#We will deepen our understanding of the Python Pandas library by learning:
    #How to merge DataFrames
    #Generate summary tables
    #Group data into logical pieces
    #Manipulate dates. 
    #Scales of data
    #Creating metrics for analysis. 
    
#Topic 1.1:Merging Dataframes (Theory)
import pandas as pd

#In this lecture we're going to address how you can bring multiple dataframe...
#...objects together, either by merging them horizontally, or by concatenating...
#:.. them vertically. 

#Relational theory (Venn Diagram)
    #A Venn Diagram is traditionally used to show set membership. 
        #For example: the circle on the left is the population of students...
        #...at a university. The circle on the right is the population of...
        #...staff at a university. And the overlapping region in the middle...
        #...are all of those students who are also staff. 
        
    #When we translate this situation (Venn Diagram) to Pandas, we can think...
    #...that we have these two populations as indices (maybe with the label...
    #...of Person Name) in separate DataFrames, . 
    #If we want a list of all the people regardless of whether...
    #...they're staff or student, and all of the information we can get on...
    #...them:
        #In database terminology, this is called a "full outer join",...
        #In set theory, it's called a "union".
        #In the Venn diagram, "it represents everyone in any circle."

    #If we want a list of all the people that are both staff or student...
    #..., and all of the information we can get on them:
        #In database terminology, this is called a "inner join",...
        #In set theory, it's called a "intersection".
        #In the Venn diagram, "it represents overlapping parts of each circle"

#Topic 1.2:Merging Dataframes (Practice)     
# First we create two DataFrames (staff and students). 
    #In this case we are going to create a staff´s DataFrame.
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
    
staff2_df = staff_df.copy()

    # And lets index these staff by name.
staff_df = staff_df.set_index('Name')

    # Now we'll create a student dataframe
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])

student2_df = student_df.copy()     

    # And we'll index this by name too
student_df = student_df.set_index('Name')

    # And lets just print out the dataframes
print("Topic 1.2.1:","\n",staff_df.head())
print("\n")

print("Topic 1.2.2:","\n",student_df.head())
print("\n")

#Topic 1.3:Merging Dataframes (Practice  - how='outer') 

#We allow the union of previous dataframes through the function "merge()" in...
#...which we use the following parameters:
    #We pass in the DataFrame on the left.
    #We pass in the DataFrame on the right.
    #We tell merge that we want it to use an "outer join". 
    #We tell to use the left and right indices as the joining columns.
        #It is important to see that both DataFrames are indexed along the...
        #...value we want to merge them on, which is called Name.
        
    #We will see in the printed DataFrame that everyone is listed. And...
    #...some values listed have missing values (NaN), because they apper just in...
    #...one dataframe.
    
    #It is very important the order of the dataframes when we put them inside...
    #...the code "merge", in that way we know which is located to the left...
    #...and to the right.
df1= pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)
print("Topic 1.3:","\n",df1)
print("\n")

#Topic 1.4:Merging Dataframes (Practice  - how='inner') 

#We allow the union of previous dataframes through the function "merge()" in...
#...which we use the following parameters:
    #We pass in the DataFrame on the left.
    #We pass in the DataFrame on the right.
    #We tell merge that we want it to use an "inner join". 
    #We tell to use the left and right indices as the joining columns.
        #It is important to see that both DataFrames are indexed along the...
        #...value we want to merge them on, which is called Name.
        
    #We will see in the printed DataFrame that only is listed the values that...
    #...belong to the "intersection" of the "left dataframe" and "right dataframe".
    
    #It is very important the order of the dataframes when we put them inside...
    #...the code "merge", in that way we know which is located to the left...
    #...and to the right.
df2= pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)
print("Topic 1.4:","\n",df2)
print("\n")


#Topic 1.5:Merging Dataframes (Practice  - how='left') 

#We allow the union of previous dataframes through the function "merge()" in...
#...which we use the following parameters:
    #We pass in the DataFrame on the left
    #We pass in the DataFrame on the right.
    #We tell merge that we want it to use an "left". 
    #We tell to use the left and right indices as the joining columns.
        #It is important to see that both DataFrames are indexed along the...
        #...value we want to merge them on, which is called Name.
        
    #We will see in the printed DataFrame that only is listed the values that...
    #...belong to the "left dataframe". However, if there is some value that...
    #...belong to the "intersection" of the "left dataframe" and as a consequence...
    #...to "right dataframe", it also will be listed.
    
    #It is very important the order of the dataframes when we put them inside...
    #...the code "merge", in that way we know which is located to the left...
    #...and to the right.
df3= pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)
print("Topic 1.5:","\n",df3)
print("\n")

#Topic 1.6:Merging Dataframes (Practice  - how='right') 

#We allow the union of previous dataframes through the function "merge()" in...
#...which we use the following parameters:
    #We pass in the DataFrame on the left.
    #We pass in the DataFrame on the right.
    #We tell merge that we want it to use an "right". 
    #We tell to use the left and right indices as the joining columns.
        #It is important to see that both DataFrames are indexed along the...
        #...value we want to merge them on, which is called Name.
        
    #We will see in the printed DataFrame that only is listed the values that...
    #...belong to the "right dataframe". However, if there is some value that...
    #...belong to the "intersection" "right dataframe" and as a consequence...
    #...to "left dataframe", it also will be listed.
    
    #It is very important the order of the dataframes when we put them inside...
    #...the code "merge", in that way we know which is located to the left...
    #...and to the right.
df4= pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True)
print("Topic 1.6:","\n",df4)
print("\n")

#Topic 1.7:Merging Dataframes (Practice  - Using: "on") 

#Instead of using the "indices of the dataframes" to join, we can use specific...
#...columns of the dataframes as well, through the parameter called "on". This...
#...parameter assign a column that both dataframe has as the joining column...
#...(instead of an index).

#It is important to say that the index is not replaced for the column called...
#...inside the parameter "on". The index is the normal index (i.e. numbers...
#...ordered from 0 to infinity).

    #It is very important the order of the dataframes when we put them inside...
    #...the code "merge", in that way we know which is located to the left...
    #...and to the right.
df5 = pd.merge(staff2_df, student2_df, how='right', on='Name')
print("Topic 1.7:","\n",df5)
print("\n")

#Topic 1.8:Merging Dataframes (Practice  - Using: "on" with "conflicts between...
#...the DataFrames") 

#If we have conflicts between the DataFrames (i.e. column with the same title...
#...or label but with different content in two or more dataframes for the same...
#..index), we will see that the "merge function" preserves all the information...
#...,but appends an "_x" or "_y" column to help differentiate between which...
#...index went with which column of data. 

#It is important to say that the index is not replaced for the column called...
#...inside the parameter "on". The index is the normal index (i.e. numbers...
#...ordered from 0 to infinity).

    #The "_x" column is always the left DataFrame information, and the "_y"...
    #..column is always the right DataFrame information.
staff3_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 
                          'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 
                          'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 
                          'Location': 'Washington Avenue'}])
student3_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 
                            'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 
                            'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 
                            'Location': '512 Wilson Crescent'}])

df6 = pd.merge(staff3_df, student3_df, how='left', on='Name')
print("Topic 1.8:","\n",df6)
print("\n")

#Topic 1.9:Merging Dataframes (Practice  - Using: "on" with "multi-indexing...
#...and multiple column") 

#In this case, we use a list of the multiple columns that should be used to...
#...join values from both dataframes. 

#It is important to say that the index is not replaced for the column called...
#...inside the parameter "on". The index is the normal index (i.e. numbers...
#...ordered from 0 to infinity).

    #Recall that the column name(s) assigned to the on parameter needs to...
    #...exist in both dataframes.
staff4_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 
                          'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 
                          'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 
                          'Role': 'Grader'}])
student4_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 
                            'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 
                            'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 
                            'School': 'Engineering'}])


df7 = pd.merge(staff4_df, student4_df, how='inner', on=['First Name','Last Name'])
print("Topic 1.9:","\n",df7)
print("\n")

#Topic 1.10: Concatenation (Theory)

#Merging: is join "horizontally" the dataframes, meaning we join on similar...
#... values in a column found in two dataframes.

#Concatenating: is join "vertically" the dataframes, meaning we put dataframes...
#... on top or at the bottom of each other.

    #For instance: We have a dataset that tracks some information over the...
    #...years. And each year's record is a separate CSV and every CSV for...
    #...every year's record has the exactly same columns. We can concatenate them.

#Topic 1.11: Concatenation 

    #Practice - Loading the data

df8 = pd.read_csv("cwurData1.csv")
df9 = df8.head()
print("Topic 1.11.1:","\n",df9)
print("\n")

df10 = pd.read_csv("cwurData2.csv")
df11 = df10.head()
print("Topic 1.11.2:","\n",df11)
print("\n")

df12 = pd.read_csv("cwurData3.csv")
df13 = df12.head()
print("Topic 1.11.3:","\n",df13)
print("\n")

   #Practice - Measuring the lentgh of the every dataframe (separately)
   
print(len(df8))
print(len(df10))
print(len(df12))
print("\n")

   #Practice - Concatenating the data with function ".concat()"
   
        #It is very interesting that we first create a list of the dataframes...
        #...that we want to concatenate. Then create a new dataframe in which...
        #...we are going to apply the code of ".concat()".
        
        #It is very interesting that the index of the concatenated dataframe...
        #...is formed by the index of every separate dataframe that we just...
        #...concatenate (i.e. a new index was no created for the new...
        #...concatenated dataframe)

df14 = [df8, df10, df12]
df15 = pd.concat(df14)
df16 = df15.head()
print("Topic 1.11.4:","\n",df16)
print("\n")

   #Practice - Measuring the lentgh of the concatenated dataframe.
   
print(len(df15))
print("\n")

    #Practice - Using "key parameters" in the concatenated dataframe.

    #To avoid any misunderstanding with the data of the concatenated...
    #...dataframe, we can use a parameter ("keys parameter") of the function...
    #...".concat()". With those parameters can set an extra level of indices...
    #...(i.e. another column of indices) that list keys (the name of those...
    #...keys are created by the user)...
    #...that we want to correspond (in the order that we concatenate the...
    #...the dataframes) to the dataframes into the keys parameter

df17 = pd.concat(df14, keys=['Dataframe1','Dataframe2','Dataframe3'])
print("Topic 1.11.5:","\n",df17)
print("\n")

    #Extra: We can use with function ".concat()" the "inner method" and "outer...
    #...method 
        #If we are concatenating two dataframes that do not have identical...
        #...columns, and choose the "outer method", some cells (columns) will...
        #...be NaN values (in other words, we are...
        #...going to see as final result all the columns of both dataframes;...
        #...therefore some columns that are not in common will be full of..
        #...NaN values).

        #If we are concatenating two dataframes that do not have identical...
        #...columns, and choose the "inner method", then some observations...
        #...(rows) will be dropped due to NaN values (in other words, we are...
        #...going to see as final result only the columns in common;...
        #...therefore columns that are not in common are dropped).

##############################################################################

#Topic 2.1: Panda Idioms
import pandas as pd
import numpy as np

# Pandas as Python has its own set of codes that are very useful (those codes...
#...are called "Pandorable").

df18 = pd.read_csv('census.csv')
df19 = df18.head()
print ("Topic 2.1:","\n", df19)  
print("\n")

df22 = df18.copy()

df32 = df18.copy()

df34 = df18.copy()

df36 = df18.copy()

##Topic 2.2: Panda Idioms (Method chaining = Pandorable Way of code)

#The main objective of "Method Chaining" is to apply several functions or...
#...methods to a object in a condensed and readable way (i.e. several lines...
#...condensed in a "statement of code").

    #The "statement of code" can be identify be parenthesis that which tells...
    #...python I'm going to span the statement over multiple lines).

    #REMEMBER[ dropna() ]:
        #It is Panda dataframe code.
        
        #Allow us to remove the rows and columns with Null and NaN values or...
        #...that do not follow certain parameter.
        
        #If we don't want the "NaN" data, we use them "dropna() function". The...
        #...returned DataFrame now has all of the "NaN" rows dropped. 
        
        #We can use the function ".dropna()", which is able to drop all of... those...
        #...rows which have any missing data (i.e. this function will eliminate...
        #...from the dataframe all the rows that have missing data. One way to...
        #...see this in a esay way is to look the values of the index and then....
        #...see the gaps).
        
        #The syntax is: dropna(self, axis=0, how="any", thresh=None, subset=None, inplace=False)
            #axis: possible values are {0 or ‘index’, 1 or ‘columns’},...
            #...default 0. If 0, drop rows with null values. If 1, drop...
            #...columns with missing values.
            #how: possible values are {‘any’, ‘all’}, default ‘any’. If ‘any’,..
            #...drop the row/column if any of the values is null. If ‘all’,...
            #...drop the row/column if all the values of every cell are missing.
            #thresh: an int value to specify the threshold for the drop operation.
            #subset: specifies the rows/columns to look for null values.
            #inplace: a boolean value. If True, the source DataFrame is...
            #...changed and None is returned.
            
    #REMEMBER[ where() ]:
        #It is Numpy code.
        
        #We can use the numpy.where() function to select elements from a...
        #...numpy array, based on a condition.
        
        #This code "hide" the data we don't want.
        
        #Despite being really handy, "where()" function isn't actually used...
        #...that often. Instead, the pandas developer created a shorthand...
        #...syntax which combines "where()" and "dropna()" function, doing...
        #...both at once, using indexing operator [] to do this.

            
df20 = (df18.where(df18['SUMLEV']==50)
    .dropna()
    .set_index(['STNAME','CTYNAME'])
    .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))
df21 = df20.head()
print ("Topic 2.2:","\n", df21)  
print("\n")

#Topic 2.3: Panda Idioms (Tradional Way of code)

#This code will allow us to get the same result of the Topic 2.2

    #It is important to say that the "Overloaded indexing operator" [] drop...
    #...NAN values; therefore, we do not need a code (i.e. "dropna()") that....
    #...get ried of the NAN values as we did in the Topic# 2.2

df24 = df22[df22['SUMLEV']==50]
df25 = df24.set_index(['STNAME','CTYNAME'])
df26 = df25.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})
df27 = df26.head()
print ("Topic 2.3:","\n", df27)  
print("\n")

#Topic 2.4: Panda Idioms ("Pandorable Way of code" vs "Tradional Way of code")

#It is important to know when to apply the way of the Topic #2.2 or Topic 2.3;...
#...therefore, a easy way to do that is through timing them. We are going to...
#...apply the timing functionality called "timeit"

    #Applying the "timeit" module
import timeit

    #REMEMBER[ global ]:
        #When a python variable is defined outside a function the code...
        #..."global" allow us to access and play with a variable that is...
        #...outside fo the function (in any part of the Python program).
        
def first_approach():
    global df23
    return (df23.where(df23['SUMLEV']==50)
             .dropna()
             .set_index(['STNAME','CTYNAME'])
             .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))
    
    # Read in our dataset
df23 = pd.read_csv('census.csv')

    # And now lets run it. Here we will just set it to 10 iterations
T1 = timeit.timeit(first_approach, number=10)
print ("Topic 2.4:","\n", T1)  
print("\n")

#Topic 2.5: Panda Idioms ("Pandorable Way of code" vs "Tradional Way of code")

#It is important to know when to apply the way of the Topic #2.2 or Topic 2.3;...
#...therefore, a easy way to do that is through timing them. We are going to...
#...apply the timing functionality called "timeit"

    #Applying the "timeit" module

def second_approach():
    global df28
    df28[df28['SUMLEV']==50]
    df28.set_index(['STNAME','CTYNAME'])
    df28.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})
    
    # Read in our dataset
df28 = pd.read_csv('census.csv')

    # And now lets run it. Here we will just set it to 10 iterations
T2 = timeit.timeit(second_approach, number=10)
print ("Topic 2.5:","\n", T2)  
print("\n")

#Topic 2.6: Panda Idioms (Apply Function - Serie)

#As Python has a function called "Map", Pandas also has a function called....
#..."Apply" that allow us to execute a function or several methods to all or...
#...certain elements (i.e. axis = columns or rows) of a Serie or Dataframe...
#...and we get as a result a Serie or Dataframe

               
    #REMEMBER[ Apply ]:
        
    #DataFrame.apply(func, axis=0, raw=False, result_type=None, args=(), **kwargs)

    #Apply a function along an axis of the DataFrame.

    #Parameters:

        #Axis (By default = 0). Rows (axis=0) <-- Vertical axis, Columns (axis=1)...
        #...<--Horizontal axis. (i.e. this is the Axis along which the...
        #...function is applied).
        
import numpy as np

#First, we create a function that we are going to apply to every row of the... 
#...dataframe(especifically to certain columns or all columns). Then as a...
#...result we get a dataframe (in this case, for instance):
    
    #In this case is very interesting that the way we get the maximun and...
    #...minimun value of a row (i.e. the rows of the list of columns inside...
    #..square brackets) is through a method of Numpy.

    #It is important to say that the variable "row" is used in the...
    #...following way:
        
        #It is a kind of variable which allow us to work or operate in a single...
        #...row of the dataframe, just with a list of the columns labels in which...
        #...we are interested. 
        
        #When we mixed it with the Panda code "apply", we are repeting the...
        #...execution of the function that is inside the Panda code "apply"...
        #...in every row of the dataframe.
        
            #Also, it is important to remember that the "axis = columns"...
            #...means that the "apply" Panda function is used in the...
            #...horizontal axis (i.e in rows).

def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    return pd.Series({'min': np.min(data), 'max': np.max(data)})

df29 = df18.apply(min_max, axis='columns').head()
print ("Topic 2.6:","\n", df29)  
print("\n")

#Topic 2.7: Panda Idioms (Apply Function - Adding columns to the existing...
#...Dataframe).

#First, we create a function that we are going to apply to every row of the... 
#...dataframe(especifically to certain columns or all columns). Then as a...
#...result we get the same Dataframe plus two added columns with the results...
#...of minimum and maximum values (in this case for instance).

#In this case is very interesting that the way we get the maximun and...
    #...minimun value of a row (i.e. the rows of the list of columns inside...
    #..square brackets) is through a method of Numpy.

    #It is important to say that the variable "row" is used in the...
    #...following way:
        
        #It is a kind of variable which allow us to work or operate in a single...
        #...row of the dataframe, just with a list of the columns labels in which...
        #...we are interested. 
        
        #When we mixed it with the Panda code "apply", we are repeting the...
        #...execution of the function that is inside the Panda code "apply"...
        #...in every row of the dataframe.
        
            #Also, it is important to remember that the "axis = columns"...
            #...means that the "apply" Panda function is used in the...
            #...horizontal axis (i.e in rows).

def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    # Create a new entry for max
    row['max'] = np.max(data)
    # Create a new entry for min
    row['min'] = np.min(data)
    return row

    # Now just apply the function across the dataframe
df30 = df18.apply(min_max, axis='columns')
df31 = df30.head()
print ("Topic 2.7:","\n", df31)  
print("\n")

#Topic 2.8: Panda Idioms (Apply Function - Creating a Serie using Lambdas).

#First, we create a function that we are going to apply to every row of the... 
#...dataframe(especifically to certain columns or all columns). Then as a...
#...result we get a Serie with the results of maximum values (in this case...
#... for instance).

    #In this case is very interesting that the way we get the maximun...
    #...value of a row (i.e. a list of columns inside...
    #..square brackets) is through a method of Numpy and the use of a "Lambda...
    #...Function"
    
    #REMEMBER[ Lambdas ]:
        # A "Lambda Function" is just an unnamed function in python, that...
        #...takes a single parameter "x" and returns a single value.
    
    #It is important to say that "Apply" is rarely used with large function...
    #...definitions, like we did in Topic 2.6 and Topic 2.7. Instead, we...
    #...typically use it with "Lambda Function". 
    
    #It is important to say that the variable "row" is used in the...
    #...following way:
        
        #It is a kind of variable which allow us to work or operate in a single...
        #...row of the dataframe, just with a list of the columns labels in which...
        #...we are interested. 
        
        #When we mixed it with the Panda code "apply", we are repeting the...
        #...execution of the function that is inside the Panda code "apply"...
        #...in every row of the dataframe.
        
            #Also, it is important to remember that the "axis = columns"...
            #...means that the "apply" Panda function is used in the...
            #...horizontal axis (i.e in rows).
            
rows = ['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013','POPESTIMATE2014', 
        'POPESTIMATE2015']
# Now we'll just apply this across the dataframe with a lambda
df33 = df32.apply(lambda x: np.max(x[rows]), axis=1).head()
print ("Topic 2.9:","\n", df33)  
print("\n")

#Topic 2.9 (Option #1): Panda Idioms (Apply Function - Adding columns to the existing...
#...Dataframe using Lambdas).

#First, we create a function that we are going to apply to every row of the... 
#...dataframe(especifically to certain columns or all columns). 
    
    #REMEMBER[ Lambdas ]:
        # A "Lambda Function" is just an unnamed function in python, that...
        #...takes a single parameter "x" and returns a single value.
    
    #It is important to say that "Apply" is rarely used with large function...
    #...definitions, like we did in Topic 2.6 and Topic 2.7. Instead, we...
    #...typically use it with "Lambda Function". 
    
    #It is important to say that the variable "row" is used in the...
    #...following way:
        
        #It is a kind of variable which allow us to work or operate in a single...
        #...row of the dataframe, just with a list of the columns labels in which...
        #...we are interested. 
        
        #When we mixed it with the Panda code "apply", we are repeting the...
        #...execution of the function that is inside the Panda code "apply"...
        #...in every row of the dataframe.
        
            #Also, it is important to remember that the "axis = columns"...
            #...means that the "apply" Panda function is used in the...
            #...horizontal axis (i.e in rows).
    
def sumval (row):
    data = row['REGION']
    row['SUM VALUE REGION 1'] = data + 10
    return row

# Now we'll just apply this across the dataframe with a lambda
df35 = df34.apply(lambda x: sumval (x), axis=1).head()
print ("Topic 2.10:","\n", df35)  
print("\n")

#Topic 2.9 (Option #2): Panda Idioms (Apply Function - Adding columns to the existing...
#...Dataframe using Lambdas).

#First, we create a function that we are going to apply to every row of the... 
#...dataframe(especifically to certain columns or all columns). 
    
    #REMEMBER[ Lambdas ]:
        # A "Lambda Function" is just an unnamed function in python, that...
        #...takes a single parameter "x" and returns a single value.
    
    #It is important to say that "Apply" is rarely used with large function...
    #...definitions, like we did in Topic 2.6 and Topic 2.7. Instead, we...
    #...typically use it with "Lambda Function". 
    
    #It is important to say that the variable "row" is used in the...
    #...following way:
        
        #It is a kind of variable which allow us to work or operate in a single...
        #...row of the dataframe, just with a list of the columns labels in which...
        #...we are interested. 
        
        #When we mixed it with the Panda code "apply", we are repeting the...
        #...execution of the function that is inside the Panda code "apply"...
        #...in every row of the dataframe.
        
            #Also, it is important to remember that the "axis = columns"...
            #...means that the "apply" Panda function is used in the...
            #...horizontal axis (i.e in rows).
    
def sumval2 (w):
    dataplus = w + 10
    return dataplus

# Now we'll just apply this across the dataframe with a lambda
df34["SUM VALUE REGION 2"] = df34['REGION'].apply(lambda x: sumval2 (x))
df37 = df34["SUM VALUE REGION 2"].head()
print ("Topic 2.11:","\n", df37)  
print("\n")

##############################################################################

#Topic 3.1: GroupBy (Split)

#MAIN CONCEPT #1 

#GroupBy it is such a powerful weapon. in fact, SQL the language has been a...
#...standard tool for advanced data analysts for decades before pandas appeared. 

#If we want to get more info about the data (deep flavor of them) we...
#...need to apply more than just simple "aggregations" of Pandas and Numpy.

#For instance, "aggregations" of Pandas are the followings:

#...count() Total number of items
#...first(), last() First and last item
#...mean(), median() Mean and median
#...min(), max() Minimum and maximum
#...std(), var() Standard deviation and Variance
#...mad() Mean absolute deviation
#...prod() Product of all items
#...sum() Sum of all items

#Therefore, in this case we can apply the concept of "split, apply and combine".

    #The "split step" involves breaking up and grouping a DataFrame depending...
    #...on the value of the specified key.
    
        #Using "Groupby" code.

    #The "apply step" involves computing some function, usually an "aggregate,...
    #...transformation, "apply" or filtering", within the individual groups.

        #Aggregation: do some statistical calculations
        
        #Apply： do some data conversion
        
        #Transformation: do some data processing transformation
        
        #Filtration: do some group level filtering

    #The combine step merges the results of these operations into an output...
    #...array.
    
        #Using concatenation "concat" code.
    
#MAIN CONCEPT #2

#Notice that what is returned  after apply a "Groupby" code is not a...
#..."DataFrames", but a "DataFrameGroupBy" object (this object is a...
#...special view of the DataFrame, which is poised to dig into the groups...
#...but does no actual computation until the aggregation or function is applied.

#Topic 3.1: Splitting

#The main concept is that we can select and...
#...extract a piece of the dataframe and then play with that (i.e. applying...
#...some code or function or method to that piece of data) with the Pandas...
#...function "groupBy()", after that, combines the results back together into...
#...another dataframe (In Pandas this is refered to as the "split-apply-...
#...combine pattern")

    #This topic is very useful because we avoid to apply the code or function...
    #...or method to all the dataframe, when we are really interested only...
    #...in analyzed a piece of the dataframe.
    
df38 = pd.read_csv('census.csv')
df39 = df38[df38["SUMLEV"]==50]

df41 = df38[df38["SUMLEV"]==50]

df40 = df39.head()
print ("Topic 3.1:","\n", df40)  
print("\n") 

    #In the first example,  I want to use the census date. Let's..
    #..get a list of the unique states, then we can iterate over all the...
    #...states and for each state we reduce the data frame and calculate the
    #...average.
    
    # Let's run such task for 3 times and time it. For this we'll use the cell...
    #...magic function %%timeit
    
    #REMEMBER[ unique() ]:
        # It is a Pandas function that allow us to deal and work with a unique...
        #...kind of values when we have repeated or redundant...
        #...values in a column of a dataframe or serie.
        
        #The syntax are the followings:
            #Option 1: dataframe name.column name.unique()
                
            #Option 2: dataframe name['column name'].unique()

#Topic 3.1.2: Splitting (Unique - Option 1)

    #First, we create a For Loop that works in every line of the column...
    #..."STNAME".
    
        #It is very interesting see and constrast the use of the "For loop" ...
        #...when we use the "Groupby" code meanwhile in all the Topic #2 we...
        #...use the function "Apply" (without the use of a "For loop") to....
        #...execute a function in several elements (rows or columns) of a...
        #...serie or dataframe.
    
    # We'll just calculate the average using numpy for this particular...
    #..."STNAME" and if we detect another "STNAME", then code does not take...
    #...in count for the average fo the column 'CENSUS2010POP'.
    
    # And we'll print it. (As an answer we will see the average population...
    #..."CENSUS2010POP" per "STNAME" and also we will see at the bottom of...
    #...that output the time to finish (fair bit, just like 5 seconds).
    
    #We will try another approach to get the answer faster and using the...
    #...code "groupby()"
    
import timeit  

mycode1 ='''
import pandas as pd
import numpy as np
df38 = pd.read_csv('census.csv')
df39 = df38[df38["SUMLEV"]==50]

for statex in df39['STNAME'].unique():
    
    averg = np.average(df39.where(df39['STNAME']==statex).dropna()['CENSUS2010POP'])
    
    print('Counties in state ' + statex + ' have an average population of ' + str(averg))  
'''

print ("Topic 3.1.1:", timeit.timeit(setup = "pass", stmt = mycode1, number = 3))
print("\n")  

#Topic 3.1.2: Splitting (Unique - Option 2)

    #The only change in this code is how we use the code "unique"

    #First, we create a For Loop that works in every line of the column...
    #..."STNAME".
    
        #It is very interesting see and constrast the use of the "For loop" ...
        #...when we use the "Groupby" code meanwhile in all the Topic #2 we...
        #...use the function "Apply" (without the use of a "For loop") to....
        #...execute a function in several elements (rows or columns) of a...
        #...serie or dataframe.
    
    # We'll just calculate the average using numpy for this particular...
    #..."STNAME" and if we detect another "STNAME", then code does not take...
    #...in count for the average fo the column 'CENSUS2010POP'.
    
    # And we'll print it. (As an answer we will see the average population...
    #..."CENSUS2010POP" per "STNAME" and also we will see at the bottom of...
    #...that output the time to finish (fair bit, just like 4.84 seconds).
    
    #We will try another approach to get the answer faster and using the...
    #...code "groupby()"

mycode2 ='''
import pandas as pd
import numpy as np
df38 = pd.read_csv('census.csv')
df39 = df38[df38["SUMLEV"]==50]

for statex in df39.STNAME.unique():

    averg = np.average(df39.where(df39['STNAME']==statex).dropna()['CENSUS2010POP'])
    
    print('Counties in state ' + statex + ' have an average population of ' + str(averg))
'''
print ("Topic 3.1.2:", timeit.timeit(setup = "pass", stmt = mycode2, number = 3))
print("\n") 

#Topic 3.1.3: Splitting ( Using "groupby()" direct in a specific column)

    # For this method, we start by telling Pandas we're interested in grouping by...
    #..."STNAME", this is the "split".

    #There are two values we set in the "For Loop":
        #The first value is the value of the key we were trying to "groupby(), in...
        #...this case a specific "STNAME".
        #The second value is dataframe from which we are going to select a column...
        #...to work based in the groupby() described previously.
    
    #Then we write inside the "For Loop" a code that is going to calculate the...
    #..average of the selected column of the dataframe ('CENSUS2010POP') based in...
    #...the groupby().

    #Finally, we print the results.(As an answer we will see the average population...
    #..."CENSUS2010POP" per "STNAME" and also we will see at the bottom of...
    #...that output the time to finish (fair bit, just like 0.5 seconds). This...
    #...is a way to see that the use of "groupby()" allow us to see the answer....
    #...in a fastest way.
    
           #It is important to notice that the "groupby()" code apparently...
           #...split also the dataframe [i.e. after the use of the "groupby()"...
           #...code were printed several dataframes according to the groups...
           #...generated].

mycode3 ='''
import pandas as pd
import numpy as np
df38 = pd.read_csv('census.csv')
df39 = df38[df38["SUMLEV"]==50]

for groupx, framex in df39.groupby('STNAME'):
   
    avg = np.average(framex['CENSUS2010POP'])

    print('Counties in state ' + groupx + ' have an average population of ' + str(avg))
'''
print ("Topic 3.1.3:", timeit.timeit(setup = "pass", stmt = mycode3, number = 3))
print("\n") 

#Topic 3.2: Splitting ( Using "groupby()" direct in a specific column through...
#...a function).

    # For this method, we start creating a function that do some calculus in..
    #...the column of interest "STNAME" (previously set as the new index of the...
    #...entire original dataframe).
    
    #Then we create a function that will work like the code that activate the...
    #...groupby(), instead of just use a simple column.

    #There are two values we set in the "For Loop":
        #The first value is the value of the key we were trying to "groupby(), in...
        #...this case a specific function that will work in the column...
        #..."STNAME".

           #It is important to notice that this time I didn't pass in a..
           #...column name to groupby(). Instead, I set the index of the...
           #...dataframe to be "STNAME", and if no column identifier is...
           #...passed groupby() will automatically use the index of the dataframe.
        
        #The second value is dataframe from which we are going to select a column...
        #...to work based in the groupby() described previously.
        
           #It is important to notice that the "groupby()" code apparently...
           #...split also the dataframe [i.e. after the use of the "groupby()"...
           #...code were printed three dataframes according to the 3 groups...
           #...generated].
        
df41 = df41.set_index('STNAME')
    
def calcul(valuepop):
    if valuepop[0] < "M":
        return 0
    elif valuepop[0]<'Q':
        return 1
    else:
        return 2

for groupx2, framex2 in df41.groupby(calcul):
    print("Topic 3.2.1:", str(len(framex2)))
    print("Topic 3.2.2", groupx2)
print("\n") 

#Topic 3.3: Splitting ( Using "groupby()" direct in specifics column through...
#...a function).

        #REMEMBER[ groupby() ]:
        #Code:
            #DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=<no_default>, observed=False, dropna=True)
            
        #Parameters:
            #by: mapping, function, label, or list of labels. Used to...
            #...determine the groups for the groupby. 
                #If "by" is a function, it’s called on each value of the...
                #...object’s index. 
                #If a dictionary or Series is passed, the Series or...
                #...dictionaries values will be used to determine the groups...
                #A label or list of labels may be passed to group by the...
                #...columns in self.
                #A tuple is interpreted as a (single) key.
                
            #axis: 0 or ‘index’; 1 or ‘columns’; default 0. Split along rows...
            #...(0) or columns (1).
            
            #level (integer): level name, or sequence of such, default None. If...
            #...the axis is a MultiIndex (hierarchical), group by a particular...
            #...level or levels.
            
            #as_index (bool): default True. For aggregated output, return...
            #...object with group labels as the index. Only relevant for...
            #...DataFrame input. "as_index=False is" effectively “SQL-style”...
            #...grouped output.
            
                #Direct use of "as_index=False" arguments are a good habit...
                #...because if dataframe very large （for example, to reach...
                #...the size of gb ） when, the master becomes one Groupby...
                #...object, and then call reset_index() there will be...
                #...additional time consumption.
                
                #If you want to get a data box with multiple indexes, use...
                #...the default as_index=True.
            
            #sort (bool): default True. Sort group keys. Get better...
            #...performance by turning this off. Note this does not...
            #...influence the order of observations within each group. Groupby...
            #...preserves the order of rows within each group.
            
                #In any operation involving data, sorting is very "the luxury...
                #...of" if you're just grouping, you don't care about order，...
                #...you should turn off sorting when you create a groupby...
                #...object， because this feature is enabled by default. This...
                #...is especially important when you are working on large data...
                #...sets (I thinki maybe is there of time consumption).

#Apparently there is not a mandate to use the "frame" inside the for loop...
#...to be specific in the printing code, because our main objective is the....
#...use of a "column or index or multindex or the application of a function...
#...in a column or index or multindex".

df42=pd.read_csv("listings.csv")
df43 = df42.head()
df44 = df42
print ("Topic 3.3:","\n", df43)  
print("\n") 

df44 = df44.set_index(["cancellation_policy","review_scores_value"])

#In this case the grouping is done alphabetically according to the level...
#...zero (0) and in ascending way according to the level one (1).

for groupx3, framex3 in df44.groupby(level=(0,1)):
    print("Topic 3.3.1.", groupx3)
print("\n") 

#In this case the grouping is done according to the level...
#...one (1).

def topten(reviewx):
    if reviewx[1] == 10:
        return (reviewx[0],"10.0")
    else:
        return (reviewx[0],"BAD")

for groupx4, framex4 in df44.groupby(topten):
    print("Topic 3.3.2.", groupx4)
print("\n") 

#Topic 4: Applying 

#The Pandas developers have 3 broad categories of data processing (i.e. operations)...
#...to happen during the apply step and available by a "GroupBy" code:
    #1- Aggregation of group data
    #2- Transformation of group data
    #3- Filtration of group data

#Topic 4: Aggregation 

#It is the most straight forward of data processing during the apply step.

#Uses the operation "agg()" on the groupby() object. 
    #It is important to say that we are invoking the agg() function on that...
    #...object, therefore we can see round parentheses after the word "agg".
    
    #The "agg()" function is going to apply one or more "functions" we specify...
    #...to the group dataframes and return a single row per dataframe grouped...
    #...in this case "cancellation_policy" is the dataframe/group ("agg()"...
    #...returns a single value per column, so one row per group).
    
        #Note that the "functions" {located inside the "agg()" functions}...
        #...are not function invocations, or function names, they are...
        #...references to functions which will return single values.

#Thus far we have only iterated through the groupby object, unpacking it...
#...into a label (the group name) and a dataframe. {this is important because...
#...in the previous steps [all Topic 3] we work with the data and functions...
#...in different steps and not in the same line of code}.
                 
#But with the groupby method "agg()" we can pass in a dictionary the...
#...following elements:
    #the columns we are interested in the "agg()" code. 
    #the function we are looking to apply to the column inside in the agg() code.
    
#It is important to say that we are only interested to print and show (the...
#...results will be in a heirarchical index [i.e. alphabetically if the index...
#...are formed by string or in descending order if the index are number]) 
#...a small part of the dataframe through groupby() the values of the column...
#..."cancellation_policy" (it is printed as an index, set as a default according...
#...to REMEMBER[ groupby() ]) and related with the "average values" of the...
#...column "review_scores_value".
    #In other words we are creating a groupby() on the dataframe object by the...
    #..column "cancellation_policy". In other words it is still a dataframe...
    #...(smaller tha the original).

df45=pd.read_csv("listings.csv")
df46 = df45.groupby("cancellation_policy").agg({"review_scores_value":np.average})
df466 = df46.head()
print ("Topic 4.1:","\n", df466)  
print("\n") 

    #In this instance we get as a printed result a table with "NaN values" in...
    #...the column "review_scores_value", because in every group of data of...
    #...the column "cancellation_policy" (flexible, moderate, strict,...
    #...super_strict_30) have related "NaN values" in the column...
    #..."review_scores_value" and that altered the function "np.average"...
    #...(because "np.average" does not ignore "NaN values").
    
    #To fix the error in the function "np.average" described in the previous...
    #...comment we use the function "np.nanmean" {Compute the standard...
    #...deviation along the specified axis, while ignoring NaNs}.

df45=pd.read_csv("listings.csv")
df47 = df45.groupby("cancellation_policy").agg({"review_scores_value":np.nanmean})
df477 = df47.head()
print ("Topic 4.2:","\n", df477)  
print("\n") 
    
    #Even:
        #We can use more than one function (per column) at the same time...
        #...inside the agg() code. In this case we use a "tuple of functions":
            #Compute the standard deviation {np.nanstd} along the specified...
            #...axis, while ignoring NaNs.
        #We can have more than one column inside the agg() code {each column....
        #...with their respective function  o functions}.
    
df45=pd.read_csv("listings.csv")
df48 = df45.groupby("cancellation_policy").agg({"review_scores_value":(np.nanmean,np.nanstd),"id":np.mean})
df488 = df48.head()
print ("Topic 4.3:","\n", df488)  
print("\n") 

#Topic 5: Transformation

#Uses the operation "transform()" on the groupby() object. 
    #This is different from "agg() function" because as an answer after...
    #...apply the "transform()" code we get an object (new entire serie or...
    #...dataframe) of the same size of the original dataframe (from which...
    #...is applied the group) based in the size of the column or...
    #...columns selected to group and as a consequence making...
    #...easy to combine in the future this result with the original dataframe...
    #...due to they have the same shape.
        #In other words, if we groupby "cancellation_policy" (flexible,...
        #...moderate, strict, super_strict_30), we are applying a function....
        #...through "transform()" code in every element of the grouped serie...
        #...or dataframe getting multiple values per column (of the selected...
        #...column or columns) and multiple values per row in each groupby().
        
    #In the case of "agg() function" we get only a single value per column (of...
    #...the selected column or columns) so one row per groupby().
    
    #While aggregation must return a reduced version of the data,...
    #...transformation can return some transformed version of the full data...
    #...to recombine. For such a transformation, the output is the same shape...
    #..as the input.
    
# First, lets define just some subset of columns (that belong to the original...
#...dataframe) we are interested in:
    #In this case the first column listed is the column which are designed to...
    #...be grouped and then following columns are those on which we are...
    #...are going to apply some function.
    
df45=pd.read_csv("listings.csv")
colsnew=['cancellation_policy','review_scores_value']


#Option #1: Now lets transform it. I'll store this in its own dataframe.
    #We need to be careful because according to every category generated by...
    #...the "groupby code" we get the mean value of the column...
    #..."review_scores_value" (For instance: for the category "moderate"...
    #...we get through the code "np.nanmean" the mean value considering all...
    #...the rows that belongs to the column "review_scores_value" of this...
    #...category, then we reproduced this unique mean value in the all the...
    #...rows of that belongs to the column "review_scores_value" of this...
    #...category; therefore, if we have 5 categories, we are going to see...
    #...only 5 mean unique values (each one por category) repetead several...
    #...times according to the number of times that appears the category...
    #...in the dataframe.
    
df49=df45[colsnew].groupby('cancellation_policy').transform(np.nanmean)
df499 = df49.head()
print ("Topic 5.1:","\n", df499)  
print("\n") 

#Option #2: Now lets transform it. I'll store this in its own Serie.
    #That produces the almost the same result (a Serie instead of a Dataframe)...
    #..of the Option #1 with a better and readeable code.
    
    #We need to be careful because according to every category generated by...
    #...the "groupby code" we get the mean value of the column...
    #..."review_scores_value" (For instance: for the category "moderate"...
    #...we get through the code "np.nanmean" the mean value considering all...
    #...the rows that belongs to the column "review_scores_value" of this...
    #...category, then we reproduced this unique mean value in the all the...
    #...rows of that belongs to the column "review_scores_value" of this...
    #...category; therefore, if we have 5 categories, we are going to see...
    #...only 5 mean unique values (each one por category) repetead several...
    #...times according to the number of times that appears the category...
    #...in the dataframe.
    
df50 = df45.groupby('cancellation_policy')["review_scores_value"].transform(np.nanmean)
df500 = df50.head()
print ("Topic 5.2:","\n", df500)  
print("\n") 

#Option #3: Now lets transform it, I'll store this in the original dataframe
    #That produces the same result of the Option #2 and then we combine that...
    #...tranformed values to the original dataframe through a new column.
    
    #We need to be careful because according to every category generated by...
    #...the "groupby code" we get the mean value of the column...
    #..."review_scores_value" (For instance: for the category "moderate"...
    #...we get through the code "np.nanmean" the mean value considering all...
    #...the rows that belongs to the column "review_scores_value" of this...
    #...category, then we reproduced this unique mean value in the all the...
    #...rows of that belongs to the column "review_scores_value" of this...
    #...category; therefore, if we have 5 categories, we are going to see...
    #...only 5 mean unique values (each one por category) repetead several...
    #...times according to the number of times that appears the category...
    #...in the dataframe.
    
df51=pd.read_csv("listings.csv")

df51["New RSV"] = df51.groupby('cancellation_policy')["review_scores_value"].transform(np.nanmean)
df511 = df51.head()
print ("Topic 5.3:","\n", df511)  
print("\n") 

#Topic 6: Filtering

#It works like a simple filter. First, we create a function and then we apply...
#...this function through the "groupby" code in the original dataframe and as...
#...result we are going to get a dataframe with only the data that accomplish...
#...the requisites of the function (it means that some of the rows of the....
#....original dataframe will be dropped because after the function application...
#...they do not meet the requisites).

    #The filter() function takes in a function which it applies to each group...
    #...dataframe and returns the values that are True (meet the requisites)...
    #...and drop the values that are False (does not meet the requisites).
    
#Option 1: Function inside the "filter" function.

df52=pd.read_csv("listings.csv")

df53 = df52.groupby('cancellation_policy').filter(lambda x: np.nanmean(x['review_scores_value'])>9.2)
df54 = df53.head()
print ("Topic 6.1:","\n", df54)  
print("\n")

#Topic 7: Apply

# By far the most common operation invoked on groupby objects is the...
#..."apply()" function. This allows us to apply an arbitrary function to...
#...a group, and put the results back for that "apply()" into a single
# dataframe where the index is preserved.

#It is important to say that Using apply can be slower than using some of...
#...the specialized functions, especially "agg()". But, if our dataframes..
#...are not huge, it's a solid general purpose approach.

df70 = pd.read_csv("listings.csv")
df71 = df70[['cancellation_policy','review_scores_value']]
df72 = df71.head()
print ("Topic 7.1:","\n", df72)  
print("\n")

#If we wanted to find the average review score of a listing and its...
#...deviation from the group mean usign the code of "transform()"...
#...it will be a two step process:
    #First we used on the groupby object.
    #Then we had to create anew column. 
    
#To solve this process we can use "apply()" which could wrap this logic in...
#...just a single line.
    #First: we create a function that compute the mean value of the...
    #..."review_scores_value" and then create the new colum that will show...
    #...the difference between of "review_scores_value" and the "mean value....
    #...of review_scores_value".

def calc_mean_review_scores(group):
    
    #In this case, inside the function the word "group" (object in which we...
    #...are going to apply the function "calc_mean_review_scores") is the...
    #...dataframe in which we are applying the code "grouped by" (in this...
    #...case the "groupby()" is considering the "cancellation policy".
    
    avg=np.nanmean(group["review_scores_value"])
    
    #The code "group[review_scores_mean]" create a new column in the...
    #...dataframe "group". This new column has the difference between of...
    #..."review_scores_value" and the "mean valuevof review_scores_value".
    
    group["review_scores_mean"]=np.abs(avg-group["review_scores_value"])
    
    #Finally this function return the dataframe called "group".
    
    return group

#Now we use the code apply() to execute the function...
#..."group[review_scores_mean]" in the dataframe called "group" based...
#...obviously in groupby selection (in this case"cancellation_policy").
df73 = df71.groupby('cancellation_policy').apply(calc_mean_review_scores).head()
print ("Topic 7.2:","\n", df73)  
print("\n")

#############################################################################

#Topic 8.1: Scales

import pandas as pd
import numpy as np

#Categorical Data
    #"Categoricals" are a Pandas data type.
    
    #A "Categorical variable" takes on a limited,...
    #....and usually fixed, number of possible values (categories). Examples:..
    #...are gender, social class, blood type, country affiliation,...
    #...observation, time or rating.
    
    #"Categorical" data...
    #...might have an order (e.g. ‘strongly agree’ vs ‘agree’ or ‘first...
    #...observation’ vs. ‘second observation’), but numerical operations...
    #...(additions, divisions, …) are not possible.
    
    #Order is defined by the order of categories, not lexical order of the...
    #..values. 
    
    #The categorical data type is useful in the following cases:
        #A string variable consisting of only a few different values....
        #...Converting such a string variable to a categorical variable...
        #...will save some memory.
        
        #The lexical order of a variable is not the same as the logical...
        #...order (“one”, “two”, “three”). By converting to a categorical...
        #...and specifying an order on the categories, sorting and min/max...
        #...will use the logical order instead of the lexical order.

#We create a dataframe of letter grades in descending order. 
df74=pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 
                       'ok', 'ok', 'ok', 'poor', 'poor'],
               columns=["Grades"])
print ("Topic 8.1:","\n", df74)  
print("\n")

#Topic 8.2: Checking the data type.

#Now, we check the datatype of this dataframe (to be specific of data that..
#...belong to the only column called "Grades"). In this case we are going... 
#...to see that it's just an "object", since it is just a set of string values.
dftype75 = df74.dtypes
print ("Topic 8.2:","\n", dftype75)  
print("\n")

#Topic 8.3: Casting the data type.

#We are going to change the datatype of this dataframe from "object" to...
#..."category" using the "astype()" function.

#As a result the we are going to see that the new datatype is formed by...
#...eleven elements (i.e. there are eleven categories). 

    #When we passed dtype='category', we used the default behavior:
        #Categories are inferred from the data.
        #Categories are unordered.
        
        #To control those behaviors, instead of passing "category",...
        #...use an instance of "CategoricalDtype".
df76 = df74["Grades"].astype("category")
print ("Topic 8.3:","\n", df76)  
print("\n")

#Topic 8.4: Applying order to categories

#We can tell Pandas in what order we want the data in case the data is...
#...not ordered, doing the following:
    #Option #1 (Failed Option):
            #IMPORTANT: This code is broke (I do not why). The program...
            #...send me the following answer: 
            #AttributeError: module 'pandas' has no attribute 'CategoricalDtype'
    
    #First: creating a new category with the code "CategoricalDtype"...
    #...which will contain the list of the categories (in order) and the...
    #...the code "ordered = True flag".
    
    #Second: We are going to change the datatype of the interested dataframe...
    #...to the category previously created using the "astype()" function. 

categoriesx = pd.CategoricalDtype(categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'], ordered=True)
df77 = df76["Grades"].astype(categoriesx)
print ("Topic 8.4:","\n", df77)  
print("\n")

    #Option #2 (OK): In this option I use the code "Categorical" described in...
    #...the following lines:
       
    #pd.Categorical(values, categories=None, ordered=None, dtype=None, fastpath=False, copy=True)[source]

        #Represent a categorical variable.
        #Categoricals can only take on only a limited, and usually fixed,...
        #...number of possible values (categories). In contrast to...
        #..."statistical categorical variables", a "Categorical" might have...
        #...an order, but numerical operations (additions, divisions, …)...
        #...are not possible.
        
        #All values of the "Categorical" are either in "categories or np.nan."
        #Assigning values outside of categories will raise a ValueError.
        #Order is defined by the order of the categories, not lexical order..
        #...of the values.

        #Parameters:
            #values: list-like. The values of the categorical. If...
            #...categories are given, values not in categories will be...
            #...replaced with NaN.
        
            #categories: Index-like (unique), optional. The unique...
            #...categories for this "categorical". If not given, the categories...
            #...are assumed to be the unique values of values (sorted,...
            #...if possible, otherwise in the order in which they appear).
            
            #ordered: bool, default False. Whether or not this "categorical"...
            #...is treated as a ordered categorical. If True, the resulting...
            #...categorical will be ordered. An ordered categorical...
            #...respects, when sorted, the order of its categories...
            #...attribute (which in turn is the categories argument, if...
            #...provided).
        
            #dtype: CategoricalDtype. An instance of "CategoricalDtype"...
            #...to use for this categorical.

    
    #First: creating "Categorical" which include the "list of categories"...
    #...the "list of categories in order that we want" and the code...
    #..."ordered = True".
    
    #Second: I will create a dataframe. In this case the dataframe will have...
    #...a column (which will be transformed in a index) and the other column...
    #...will be the categories create with the code "Categorical".
    
    #Third: I check the data type of thee dataframe created in the previous ...
    #..step
    
categoriesx = pd.Categorical(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'], ordered=True)
df78 = pd.DataFrame({"Indice":['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 
                       'ok', 'ok', 'ok', 'poor', 'poor']})
df78["Grades"] = categoriesx
df78 = df78.set_index('Indice')       
df79 = df78.dtypes
print ("Topic 8.5:","\n", df79)  
print("\n")

    #Bonus: Similar to what we do in the Option #2, in this case we work with...
    #...a Serie instead of a Dataframe and we see clearly in the printed...
    #...result the data type, quantity of categories and also the order of...
    #...the categories.

categoriesx2 = pd.Categorical(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'], ordered=True)
df80 = pd.Series(categoriesx2)
print(df80)
df81 = df80.dtypes
print(df81)

#Topic 8.5: Filtering based in the oredered categories.

#Now we can apply a code that allow us to do a filter based in the ordered..
#...categories. 

    #We see that the operator works as we would expect. We can then use a...
    #...certain set of mathematical operators, like minimum, maximum, etc.,..
    #...on the ordinal data.
    
df82 = df78[df78["Grades"]>"C"]
print ("Topic 8.5:","\n", df82)  
print("\n")

#Topic 8.6: represent categorical values #with dummy variables#

#Sometimes it is useful to represent categorical values as each being a..
#...column with a true or a false as to whether the category applies...
#...(this is especially common in feature. extraction, which is a topic in...
#...the data mining course). Variables with a boolean value are typically..
#...called "dummy variables".
    #Pandas function "get_dummies" allow us convert the values of a single..
    #...column into multiple columns of zeros and ones indicating the...
    #...presence of the dummy variable.

#Topic 8.7: Ranges of scale.

#The main concept is that if we have several categories we can create a filter...
#...(in this case a "cut") of the data. Divide the data in several ranges (the...
#...criteria for the "ranges" is established bu the user) or also called bins.

    # Now if we just want to make "bins" of each of these, we can use the...
    #...code "cut()".    
       #There are other methods. For instance, "cut()" gives you interval...
       #...data, where the spacing between each category is equal sized....
       #...But sometimes you want to form categories based on frequency...
       #...– you want the number of items in each bin to the be the same,...
       #...instead of the spacing between bins. 

df83=pd.read_csv("census.csv")
df83=df83[df83['SUMLEV']==50]
df83=df83.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg(np.average)
print ("Topic 8.7.1:","\n", df83)  
print("\n")

    #We will see in the result (after the cut in 10 bins) that states like...
    #..."Alabama" and "Alaska" fall into the same category of , while...
    #..."California" and the disctrict of "Columbia" fall in a very...
    #...different category.

df84 = pd.cut(df83,10)
print ("Topic 8.7.2:","\n", df84)  
print("\n")

#############################################################################

#Topic 9.1: Pivot Tables

import pandas as pd
import numpy as np

df85=pd.read_csv("cwurData.csv")
print ("Topic 9.1:","\n", df85)  
print("\n")

def create_category(ranking):
    if 1 <= ranking <= 100:
        return "First Tier Top Unversity"
    elif 101 <= ranking <= 200:
        return "Second Tier Top Unversity"
    elif 201 <= ranking <= 300:
        return "Third Tier Top Unversity"
    return "Other Top Unversity"

df85['Rank_Level'] = df85['world_rank'].apply(lambda x: create_category(x))

#A "pivot table" use the same concept of a pivot columns in MS Excel...
#...(playing with rows and columns in way that allow us get some insights...
#...of them; i.e. pivot columns {transposing a column to a row position}).

#For instance: Let's say we want to compare "rank level" (which is a column...
#...with several classes in the original dataframe and now in the "pivot...
#...table" are several columns {each represented a class}) versus country...
#...of the universities and we want to compare in terms of overall score.

    #To do this, we tell Pandas we need to apply the code "pivot_table",...
    #...where:
        #values: be the column "score" (values over which we are going to...
        #...apply some math operation).
        #index: be the the column "country"
        #columns: be the column "Rank_Level" {each represented a class}. 
        #Then we specify the aggregation function (math operation to apply...
        #...over the values of column that we put in the parameter "values"),...
        #...and here we'll use the "NumPy mean" to get the average rating...
        #...of "score" for universities in that country.
        
    #We are going to see as an answer that there are some "NaN values", for...
    #...example (Argentina), the "NaN values" indicate that Argentina has...
    #...only observations in one or some of the categories of "Rank_Level".
        
        
df86 = df85.pivot_table(values='score', index='country', columns='Rank_Level', aggfunc=[np.mean])
print ("Topic 9.2:","\n", df86)  
print("\n")

    #To do this, we tell Pandas we need to apply the code "pivot_table",...
    #...where:
        #values: be the column "score" (values over which we are going to...
        #...apply some math operation).
        #index: be the the column "country"
        #columns: be the column "Rank_Level" {each represented a class}. 
        #Then we specify the aggregation function (math operation to apply...
        #...over the values of column that we put in the parameter "values"),...
        #...and here we'll use the "NumPy mean" to get the average rating...
        #...of "score" for universities in that country.
        
    #We are going to see as an answer that there are some "NaN values", for...
    #...example (Argentina), the "NaN values" indicate that Argentina has...
    #...only observations in one or some of the categories of "Rank_Level".
        
        #This is called a "Named Parameter" (i.e. a list of the...
        #...different functions to apply, and pandas will provide us...
        #...with the result using hierarchical column names).  

df87 = df85.pivot_table(values='score', index='country', columns='Rank_Level', aggfunc=[np.mean, np.max])
print ("Topic 9.3:","\n", df87)  
print("\n")

# So now we see we have both the "mean" and the "max" and we want in addition...
#...of what we did previously to...
#...summarize "mean" and the "max" per country applying...
#...the code "margins"...
#...to get "marginal values" of "mean" and the "max":
    #For the "mean" we are going to see a new column with the "overall average...
    #...score per the country"
    #For the "max" we are going to see a new column with the "max score...
    #...per the country"

df88 = df85.pivot_table(values='score', index='country', columns='Rank_Level', aggfunc=[np.mean, np.max], margins=True)

# A pivot table is just a multi-level dataframe, and we can access series or...
#..cells in the dataframe in a similar way as we do so for a regular dataframe. 

    #Now let's look at the index
df89 = df88.index
print ("Topic 9.4:","\n", df89)  
print("\n")

    #And let's look at the columns
        # We can see the columns are "hierarchical". The top level column...
        #...indices have two categories: "mean and max", and the lower...
        #...level column indices have "four categories" ("four rank levels").
df90 = df88.columns
print ("Topic 9.5:","\n", df90)  
print("\n")

    #If we want to get the average scores of "First Tier Top Unversity levels"...
    #...in each country, we just need in this case to make "two dataframe...
    #...projections", the "first" for the "mean", then the "second" for the...
    #..."top tier" (i.e. each dataframe projection is equal to a level of the...
    #...column hierarchy).
        #This code is just a reflex of the "hierarchical arrange" of the...
        #...columns, and as a consequence we use this code as a way to extract..
        #...information from them using "dataframe projections".
        
        # We can see that the output is a series object (i.e. when we...
        #...want a single column of values of a DataFrame...
        #...we will you get a Series) which we can confirm by printing...
        #...the type.
        
df91 = df88['mean']['First Tier Top Unversity']
print ("Topic 9.6:","\n", df91)  
print("\n")
 
df92 = type(df91)
print ("Topic 9.7:","\n", df92)  
print("\n")

    #If we want to find the country that has the "maximum average score" on...
    #..."First Tier Top University level" we use the concept of "dataframe...
    #...projections" and also the code "idxmax".
    
        #The "idxmax()": method that returns a Series with the index of the...
        #...maximum value for each column. By specifying the column axis...
        #...(axis='columns'), the "idxmax()" method returns a Series with...
        #...the index of the maximum value for each row. It is important to...
        #...say that this code is not special for pivot tables.
        
            #Syntax
                #dataframe.idxmax(axis, skipna)
                #axis: Optional (0 or 1 or 'index' or 'columns'), which axis...
                #...to check, default 0.
                #Optional: default True. Specifies whether to skip NULL...
                #...values or not.
df93 = df88['mean']['First Tier Top Unversity'].idxmax()
print ("Topic 9.8:","\n", df93)  
print("\n")
 

#If we want to achieve a different shape of your pivot table, we can do so...
#... with the functions "stack" and "unstack". 
    #Stack: pivot the lowermost column index (i.e. the column index that...
    #...belong to the lower "hierarchical arrange" of the columns {i.e. are...
    #...near to the data}) to become the innermost row index (i.e. the row...
    #...index that in the "hierarchical arrange" of the row index is near...
    #...to the data).
    
    #Unstack: is the inverse of stacking, pivoting the "innermost row index"...
    #...to become the "lowermost column index".

    #Applying "stack", this should move the "lowermost column" ("tiers...
    #...of the university rankings) to the "inner most row".
    
        #This code omit the cells with NaN values.
df94 = df88.copy()
df95 = df94.stack()
print ("Topic 9.9:","\n", df95)  
print("\n")

    #Applying "unstack", this should move the "inner most row" ("tiers...
    #...of the university rankings) stacked in the previous step, to the...
    #..."lowermost column".
df96 = df95.copy()
df97 = df96.unstack()
print ("Topic 9.10:","\n", df97)  
print("\n")

#If we unstacked twice, we end up unstacking all the way to just a...
#....single column, so a series object is returned. This column is just...
#...a "value", the meaning of which is denoted by the heirarachical index...
#...of: "operation", then "rank", and finally "country" (where "country" is...
#...the "inner most row".)
df98 = df96.unstack().unstack()
print ("Topic 9.11:","\n", df98)  
print("\n")

#############################################################################

#Topic 10: Date Functionality

import pandas as pd
import numpy as np

#Pandas has four main time related classes:
    #Timestamp
    #DatetimeIndex
    #Period
    #PeriodIndex.

#Topic 10.1: Timestamp (Instance #1)

#A specific definitions of them are the followings:
    
    #Timestamp:
        #"Timestamp" is the pandas class equivalent of "Python’s Datetime"...
        #...and is interchangeable with it in most cases. 
        
        #It is useful if we want:
            #Set a date (year, month, day, hour,..).
            #Do some math about a specific date (count years, months, days,...
            #...hours,...etc.).
            #Convert information (strings, timezone) to date.
            #Return boolen to confirm or deny if a specific date (year,...
            #...month, day, hour,..).
            
        #Timestamped data: is the most basic type of time series data that...
        #...associates values with points in time. For Pandas objects it...
        #...means using the points in time.
        
#For example, let's create a timestamp using a string 3/6/2022 10:05AM
    #In this case we introduce the data in the following....
    #...order: month, day, year, hour, minutes (using commas)
    #It is important to say that the printed result show us the following....
    #...order: year, month, day.
df99 = pd.Timestamp('3,6,2022 10:05AM')
print ("Topic 10.1.1:","\n", df99)  
print("\n")

    #In this case we introduce the data in the following....
    #...order: month, day, year, hour, minutes (using slashes)
    #It is important to say that the printed result show us the following....
    #...order: year, month, day.
df991 = pd.Timestamp('3/6/2022 10:05AM')
print ("Topic 10.1.1.1:","\n", df991)  
print("\n")

    #In this case we introduce the data in the following....
    #...order: day, month, year, hour, minutes.
    #It is important to say that the printed result show us the following....
    #...order: year, month, day.
df100 = pd.Timestamp('14/9/2002 10:05AM')
print ("Topic 10.1.2:","\n", df100)  
print("\n")

#Topic 10.1: Timestamp (Instance #2)

# We can also create a timestamp by passing multiple parameters such as...
#...year, month, date, hour, minute,... separately, following the order of ...
#...the code:

    #class pandas.Timestamp(ts_input=<object object>, freq=None, tz=None, unit=None, year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None, nanosecond=None, tzinfo=None, *, fold=None)

    #In this case we introduce the data in the following....
    #...order: year, month, day, hour, minute.
    #It is important to say that the printed result show us the following....
    #...order: year, month, day, hour, minute, second.
df101 = pd.Timestamp(2022, 3, 6, 0, 0)
print ("Topic 10.1.3:","\n", df101)  
print("\n")    
  
#Topic 10.1: Timestamp (Instance #3)

# Timestamp also has some useful attributes, such as "isoweekday()" (which...
#...return the day of the week represented by the date of the timestamp).

    #In this case we introduce the data in the following....
    #...order: year, month, day, hour, minute.
                                                                
    ##It is important to say that the printed result show us the number "7".
    #Note that "1" represents "Monday" and "7" represents "Sunday"
df102 = pd.Timestamp(2022, 3, 6, 0, 0).isoweekday()
print ("Topic 10.1.4:","\n", df102)  
print("\n")      

#Topic 10.1: Timestamp (Instance #4)

# You can find extract the specific year, month, day, hour, minute, second..
#...from a timestamp.

    #In this case we introduce the data in the following....
    #...order: year, month, day, hour, minute, second.
                                                                
    ##It is important to say that the printed result show us the number "3".
    #Note that "3" represents the number of the month (that we introduce...
    #...in the timestamp).
df103 = pd.Timestamp(2022, 3, 6, 5, 2,23).month
print ("Topic 10.1.5:","\n", df103)  
print("\n")      

#Topic 10.2: Period (Instance #1)

#A specific definitions of them are the followings:

    #Represents a period of time.
    
    #Suppose we are interested in a specific point in time (i.e....
    #...we want a specific date in the future or in the past). This...
    #...is where the "Period" class comes into play. Period represents a...
    #...specific day or month or year or hour or etc...that we get as a...
    #...result of an arithmetic operation (i.e. we get a date, not a...
    #...span of time).

#Here we are creating or set a specific period of time:
    #The key here is that the period object encapsulates the granularity...
    #... of time (i.e. we can only "year" or "year/month" or "year/month/day...
    #...and so on) for arithmetic.
    
# We can create a period by passing multiple parameters such as...
#...year, month, date, hour, minute,... separately, following the order of ...
#...the code:
    
    #class pandas.Period(value=None, freq=None, ordinal=None, year=None, month=None, quarter=None, day=None, hour=None, minute=None, second=None)
                                                                
    #It is important to say that the printed result show us the specific....
    #...date Period date created.

df104 = pd.Period('2022/3')
print ("Topic 10.2.1:","\n", df104)  
print("\n")

df105 = pd.Period('2022/3/6')
print ("Topic 10.2.2:","\n", df105)  
print("\n")  

    #Then after establish a specific date Period we can get a timespan...
    #...according wth the arithmetic that we specify. For instance: if we...
    #...want to find out 5 months after March 2022, we simply plus "5".
    
    #It is important to say that the printed result show us the specific....
    #...date Period date created through arithmetic.
df106 = pd.Period('2022/3') + 5
print ("Topic 10.2.3:","\n", df106)  
print("\n") 

    #Then after establish a specific date Period we can get a timespan...
    #...accorrding wth the arithmetic that we specify. For instance: if we...
    #...want to find out 7 days before March 6 of 2022, we simply subtract "7".
    
    #It is important to say that the printed result show us the specific....
    #...date Period date created through arithmetic.
df107 = pd.Period('2022/3/6') - 7
print ("Topic 10.2.4:","\n", df107)  
print("\n") 

#Topic 10.3: DatetimeIndex and PeriodIndex (Instance #1)

#A specific definitions of them are the followings:

#PeriodIndex

    #It is just an index, but for Period.
    
    #Immutable ndarray holding ordinal values indicating regular periods...
    #...in time. 
    #Index keys are boxed to Period objects which carries the metadata...
    #...(eg, frequency information).
        #Apparently, it is important the use of square brackets for the...
        #...Period.
        
#DatetimeIndex

    #It is just an index, but for Timestamp.
    
    #Immutable ndarray-like of datetime64 data.
    #Represented internally as int64, and which can be boxed to Timestamp...
    #...objects that are subclasses of datetime and carry metadata.
        #Apparently, it is important the use of square brackets for the...
        #...Timestamp.
    
#For instance: 

    #In this case we create a "series"...
    #..., we'll use the Timestamp of September 1st, 2nd and 3rd of 2016. 
                                                                
    #It is important to say that the printed result show us a "Timestamp"..
    #...as index and has a value associated with it, in this case, "a, b and c".

df108 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
print ("Topic 10.3.1:","\n", df108)  
print("\n") 

    # Looking at the type of our series index, we see that it's "DatetimeIndex".
df109 = type(df108.index)
print ("Topic 10.3.2:","\n", df109)  
print("\n") 

#For instance: 

    #In this case we create a "series"...
    #..., we'll use the Timestamp of September, October and November of 2016. 
                                                                
    #It is important to say that the printed result show us a "Period"..
    #...as index and has a value associated with it, in this case, "e, d and f".

df110 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'), pd.Period('2016-11')])
print ("Topic 10.3.3:","\n", df110)  
print("\n") 

    # Looking at the type of our series index, we see that it's "PeriodIndex".
df111 = type(df110.index)
print ("Topic 10.3.4:","\n", df111)  
print("\n") 

#Topic 10.4: Converting to Datetime (Instance #1)

#A specific definition is:
    
    #Convert argument to datetime. This function converts a scalar,...
    #...array-like, Series or DataFrame/dict-like to a pandas datetime object.
    
    #The syntax is: 
        #pandas.to_datetime(arg, errors='raise', dayfirst=False, yearfirst=False, utc=None, format=None, exact=True, unit=None, infer_datetime_format=False, origin='unix', cache=True)[source]
        
        #Some of the Parameters are:
            #arg: int, float, str, datetime, list, tuple, 1-d array, Series,...
            #...DataFrame/dict-like. If a DataFrame is provided, the...
            #...method expects minimally the following columns: "year",...
            #..."month", "day".
            
            #dayfirst: bool (default False). Specify a date parse order if...
            #...arg is str or is list-like. If True, parses dates with the...
            #...day first, e.g. "10/11/12" is parsed as 2012-11-10.
            
                #dayfirst = True is not strict, but will prefer to parse...
                #...with day first. If a delimited date string cannot be...
                #...parsed in accordance with the given dayfirst option,...
                #...e.g. to_datetime(['31-12-2021']), then a warning will...
                #...be shown.
                
df112 ='2 June 2013'
df113 = pd.to_datetime(df112)
print ("Topic 10.4.1:","\n", df113)  
print("\n") 

#Topic 10.4: Converting to Datetime (Instance #2)

#Suppose we have a list of dates (in this case trying a bunch of...
#...different date formats) as strings and we want to transform them with...
#...the pandas code "to_datetime".

    #First, we create the list with the dates.
df114 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
print ("Topic 10.4.2:","\n", df114)  
print("\n") 

    #Second: some random data is put it together in the dataframe ...
    #...with the date (in this case the dates are the index of the dataframe).
    
    #A way to generate random integers in Pandas DataFrame under "Multiple...
    #...DataFrame columns".
        #Syntax:
            #np.random.randint(lowest integer, highest integer, size=(number of random integers per column, number of columns))
            
            #In this case:
                #lowest integer = 10
                #highest integer = 100
                #number of random integers per column= 4 (because there are...
                #...four rows).
                #number of columns = 2 
                            
df115 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=df114, columns=list('ab'))
print ("Topic 10.4.3:","\n", df115)  
print("\n") 

    #Third: using pandas "to_datetime", Pandas will convert these dates (in...
    #...different date formats) to "Datetime" and put them in a standard format...
    #...(year-month-day hour:minute:second)
df115.index = pd.to_datetime(df115.index)

#Topic 10.4: Converting to Datetime (Instance #3)

#"to_datetime also()" has options to change the date parse order. For...
#...example, we can pass in the argument "dayfirst = True" to parse the...
#...date in European date (i.e. if in our input we put the format...
#..."day.month.year, we are going to get as an answer the date in format....
#...year-month-day hour:minute:second).

df116 = pd.to_datetime('4.7.12', dayfirst=True)
print ("Topic 10.4.4:","\n", df116)  
print("\n")

df117 = pd.to_datetime('2 June 2013', dayfirst=True)
print ("Topic 10.4.5:","\n", df117)  
print("\n")

#Topic 10.5: Timedelta (Instance #1)

#A specific definition is:
    
    #Use the code "Timestamp".
    
    #Timedeltas: are differences in times (i.e. a duration or span of time)...
    #...This is not the same as a period but conceptually similar, because...
    #...with the "Timedeltas" concept we do not get a specific data of the...
    #...present or future, but duration or span of time.
    
#For instance, if we want to take the difference between September 3rd and...
#... September 1st, we get Timedelta result of two days zero hours, minutes..
#...and seconds.
df118 = pd.Timestamp('9/3/2016') - pd.Timestamp('9/1/2016')
print ("Topic 10.5.1:","\n", df118)  
print("\n")

#For instance, if we want to find what the date and time lapsed is for...
#...12 days and 3 hours past September 2nd, at 8:10 AM.
df119 = pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H')
print ("Topic 10.5.2:","\n", df119)  
print("\n")

#Topic 10.6: Offset (Instance #1)

#A specific definition is:
    
    #Use the code "Timestamp".

    #"Offset" follows specific calendar...
    #...duration rules. "Offset" allows flexibility in terms of types of...
    #...time intervals. Besides hour, day, week, month, etc. it also has..
    #...business day, end of month, semi month begin etc.
    
    #We get as a result a specific date and not a span or duration of time.

#Let's create a timestamp, and see:
    #It is important to say that the printed result show us the number "6".
    #Note that "1" represents "Monday" and "7" represents "Sunday".
        #Although this code "weekday()" is useless.
df120 = pd.Timestamp('9/4/2016').weekday()
print ("Topic 10.6.1:","\n", df120)  
print("\n")

#Now we can now add the timestamp with a week ahead
    #In essence we add seven days with the code "pd.offsets.Week()" to the...
    #...original date.
df121 = pd.Timestamp('9/4/2016') + pd.offsets.Week()
print ("Topic 10.6.2:","\n", df121)  
print("\n")

#Now let's try to do the month end, then we would have the last day of Septemer
    #In essence we reach the last day of the month with the code...
    #..."pd.offsets.MonthEnd()" based in the month of original date (no matter...
    #...the year, day, hour, minutes or seconds of our  original date).
df122 = pd.Timestamp('9/1/2016') + pd.offsets.MonthEnd()
print ("Topic 10.6.2:","\n", df122)  
print("\n")

#Topic 10.7: Working with Dates in a Dataframe (Instance #1)

#A specific definition of the code "date_range" is:

    #Return a fixed frequency "DatetimeIndex" of "timestamps" (i.e. an index...
    #...of specific dates).
        
    #Returns the range of equally spaced time points (where the difference...
    #...between any two adjacent points is specified by the given frequency)...
    #...such that they all satisfy start <[=] x <[=] end. The first and...
    #...last time points in that range that fall on the boundary of freq ...
    #...(if given as a frequency string). If exactly one of start, end,...
    #...or freq is not specified, this missing parameter can be computed...
    #...given periods, the number of timesteps in the range.
    
    #We have to either specify the start or end date (if it is...
    #...not explicitly specified, by default, the date is considered the start..
    #...date. Then we have to specify number of periods, and a frequency. 

#Suppose we want to look at 9 measurements, taken bi-weekly (i.e. every two...
#...weeks), every Sunday, starting in 27 March 2022. We use the code...
#..."date_range".

    #Syntax:
    #pandas.date_range(start=None, end=None, periods=None, freq=None, tz=None, normalize=False, name=None, closed=NoDefault.no_default, inclusive=None, **kwargs)
    
    #Some Parameters are:
        #start: str or datetime-like, optional. Left bound for generating dates.
        #end: str or datetime-like, optional. Right bound for generating dates.
        #periods: int, optional. Number of periods to generate.
        #freq: str or DateOffset, default ‘D’. Frequency strings can have...
        #...multiples, e.g. ‘5H’. See below a list of frequency aliases.
        
            #Some "Offset aliases":
                #A number of string aliases are given to useful common time...
                #...series frequencies. We will refer to these aliases as...
                #...offset aliases.
                #B: business day frequency
                #C: custom business day frequency
                #D: calendar day frequency
                #W: weekly frequency
                #M: month end frequency
                #QS: quarter start frequency
                
            #Some "Anchored offsets":
                #For some frequencies you can specify an anchoring suffix:
                #W-SUN: weekly frequency (Sundays). Same as "W"
                #W-MON: weekly frequency (Mondays)
                #W-TUE: weekly frequency (Tuesdays)
                #W-WED: weekly frequency (Wednesdays)
                #W-THU: weekly frequency (Thursdays)
                #W-FRI: weekly frequency (Fridays)
                #W-SAT: weekly frequency (Saturdays)    

df123 = pd.date_range('26-03-2022', periods=9, freq='2W-SUN')
print ("Topic 10.7.1:","\n", df123)  
print("\n")

#Topic 10.7: Working with Dates in a Dataframe (Instance #2)

#Suppose we want to look at 9 measurements, taken bi-weekly (i.e. every two...
#...weeks), every Saturday, starting in 27 March 2022. We use the code...
#..."date_range".

    #In this case the "start_date" (sunday 27-03-2022) does not correspond...
    #...to the frequency ('2W-SAT'); therefore the returned "timestamps"...
    #...will start at the next valid "timestamp", in this case the next...
    #...saturday (saturday 2022-04-02).

    #When using the offset aliases above, it should be noted...
    #...that functions such as "date_range()", will only return...
    #...timestamps that are in the interval defined by "start_date"...
    #...and "end_date". If the "start_date" does not correspond to...
    #....the frequency, the returned "timestamps" will start at...
    #...the next valid "timestamp", same for "end_date", the..
    #...returned timestamps will stop at the previous valid timestamp. 

df124 = pd.date_range('27-03-2022', periods=9, freq='2W-SAT')
print ("Topic 10.7.2:","\n", df124)  
print("\n")

#Topic 10.7: Working with Dates in a Dataframe (Instance #3)

#Suppose we want to look at 9 measurements, taken every business day,...
#...starting in 27 March 2022. We use the cod "date_range".
df125 = pd.date_range('27-03-2022', periods=9, freq='B')
print ("Topic 10.7.3:","\n", df125)  
print("\n")

#Topic 10.7: Working with Dates in a Dataframe (Instance #4)

#Suppose we want to look at 12 measurements, taken quarterly (i.e. every 3...
#...months), starting in 27 March 2022. We use the cod "date_range".
df126 = pd.date_range('27-03-2022', periods=12, freq='QS-JUN')
print ("Topic 10.7.4:","\n", df126)  
print("\n")

#Topic 10.7: Working with Dates in a Dataframe (Instance #5)

#Suppose we want to look at 9 measurements, taken bi-weekly (i.e. every two...
#...weeks), every Sunday, starting in 27 March 2022. We use the code...
#..."date_range".

    #This time I create a DataFrame using the dates (in this case, the...
    #...dates are assigned as index of the dataframe) The dataframe columns...
    #...have some random data.

datesx = pd.date_range('27-03-2022', periods=9, freq='2W-SUN')
df127 = pd.DataFrame({'Count 1': 100 + np.random.randint(-5, 10, 9).cumsum(),
                  'Count 2': 120 + np.random.randint(-5, 10, 9)}, index=datesx)
print ("Topic 10.7.5:","\n", df127)  
print("\n")

    #Option #1: We even can check what day of the week a specific date is.....
    #...In the following answer we can see that all the dates in our index...
    #...are on a Sunday (which matches the frequency that we set).
    
    #This method is available on both Series with datetime values or..
    #...DatetimeIndex.
df128 = df127.index.weekday_name
print ("Topic 10.7.6:","\n", df128)  
print("\n")
    
    #Option #2: We even can check what day of the week a specific date is.....
    #...In the following answer we can see that all the dates in our index...
    #...are on a 6 (which matches the frequency that we set, i.e. Sunday).
    
    #The day of the week with Monday=0 through Sunday=6. This method is...
    #...available on both Series with datetime values or DatetimeIndex.
df129 = df127.index.weekday
print ("Topic 10.7.7:","\n", df129)  
print("\n")
    
    #We can also use "diff()" to find the difference between each data value...
    #...In this case the difference between the previous and actual row.
    
    #diff(): Calculates the difference of a Dataframe element compared...
    #...with another element in the Dataframe (default is element in...
    #...previous row).
                     
    #Syntax
        #DataFrame.diff(periods=1, axis=0)
        
        #Parameters
            #periods: int (default 1). Periods to shift for calculating...
            #...difference, accepts negative values.
            #axis: {0 or ‘index’, 1 or ‘columns’}, default 0. Take...
            #...difference over rows (0) or columns (1).
df130 = df127.diff(periods=1, axis=0)
print ("Topic 10.7.8:","\n", df130)  
print("\n")
    
    #Suppose we want to know the mean count (of our columns of data) for..
    #...each month in our DataFrame:
    #...We can do this using the function "resample". Converting data (which...
    #...index are dates) from a higher frequency from a lower frequency (i.e...
    #...we are taking our multiples lines of data and reduce it to just a few...
    #...lines of data considering a specific span of time) is called...
    #..."downsampling".
    
        #In this case our downsampling is monthly (i.e. that we are going...
        #...to get a mean value per month: March, April, May, June and July).
    
    #Convenience method for frequency conversion and resampling of time...
    #...series. The object must have a datetime-like index (DatetimeIndex,...
    #...PeriodIndex, or TimedeltaIndex), or the caller must pass the label...
    #...of a datetime-like series/index to the on/level keyword parameter.

    #Syntax      
        #DataFrame.resample(rule, axis=0, closed=None, label=None, convention='start', kind=None, loffset=None, base=None, on=None, level=None, origin='start_day', offset=None)

    #Some of the Parameters are:
        #axis ({0 or ‘index’, 1 or ‘columns’}, default 0): Which axis to use...
        #...for up or down-sampling. For Series this will default to 0, ...
        #....i.e. along the rows. Must be DatetimeIndex, TimedeltaIndex or...
        #...PeriodIndex..
        #closed ({‘right’, ‘left’}, default None): Which side of bin...
        #...interval is closed. The default is ‘left’ for all frequency...
        #...offsets except for ‘M’, ‘A’, ‘Q’, ‘BM’, ‘BA’, ‘BQ’, and ‘W’ which...
        #...all have a default of ‘right’.
        #label ({‘right’, ‘left’}, default None): Which bin edge label to...
        #...label bucket with. The default is ‘left’ for all frequency...
        #...offsets except for ‘M’, ‘A’, ‘Q’, ‘BM’, ‘BA’, ‘BQ’, and ‘W’...
        #...which all have a default of ‘right’.
df131 = df127.copy()
df132 = df131.resample('M').mean() 
print ("Topic 10.7.9:","\n", df132)  
print("\n")  
    
    #Datetime indexing and slicing. It is very useful it we want only a...
    #...portion of the dataframe according to the dates.
        #For instance, we can use partial string indexing to find values...
        #...from a particular year (in this case 2022).
df133 = df127['2022']
print ("Topic 10.7.10:","\n", df133)  
print("\n")   
    
        #For instance, we can use partial string indexing to find values...
        #...from a particular month (in this case April 2022 only).
df134 = df127['2022-4']
print ("Topic 10.7.11:","\n", df134)  
print("\n") 

        #For instance, we can even slice on a range of dates For example,...
        #...from a particular month (in this case June 2022 onwards).
df135 = df127['2022-6':]
print ("Topic 10.7.12:","\n", df135)  
print("\n") 

##############################################################################

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 
    
#Quiz 3 - March 28, 2021 (RMDLC)

#QUIZ #3  

import pandas as pd
import numpy as np

#Problem #1 <--WINNER 
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])    
staff_df = staff_df.set_index('Name')

studentspluscharge= pd.merge(student_df, staff_df, how='left', left_index=True, right_index=True)
print ("Topic Q3.1:","\n", studentspluscharge)  
print("\n")

#Problem #2 <--WINNER
#Axis: 0 for rows and 1 for columns.
X = 0
Y = 1
result_df = studentspluscharge.drop("School",axis=1)
print ("Topic Q3.2:","\n", result_df)  

#Problem #3 <--WINNER
#It is important the code "ordered=True" in the categories.
my_categories = pd.CategoricalDtype(categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'], ordered=True)

#Problem #4 <--WINNER
#It is important the code "margins=True", because showed us at the end...
#...of thee pivot table a resume column that have the median values...
#...of all the median values per country (i.e. per row).
df.pivot_table(values='score', index='country', columns='Rank_Level', aggfunc=[np.median], margins=True)

#Problem #5 <--WINNER
#We just move from 11/29/2019 (4th day of the week) to the end of november...
#...11/30/2019 (5th day of the week)

#Problem #6 <--WINNER
#Because we want to create "groups" based on the column "group_key" in...
#...the DataFrame
df.groupby(group_key).aggregate(filling_mean)

#Problem #7 <--WINNER
#What matter is the dataframe of students; therefore I choose the option...
#..."right (position)".
result_df = pd.merge(staff_df, student_df, how='right', on=['First Name', 'Last Name'])

#Problem #8 <--WINNER
#It is important the "groupby column", then the functions...
#..."np.nanmean, np.nanstd" that compute the "mean" and "standard deviation"
#...ignoring the presence of "NaN values".
df.groupby('review_scores_value').agg({'name': len, 'reviews_per_month': (np.nanmean, np.nanstd)})

#Problem #9 <--WINNER
#I add 5 months to the original date (January 12 2019)
DateFuture = pd.Period('01/12/2019', 'M') + 5
print(DateFuture)

#Problem #10 <--WINNER
#I do not group by the content of the columns.
df.groupby('vegetable')

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#Assignment 3 - September 16, 2020 (RMDLC)

import pandas as pd
import numpy as np
import re

#1.0.1 Question 1 <--WINNER (Option without function)

#Story:

#First: Load the energy data from the ﬁle Energy Indicators.xls, which is...
#...a list of indicators of energy supply and renewable electricity...
#...production from the United Nations for the year 2013, and should be put...
#...into a DataFrame with the variable name of energy. Keep in mind that...
#...this is an Excel ﬁle, and not a comma separated values ﬁle. Also,...
#...make sure to exclude the footer and header information from...
#...the dataﬁle.

#Second: The ﬁrst two columns are unneccessary, so you should get...
#...rid of them, and you should change the column labels so that the columns...
#...are: [ ’ Country ’ , ’ Energy Supply ’ , ’ Energy Supply per Capita ’ ,...
#...’ % Renewable ’ ].

#Third: Convert Energy Supply to gigajoules (there are 1,000,000 gigajoules..
#...in a petajoule). 

#Fourth: For all countries which have missing data (e.g. data with "...")...
#...make sure this is reﬂected as np.NaN values.

#Fifth: Rename the following list of countries (for use in later questions):...
#..."Republic of Korea": "South Korea", "United States of America":...
#..."United States", "United Kingdom of Great Britain and Northern Ireland":..
#..."United Kingdom", "China, Hong Kong Special Administrative Region":...
#..."Hong Kong".

#Sixth: There are also several countries with numbers and/or parenthesis...
#...in their name. Be sure to remove these, e.g.’ Bolivia (Plurinational...
#...State of) ’ should be ’ Bolivia ’ ,’ Switzerland17 ’ should be...
#...’ Switzerland ’ .

#First:
#I read the file MS Excel File (xls format), then I skip (delete) certain...
#...number of rows with the code "skiprows" (header; in this case the first...
#...17 rows of the file) and also skip (delete) certain number of rows with...
#...the code "skipfooter" (footer; in this case the last 38 rows of the file).

   #Extremely Important: some MS Excel files can be in (xls format) or in...
   #...(xlsx format), which depends on the version of MS Excel file.
   
   #Extremely Important: the header can affect the opening of the file and as...
   #...consequence it is highly likely that we are going to get an error...
   #...message if we do no control this situation.

energy = pd.read_excel("Energy Indicators.xls", skiprows = 17, skipfooter= 38)
print(energy)
print("\n") 

#Second:
#I drop the first two columns (useless) of my dataframe an establish in the...
#...code that those changes be reflected in the actual dataframe.

#Then, I changed the name of all the columns.
energy.drop(["Unnamed: 0","Unnamed: 1"], inplace=True, axis=1)

energy = energy.rename(columns={'Unnamed: 2':'Country',
                                 "Petajoules":"Energy Supply",
                                 "Gigajoules":"Energy Supply per Capita",
                                 "%":"% Renewable"})
print (energy)  
print("\n")       

#Fourth: For all countries which have missing data (e.g. data with "...")...
#...I changed those cells to "np.nan" values.
    #Although is a Numpy code, it can be used in the Panda environment.
    #"NaN" is short for "Not a number". It is used to represent entries...
    #...that are undefined or missing values in a dataset.
    #The concept of NaN existed even before Python was created. 
    #"NaN" is a special floating-point value which cannot be converted to...
    #...any other type than float.
    
    #The Option #1 
        #The Main advantage is that it does not care about in what part...
        #...(specific index) of a certain column of the dataframe is...
        #...located the data that we want to fix or change. 
        #The main disvantage is that we need to know very well the text....
        #...that we want to change.
    #The Option #2 
        #The Main advantage is that we do not need to know very well the text...
        #...that we want to change. 
        #The main disvantage is that we need to know very well in what part...
        #...(specific index) of a certain column of the dataframe is...
        #...located the data that we want to fix or change. 
        
#Option #1 (selected option)
energy = energy.replace(['...'],np.nan)
print (energy)  
print("\n")    

#Option #2
energy.loc[[3,86,150,210,217], ["Energy Supply","Energy Supply per Capita"]] = np.nan
print (energy)  
print("\n")      

#Fifth: I rename some countries using te Option #1 (selected option) and..
#...Option#2
    #The Option #1 
        #The Main advantage is that it does not care about in what part...
        #...(specific index) of a certain column of the dataframe is...
        #...located the data that we want to fix or change. 
        #The main disvantage is that we need to know very well the text....
        #...that we want to change.
    #The Option #2 
        #The Main advantage is that we do not need to know very well the text...
        #...that we want to change. 
        #The main disvantage is that we need to know very well in what part...
        #...(specific index) of a certain column of the dataframe is...
        #...located the data that we want to fix or change. 
        
#Option #1 (selected option)
energy['Country']= energy['Country'].replace(['China, Hong Kong Special Administrative Region3',
                                              "Republic of Korea",
                                              "United Kingdom of Great Britain and Northern Ireland19",
                                              "United States of America20"],
                                             ['Hong Kong',
                                              "South Korea",
                                              "United Kingdom",
                                              "United States"])
print (energy)  
print("\n") 

#Option #2
energy.loc[43, "Country"] = "Hong Kong"
energy.loc[164, "Country"] = "South Korea"
energy.loc[214, "Country"] = "United Kingdom"
energy.loc[216, "Country"] = "United States"
print (energy)  
print("\n")      

#Sixth: 
#There are also several countries with numbers and/or parenthesis...
#...in their name. Be sure to remove these, e.g.’ Bolivia (Plurinational...
#...State of) ’ should be ’ Bolivia ’ ,’ Switzerland17 ’ should be...
#...’ Switzerland ’.

#As we do previously we use the code "Replace". 
    
    #With "Replace" code the values of the DataFrame are replaced with other..
    #...values dynamically.

    #"Replace" code differs from updating with "loc" or "iloc", which...
    #...require you to specify a location to update with some value.

    #Syntax:
        #DataFrame.replace(to_replace=None, value=NoDefault.no_default, inplace=False, limit=None, regex=False, method=NoDefault.no_default)[source]

#Option #1 (selected option)

    #Step #1:
        
    #This option is not time consuming and is very convenient if we think in...
    #...large datasets. The main notion of the "Option #1" is the use of..
    #..."Regex"

    #In this case we use the Metacharacter "Square brackets" []. To be...
    #...specific [0-9] matches any single decimal digit character (any...
    #:..character between '0' and '9', inclusive). 
    
    #Due to the fact that "Replace" only accept in the parameter...
    #..."to_replace=None" values like: "str, regex, list, dict, Series, int,..
    #...float, or None" we use in our following code only the column of...
    #...interest (i.e. this is our "Serie")

energy["Country2"] = energy['Country']
energy['Country2']= energy['Country'].replace('([0-9])','',regex=True)
print (energy) 
print("\n")   

    #Step #2:

        #We used "\w" if we want to find any alphanumeric word character...
        #...(a word characters are uppercase and lowercase letters, digits,...
        #...and the underscore (_) character. 
        
        #In this case we use The code"[\w ]*" try to match any quantity...
        #...of characters and spaces.
        
        #If we want to find literally in a string a piece of parentheses...
        #...character, we can place the piece of parentheses as first or...
        #...last character or with a backslash "\".

        #It is important to say that the metacharacter "\" espaces a...
        #...metacharacter of its special meaning.

energy["Country3"] = energy['Country2']
energy['Country3']= energy['Country2'].replace('\([\w ]*\)','',regex=True)
print (energy) 
print("\n")   

    #Step #3:
    
    #Choosing the columns that we want to see in the datframe.
energy = energy[['Country3',"Energy Supply","Energy Supply per Capita","% Renewable"]]
print (energy) 
print("\n")   

    #Step #4:
    
    #Renaming the column "Country3" to "Country3" in the datframe.
energy = energy.rename(columns={'Country3':'Country'})
print (energy)  
print("\n")  


#Option #2
    #This option is time consuming and intractable if we think in large datasets.
energy['Country']= energy['Country'].replace(['Australia1',
                                              "Bolivia (Plurinational State of)",
                                              "China2",
                                              "China, Macao Special Administrative Region4",
                                              'Denmark5',
                                              "Falkland Islands (Malvinas)",
                                              "France6",
                                              "Greenland7",
                                              'Indonesia8',
                                              "Iran (Islamic Republic of)",
                                              "Italy9",
                                              "Japan10",
                                              'Micronesia (Federated States of)',
                                              "Netherlands12",
                                              "Portugal13",
                                              "Saudi Arabia14",
                                              "Serbia15",
                                              "Sint Maarten (Dutch part)",
                                              "Spain16",
                                              'Switzerland17',
                                              "Ukraine18",
                                              "Venezuela (Bolivarian Republic of)"],
                                             ['Australia',
                                              "Bolivia",
                                              "China",
                                              "China, Macao Special Administrative Region",
                                              'Denmark',
                                              "Falkland Islands",
                                              "France",
                                              "Greenland",
                                              'Indonesia',
                                              "Iran",
                                              "Italy",
                                              "Japan",
                                              'Micronesia',
                                              "Netherlands",
                                              "Portugal",
                                              "Saudi Arabia",
                                              "Serbia",
                                              "Sint Maarten",
                                              "Spain",
                                              'Switzerland',
                                              "Ukraine",
                                              "Venezuela"])

print (energy)  
print("\n")      

#Third: 
#I Convert the values of thee column "Energy Supply" to gigajoules (there...
#...are 1,000,000 gigajoules in a petajoule).
energy["Energy Supply"] = (energy["Energy Supply"])*1000000
print (energy)  
print("\n")     

#1.0.1 Question 1 (Part 2)

#Seventh: Next, load the GDP data from the ﬁle world_bank.csv, which is a...
#...csv containing countries’ GDP from 1960 to 2015 from World Bank. Call...
#...this DataFrame GDP.

    ##I read the file MS Excel File (csv format), then I skip (delete)...
    #...certain number of rows with the code "skiprows" (header; in this...
    #...case the first 4 rows of the file).
    
    #The only way to avoid problems with this file (to be specific: "Error...
    #...tokenizing data") is deleting the first 3 rows of the file.
    
   #Extremely Important: the header can affect the opening of the file and as...
   #...consequence it is highly likely that we are going to get an error...
   #...message if we do no control this situation.

#Option #1 (option runned)
Gdp = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_1345540.csv',skiprows = 3)
print(Gdp)
print("\n") 

#Option #2 (selected option)
    #The only difference with the Option #1 is the we use tha dataframe name...
    #...GDP as the assignment request.
GDP = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_1345540.csv',skiprows = 3)
print(GDP)
print("\n") 

#Eigth: Make sure to skip the header, and rename the following list of...
#...countries: "Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran",...
#..."Hong Kong SAR, China": "Hong Kong"

#Option #1 (option runned)
Gdp['Country Name']= Gdp['Country Name'].replace(['Korea, Rep.',
                                              "Iran, Islamic Rep.",
                                              "Hong Kong SAR, China"],
                                             ["South Korea",
                                              "Iran",
                                              "Hong Kong"])
print (Gdp)  
print("\n") 

#Option #2 (selected option)
    #The only difference with the Option #1 is the we use tha dataframe name...
    #...GDP as the assignment request.
GDP['Country Name']= GDP['Country Name'].replace(['Korea, Rep.',
                                              "Iran, Islamic Rep.",
                                              "Hong Kong SAR, China"],
                                             ["South Korea",
                                              "Iran",
                                              "Hong Kong"])
print (GDP)  
print("\n") 

#1.0.1 Question 1 (Part 3)

#Ninth: Finally, load the Sciamgo Journal and Country Rank data for...
#....Energy Engineering and Power Technology from the ﬁle scimagojr-3.xlsx,...
#...which ranks countries based on their journal contributions in the...
#...aforementioned area. Call this DataFrame ScimEn.

#I read the file MS Excel File (xlsx format).

   #Extremely Important: some MS Excel files can be in (xls format) or in...
   #...(xlsx format), which depends on the version of MS Excel file.
ScimEn = pd.read_excel("scimagojr country rank 1996-2019.xlsx")
print(ScimEn)
print("\n") 

#1.0.1 Question 1 (Part 4)

#Tenth: Join the three datasets: GDP, Energy, and ScimEn into a new dataset...
#...(using the intersection of country names). Use only the last 10 years...
#...(2006-2015) of GDP data and only the top 15 countries by Scimagojr...
#...’Rank’ (Rank 1 through 15).

#IDEAS:
    #Do i need to set the country name as a index before the joining?
    #Do i need to apply some order (top 15) before the joining?
    #I think that I cannot mix 3 dataframes at the same time.
    #Join first "Sciem" and "energy" (because they have the same name for..
    #...the column "Country") meanwhile "Gdp" has the name "Country Name"...
    #...Does it affect?
    #Do the joining considering aas main paramente the "Sciem" rank (top 15).

    #Step 1: Setting the "countries" as the index of every dataframe
ScimEn = ScimEn.set_index('Country')           

energy = energy.set_index('Country')     

Gdp = Gdp.set_index('Country Name')     
           
    #Step 2: Do the merging of the dataframes ("Sciem" and "energy"), taking...
    #...as a main guide the dataframe of "Sciem".
DataMerge1= pd.merge(ScimEn, energy, how='left', left_index=True, right_index=True)
print(DataMerge1)
print("\n")         

    #Step 3: Do the merging of the dataframe generated in the "Step 2",...
    #...with the dataframe "Gdp".
DataMerge2= pd.merge(DataMerge1, Gdp, how='left', left_index=True, right_index=True)
print(DataMerge2)
print("\n")             
                 
    #Step 4: Adjusting the dataframe using only the last 10 years...
    #...(2006-2015) of GDP data and only the top 15 countries by Scimagojr...
    #...’Rank’ (Rank 1 through 15).
DataMerge2 = DataMerge2.head(15)                        
print (DataMerge2)  
print("\n")                                            

DataMerge2.drop(['1960',
                 "1961",
                 "1962",
                 "1963",
                 "1964",
                 "1965",
                 "1966",
                 "1967",
                 "1968",
                 "1969",
                 "1970",
                 "1971",
                 "1972",
                 "1973",
                 "1974",
                 "1975",
                 "1976",
                 "1977",
                 "1978",
                 "1979",
                 "1980",
                 "1981",
                 "1982",
                 "1983",
                 "1984",
                 "1985",
                 "1986",
                 "1987",
                 "1988",
                 "1989",
                 "1990",
                 "1991",
                 "1992",
                 "1993",
                 "1994",
                 "1995",
                 "1996",
                 "1997",
                 "1998",
                 "1999",
                 "2000",
                 "2001",
                 "2002",
                 "2003",
                 "2004",
                 "2005",
                 "2017",
                 "2018",
                 "2019",], inplace=True, axis=1)                                                   
print (DataMerge2)  
print("\n")                                                                       
                                                                    
#Eleventh: The index of this DataFrame should be the name of the country,...
#...and the columns should be [’Rank’, ’Documents’, ’Citable documents’,...
#...’Citations’, ’Self-citations’, ’Citations per document’, ’H index’,...
#... ’Energy Supply’, ’Energy Supply per Capita’, ’% Renewable’, ’2006’,...
#...’2007’, ’2008’, ’2009’, ’2010’, ’2011’, ’2012’, ’2013’, ’2014’, ’2015’].

#This function should return a DataFrame with 20 columns and 15 entries.

    #Base in which indications request I proceed to drop the following...
    #...colums: Delete: Region, Country Code, Indicator Name, Indicator Code,...
    #...2016, Unnamed: 64
DataMerge2.drop(['Region',
                 "Country Code",
                 "Indicator Name",
                 "Indicator Code",
                 "2016",
                 "Unnamed: 64",], inplace=True, axis=1)                                                   
print (DataMerge2)  
print("\n")      

#1.0.1 Question 1 <--WINNER (Option with function)

import pandas as pd
import numpy as np
import re

def answer_one():
    #First:
    energy = pd.read_excel("Energy Indicators.xls", skiprows = 17, skipfooter= 38)
    #Second:
    energy.drop(["Unnamed: 0","Unnamed: 1"], inplace=True, axis=1)
    energy = energy.rename(columns={'Unnamed: 2':'Country',
                                 "Petajoules":"Energy Supply",
                                 "Gigajoules":"Energy Supply per Capita",
                                 "%":"% Renewable"})
    #Fourth: 
    energy = energy.replace(['...'],np.nan)
    #Fifth: 
    energy['Country']= energy['Country'].replace(['China, Hong Kong Special Administrative Region3',
                                              "Republic of Korea",
                                              "United Kingdom of Great Britain and Northern Ireland19",
                                              "United States of America20"],
                                             ['Hong Kong',
                                              "South Korea",
                                              "United Kingdom",
                                              "United States"])
    #Sixth: 
    energy["Country2"] = energy['Country']
    energy['Country2']= energy['Country'].replace('([0-9])','',regex=True)
    energy["Country3"] = energy['Country2']
    energy['Country3']= energy['Country2'].replace('\([\w ]*\)','',regex=True)
    energy = energy[['Country3',"Energy Supply","Energy Supply per Capita","% Renewable"]]
    energy = energy.rename(columns={'Country3':'Country'})
    #Third: 
    energy["Energy Supply"] = (energy["Energy Supply"])*1000000
    #Seventh:
    Gdp = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_1345540.csv',skiprows = 3)
    #Eigth: 
    Gdp['Country Name']= Gdp['Country Name'].replace(['Korea, Rep.',
                                              "Iran, Islamic Rep.",
                                              "Hong Kong SAR, China"],
                                             ["South Korea",
                                              "Iran",
                                              "Hong Kong"])
    #Ninth: 
    ScimEn = pd.read_excel("scimagojr country rank 1996-2019.xlsx")
    #Tenth: 
    ScimEn = ScimEn.set_index('Country')           
    energy = energy.set_index('Country')     
    Gdp = Gdp.set_index('Country Name')     
    DataMerge1= pd.merge(ScimEn, energy, how='left', left_index=True, right_index=True)
    DataMerge2= pd.merge(DataMerge1, Gdp, how='left', left_index=True, right_index=True)
    DataMerge2 = DataMerge2.head(15)                        
    DataMerge2.drop(['1960',
                     "1961",
                     "1962",
                     "1963",
                     "1964",
                     "1965",
                     "1966",
                     "1967",
                     "1968",
                     "1969",
                     "1970",
                     "1971",
                     "1972",
                     "1973",
                     "1974",
                     "1975",
                     "1976",
                     "1977",
                     "1978",
                     "1979",
                     "1980",
                     "1981",
                     "1982",
                     "1983",
                     "1984",
                     "1985",
                     "1986",
                     "1987",
                     "1988",
                     "1989",
                     "1990",
                     "1991",
                     "1992",
                     "1993",
                     "1994",
                     "1995",
                     "1996",
                     "1997",
                     "1998",
                     "1999",
                     "2000",
                     "2001",
                     "2002",
                     "2003",
                     "2004",
                     "2005",
                     "2017",
                     "2018",
                     "2019",], inplace=True, axis=1)                                                   
        #Eleventh: 
    DataMerge2.drop(['Region',
                     "Country Code",
                     "Indicator Name",
                     "Indicator Code",
                     "2016",
                     "Unnamed: 64",], inplace=True, axis=1)                                                  
    return DataMerge2
answer_one()

#1.0.2 Question 2  <--WINNER (Option with function)

import pandas as pd
import numpy as np
import re

#The previous question joined three datasets then reduced this to just the...
#...top 15 entries. When you joined the datasets, but before you reduced...
#...this to the top 15 items, how many entries did you lose?

#This function should return a single number.

#Story:
    #1.I just took almost the same function "1.0.1 Question 1 (Part 1)" and...
    #...at the end I estimate the "len" difference between dataframes.

def answer_two():
    #First:
    energy = pd.read_excel("Energy Indicators.xls", skiprows = 17, skipfooter= 38)
    #Second:
    energy.drop(["Unnamed: 0","Unnamed: 1"], inplace=True, axis=1)
    energy = energy.rename(columns={'Unnamed: 2':'Country',
                                 "Petajoules":"Energy Supply",
                                 "Gigajoules":"Energy Supply per Capita",
                                 "%":"% Renewable"})
    #Fourth: 
    energy = energy.replace(['...'],np.nan)
    #Fifth: 
    energy['Country']= energy['Country'].replace(['China, Hong Kong Special Administrative Region3',
                                              "Republic of Korea",
                                              "United Kingdom of Great Britain and Northern Ireland19",
                                              "United States of America20"],
                                             ['Hong Kong',
                                              "South Korea",
                                              "United Kingdom",
                                              "United States"])
    #Sixth: 
    energy["Country2"] = energy['Country']
    energy['Country2']= energy['Country'].replace('([0-9])','',regex=True)
    energy["Country3"] = energy['Country2']
    energy['Country3']= energy['Country2'].replace('\([\w ]*\)','',regex=True)
    energy = energy[['Country3',"Energy Supply","Energy Supply per Capita","% Renewable"]]
    energy = energy.rename(columns={'Country3':'Country'})
    #Third: 
    energy["Energy Supply"] = (energy["Energy Supply"])*1000000
    #Seventh:
    Gdp = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_1345540.csv',skiprows = 3)
    #Eigth: 
    Gdp['Country Name']= Gdp['Country Name'].replace(['Korea, Rep.',
                                              "Iran, Islamic Rep.",
                                              "Hong Kong SAR, China"],
                                             ["South Korea",
                                              "Iran",
                                              "Hong Kong"])
    #Ninth: 
    ScimEn = pd.read_excel("scimagojr country rank 1996-2019.xlsx")
    #Tenth: 
    ScimEn = ScimEn.set_index('Country')           
    energy = energy.set_index('Country')     
    Gdp = Gdp.set_index('Country Name')     
    DataMerge1= pd.merge(ScimEn, energy, how='left', left_index=True, right_index=True)
    DataMerge2= pd.merge(DataMerge1, Gdp, how='left', left_index=True, right_index=True)
    DataMerge3 = DataMerge2.head(15)                        
    #1.0.2 Question 2:
    DifferenceLength = len(DataMerge2)-len(DataMerge3)
    return DifferenceLength
answer_two()

#1.1.1 Question 3 <--WINNER (Option with function)

import pandas as pd
import numpy as np
import re

#Answer the following questions in the context of only the top 15 countries by
#...Scimagojr Rank (aka the DataFrame returned by answer_one())

#What is the average GDP over the last 10 years for each country? (exclude...
#...missing values from this calculation.)

#This function should return a Series named avgGDP with 15 countries and....
#... their average GDP sorted in descending order.

#Story:
    #1.I just took the same function "1.0.1 Question 1 (Part 1)".
    #2.Then I compute the "mean" (average) of the GDP of every country taking...
    #...the specific columns (years) then choosing the axis (in this case the...
    #..."axis = 1"; that belong to move horizontally through the columns...
    #...the code and finally apply the code "skipna = True", which...
    #..."Exclude NA/null values when computing the result"). It is important...
    #...to say that as a result of this code we are going to get a Serie.
    #3.I sort the values of the serie with the code "ascending=False" (i.e....
    #...we are going to get the values sorted from the bigger to the smallest...
    #...and finally we place the same code as "inplace=True" to apply and...
    #...show the changes in the same Serie.

def answer_three():
    #First:
    energy = pd.read_excel("Energy Indicators.xls", skiprows = 17, skipfooter= 38)
    #Second:
    energy.drop(["Unnamed: 0","Unnamed: 1"], inplace=True, axis=1)
    energy = energy.rename(columns={'Unnamed: 2':'Country',
                                 "Petajoules":"Energy Supply",
                                 "Gigajoules":"Energy Supply per Capita",
                                 "%":"% Renewable"})
    #Fourth: 
    energy = energy.replace(['...'],np.nan)
    #Fifth: 
    energy['Country']= energy['Country'].replace(['China, Hong Kong Special Administrative Region3',
                                              "Republic of Korea",
                                              "United Kingdom of Great Britain and Northern Ireland19",
                                              "United States of America20"],
                                             ['Hong Kong',
                                              "South Korea",
                                              "United Kingdom",
                                              "United States"])
    #Sixth: 
    energy["Country2"] = energy['Country']
    energy['Country2']= energy['Country'].replace('([0-9])','',regex=True)
    energy["Country3"] = energy['Country2']
    energy['Country3']= energy['Country2'].replace('\([\w ]*\)','',regex=True)
    energy = energy[['Country3',"Energy Supply","Energy Supply per Capita","% Renewable"]]
    energy = energy.rename(columns={'Country3':'Country'})
    #Third: 
    energy["Energy Supply"] = (energy["Energy Supply"])*1000000
    #Seventh:
    Gdp = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_1345540.csv',skiprows = 3)
    #Eigth: 
    Gdp['Country Name']= Gdp['Country Name'].replace(['Korea, Rep.',
                                              "Iran, Islamic Rep.",
                                              "Hong Kong SAR, China"],
                                             ["South Korea",
                                              "Iran",
                                              "Hong Kong"])
    #Ninth: 
    ScimEn = pd.read_excel("scimagojr country rank 1996-2019.xlsx")
    #Tenth: 
    ScimEn = ScimEn.set_index('Country')           
    energy = energy.set_index('Country')     
    Gdp = Gdp.set_index('Country Name')     
    DataMerge1= pd.merge(ScimEn, energy, how='left', left_index=True, right_index=True)
    DataMerge2= pd.merge(DataMerge1, Gdp, how='left', left_index=True, right_index=True)
    DataMerge2 = DataMerge2.head(15)                        
    DataMerge2.drop(['1960',
                     "1961",
                     "1962",
                     "1963",
                     "1964",
                     "1965",
                     "1966",
                     "1967",
                     "1968",
                     "1969",
                     "1970",
                     "1971",
                     "1972",
                     "1973",
                     "1974",
                     "1975",
                     "1976",
                     "1977",
                     "1978",
                     "1979",
                     "1980",
                     "1981",
                     "1982",
                     "1983",
                     "1984",
                     "1985",
                     "1986",
                     "1987",
                     "1988",
                     "1989",
                     "1990",
                     "1991",
                     "1992",
                     "1993",
                     "1994",
                     "1995",
                     "1996",
                     "1997",
                     "1998",
                     "1999",
                     "2000",
                     "2001",
                     "2002",
                     "2003",
                     "2004",
                     "2005",
                     "2017",
                     "2018",
                     "2019",], inplace=True, axis=1)                                                   
    #Eleventh: 
    DataMerge2.drop(['Region',
                     "Country Code",
                     "Indicator Name",
                     "Indicator Code",
                     "2016",
                     "Unnamed: 64",], inplace=True, axis=1)
    #1.1.1 Question 3
    avgGDP = DataMerge2[["2006","2007","2008","2009","2010","2011","2012","2013","2014","2015"]].mean(axis = 1, skipna = True)                                
    avgGDP.sort_values(ascending=False, inplace=True)
    return avgGDP
answer_three()

#1.1.2 Question 4 <--WINNER (Option with function)

import pandas as pd
import numpy as np
import re

#By how much had the GDP changed over the 10 year span for the country...
#... with the 6th largest average GDP? 

#This function should return a single number.

#Story:
    #1.I just took the same function "1.1.1 Question 3".
    #2.Then I add the Serie that we generate in the "1.1.1 Question 3" as a...
    #...column to the dataframe.
    #3.I compute the difference between the GDP of the year 2006 and 2015.
    #4.Then I sort the dataframe using as a guide the column "avgGDP" with...
    #...also the codes of "ascending=False" and "inplace=True".
    #5.Finally I apply the code "iloc" to find the "how much had the GDP...
    #...changed over the 10 year span for the country 6th largest average GDP".
        #The attributes "iloc" is used through the position of the index..
        #...(Python Index); therefore I used the iloc[5,21]:
            #Where "5" means 6 position according to the index (to be...
            #...specific the city of France).
        #Where "21" means the colum "avgGDP" (the Python Index does not apply).
            
def answer_four():
    #First:
    energy = pd.read_excel("Energy Indicators.xls", skiprows = 17, skipfooter= 38)
    #Second:
    energy.drop(["Unnamed: 0","Unnamed: 1"], inplace=True, axis=1)
    energy = energy.rename(columns={'Unnamed: 2':'Country',
                                 "Petajoules":"Energy Supply",
                                 "Gigajoules":"Energy Supply per Capita",
                                 "%":"% Renewable"})
    #Fourth: 
    energy = energy.replace(['...'],np.nan)
    #Fifth: 
    energy['Country']= energy['Country'].replace(['China, Hong Kong Special Administrative Region3',
                                              "Republic of Korea",
                                              "United Kingdom of Great Britain and Northern Ireland19",
                                              "United States of America20"],
                                             ['Hong Kong',
                                              "South Korea",
                                              "United Kingdom",
                                              "United States"])
    #Sixth: 
    energy["Country2"] = energy['Country']
    energy['Country2']= energy['Country'].replace('([0-9])','',regex=True)
    energy["Country3"] = energy['Country2']
    energy['Country3']= energy['Country2'].replace('\([\w ]*\)','',regex=True)
    energy = energy[['Country3',"Energy Supply","Energy Supply per Capita","% Renewable"]]
    energy = energy.rename(columns={'Country3':'Country'})
    #Third: 
    energy["Energy Supply"] = (energy["Energy Supply"])*1000000
    #Seventh:
    Gdp = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_1345540.csv',skiprows = 3)
    #Eigth: 
    Gdp['Country Name']= Gdp['Country Name'].replace(['Korea, Rep.',
                                              "Iran, Islamic Rep.",
                                              "Hong Kong SAR, China"],
                                             ["South Korea",
                                              "Iran",
                                              "Hong Kong"])
    #Ninth: 
    ScimEn = pd.read_excel("scimagojr country rank 1996-2019.xlsx")
    #Tenth: 
    ScimEn = ScimEn.set_index('Country')           
    energy = energy.set_index('Country')     
    Gdp = Gdp.set_index('Country Name')     
    DataMerge1= pd.merge(ScimEn, energy, how='left', left_index=True, right_index=True)
    DataMerge2= pd.merge(DataMerge1, Gdp, how='left', left_index=True, right_index=True)
    DataMerge2 = DataMerge2.head(15)                        
    DataMerge2.drop(['1960',
                     "1961",
                     "1962",
                     "1963",
                     "1964",
                     "1965",
                     "1966",
                     "1967",
                     "1968",
                     "1969",
                     "1970",
                     "1971",
                     "1972",
                     "1973",
                     "1974",
                     "1975",
                     "1976",
                     "1977",
                     "1978",
                     "1979",
                     "1980",
                     "1981",
                     "1982",
                     "1983",
                     "1984",
                     "1985",
                     "1986",
                     "1987",
                     "1988",
                     "1989",
                     "1990",
                     "1991",
                     "1992",
                     "1993",
                     "1994",
                     "1995",
                     "1996",
                     "1997",
                     "1998",
                     "1999",
                     "2000",
                     "2001",
                     "2002",
                     "2003",
                     "2004",
                     "2005",
                     "2017",
                     "2018",
                     "2019",], inplace=True, axis=1)                                                   
    #Eleventh: 
    DataMerge2.drop(['Region',
                     "Country Code",
                     "Indicator Name",
                     "Indicator Code",
                     "2016",
                     "Unnamed: 64",], inplace=True, axis=1)
    avgGDP = DataMerge2[["2006","2007","2008","2009","2010","2011","2012","2013","2014","2015"]].mean(axis = 1, skipna = True)                                
    avgGDP.sort_values(ascending=False, inplace=True)
    #1.1.2 Question 4
    DataMerge2['avgGDP'] = avgGDP
    DataMerge2["DifferenceGDP"] = abs(DataMerge2["2015"] - DataMerge2["2006"])
    DataMerge2.sort_values(by=['avgGDP'], ascending=False, inplace=True)
    return DataMerge2.iloc[5,21]
answer_four()

#1.1.3 Question 5 <--WINNER (Option with function)

import pandas as pd
import numpy as np
import re

#What is the mean Energy Supply per Capita?

#This function should return a single number.

#Story:
    #1.I just took the same function "1.0.1 Question 1 (Part 1)".
    #2.Then I compute the "mean" (average) of the "Energy Supply per Capita"...
    #...choosing the axis (in this case the "axis = 0"; that belong to move...
    #...vertically through the rows of the column "Energy Supply per Capita"...
    #...Also I apply the code "skipna = True", which "Exclude NA/null...
    #...values when computing the result").

def answer_five():
    #First:
    energy = pd.read_excel("Energy Indicators.xls", skiprows = 17, skipfooter= 38)
    #Second:
    energy.drop(["Unnamed: 0","Unnamed: 1"], inplace=True, axis=1)
    energy = energy.rename(columns={'Unnamed: 2':'Country',
                                 "Petajoules":"Energy Supply",
                                 "Gigajoules":"Energy Supply per Capita",
                                 "%":"% Renewable"})
    #Fourth: 
    energy = energy.replace(['...'],np.nan)
    #Fifth: 
    energy['Country']= energy['Country'].replace(['China, Hong Kong Special Administrative Region3',
                                              "Republic of Korea",
                                              "United Kingdom of Great Britain and Northern Ireland19",
                                              "United States of America20"],
                                             ['Hong Kong',
                                              "South Korea",
                                              "United Kingdom",
                                              "United States"])
    #Sixth: 
    energy["Country2"] = energy['Country']
    energy['Country2']= energy['Country'].replace('([0-9])','',regex=True)
    energy["Country3"] = energy['Country2']
    energy['Country3']= energy['Country2'].replace('\([\w ]*\)','',regex=True)
    energy = energy[['Country3',"Energy Supply","Energy Supply per Capita","% Renewable"]]
    energy = energy.rename(columns={'Country3':'Country'})
    #Third: 
    energy["Energy Supply"] = (energy["Energy Supply"])*1000000
    #Seventh:
    Gdp = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_1345540.csv',skiprows = 3)
    #Eigth: 
    Gdp['Country Name']= Gdp['Country Name'].replace(['Korea, Rep.',
                                              "Iran, Islamic Rep.",
                                              "Hong Kong SAR, China"],
                                             ["South Korea",
                                              "Iran",
                                              "Hong Kong"])
    #Ninth: 
    ScimEn = pd.read_excel("scimagojr country rank 1996-2019.xlsx")
    #Tenth: 
    ScimEn = ScimEn.set_index('Country')           
    energy = energy.set_index('Country')     
    Gdp = Gdp.set_index('Country Name')     
    DataMerge1= pd.merge(ScimEn, energy, how='left', left_index=True, right_index=True)
    DataMerge2= pd.merge(DataMerge1, Gdp, how='left', left_index=True, right_index=True)
    DataMerge2 = DataMerge2.head(15)                        
    DataMerge2.drop(['1960',
                     "1961",
                     "1962",
                     "1963",
                     "1964",
                     "1965",
                     "1966",
                     "1967",
                     "1968",
                     "1969",
                     "1970",
                     "1971",
                     "1972",
                     "1973",
                     "1974",
                     "1975",
                     "1976",
                     "1977",
                     "1978",
                     "1979",
                     "1980",
                     "1981",
                     "1982",
                     "1983",
                     "1984",
                     "1985",
                     "1986",
                     "1987",
                     "1988",
                     "1989",
                     "1990",
                     "1991",
                     "1992",
                     "1993",
                     "1994",
                     "1995",
                     "1996",
                     "1997",
                     "1998",
                     "1999",
                     "2000",
                     "2001",
                     "2002",
                     "2003",
                     "2004",
                     "2005",
                     "2017",
                     "2018",
                     "2019",], inplace=True, axis=1)                                                   
    #Eleventh: 
    DataMerge2.drop(['Region',
                     "Country Code",
                     "Indicator Name",
                     "Indicator Code",
                     "2016",
                     "Unnamed: 64",], inplace=True, axis=1)
    #1.1.3 Question 5
    MeanESPC = DataMerge2["Energy Supply per Capita"].mean(axis = 0, skipna = True)                                
    return MeanESPC
answer_five()

#1.1.4 Question 6  <--WINNER (Option with function)

import pandas as pd
import numpy as np
import re

#What country has the maximum % Renewable and what is the percentage?

#This function should return a tuple with the name of the country and...
#...the percentage.

#Story:
    #1.I just took the same function "1.0.1 Question 1 (Part 1)".
    #2.Then I sort the dataframe using as a guide the column "% Renewable"...
    #...with also the codes of "ascending=False" and "inplace=True".
    #3.After that I look for the top value of the sorted column "% Renewable"...
    #...It is important to consider the position of the cell (Python Index)...
    #...when I count the columns.
    #4.Then I create a variable that is going to contain the index of my...
    #...dataframe.
    #5.Finally I create an tuple with the (zero value [0] position of the...
    #...index variable contain the index of my dataframe, top value of the...
    #...sorted column "% Renewable"). It is important to consider the position...
    #...of the cell (Python Index) when I count the rows.

def answer_six():
    #First:
    energy = pd.read_excel("Energy Indicators.xls", skiprows = 17, skipfooter= 38)
    #Second:
    energy.drop(["Unnamed: 0","Unnamed: 1"], inplace=True, axis=1)
    energy = energy.rename(columns={'Unnamed: 2':'Country',
                                 "Petajoules":"Energy Supply",
                                 "Gigajoules":"Energy Supply per Capita",
                                 "%":"% Renewable"})
    #Fourth: 
    energy = energy.replace(['...'],np.nan)
    #Fifth: 
    energy['Country']= energy['Country'].replace(['China, Hong Kong Special Administrative Region3',
                                              "Republic of Korea",
                                              "United Kingdom of Great Britain and Northern Ireland19",
                                              "United States of America20"],
                                             ['Hong Kong',
                                              "South Korea",
                                              "United Kingdom",
                                              "United States"])
    #Sixth: 
    energy["Country2"] = energy['Country']
    energy['Country2']= energy['Country'].replace('([0-9])','',regex=True)
    energy["Country3"] = energy['Country2']
    energy['Country3']= energy['Country2'].replace('\([\w ]*\)','',regex=True)
    energy = energy[['Country3',"Energy Supply","Energy Supply per Capita","% Renewable"]]
    energy = energy.rename(columns={'Country3':'Country'})
    #Third: 
    energy["Energy Supply"] = (energy["Energy Supply"])*1000000
    #Seventh:
    Gdp = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_1345540.csv',skiprows = 3)
    #Eigth: 
    Gdp['Country Name']= Gdp['Country Name'].replace(['Korea, Rep.',
                                              "Iran, Islamic Rep.",
                                              "Hong Kong SAR, China"],
                                             ["South Korea",
                                              "Iran",
                                              "Hong Kong"])
    #Ninth: 
    ScimEn = pd.read_excel("scimagojr country rank 1996-2019.xlsx")
    #Tenth: 
    ScimEn = ScimEn.set_index('Country')           
    energy = energy.set_index('Country')     
    Gdp = Gdp.set_index('Country Name')     
    DataMerge1= pd.merge(ScimEn, energy, how='left', left_index=True, right_index=True)
    DataMerge2= pd.merge(DataMerge1, Gdp, how='left', left_index=True, right_index=True)
    DataMerge2 = DataMerge2.head(15)                        
    DataMerge2.drop(['1960',
                     "1961",
                     "1962",
                     "1963",
                     "1964",
                     "1965",
                     "1966",
                     "1967",
                     "1968",
                     "1969",
                     "1970",
                     "1971",
                     "1972",
                     "1973",
                     "1974",
                     "1975",
                     "1976",
                     "1977",
                     "1978",
                     "1979",
                     "1980",
                     "1981",
                     "1982",
                     "1983",
                     "1984",
                     "1985",
                     "1986",
                     "1987",
                     "1988",
                     "1989",
                     "1990",
                     "1991",
                     "1992",
                     "1993",
                     "1994",
                     "1995",
                     "1996",
                     "1997",
                     "1998",
                     "1999",
                     "2000",
                     "2001",
                     "2002",
                     "2003",
                     "2004",
                     "2005",
                     "2017",
                     "2018",
                     "2019",], inplace=True, axis=1)                                                   
        #Eleventh: 
    DataMerge2.drop(['Region',
                     "Country Code",
                     "Indicator Name",
                     "Indicator Code",
                     "2016",
                     "Unnamed: 64",], inplace=True, axis=1)     
    #1.1.4 Question 6
    DataMerge2.sort_values(by=['% Renewable'], ascending=False, inplace=True)
    TopPercentage = DataMerge2.iloc[0,9]   
    GetIndex = DataMerge2.index
    TupleAnswer = (GetIndex[0],TopPercentage)                                           
    return TupleAnswer
answer_six()

#1.1.5 Question 7 <--WINNER (Option with function)

import pandas as pd
import numpy as np
import re

#Create a new column that is the ratio of Self-Citations to Total...
#...Citations. What is the maximum value for this new column, and what..
#...country has the highest ratio?

#This function should return a tuple with the name of the country and the...
#...ratio.

#Story:
    #1.I just took the same function "1.0.1 Question 1 (Part 1)".
    #2.After that, I create a new column called "Ratio", which is a division...
    #...between the columns ["Self-citations"] / ["Citations"]
    #3.Then I sort the dataframe using as a guide the column "Ratio"...
    #...with also the codes of "ascending=False" and "inplace=True".
    #4.After that I look for the top value of the sorted column "Ratio"...
    #...It is important to consider the position of the cell (Python Index)...
    #...when I count the columns.
    #5.Then I create a variable that is going to contain the index of my...
    #...dataframe.
    #6.Finally I create an tuple with the (zero value [0] position of the...
    #...index variable contain the index of my dataframe, top value of the...
    #...sorted column "Ratio"). It is important to consider the position...
    #...of the cell (Python Index) when I count the rows.

def answer_seven():
    #First:
    energy = pd.read_excel("Energy Indicators.xls", skiprows = 17, skipfooter= 38)
    #Second:
    energy.drop(["Unnamed: 0","Unnamed: 1"], inplace=True, axis=1)
    energy = energy.rename(columns={'Unnamed: 2':'Country',
                                 "Petajoules":"Energy Supply",
                                 "Gigajoules":"Energy Supply per Capita",
                                 "%":"% Renewable"})
    #Fourth: 
    energy = energy.replace(['...'],np.nan)
    #Fifth: 
    energy['Country']= energy['Country'].replace(['China, Hong Kong Special Administrative Region3',
                                              "Republic of Korea",
                                              "United Kingdom of Great Britain and Northern Ireland19",
                                              "United States of America20"],
                                             ['Hong Kong',
                                              "South Korea",
                                              "United Kingdom",
                                              "United States"])
    #Sixth: 
    energy["Country2"] = energy['Country']
    energy['Country2']= energy['Country'].replace('([0-9])','',regex=True)
    energy["Country3"] = energy['Country2']
    energy['Country3']= energy['Country2'].replace('\([\w ]*\)','',regex=True)
    energy = energy[['Country3',"Energy Supply","Energy Supply per Capita","% Renewable"]]
    energy = energy.rename(columns={'Country3':'Country'})
    #Third: 
    energy["Energy Supply"] = (energy["Energy Supply"])*1000000
    #Seventh:
    Gdp = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_1345540.csv',skiprows = 3)
    #Eigth: 
    Gdp['Country Name']= Gdp['Country Name'].replace(['Korea, Rep.',
                                              "Iran, Islamic Rep.",
                                              "Hong Kong SAR, China"],
                                             ["South Korea",
                                              "Iran",
                                              "Hong Kong"])
    #Ninth: 
    ScimEn = pd.read_excel("scimagojr country rank 1996-2019.xlsx")
    #Tenth: 
    ScimEn = ScimEn.set_index('Country')           
    energy = energy.set_index('Country')     
    Gdp = Gdp.set_index('Country Name')     
    DataMerge1= pd.merge(ScimEn, energy, how='left', left_index=True, right_index=True)
    DataMerge2= pd.merge(DataMerge1, Gdp, how='left', left_index=True, right_index=True)
    DataMerge2 = DataMerge2.head(15)                        
    DataMerge2.drop(['1960',
                     "1961",
                     "1962",
                     "1963",
                     "1964",
                     "1965",
                     "1966",
                     "1967",
                     "1968",
                     "1969",
                     "1970",
                     "1971",
                     "1972",
                     "1973",
                     "1974",
                     "1975",
                     "1976",
                     "1977",
                     "1978",
                     "1979",
                     "1980",
                     "1981",
                     "1982",
                     "1983",
                     "1984",
                     "1985",
                     "1986",
                     "1987",
                     "1988",
                     "1989",
                     "1990",
                     "1991",
                     "1992",
                     "1993",
                     "1994",
                     "1995",
                     "1996",
                     "1997",
                     "1998",
                     "1999",
                     "2000",
                     "2001",
                     "2002",
                     "2003",
                     "2004",
                     "2005",
                     "2017",
                     "2018",
                     "2019",], inplace=True, axis=1)                                                   
        #Eleventh: 
    DataMerge2.drop(['Region',
                     "Country Code",
                     "Indicator Name",
                     "Indicator Code",
                     "2016",
                     "Unnamed: 64",], inplace=True, axis=1)     
    #1.1.5 Question 7
    DataMerge2["Ratio"] = abs(DataMerge2["Self-citations"] /DataMerge2["Citations"])
    DataMerge2.sort_values(by=['Ratio'], ascending=False, inplace=True)
    TopRatio = DataMerge2.iloc[0,20]   
    GetIndexDataframeRatio = DataMerge2.index
    TupleAnswerRatio = (GetIndexDataframeRatio[0],TopRatio)                                           
    return TupleAnswerRatio
answer_seven()

#1.1.6 Question 8  <--WINNER (Option with function)

import pandas as pd
import numpy as np
import re

#Create a column that estimates the population using Energy Supply and...
#...Energy Supply per capita.

#What is the third most populous country according to this estimate?

#This function should return a single string value.

#Story:
    #1.I just took the same function "1.0.1 Question 1 (Part 1)".
    #2.After that, I create a new column called "Population", which is a...
    #...division between the columns ["Energy Supply"] / ["Energy Supply per Capita"]
    #3.Then I sort the dataframe using as a guide the column "Population"...
    #...with also the codes of "ascending=False" and "inplace=True".
    #4.Then I create a variable that is going to contain the index of my...
    #...dataframe.
    #5.Finally I extract the country in the form of string (second value [2]...
    #...position of the index variable contain the index of my dataframe. It...
    #...is important to consider the position of the cell (Python Index) when...
    #...I count the rows.

def answer_eigth():
    #First:
    energy = pd.read_excel("Energy Indicators.xls", skiprows = 17, skipfooter= 38)
    #Second:
    energy.drop(["Unnamed: 0","Unnamed: 1"], inplace=True, axis=1)
    energy = energy.rename(columns={'Unnamed: 2':'Country',
                                 "Petajoules":"Energy Supply",
                                 "Gigajoules":"Energy Supply per Capita",
                                 "%":"% Renewable"})
    #Fourth: 
    energy = energy.replace(['...'],np.nan)
    #Fifth: 
    energy['Country']= energy['Country'].replace(['China, Hong Kong Special Administrative Region3',
                                              "Republic of Korea",
                                              "United Kingdom of Great Britain and Northern Ireland19",
                                              "United States of America20"],
                                             ['Hong Kong',
                                              "South Korea",
                                              "United Kingdom",
                                              "United States"])
    #Sixth: 
    energy["Country2"] = energy['Country']
    energy['Country2']= energy['Country'].replace('([0-9])','',regex=True)
    energy["Country3"] = energy['Country2']
    energy['Country3']= energy['Country2'].replace('\([\w ]*\)','',regex=True)
    energy = energy[['Country3',"Energy Supply","Energy Supply per Capita","% Renewable"]]
    energy = energy.rename(columns={'Country3':'Country'})
    #Third: 
    energy["Energy Supply"] = (energy["Energy Supply"])*1000000
    #Seventh:
    Gdp = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_1345540.csv',skiprows = 3)
    #Eigth: 
    Gdp['Country Name']= Gdp['Country Name'].replace(['Korea, Rep.',
                                              "Iran, Islamic Rep.",
                                              "Hong Kong SAR, China"],
                                             ["South Korea",
                                              "Iran",
                                              "Hong Kong"])
    #Ninth: 
    ScimEn = pd.read_excel("scimagojr country rank 1996-2019.xlsx")
    #Tenth: 
    ScimEn = ScimEn.set_index('Country')           
    energy = energy.set_index('Country')     
    Gdp = Gdp.set_index('Country Name')     
    DataMerge1= pd.merge(ScimEn, energy, how='left', left_index=True, right_index=True)
    DataMerge2= pd.merge(DataMerge1, Gdp, how='left', left_index=True, right_index=True)
    DataMerge2 = DataMerge2.head(15)                        
    DataMerge2.drop(['1960',
                     "1961",
                     "1962",
                     "1963",
                     "1964",
                     "1965",
                     "1966",
                     "1967",
                     "1968",
                     "1969",
                     "1970",
                     "1971",
                     "1972",
                     "1973",
                     "1974",
                     "1975",
                     "1976",
                     "1977",
                     "1978",
                     "1979",
                     "1980",
                     "1981",
                     "1982",
                     "1983",
                     "1984",
                     "1985",
                     "1986",
                     "1987",
                     "1988",
                     "1989",
                     "1990",
                     "1991",
                     "1992",
                     "1993",
                     "1994",
                     "1995",
                     "1996",
                     "1997",
                     "1998",
                     "1999",
                     "2000",
                     "2001",
                     "2002",
                     "2003",
                     "2004",
                     "2005",
                     "2017",
                     "2018",
                     "2019",], inplace=True, axis=1)                                                   
        #Eleventh: 
    DataMerge2.drop(['Region',
                     "Country Code",
                     "Indicator Name",
                     "Indicator Code",
                     "2016",
                     "Unnamed: 64",], inplace=True, axis=1)     
    #1.1.6 Question 8
    DataMerge2["Population"] = abs(DataMerge2["Energy Supply"] /DataMerge2["Energy Supply per Capita"])
    DataMerge2.sort_values(by=['Population'], ascending=False, inplace=True)
    GetIndexDataframeRatio = DataMerge2.index
    ThirdPopulation = GetIndexDataframeRatio[2]                                     
    return ThirdPopulation
answer_eigth()

#1.1.7 Question 9  <--WINNER (Option with function)

import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

#Create a column that estimates the number of citable documents per person....
#...What is the correlation between the number of citable documents per...
#...capita and the energy supply per capita? Use the .corr() method,...
#...(Pearson’s correlation).

#This function should return a single number.

#(Optional: Use the built-in function plot9() to visualize the relationship...
#...between Energy Supply per Capita vs. Citable docs per Capita)

#Story:
    #1.I just took the same function "1.0.1 Question 1 (Part 1)".
    #2.After that, I create a new column called "Population", which is a...
    #...division between the columns ["Energy Supply"] / ["Energy Supply per Capita"]
    #3.After that, I create a new column called "Citable per Person", which...
    #...is adivision between the columns ["Citable documents"] / ["Population"]
    #4.Then I apply the "Correlation Method" (the same of HMLSL) to all the...
    #...data (the columns) of the dataframe, getting as an answer a matrix...
    #...with columns as columns and as rows and as diagonal all values are 1.
        #It is important to say that we get through this code the value of...
        #...the "Pearson correlation coefficient" , also called "Standard...
        #...correlation coefficient". In addition we have the code (Final...
        #...Comment) to check the correlation between atributes through a...
        #...amtrix graph.
        
    #5.Finally, I print only the value of the cell that contain the...
    #...Correlation value between 'Citable per Person' and "Energy Supply...
    #...per Capita"
    
    #Final Comment: I left the code of to generate the graph (scatterplot)...
    #:..which was not necessary to put inside the final function
    
        # DataMerge2.plot(x="Citable per Person", y="Energy Supply per Capita",color="orange", kind= "scatter")

def answer_nine():
    #First:
    energy = pd.read_excel("Energy Indicators.xls", skiprows = 17, skipfooter= 38)
    #Second:
    energy.drop(["Unnamed: 0","Unnamed: 1"], inplace=True, axis=1)
    energy = energy.rename(columns={'Unnamed: 2':'Country',
                                 "Petajoules":"Energy Supply",
                                 "Gigajoules":"Energy Supply per Capita",
                                 "%":"% Renewable"})
    #Fourth: 
    energy = energy.replace(['...'],np.nan)
    #Fifth: 
    energy['Country']= energy['Country'].replace(['China, Hong Kong Special Administrative Region3',
                                              "Republic of Korea",
                                              "United Kingdom of Great Britain and Northern Ireland19",
                                              "United States of America20"],
                                             ['Hong Kong',
                                              "South Korea",
                                              "United Kingdom",
                                              "United States"])
    #Sixth: 
    energy["Country2"] = energy['Country']
    energy['Country2']= energy['Country'].replace('([0-9])','',regex=True)
    energy["Country3"] = energy['Country2']
    energy['Country3']= energy['Country2'].replace('\([\w ]*\)','',regex=True)
    energy = energy[['Country3',"Energy Supply","Energy Supply per Capita","% Renewable"]]
    energy = energy.rename(columns={'Country3':'Country'})
    #Third: 
    energy["Energy Supply"] = (energy["Energy Supply"])*1000000
    #Seventh:
    Gdp = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_1345540.csv',skiprows = 3)
    #Eigth: 
    Gdp['Country Name']= Gdp['Country Name'].replace(['Korea, Rep.',
                                              "Iran, Islamic Rep.",
                                              "Hong Kong SAR, China"],
                                             ["South Korea",
                                              "Iran",
                                              "Hong Kong"])
    #Ninth: 
    ScimEn = pd.read_excel("scimagojr country rank 1996-2019.xlsx")
    #Tenth: 
    ScimEn = ScimEn.set_index('Country')           
    energy = energy.set_index('Country')     
    Gdp = Gdp.set_index('Country Name')     
    DataMerge1= pd.merge(ScimEn, energy, how='left', left_index=True, right_index=True)
    DataMerge2= pd.merge(DataMerge1, Gdp, how='left', left_index=True, right_index=True)
    DataMerge2 = DataMerge2.head(15)                        
    DataMerge2.drop(['1960',
                     "1961",
                     "1962",
                     "1963",
                     "1964",
                     "1965",
                     "1966",
                     "1967",
                     "1968",
                     "1969",
                     "1970",
                     "1971",
                     "1972",
                     "1973",
                     "1974",
                     "1975",
                     "1976",
                     "1977",
                     "1978",
                     "1979",
                     "1980",
                     "1981",
                     "1982",
                     "1983",
                     "1984",
                     "1985",
                     "1986",
                     "1987",
                     "1988",
                     "1989",
                     "1990",
                     "1991",
                     "1992",
                     "1993",
                     "1994",
                     "1995",
                     "1996",
                     "1997",
                     "1998",
                     "1999",
                     "2000",
                     "2001",
                     "2002",
                     "2003",
                     "2004",
                     "2005",
                     "2017",
                     "2018",
                     "2019",], inplace=True, axis=1)                                                   
        #Eleventh: 
    DataMerge2.drop(['Region',
                     "Country Code",
                     "Indicator Name",
                     "Indicator Code",
                     "2016",
                     "Unnamed: 64",], inplace=True, axis=1)     
    #1.1.7 Question 9
    DataMerge2["Population"] = abs(DataMerge2["Energy Supply"] /DataMerge2["Energy Supply per Capita"])
    DataMerge2["Citable per Person"] = abs(DataMerge2["Citable documents"] /DataMerge2["Population"])
    PearsonMatrix = DataMerge2.corr(method="pearson")
    CorrelationX = PearsonMatrix.loc['Citable per Person', "Energy Supply per Capita"]
    return CorrelationX
answer_nine()

#1.1.8 Question 10  <--WINNER (Option with function)

import pandas as pd
import numpy as np
import re

#Create a new column with a 1 if the country’s % Renewable value is at or...
#...above the median for all countries in the top 15, and a 0 if the...
#...country’s % Renewable value is below the median.

#This function should return a series named HighRenew whose index is the...
#...country name sorted in ascending order of rank.

#Story:
    #1.I just took the same function "1.0.1 Question 1 (Part 1)".
    #2.After that, I found the mean value of all values shown in the column...
    #...of ["% Renewable"]
    #3.Then I replace the value "np.nan" in the dataframe (but with the...
    #...purpose to work over the column ["% Renewable"]) for the value of...
    #4.Then I create a blank list.
    #5.I create a for loop to move in every row of the column ["% Renewable"]...
    #...to find those values "under the mean, above the mean and equal to mean"...
    #...an then put those values equal to "0,1 or np.nan". Afterwards...
    #...those values are append to the list created in the step 4.
    #6.I convert the list in a Serie and added (manually) the country names...
    #...as index.
    #7.Finally I sort the Index of the Serie.


#Ideas Extras (to try in another moment):
    #Do the "if process" of indentify values considering a type of data (type...
    #..."float" for the "nan" and "int" the "numbers"?
    #Play with the index when we think about merge dataframes together...
    #...or a Series together.
    #Apply the code "apply" or "filter" or "transformation" or "aggregation"....
    #...as a way to a apply a function over a dataframe (i.e. over column or...
    #...columns of a dataframe).
    #Use of Lambda as a function inside of "apply" or "filter" or...
    #..."transformation" or "aggregation".
    #Create a specific function that will work inside the code "apply" or...
    #..."filter" or "transformation" or "aggregation"
    #Review codes of Week 1 and 2 to check some posible answer.
    #Review in the web some code to a apply a function over a dataframe (i.e...
    #...over column or columns of a dataframe).

def answer_ten():
    #First:
    energy = pd.read_excel("Energy Indicators.xls", skiprows = 17, skipfooter= 38)
    #Second:
    energy.drop(["Unnamed: 0","Unnamed: 1"], inplace=True, axis=1)
    energy = energy.rename(columns={'Unnamed: 2':'Country',
                                 "Petajoules":"Energy Supply",
                                 "Gigajoules":"Energy Supply per Capita",
                                 "%":"% Renewable"})
    #Fourth: 
    energy = energy.replace(['...'],np.nan)
    #Fifth: 
    energy['Country']= energy['Country'].replace(['China, Hong Kong Special Administrative Region3',
                                              "Republic of Korea",
                                              "United Kingdom of Great Britain and Northern Ireland19",
                                              "United States of America20"],
                                             ['Hong Kong',
                                              "South Korea",
                                              "United Kingdom",
                                              "United States"])
    #Sixth: 
    energy["Country2"] = energy['Country']
    energy['Country2']= energy['Country'].replace('([0-9])','',regex=True)
    energy["Country3"] = energy['Country2']
    energy['Country3']= energy['Country2'].replace('\([\w ]*\)','',regex=True)
    energy = energy[['Country3',"Energy Supply","Energy Supply per Capita","% Renewable"]]
    energy = energy.rename(columns={'Country3':'Country'})
    #Third: 
    energy["Energy Supply"] = (energy["Energy Supply"])*1000000
    #Seventh:
    Gdp = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_1345540.csv',skiprows = 3)
    #Eigth: 
    Gdp['Country Name']= Gdp['Country Name'].replace(['Korea, Rep.',
                                              "Iran, Islamic Rep.",
                                              "Hong Kong SAR, China"],
                                             ["South Korea",
                                              "Iran",
                                              "Hong Kong"])
    #Ninth: 
    ScimEn = pd.read_excel("scimagojr country rank 1996-2019.xlsx")
    #Tenth: 
    ScimEn = ScimEn.set_index('Country')           
    energy = energy.set_index('Country')     
    Gdp = Gdp.set_index('Country Name')     
    DataMerge1= pd.merge(ScimEn, energy, how='left', left_index=True, right_index=True)
    DataMerge2= pd.merge(DataMerge1, Gdp, how='left', left_index=True, right_index=True)
    DataMerge2 = DataMerge2.head(15)                        
    DataMerge2.drop(['1960',
                     "1961",
                     "1962",
                     "1963",
                     "1964",
                     "1965",
                     "1966",
                     "1967",
                     "1968",
                     "1969",
                     "1970",
                     "1971",
                     "1972",
                     "1973",
                     "1974",
                     "1975",
                     "1976",
                     "1977",
                     "1978",
                     "1979",
                     "1980",
                     "1981",
                     "1982",
                     "1983",
                     "1984",
                     "1985",
                     "1986",
                     "1987",
                     "1988",
                     "1989",
                     "1990",
                     "1991",
                     "1992",
                     "1993",
                     "1994",
                     "1995",
                     "1996",
                     "1997",
                     "1998",
                     "1999",
                     "2000",
                     "2001",
                     "2002",
                     "2003",
                     "2004",
                     "2005",
                     "2017",
                     "2018",
                     "2019",], inplace=True, axis=1)                                                   
        #Eleventh: 
    DataMerge2.drop(['Region',
                     "Country Code",
                     "Indicator Name",
                     "Indicator Code",
                     "2016",
                     "Unnamed: 64",], inplace=True, axis=1)     
    #1.1.8 Question 10
    MeanColumn = DataMerge2["% Renewable"].mean(axis = 0, skipna = True) 
    DataMerge2 = DataMerge2.replace([np.nan],MeanColumn)                          
    BlankList1 = []
    for X in DataMerge2["% Renewable"]:
        if X < MeanColumn:
            W1 = BlankList1.append(0)
        elif X > MeanColumn:
            W2 = BlankList1.append(1)
        elif X == MeanColumn:
            W3 = BlankList1.append(np.nan)      
    HighRenew = pd.Series(BlankList1,index=['China','United States','Japan',"India","United Kingdom","Germany","Russian Federation","Canada","Italy","South Korea","France","Iran","Spain","Australia","Brazil"])
    HighRenew.sort_index(ascending=True, inplace=True)
    return HighRenew
answer_ten()

#1.1.9 Question 11 <--WINNER (Option with function)

import pandas as pd
import numpy as np
import re

#Use the following dictionary to group the Countries by Continent, then...
#...create a dateframe that displays the sample size (the number of...
#...countries in each continent bin), and the sum, mean, and std deviation..
#..for the estimated population of each country.

ContinentDict = {"China":"Asia",
                 "United States":"North America",
                 "Japan":"Asia",
                 "United Kingdom":"Europe",
                 "Russian Federation":"Europe",
                 "Canada":"North America",
                 "Germany":"Europe",
                 "India":"Asia",
                 "France":"Europe",
                 "South Korea":"Asia",
                 "Italy":"Europe",
                 "Spain":"Europe",
                 "Iran":"Asia",
                 "Australia":"Australia",
                 "Brazil":"South America"}

#This function should return a DataFrame with index named Continent...
#...[ ’ Asia ’ , ’ Australia ’ ,’ Europe ’ , ’ North America ’ , ’ South...
#...America ’ ] and columns [ ’ size ’ , ’ sum ’ , ’ mean ’ ,’ std ’ ]

#Story:
    #1.I just took the same function "1.0.1 Question 1 (Part 1)".
    #2.I create a Dataframe with the dictionary called "dfDictio"
    #3.I apply the transpose of the newly created dataframe "dfDictio" to...
    #...adjust the values; therefore I create the new datafrane called...
    #..."dfDictioTranspose".
    #4.After that I merge my dataframe generated in the...
    #...."1.0.1 Question 1 (Part 1)" with the dataframe "dfDictioTranspose"...
    #...to get the dataframe "df1". It is important to say that at the...
    #...moment of the merge both dataframes have in common the column of ...
    #..."Country" as index.
    #5.Then I reset the index of the dataframe "df1".
    #6.After that, I create a new column called "Population", which is a...
    #...division between the columns ["Energy Supply"] / ["Energy Supply per Capita"]
    #7.THen I drop all the columns except for the columns of "Country",...
    #..."Continent" and "Population".
    #8.I rename the column of "Country".
    #9.I apply the code "groupby by" "aggregation" considering the "groupby"...
    #...of the column "Continent". In addition, all math operations with...
    #...Numpy (count all non zero elements, sum all the values,the mean...
    #...without the nan values, the standarad deviation without the nan values)
    #10.I change the name of the columns to ['size', 'sum', 'mean', 'std'].

def answer_eleven():
    #First:
    energy = pd.read_excel("Energy Indicators.xls", skiprows = 17, skipfooter= 38)
    #Second:
    energy.drop(["Unnamed: 0","Unnamed: 1"], inplace=True, axis=1)
    energy = energy.rename(columns={'Unnamed: 2':'Country',
                                 "Petajoules":"Energy Supply",
                                 "Gigajoules":"Energy Supply per Capita",
                                 "%":"% Renewable"})
    #Fourth: 
    energy = energy.replace(['...'],np.nan)
    #Fifth: 
    energy['Country']= energy['Country'].replace(['China, Hong Kong Special Administrative Region3',
                                              "Republic of Korea",
                                              "United Kingdom of Great Britain and Northern Ireland19",
                                              "United States of America20"],
                                             ['Hong Kong',
                                              "South Korea",
                                              "United Kingdom",
                                              "United States"])
    #Sixth: 
    energy["Country2"] = energy['Country']
    energy['Country2']= energy['Country'].replace('([0-9])','',regex=True)
    energy["Country3"] = energy['Country2']
    energy['Country3']= energy['Country2'].replace('\([\w ]*\)','',regex=True)
    energy = energy[['Country3',"Energy Supply","Energy Supply per Capita","% Renewable"]]
    energy = energy.rename(columns={'Country3':'Country'})
    #Third: 
    energy["Energy Supply"] = (energy["Energy Supply"])*1000000
    #Seventh:
    Gdp = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_1345540.csv',skiprows = 3)
    #Eigth: 
    Gdp['Country Name']= Gdp['Country Name'].replace(['Korea, Rep.',
                                              "Iran, Islamic Rep.",
                                              "Hong Kong SAR, China"],
                                             ["South Korea",
                                              "Iran",
                                              "Hong Kong"])
    #Ninth: 
    ScimEn = pd.read_excel("scimagojr country rank 1996-2019.xlsx")
    #Tenth: 
    ScimEn = ScimEn.set_index('Country')           
    energy = energy.set_index('Country')     
    Gdp = Gdp.set_index('Country Name')     
    DataMerge1= pd.merge(ScimEn, energy, how='left', left_index=True, right_index=True)
    DataMerge2= pd.merge(DataMerge1, Gdp, how='left', left_index=True, right_index=True)
    DataMerge2 = DataMerge2.head(15)                        
    DataMerge2.drop(['1960',
                     "1961",
                     "1962",
                     "1963",
                     "1964",
                     "1965",
                     "1966",
                     "1967",
                     "1968",
                     "1969",
                     "1970",
                     "1971",
                     "1972",
                     "1973",
                     "1974",
                     "1975",
                     "1976",
                     "1977",
                     "1978",
                     "1979",
                     "1980",
                     "1981",
                     "1982",
                     "1983",
                     "1984",
                     "1985",
                     "1986",
                     "1987",
                     "1988",
                     "1989",
                     "1990",
                     "1991",
                     "1992",
                     "1993",
                     "1994",
                     "1995",
                     "1996",
                     "1997",
                     "1998",
                     "1999",
                     "2000",
                     "2001",
                     "2002",
                     "2003",
                     "2004",
                     "2005",
                     "2017",
                     "2018",
                     "2019",], inplace=True, axis=1)                                                   
        #Eleventh: 
    DataMerge2.drop(['Region',
                     "Country Code",
                     "Indicator Name",
                     "Indicator Code",
                     "2016",
                     "Unnamed: 64",], inplace=True, axis=1)     
    #1.1.9 Question 11
    ContinentDict = {"China":"Asia",
                 "United States":"North America",
                 "Japan":"Asia",
                 "United Kingdom":"Europe",
                 "Russian Federation":"Europe",
                 "Canada":"North America",
                 "Germany":"Europe",
                 "India":"Asia",
                 "France":"Europe",
                 "South Korea":"Asia",
                 "Italy":"Europe",
                 "Spain":"Europe",
                 "Iran":"Asia",
                 "Australia":"Australia",
                 "Brazil":"South America"}
    dfDictio = pd.DataFrame(ContinentDict, index=['Continent'])
    dfDictioTranspose = dfDictio.T
    df1= pd.merge(DataMerge2, dfDictioTranspose, how='outer', left_index=True, right_index=True)
    df1 = df1.reset_index()
    df1["Population"] = abs(df1["Energy Supply"] /df1["Energy Supply per Capita"])
    df1.drop(df1.iloc[:, 1:21], inplace = True, axis = 1)
    df1 = df1.rename(columns={'index':'Country'})
    dfFinal = df1.groupby("Continent").agg({"Population":(np.count_nonzero,np.sum,np.nanmean,np.nanstd)})
    dfFinal.columns = ['size', 'sum', 'mean', 'std']
    return dfFinal
answer_eleven()

#1.1.10 Question 12 -  <--WINNER (Option with function)

import pandas as pd
import numpy as np
import re

#Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these...
#...new % Renewable bins. How many countries are in each of these groups?

#This function should return a Series with a MultiIndex of Continent, then...
#...the bins for % Renewable. Do not include groups with no countries.

#Story:
    #1.I just took the same function "1.0.1 Question 1 (Part 1)".
    #2.I create a Dataframe with the dictionary called "dfDictio12"
    #3.I apply the transpose of the newly created dataframe "dfDictio12" to...
    #...adjust the values; therefore I create the new datafrane called...
    #..."dfDictio12Transpose".
    #4.After that I merge my dataframe generated in the...
    #...."1.0.1 Question 1 (Part 1)" with the dataframe "dfDictio12Transpose"...
    #...to get the dataframe "df112". It is important to say that at the...
    #...moment of the merge both dataframes have in common the column of ...
    #..."Country" as index.
    #5.Then I reset the index of the dataframe "df112".
    #6.THen I drop all the columns except for the columns of "Country",...
    #..."Continent" and "% Renewable".
    #7.I rename the column of "Country".
    #8.I apply the code "groupby by" "aggregation" considering the "groupby"...
    #...of the column "Continent". In addition, the math operation with...
    #...Numpy (count all non zero elements) is applied in the columns of...
    #..."Country" and "% Renewable".
    #9.I reset the index
    #10.I applied a multiindex considering the columns of 'Continent'...
    #...and '% Renewable'.
    #11.I create a Serie from the dataframe, selecting to build this Serie...
    #...only the column "Country". As a consequence we get a Serie with this....
    #...column and the Serie also have the same index of the dataframe (like...
    #...inheritance).

def answer_twelve():
    #First:
    energy = pd.read_excel("Energy Indicators.xls", skiprows = 17, skipfooter= 38)
    #Second:
    energy.drop(["Unnamed: 0","Unnamed: 1"], inplace=True, axis=1)
    energy = energy.rename(columns={'Unnamed: 2':'Country',
                                 "Petajoules":"Energy Supply",
                                 "Gigajoules":"Energy Supply per Capita",
                                 "%":"% Renewable"})
    #Fourth: 
    energy = energy.replace(['...'],np.nan)
    #Fifth: 
    energy['Country']= energy['Country'].replace(['China, Hong Kong Special Administrative Region3',
                                              "Republic of Korea",
                                              "United Kingdom of Great Britain and Northern Ireland19",
                                              "United States of America20"],
                                             ['Hong Kong',
                                              "South Korea",
                                              "United Kingdom",
                                              "United States"])
    #Sixth: 
    energy["Country2"] = energy['Country']
    energy['Country2']= energy['Country'].replace('([0-9])','',regex=True)
    energy["Country3"] = energy['Country2']
    energy['Country3']= energy['Country2'].replace('\([\w ]*\)','',regex=True)
    energy = energy[['Country3',"Energy Supply","Energy Supply per Capita","% Renewable"]]
    energy = energy.rename(columns={'Country3':'Country'})
    #Third: 
    energy["Energy Supply"] = (energy["Energy Supply"])*1000000
    #Seventh:
    Gdp = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_1345540.csv',skiprows = 3)
    #Eigth: 
    Gdp['Country Name']= Gdp['Country Name'].replace(['Korea, Rep.',
                                              "Iran, Islamic Rep.",
                                              "Hong Kong SAR, China"],
                                             ["South Korea",
                                              "Iran",
                                              "Hong Kong"])
    #Ninth: 
    ScimEn = pd.read_excel("scimagojr country rank 1996-2019.xlsx")
    #Tenth: 
    ScimEn = ScimEn.set_index('Country')           
    energy = energy.set_index('Country')     
    Gdp = Gdp.set_index('Country Name')     
    DataMerge1= pd.merge(ScimEn, energy, how='left', left_index=True, right_index=True)
    DataMerge2= pd.merge(DataMerge1, Gdp, how='left', left_index=True, right_index=True)
    DataMerge2 = DataMerge2.head(15)                        
    DataMerge2.drop(['1960',
                     "1961",
                     "1962",
                     "1963",
                     "1964",
                     "1965",
                     "1966",
                     "1967",
                     "1968",
                     "1969",
                     "1970",
                     "1971",
                     "1972",
                     "1973",
                     "1974",
                     "1975",
                     "1976",
                     "1977",
                     "1978",
                     "1979",
                     "1980",
                     "1981",
                     "1982",
                     "1983",
                     "1984",
                     "1985",
                     "1986",
                     "1987",
                     "1988",
                     "1989",
                     "1990",
                     "1991",
                     "1992",
                     "1993",
                     "1994",
                     "1995",
                     "1996",
                     "1997",
                     "1998",
                     "1999",
                     "2000",
                     "2001",
                     "2002",
                     "2003",
                     "2004",
                     "2005",
                     "2017",
                     "2018",
                     "2019",], inplace=True, axis=1)                                                   
        #Eleventh: 
    DataMerge2.drop(['Region',
                     "Country Code",
                     "Indicator Name",
                     "Indicator Code",
                     "2016",
                     "Unnamed: 64",], inplace=True, axis=1)     
    #1.1.10 Question 12
    ContinentDict = {"China":"Asia",
                 "United States":"North America",
                 "Japan":"Asia",
                 "United Kingdom":"Europe",
                 "Russian Federation":"Europe",
                 "Canada":"North America",
                 "Germany":"Europe",
                 "India":"Asia",
                 "France":"Europe",
                 "South Korea":"Asia",
                 "Italy":"Europe",
                 "Spain":"Europe",
                 "Iran":"Asia",
                 "Australia":"Australia",
                 "Brazil":"South America"}
    dfDictio12 = pd.DataFrame(ContinentDict, index=['Continent'])
    dfDictio12Transpose = dfDictio12.T
    df112= pd.merge(DataMerge2, dfDictio12Transpose, how='outer', left_index=True, right_index=True)
    df112 = df112.reset_index()
    df112.drop(df112.iloc[:, 1:10], inplace = True, axis = 1)
    df112.drop(df112.iloc[:, 2:12], inplace = True, axis = 1)
    df112 = df112.rename(columns={'index':'Country'})
    dfFinal12 = df112.groupby("Continent").agg({"Country":np.count_nonzero,"% Renewable":np.count_nonzero})
    dfFinal12 = dfFinal12.reset_index()
    dfFinal12 = dfFinal12.set_index(['Continent', '% Renewable'])
    seriesx = dfFinal12.iloc[:,0]
    return seriesx
answer_twelve()

#1.1.11 Question 13 (6.6%)  <--WINNER (Option with function)

import pandas as pd
import numpy as np
import re

#Convert the Population Estimate series to a string with thousands separator...
#...(using commas). Do not round the results.
#e.g. 317615384.61538464 -> 317,615,384.61538464

#This function should return a Series PopEst whose index is the country name...
#...and whose values are the population estimate string.

#Story:
    #1.I just took the same function "1.0.1 Question 1 (Part 1)".
    #2.After that, I create a new column called "Population", which is a...
    #...division between the columns ["Energy Supply"] / ["Energy Supply per Capita"]
    #3.1.Then I locate the column "" in the dataframe and applied a "map()"...
    #...function over the column "PopEst"
        #Inside "map()" ww put a "function and an iterable", then...
        #..."map()" will create an object. This "object" contains the...
        #...output you would get from running each iterable element through...
        #...the supplied function.
        
        #Map() is iterable, so we can use like a for loop to look at all...
        #...of the values or items in the map(). 
    #3.2.To be specific, the function to apply is a change in...
    #...format of the numbers to a object "string" where thousands...
    #...are separate by commas{:,} (i.e. after this we generate the change...
    #...from one type of variable to another).
        #We can check this if we print the information of the dataframe...
        #..."DataMerge2.info()" before the format transformation (it will...
        #...show us the presence of "15 non-null object", i.e., the presence...
        #...of non-strings) and the description of the serie...
        #..."Series13.describe()" after the format transformation (it will...
        #...show us the presence of "object", i.e., the presence...
        #...of strings).
        
        #Pandas dtype (object) = Python type (str or mixed)
        #Usage = Text or mixed numeric and non-numeric values
                              
        #Pandas dtype (float64) = Python type (float)
        #Usage = 	Floating point numbers                
    #4.I drop all the columns except from "PopEst".
    #5.I create a Serie from the dataframe, selecting to build this Serie...
    #...only the column "PopEst". As a consequence we get a Serie with this....
    #...column and the Serie also have the same index of the dataframe (like...
    #...inheritance).

def answer_thirteen():
    #First:
    energy = pd.read_excel("Energy Indicators.xls", skiprows = 17, skipfooter= 38)
    #Second:
    energy.drop(["Unnamed: 0","Unnamed: 1"], inplace=True, axis=1)
    energy = energy.rename(columns={'Unnamed: 2':'Country',
                                 "Petajoules":"Energy Supply",
                                 "Gigajoules":"Energy Supply per Capita",
                                 "%":"% Renewable"})
    #Fourth: 
    energy = energy.replace(['...'],np.nan)
    #Fifth: 
    energy['Country']= energy['Country'].replace(['China, Hong Kong Special Administrative Region3',
                                              "Republic of Korea",
                                              "United Kingdom of Great Britain and Northern Ireland19",
                                              "United States of America20"],
                                             ['Hong Kong',
                                              "South Korea",
                                              "United Kingdom",
                                              "United States"])
    #Sixth: 
    energy["Country2"] = energy['Country']
    energy['Country2']= energy['Country'].replace('([0-9])','',regex=True)
    energy["Country3"] = energy['Country2']
    energy['Country3']= energy['Country2'].replace('\([\w ]*\)','',regex=True)
    energy = energy[['Country3',"Energy Supply","Energy Supply per Capita","% Renewable"]]
    energy = energy.rename(columns={'Country3':'Country'})
    #Third: 
    energy["Energy Supply"] = (energy["Energy Supply"])*1000000
    #Seventh:
    Gdp = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_1345540.csv',skiprows = 3)
    #Eigth: 
    Gdp['Country Name']= Gdp['Country Name'].replace(['Korea, Rep.',
                                              "Iran, Islamic Rep.",
                                              "Hong Kong SAR, China"],
                                             ["South Korea",
                                              "Iran",
                                              "Hong Kong"])
    #Ninth: 
    ScimEn = pd.read_excel("scimagojr country rank 1996-2019.xlsx")
    #Tenth: 
    ScimEn = ScimEn.set_index('Country')           
    energy = energy.set_index('Country')     
    Gdp = Gdp.set_index('Country Name')     
    DataMerge1= pd.merge(ScimEn, energy, how='left', left_index=True, right_index=True)
    DataMerge2= pd.merge(DataMerge1, Gdp, how='left', left_index=True, right_index=True)
    DataMerge2 = DataMerge2.head(15)                        
    DataMerge2.drop(['1960',
                     "1961",
                     "1962",
                     "1963",
                     "1964",
                     "1965",
                     "1966",
                     "1967",
                     "1968",
                     "1969",
                     "1970",
                     "1971",
                     "1972",
                     "1973",
                     "1974",
                     "1975",
                     "1976",
                     "1977",
                     "1978",
                     "1979",
                     "1980",
                     "1981",
                     "1982",
                     "1983",
                     "1984",
                     "1985",
                     "1986",
                     "1987",
                     "1988",
                     "1989",
                     "1990",
                     "1991",
                     "1992",
                     "1993",
                     "1994",
                     "1995",
                     "1996",
                     "1997",
                     "1998",
                     "1999",
                     "2000",
                     "2001",
                     "2002",
                     "2003",
                     "2004",
                     "2005",
                     "2017",
                     "2018",
                     "2019",], inplace=True, axis=1)                                                   
        #Eleventh: 
    DataMerge2.drop(['Region',
                     "Country Code",
                     "Indicator Name",
                     "Indicator Code",
                     "2016",
                     "Unnamed: 64",], inplace=True, axis=1)     
    #1.1.11 Question 13
    DataMerge2["PopEst"] = abs(DataMerge2["Energy Supply"] /DataMerge2["Energy Supply per Capita"])
    DataMerge2.loc[:, "PopEst"] =  DataMerge2["PopEst"].map('{:,}'.format)
    DataMerge2.drop(DataMerge2.iloc[:, 0:20], inplace = True, axis = 1)
    Series13 = DataMerge2.iloc[:,0]
    return Series13
answer_thirteen()
    
#M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M

#MICROTEST N°1: Testing the benefits of "turning off" or "turning on" the...
#..."as_index" and "sort" that belong to the "groupby" code at the same time...
#...and in different time.  

#RESULT 1: I can see clearly the differences in the printed output and how...
#...important is to set "True" both concepts ("as_index" and "sort") allowing...
#...us to see in a clear way how the groups are form in a ordered way and...
#...most important how different can be the results if they are ordered as...
#...True or as False.

#RESULT 2:Also the code "as_index" set in True show us a shortcut to set...
#...the index of the dataframe generated instead of use explicitly the code...
#..."set_index" as long as we use or apply some function or method in the...
#...groupby code (in this case the "agg()").

df55=pd.read_csv("listings.csv")

df56 = df55.groupby(['cancellation_policy',"review_scores_value"],as_index=False, sort=False).agg({"id":np.mean})
print ("Topic 6.2:","\n", df56)  
print("\n") 

df58=pd.read_csv("listings.csv")

df60 = df58.groupby(['cancellation_policy',"review_scores_value"],as_index=True, sort=True).agg({"id":np.mean})
print ("Topic 6.3:","\n", df60)  
print("\n") 

df59=pd.read_csv("listings.csv")

df62 = df59.groupby(['cancellation_policy',"review_scores_value"]).agg({"id":np.mean})
print ("Topic 6.4:","\n", df62)  
print("\n") 

df64=pd.read_csv("listings.csv")

df65 = df64.groupby(['cancellation_policy',"review_scores_value"],as_index=True, sort=False).agg({"id":np.mean})
print ("Topic 6.5:","\n", df65)  
print("\n") 

#M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M

#MICROTEST N°2: Testing the benefits of "turning off" or "turning on" the..
#..."as_index" that belong to the "groupby" code using "transform()" instead...
#...of code "agg()".

df66=pd.read_csv("listings.csv")

df67 = df66.groupby('cancellation_policy', as_index=True)["review_scores_value"].transform(np.nanmean)
df68 = df67.head()
print ("Topic 6.6:","\n", df68)  
print("\n") 

#RESULT: No matter if we set as "True" the "as_index=True" inside the transform...
#...we are going to get a "serie" (as in this case) or a dataframe with the...
#...same index of the original dataframe, supporting this the main idea that...
#..."transform()" code allow to combine its output later on with the original...
#...dataframe.

##RESULT:  Testing the benefits of "turning off" or "turning on" the...
#..."as_index" show us that only  work for the code "agg()".

#M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M

#MICROTEST N°3: Testing the type of data of my printed output when we use the...
#...way of code of "Michigan University" vs "Random Web Page".

#Way of code of "Michigan University"

print ("Topic 6.7:","\n", type(df49))  
print("\n")

#Way of code of "Random Web Page"

print ("Topic 6.8:","\n", type(df50))  
print("\n")

#RESULT: I can see that we get as a result a "dataframe" with...
#..."Michigan University" code and serie with "Random Web Page" code. I am not...
#...sure why. <---????????

#M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M+M





































                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    









