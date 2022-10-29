# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import pandas as pd
import numpy as np

#WEEK 3 (TRIAL VIDEOS)

#Topic 1: Dataframes in PANDAS
#First, we create a dataframe (it means a table with more than 2 columns),...
#...then when we print, we will see that the order of the title of the...
#...columns is alphabetically, no  matter if the order of the title of the...
#...columns in the code is in a differente way.
df = pd.DataFrame([{"Name":"Chris","Item Purchased":"Sponge","Cost":22.50},{"Name":"Kevyn","Item Purchased":"Kitty Litter","Cost":2.50}, {"Name":"Filip","Item Purchased":"Spoon","Cost":5.00}],index = ["Store 1", "Store 2", "Store 3"])
print ("Topic 1:\n",df)
print("\n")

#Topic 2: Add a column in a Dataframe in PANDAS
df["Date"] = ["January","March","June"]
print ("Topic 2:\n",df)
print("\n")
    
#Topic 3: Add a field in a Dataframe in PANDAS
df["Fancy"] = True
print ("Topic 3:\n",df)
print("\n")

#Topic 4: When we have the situation of unkown values in our dataframe, we...
#...have two options:
    
##Topic 4.1: Option 1: We can put ourselves the the unkown value in a new...
#...column or modifying and existing column, through the code "None"...
#..It means "None Type" in Python or "NaN = Not a Number" on Pandas...
#...Pandas does a conversion from "None Type" to "NaN". "Nan" is "Floting...
#...Point Value" (it means it is similar to None, but it is a special...
#...numerica value).

#In this case, we create a column in which we do not know the value number one.
df["Delivery Option"] = ["Yes",None,"No"]
print ("Topic 4.1:\n",df)
print("\n")

##Topic 4.2: Option 2: We can code in way that the computer itself put the...
#... code "None" in unkown values for the user (i.e.unkown values for the us)...
#...We can do that through the creation and application of an new index to...
#...he existing dataframe, then we create a Panda Series that will carry the...
#...values inside of the Dataframe, and in consequence will be created a...
#...new Dataframe that will reflect the new index.

#It is important to see that we put ourselve only the value zero and the...
#:..value two and then the computer automatically put the value of "NaN"...
#...in the value one (this "Nan" value is reflected when we print). In other...
#...words, PANDAS put for us the missing values.
dfnewindex = df.reset_index()
dfnewindex["Date"] = pd.Series({0:"January",2:"June"})
print ("Topic 4.2:\n",df)
print("\n")

##Topic 5: Wen we talk about merge dataframes, we have two of the following...
#...options:
    
#Option 1: Merge all the data of the two or more dataframes in one Dataframe...
#...In "DataBase Terminology" it is called the "Full outer join" (in Venn...
#...Diagram is called "Union"). In other words, we are mixing the index of...
#...two or more different dataframes.

##Option 2: Merge only the data of the two or more dataframes have in common..
#..in one Dataframe. In "DataBase Terminology" it is called the "Inner Join..
#...(in Venn Diagram is called "Intersection"). In other words, we are mixing...
#...the index of two or more different dataframes and only selecting the...
#...elements in common.

#It is important to see in the following instance that there are some common...
#...values between the dataframes. To be specific the will share or will...
#...connected through the index (in this case column "Name").
staff = pd.DataFrame([{"Name":"Kelly","Role":"Director of HR"},{"Name":"Sally","Role":"Course Liaison"}, {"Name":"James","Role":"Grader"}])
staff = staff.set_index("Name")
student = pd.DataFrame([{"Name":"James","School":"Business"},{"Name":"Mike","School":"Law"}, {"Name":"Sally","School":"Engineering"}])
student = student.set_index("Name")
print ("Topic 5:\n",staff)
print ("Topic 5:\n",student)
print("\n")

##Topic 5.1: Now we will merge both dataframes, from left to right (imagine...
#...a Venn Diagram), of all the values of the dataframe (because we are using...
#...the code "How=outer") and using the index as the connection between dataframes...
#...(in this case column "Name").

#We can see the the printed result will show cells of the merge dataframe fill...
#...with the value None ("nan"), because according to that index, there is no...
#...value in some columns (i.e. that the code automatically fill that unkown...
#...cell with the value None ("nan").
staffstud1 = pd.merge(staff,student, how ="outer",left_index=True,right_index=True)
print("Topic 5.1:\n",staffstud1)
print("\n")
    
##Topic 5.2: Now we will merge both dataframes, from left to right (imagine...
#...a Venn Diagram), of the common values of the dataframe (because we are using...
#...the code "How=inner") and using the index as the connection between dataframes...
#...(in this case column "Name").

#We can see the the printed result will show only values that we have in...
#...common between both dataframes.
staffstud2 = pd.merge(staff,student, how ="inner",left_index=True,right_index=True)
print("Topic 5.2:\n",staffstud2)
print("\n")

##Topic 5.3: Now we will merge both dataframes, from left to right (imagine...
#...a Venn Diagram), of the values of the dataframe that belong or share...
#...index with the left side (because we are using the code "How=left") and...
#...using the index as the connection between dataframes...
#...(in this case column "Name").

#We can see the the printed result will show only values that  belong or share...
#...index with the left side

#We can see the the printed result will show cells of the merge dataframe fill...
#...with the value None ("nan"), because according to that index, there is no...
#...value in some columns (i.e. that the code automatically fill that unkown...
#...cell with the value None ("nan").
staffstud3 = pd.merge(staff,student, how ="left",left_index=True,right_index=True)
print("Topic 5.3:\n",staffstud3)
print("\n")
    
##Topic 5.4: Now we will merge both dataframes, from left to right (imagine...
#...a Venn Diagram), of the values of the dataframe that belong or share...
#...index with the right side (because we are using the code "How=right") and...
#...using the index as the connection between dataframes...
#...(in this case column "Name").

#We can see the the printed result will show only values that  belong or share...
#...index with the right side

#We can see the the printed result will show cells of the merge dataframe fill...
#...with the value None ("nan"), because according to that index, there is no...
#...value in some columns (i.e. that the code automatically fill that unkown...
#...cell with the value None ("nan").
staffstud4 = pd.merge(staff,student, how ="right",left_index=True,right_index=True)
print("Topic 5.4:\n",staffstud4)
print("\n")
    
#Topic 5.5: Also we have the available option of using a different "column" 
#...instead of the previous "index" like the connection between...
#...dataframes. Therefore, we apply the following code in which we reset the...
#...index and then the index (column "Name") is not anymore the index column (i.e...
#...it is now just another column in the dataframe, in this case the other...
#...column in the dataframe is called "Name"), and that column will be...
#...very helpful to be the connection between dataframes. The new index...
#...will be 1,2,3,4,...

#Also it is important to say that the "reseting of index column" need to be...
#...applied to all the dataframes. Morover, we need to put in the code the...
#...name of the new index column, in this is called "Name"

staffnewindex = staff.reset_index()
studentnewindex = student.reset_index()
staffstud5 = pd.merge(staffnewindex,studentnewindex, how ="left",left_on="Name",right_on="Name")
print("Topic 5.5:\n",staffstud5)
print("\n")

#Topic 6: Conflict between dataframes. First, we need to create the dataframes.
staff2 = pd.DataFrame([{"Name":"Kelly","Role":"Director of HR","Location":"Panama"},{"Name":"Sally","Role":"Course Liaison","Location":"Bogota"}, {"Name":"James","Role":"Grader","Location":"Panama"}])
staff2 = staff2.set_index("Name")
student2 = pd.DataFrame([{"Name":"James","School":"Business","Location":"USA"},{"Name":"Mike","School":"Law","Location":"Morocco"}, {"Name":"Sally","School":"Engineering","Location":"Sweden"}])
student2 = student2.set_index("Name")
print ("Topic 6:\n",staff2)
print ("Topic 6:\n",student2)
print("\n")

#Topic 6.1: Then we merge the dataframes and also reset the index in the same...
#...way we did in the Topic 5.3 and Topic 5.5.

#We will see when we print the merge dataframe that appear two new columns...
#...called "Location_X" and "Location_Y" because it detects that the data....
#...that share info in common have conflicts (specifically in the column of...
#..."Location"), it means that for the same index, we have the same column...
#...but that column with different data. Therefore, the print dataframe...
#...separate the column wiht that situation in two or more columns, called...
#...the subindex X (for the left side info "thinking of Venn Diagram"),Y(for..
#...the right side info "thinking of Venn Diagram").

#...According to thee teacher the subindex X,Y,..etc can be change with other...
#...parameters.
                   
staffnewindex2 = staff2.reset_index()
studentnewindex2 = student2.reset_index()
staffstud11 = pd.merge(staffnewindex2,studentnewindex2, how ="left",left_on="Name",right_on="Name")
print("Topic 6.1:\n",staffstud11)
print("\n")

#MicroTest1****************************************************************
#First, we create the frames
Product = pd.DataFrame([{"Product ID":"4109","Price":5.0,"Product":"Sushi Roll"},{"Product ID":"1412","Price":0.5,"Product":"Egg"}, {"Product ID":"8931","Price":1.5,"Product":"Bagel"}])
Product = Product.set_index("Product ID")
Invoice = pd.DataFrame([{"Customer":"Ali","Product ID":"4109","Quantity":1},{"Customer":"Eric","Product ID":"1412","Quantity":12}, {"Customer":"Ande","Product ID":"8931","Quantity":6}, {"Customer":"Sam","Product ID":"4109","Quantity":2}])
Invoice = Invoice.set_index("Product ID")
print ("Topic 7:\n",Product)
print ("Topic 7:\n",Invoice)
print("\n")

#Second, we merge both dataframes with the "Product ID" as the guide index...
#...to do the merge.
ProdInv = pd.merge(Product,Invoice, how ="outer",left_index=True,right_index=True)
print("Topic 7.1:\n",ProdInv)
print("\n")

#Third, we merge both dataframes with the "Product ID" as the guide index...
#...to do the merge. And then we create a column called "Total" as a result...
#...of the multiplication of columns "Price" and "Quantity".
ProdInv["Total"]= ((ProdInv["Price"])*(ProdInv["Quantity"]))
print("Topic 7.3:\n",ProdInv)
print("\n")
#MicroTest1******************************************************************

#Topic 8: Multiple Columns and Multindexing

#Topic 8.1: In this case we have other option to deal with conflicts between...
#...data in the dataframes. In this case we have the option to use more than...
#...one column to apply the index. In this case the index arrange will be...
#...done through the columns of "Name" and "Lastname"

#Another fun fact about this new thecnique is that we do no set any index...
#...previously to the establishment of the index arrange of several columns.
staff3 = pd.DataFrame([{"Name":"Kelly","Lastname":"Preston","Role":"Director of HR"},{"Name":"Sally","Lastname":"Salada","Role":"Course Liaison"}, {"Name":"James","Lastname":"Bond","Role":"Grader"}])
student3 = pd.DataFrame([{"Name":"James","Lastname":"Rodriguez","School":"Business"},{"Name":"Mike","Lastname":"Mouse","School":"Law"}, {"Name":"Sally","Lastname":"Salada","School":"Engineering"}])
staffstud22 = pd.merge(staff3,student3, how ="inner",left_on=["Name","Lastname"],right_on=["Name","Lastname"])
print("Topic 8.1:\n",staffstud22)
print("\n")

#############################################################################

#Topic 9: Idiomatics.

#Why vectorization instead of iterable loop?

dfcensus = pd.read_csv("census.csv")
print("Topic 9:\n",dfcensus)
print("\n")

dfcensus0 = pd.read_csv("census.csv")
print("Topic 9:\n",dfcensus0)
print("\n")

#Topic 9.1:There is another way to set the index of a dataframe with take in count...
#...the columns that belong to that data frame
dfcensus0 = dfcensus0[dfcensus["SUMLEV"]==50]
dfcensus0.set_index(["STNAME","CTYNAME"],inplace=True)

#Topic 9.2.1:The following code is very usdeful to change the name of the...
#..title of a.columns of a dataframe.

#It is important to say that we will do the change of the title of a column...
#...of a dataframe through a mapper or a dictionary with old name as keys and...
#...new name as values. 
dfcensus0.rename(columns={"ESTIMATESBASE2010":"ESBA2010"}, inplace=True)
print("Topic 9.2.1:\n",dfcensus0)
print("\n")

#Topic 9.2.2:The following code is very useful to change the name of the...
#..title of a row of a dataframe.

#It is important to say that we will do the change of the title of a row...
#...of a dataframe through a mapper or a dictionary with old name as keys and...
#...new name as values. 
dfcensus0.rename(index={"Alabama":"Obama"}, inplace=True)
print("Topic 9.2.2:\n",dfcensus0)
print("\n")

#Topic 9.3:The dropna() function is used to remove missing values.
#Code: DataFrame.dropna(self, axis=0, how='any', thresh=None, subset=None, inplace=False)

##Topic 9.3.1:If we use only "dropna()" this code will delete all the rows...
#...and columns that have a None Vale (NaN). And then will print the...
#...dataframe with the existing values.
staff4 = pd.DataFrame([{"Name":"Kelly","Role":"Director of HR","Location":None},{"Name":"Sally","Role":None,"Location":"Bogota"}, {"Name":"James","Role":"Teacher","Location":"Panama"}])
staff4 = staff4.dropna()
print("Topic 9.3.1:\n",staff4)
print("\n")

#Topic 9.3.2.1:If we use "dropna(axis =1)" this code will delete all the columns...
#...that have a None Vale (NaN). And then will print the dataframe with...
#...the columns that have existing values.
staff5 = pd.DataFrame([{"Name":"Kelly","Role":"Director of HR","Location":None},{"Name":"Sally","Role":None,"Location":"Bogota"}, {"Name":"James","Role":"Teacher","Location":"Panama"}])
staff5 = staff5.dropna(axis=1)
print("Topic 9.3.2.1:\n",staff5)
print("\n")

#Topic 9.3.2.2:If we use "dropna(axis ="columns")"this code will delete all...
#...the columns that have a None Vale (NaN). And then will print the...
#...dataframe with the columns that have existing values.

#There is another way to play with the axis. In this case instead of refer...
#....to the columns like "axis=1" we can use (axis = "columns") and the result...
#...will be the same.

staff6 = pd.DataFrame([{"Name":"Kelly","Role":"Director of HR","Location":None},{"Name":"Sally","Role":None,"Location":"Bogota"}, {"Name":"James","Role":"Teacher","Location":"Panama"}])
staff6 = staff6.dropna(axis="columns")
print("Topic 9.3.2.2:\n",staff6)
print("\n")

#Topic 9.3.2.3:If we use "dropna(axis =0)" this code will delete all the rows...
#...that have a None Vale (NaN). And then will print the dataframe with...
#...the rows that have existing values.
staff7 = pd.DataFrame([{"Name":"Kelly","Role":"Director of HR","Location":None},{"Name":"Sally","Role":None,"Location":"Bogota"}, {"Name":"James","Role":"Teacher","Location":"Panama"}])
staff7 = staff7.dropna(axis=0)
print("Topic 9.3.2.3:\n",staff7)
#print("\n")

#Topic 9.3.2.4:If we use "dropna(axis ="index")"this code will delete all...
#...the rows that have a None Vale (NaN). And then will print the...
#...dataframe with the columns that have existing values.

#There is another way to play with the axis. In this case instead of refer...
#....to the rows like "axis=0" we can use (axis = "index") and the result...
#...will be the same.

staff8 = pd.DataFrame([{"Name":"Kelly","Role":"Director of HR","Location":None},{"Name":"Sally","Role":None,"Location":"Bogota"}, {"Name":"James","Role":"Teacher","Location":"Panama"}])
staff8 = staff8.dropna(axis="index")
print("Topic 9.3.2.4:\n",staff8)
print("\n")

#Topic 9.3.2.5:If we use "dropna()", we also have the option to delete the...
#...parts of the dataframe (no matter if that is a column or a row) with the...
#....following code:
    
#If we want to delete an entire row or an entire column only if all their...
#...values are None Vale (NaN) we use the code dropna(how='all')

staff9 = pd.DataFrame([{"Name":"Kelly","Role":"Director of HR","Location":None},{"Name":"Sally","Role":None,"Location":"Bogota"}, {"Name":"James","Role":"Teacher","Location":"Panama"}])
staff9 = staff9.dropna(how="all")
print("Topic 9.3.2.5:\n",staff9)
print("\n")

#Topic 9.3.2.6:If we use "dropna()", we also have the option to delete the...
#...parts of the dataframe (specifically a row) with the following code:
    
#If w want to delete an entire row only if any of their values are None Vale...
#...(NaN) we use the code dropna(how='any').

staff10 = pd.DataFrame([{"Name":"Kelly","Role":"Director of HR","Location":None},{"Name":"Sally","Role":None,"Location":"Bogota"}, {"Name":"James","Role":"Teacher","Location":"Panama"}])
staff10 = staff10.dropna(how="any")
print("Topic 9.3.2.6:\n",staff10)
print("\n")

#Topic 9.3.2.7:If we use "dropna()", we also have the option to delete rows...
#...from specific columns of the dataframe with the following code:    
staff11 = pd.DataFrame([{"Name":"Kelly","Role":"Director of HR","Location":None},{"Name":"Sally","Role":None,"Location":"Bogota"}, {"Name":"James","Role":"Teacher","Location":"Panama"}])
staff11 = staff11.dropna(subset=["Role", "Location"])
print("Topic 9.3.2.7:\n",staff11)
print("\n")

#Topic 9.3.2.8:If we use "drop", we also have the option to delete rows...
#...from specific columns of the dataframe with the following code, in this...
#...case the code is write in this particular way from outside to inside (...
#...selected dataframe, selected row and selected column.
staff14 = pd.DataFrame([{"Name":"Kelly","Role":"Director of HR","Location":0},{"Name":"Sally","Role":None,"Location":0}, {"Name":"James","Role":"Teacher","Location":"Panama"}])
staff14 = staff14.drop(staff14[staff14["Location"]==0].index)
print("Topic 9.3.2.7:\n",staff14)
print("\n")

#Topic 9.4:The "inplace parameter" is just a code that allow us to establish...
#...if the change that we want to do to thee dataframe will be reflectde and...
#....permanently in that dataframe. In other words if we set the the...
#...."inplace parameter" as True, we will overwrite the original dataframe...
#...ad if we set the "inplace parameter" as False, (it means, its default...
#...value) we will not change anything in  the original dataframe.

#It is an advice to make a copy of the dataframe, if we want to set the...
#..."inplace parameter" as True to maintain the original untouchable.

#Topic 9.5:Practicing the "Pandas Method Chaining". There are the main ideas:

#First: This is a method in what we write code of a PANDAS (objects and...
#...methods of dataframes and series) in a readable way and with the concept..
#...that we use the result of one method object, in the following method...
#...object and so on (like a chain).

#Second: The code is wrote in a single line or in a couple of lines with...
#...certain indentation in the following lines after of the first line (that...
#...will show the result).

#Third: Python is an Object Oriented Programming Language. Unlike procedure...
#...oriented programming, where the main emphasis is on functions, object...
#...oriented programming stresses on objects.

#Fourth: An Object is simply a collection of data (variables) and Methods...
#...(Functions) that act on those data.

#Fifth:Their primary reasons for preferring method chains are readability and...
#...performance (since the method chain tells pandas everything you want to...
#...do ahead of time, pandas can plan its operations more efficiently). We...
#...can prove it if use "time code" to calcule how long it will take to...
#...dothee job.

#Sexth: the downside of the ""chaining code" is that sometimes is hard to...
#...find the due to do not have a intermediate mechanism to inspect or check...
#...the code.

#The first intance of how we apply the "chaining code" is the following...
#...(certain indentation in the following lines after of the first line that...
#...will show the result directly).

staff12 = pd.DataFrame([{"Name":"Kelly","Role":"Director of HR","Location":None},{"Name":"Sally","Role":None,"Location":"Bogota"}, {"Name":"James","Role":"Teacher","Location":"Panama"}])
resultstaff12 =  (staff12.dropna(subset=["Location"])
                         .rename(columns={"Role":"Work"}))
print("Topic 9.5.1:\n",resultstaff12)
print("\n")

#The second intance of how we apply the "chaining code" is the following...
#...(only first line that will show the result directly).

staff13 = pd.DataFrame([{"Name":"Kelly","Role":"Director of HR","Location":None},{"Name":"Sally","Role":None,"Location":"Bogota"}, {"Name":"James","Role":"Teacher","Location":"Panama"}])
resultstaff13 =  (staff13.dropna(subset=["Location"]).rename(columns={"Role":"Work"}))
print("Topic 9.5.2:\n",resultstaff13)
print("\n")

#Topic 9.6: Another important fact about "sort" is that we can select how...
#...many elements sorted we want to see (it means, "print") through the..
#...square brackets at the end of the code (in this instance, we use [0:2]...
#...which means the rows 0 and 1, exclusive row 2 of the column called "Price"). 
#Also it is important to clarify that when the sort is "Ascending = False",...
#...it means that the result will be showed in a descending way (from the...
#...highest value to the lowest value).

Product2 = pd.DataFrame([{"Product ID":"4109","Price":5.0,"Product":"Sushi Roll"},{"Product ID":"1412","Price":0.5,"Product":"Egg"}, {"Product ID":"8931","Price":1.5,"Product":"Bagel"}])
Product3 = Product2.sort_values('Price', ascending=False)[:2]
print ("Topic 9.6:\n",Product3)
print("\n")

#Topic 9.7: Another important code in PANDAS is use of "Lambda Function". It..
#...is a type of function that allow us to apply a function several times...
#...in a the elements of a dataframe (for instance: the elements of a column)...
#...without the necessity to write a traditional code or declaration of a...
#...function. However, we are not able to recycle this kind of lambda function.

#In this case, we use the "Lambda Function" to do a filter, and then saved...
#...the result of the filter.

#The return of the "Lambda Function" will be "True or False", it means, that...
#...the "Lambda Function" is a boolean function which printed results are...
#...True or False..

Product4 = pd.DataFrame([{"Product ID":"4109","Price":5.0,"Product":"Sushi Roll"},{"Product ID":"1412","Price":0.5,"Product":"Egg"}, {"Product ID":"8931","Price":1.5,"Product":"Bagel"}])
Product4['NewPrice'] = Product4['Price'].apply(lambda x: x > 3)
print ("Topic 9.7:\n",Product4)
print("\n")

Product7 = pd.DataFrame([{"Product ID":"4109","Price":5.0,"Product":"Sushi Roll"},{"Product ID":"1412","Price":0.5,"Product":"Egg"}, {"Product ID":"8931","Price":1.5,"Product":"Bagel"}])
Product7['NewPrice'] = Product7['Price'].apply(lambda x: x**2)
print ("Topic 9.7:\n",Product7)
print("\n")


#Topic 9.8: If we want to work with some statistics, we can "counts" the...
#...values of the data, taking as a reference one column. For instance:...
#...this code count the how many values we have the column. For instance...
#...if we have the following values in the analized column (it means...
#...in every row of that column we have a value): 1,2,3,4,3 then code...
#...will print has a resulta that we have in the analized column the...
#...following: 1 value of 1, 1 value of 2, 2 values of 3 and 1 value of 4.

#In this case the printed result of the "counts code" is a Serie, in which...
#...the index is the column that we select to apply the "counts code".
Product4Count= Product4['Price'].value_counts()
print ("Topic 9.8:\n",Product4Count)
print("\n")

#Topic 9.9: If we want to group or re-arrange the data of dataframe...
#...according with type of data that they have in the columns, we have the...
#...the code "group by" and the result will be expressed in a "dataframegroupby"...
#...object (we can overwrite the old dataframe or we can create a new dataframe)

#...The is a lil bit trickier because we need to express what we are going to...
#...do with the grouped values (those that have or share the same values and...
#... those that do not have or share the same values), in this case we use...
#...the code "count"  to express what we are going to do with the grouped...
#...values.

#In this case the printed result of the "groupby code" is a dataframe, in which...
#...the index is the columns that we select to apply the "groupby code".

Product5 = pd.DataFrame([{"Product ID":"4109","Price":5.0,"Product":"Sushi Roll"},{"Product ID":"1412","Price":0.5,"Product":"Egg"}, {"Product ID":"8931","Price":1.5,"Product":"Bagel"},{"Product ID":"4567","Price":5.0,"Product":"Chicken"},{"Product ID":"4567","Price":5.0,"Product":"Chicken Wings"},{"Product ID":"4567","Price":5.0,"Product":"Chicken Soup"}])
Product5 = Product5.groupby(["Price","Product ID"]).count().unstack()
print ("Topic 9.9:\n",Product5)
print("\n")

#Topic 9.9: The use of the code "unstack" allow us to see in a more readable...
#...way the result executed by the code "groupby"

Product6 = pd.DataFrame([{"Product ID":"4109","Price":5.0,"Product":"Sushi Roll"},{"Product ID":"1412","Price":0.5,"Product":"Egg"}, {"Product ID":"8931","Price":1.5,"Product":"Bagel"},{"Product ID":"4567","Price":5.0,"Product":"Chicken"},{"Product ID":"4567","Price":5.0,"Product":"Chicken Wings"},{"Product ID":"4567","Price":5.0,"Product":"Chicken Soup"}])
Product6 = Product6.groupby(["Price","Product ID"]).count().unstack()
print ("Topic 9.9.1:\n",Product6)
print("\n")

#############################################################################

#Topic 10: Group By.

#Topic 10: We can use function (invented by us), lambdas (invented by us)...
#...combined with a loop to iterate over the data ann get some information...
#...The other option we have is to use the code "GroupBy"

#Topic 10.1.1: The use of the code "unique()" allow us to do a filter and only...
#...see the unique values that have a serie have. The result is an array...
#...of numbers, in this case the printed result will be 2,1 and 3.

Product7 = pd.unique(pd.Series([2, 1, 3, 3]))
print ("Topic 10.1.1:\n",Product7)
print("\n")

#Topic 10.1.2: The use of the code "where()" allow us to do a filter (based...
#...in some conditions) in the dataframe. The result is the filtered dataframe.
#By default, the rows not satisfying the condition are filled with NaN value.
#To be specific the rules of the code "where()" is the following:
#DataFrame.where(cond, other=nan, inplace=False, axis=None, level=None, errors=’raise’, try_cast=False, raise_on_error=None)
#Parameters:
    #cond: One or more condition to check data frame for.
    #other: Replace rows which don’t satisfy the condition with user...
    #....defined object, Default is NaN
    #inplace: Boolean value, Makes changes in data frame itself if True
    #axis: axis to check( row or columns) 

Product8 = pd.DataFrame([{"Product ID":"4109","Price":5.0,"Product":"Sushi Roll"},{"Product ID":"1412","Price":0.5,"Product":"Egg"}, {"Product ID":"8931","Price":1.5,"Product":"Bagel"},{"Product ID":"4567","Price":7.0,"Product":"Chicken"},{"Product ID":"4567","Price":23.0,"Product":"Chicken Wings"},{"Product ID":"4567","Price":11.0,"Product":"Chicken Soup"}])
Filter1 = Product8["Price"]>5
Product8.where (Filter1, inplace=True)
print ("Topic 10.1.2:\n",Product8)
print("\n")

#Topic 10.2: There are several ways to iterate over the data of a dataframe...
#...We will describe the followings:

##Topic 10.2.1: We can use use a "For Loop" to iterate over the data of a...
#...dataframe; however, we need to be careful to set the values in what we are...
#...going to iterate, because if we use in a simple way the "loop", we are...
#...going to only obtain the title of the dataframe´s columns.

Product9 = pd.DataFrame([{"Product ID":"4109","Price":5.0,"Product":"Sushi Roll"},{"Product ID":"1412","Price":0.5,"Product":"Egg"}, {"Product ID":"8931","Price":1.5,"Product":"Bagel"},{"Product ID":"4567","Price":7.0,"Product":"Chicken"},{"Product ID":"4567","Price":23.0,"Product":"Chicken Wings"},{"Product ID":"4567","Price":11.0,"Product":"Chicken Soup"}])

for Value1 in Product9:
    print("Topic 10.2.1:\n",Value1)
print("\n")

#Topic 10.2.2: We can use use a "For Loop" to iterate over the data of a...
#...dataframe; therefore, we can establish the that the "For loop" work in...
#...rows through the code "iterrows()". The result will be that the code...
#...printed every single row of the dataframe (index and data together).

Product10 = pd.DataFrame([{"Product ID":"4109","Price":5.0,"Product":"Sushi Roll"},{"Product ID":"1412","Price":0.5,"Product":"Egg"}, {"Product ID":"8931","Price":1.5,"Product":"Bagel"},{"Product ID":"4567","Price":7.0,"Product":"Chicken"},{"Product ID":"4567","Price":23.0,"Product":"Chicken Wings"},{"Product ID":"4567","Price":11.0,"Product":"Chicken Soup"}])

for Value2 in Product10.iterrows():
    print("Topic 10.2.2:\n",Value2) 
print("\n")    

#Topic 10.2.3: We can use use a "For Loop" to iterate over the data of a...
#...dataframe; therefore, we can establish the that the "For loop" work in...
#...rows through the code "iterrows()". The result will be that the code...
#...printed every single row of the dataframe (index and data separatly).

#It is important to say that when we use the two iterable variables, one of...
#...variables (especificaly the first declared variable) iterate over the...
#...index column of the dataframe or serie. Meanwhile, the second declared...
#...variable iterate over the rest of the dataframe or serie or over a specific...
#...column of the dataframe (if we determine this).

Product11 = pd.DataFrame([{"Product ID":"4109","Price":5.0,"Product":"Sushi Roll"},{"Product ID":"1412","Price":0.5,"Product":"Egg"}, {"Product ID":"8931","Price":1.5,"Product":"Bagel"},{"Product ID":"4567","Price":7.0,"Product":"Chicken"},{"Product ID":"4567","Price":23.0,"Product":"Chicken Wings"},{"Product ID":"4567","Price":11.0,"Product":"Chicken Soup"}])

for Value3, Value4 in Product11.iterrows():
    print("Topic 10.2.3.1:\n",Value3) 
    print("Topic 10.2.3.2\n",Value4) 
print("\n")  

#Topic 10.2.4: We can use use a "For Loop" to iterate over the data of a...
#...dataframe; therefore, we can establish the that the "For loop" work in...
#...rows through the code "iterrows()". The result can be also that the code...
#...printed row values of a specific column in the dataframe.

#It is important to say that when we use the two iterable variables, one of...
#...variables (especificaly the first declared variable) iterate over the...
#...index column of the dataframe or serie. Meanwhile, the second declared...
#...variable iterate over the rest of the dataframe or serie or over a specific...
#...column of the dataframe (if we determine this).

Product12 = pd.DataFrame([{"Product ID":"4109","Price":5.0,"Product":"Sushi Roll"},{"Product ID":"1412","Price":0.5,"Product":"Egg"}, {"Product ID":"8931","Price":1.5,"Product":"Bagel"},{"Product ID":"4567","Price":7.0,"Product":"Chicken"},{"Product ID":"4567","Price":23.0,"Product":"Chicken Wings"},{"Product ID":"4567","Price":11.0,"Product":"Chicken Soup"}])

for Value5, Value6 in Product12.iterrows():
    print(Value5) 
    print("Topic 10.2.4",Value6["Price"]) 
print("\n")  

#Topic 10.2.5: We can use use a "For Loop" to iterate over the data of a...
#...dataframe; therefore, we can establish the that the "For loop" work in...
#...rows through the code "iterrows()". The result can be also that the code...
#...printed values in a brand new columm in the dataframe.

#It is important to say that when we use the two iterable variables, one of...
#...variables (especificaly the first declared variable) iterate over the...
#...index column of the dataframe or serie. Meanwhile, the second declared...
#...variable iterate over the rest of the dataframe or serie or over a specific...
#...column of the dataframe (if we determine this).

Product13 = pd.DataFrame([{"Product ID":"4109","Price":5.0,"Product":"Sushi Roll"},{"Product ID":"1412","Price":0.5,"Product":"Egg"}, {"Product ID":"8931","Price":1.5,"Product":"Bagel"},{"Product ID":"4567","Price":7.0,"Product":"Chicken"},{"Product ID":"4567","Price":23.0,"Product":"Chicken Wings"},{"Product ID":"4567","Price":11.0,"Product":"Chicken Soup"}])

for Value7, Value8 in Product13.iterrows():
    Product13.loc[Value7, "Total"] = Value8["Price"]*2
print("Topic 10.2.5:\n",Product13) 
print("\n")  
                                                                     
                                                                       
#Topic 10.3.1: We use a "For Loop" (with one iterative variable) to apply an...
#...operation in the dataframe.
#...First, we adjust the data to only see rows with values en SUMLEV =50....
#...Then we apply a "For Loop" in a specific column of the dataframe (not in...
#...the all dataframe) with the code "unique()".After that, we use a code...
#...of Numpy "np" to apply the function "average" due to Panda Dataframe does...
#...not has this function "average". It is important to say that the function...
#..."average" is combined with the code "where" to apply especifically the...
#..."average" of the column "CENSUS2010POP", when the "STNAME" is same of...
#...the iterative variable that move through the column "STNAME", and even...
#...at the same time we are removing missing values with the function...
#..."dropna()"

dfcensus1 = pd.read_csv("census.csv")
dfcensus1 = dfcensus1[dfcensus1["SUMLEV"]==50]

for X in dfcensus1["STNAME"].unique():
    avg = np.average(dfcensus1.where(dfcensus1["STNAME"]== X).dropna()["CENSUS2010POP"])             
    print ("Topic 10.3.1:\n",X, str(avg))
print("\n")

#Topic 10.3.2: We use a "For Loop" (with two iterative variables) to apply an...
#...operation in the dataframe.
#...First, we adjust the data to only see rows with values en SUMLEV =50....
#...Then we apply a "For Loop"(with two variables), one iterative variable...
#...(called "group2") for a specific column of the dataframe that we select...
#...with the code "groupby()". After that, we use a code of Numpy "np" to...
#...apply the function "average" due to Panda Dataframe does not has this function....
#..."average". It is important to say that the function "average" is combined...
#...with the second iterative variablev(called "frame2") to apply...
#...especifically the "average" of the column "CENSUS2010POP", when the...
#..."STNAME" is same of the iterative variable that move through the column...
#..."STNAME".

#Just for th record, this code of "Topic 10.3.2" is faster than the code...
#...of "Topic 10.3.1.

dfcensus2 = pd.read_csv("census.csv")
dfcensus2 = dfcensus2[dfcensus2["SUMLEV"]==50]

for group2, frame2 in dfcensus2.groupby(["STNAME"]):
    avg = np.average(frame2["CENSUS2010POP"])             
    print ("Topic 10.3.2:\n",group2, str(avg))
print("\n")

#Topic 10.4: Application of a groupby() in a function (that apparently contains..
#...the dataframe or serie) and not in column dataframe directly. This is...
#...to simple apply the segmentation of the data with a function instead...
#...of do that with groupby() directly.

#We need to be aware that it is a clever way to select the part of the...
#...dataframa that we are interesting to work.

#For instance, we establish the index to be the column "STNAME". Then we...
#...create a function that will iterate in this case over index column...
#..."STNAME" and will return the values of 0, 1 or 2 (if the first letter...
#...of the index name begin with "M", "Q" or anything else). Then we apply....
#...a "for loop" code in the dataframe considering the effect of the function...
#...to segment the data of the dataframe (it means that we are going to...
#...iterate over segmented data by the funtion).

#Important: We are applying just one function to one column.

dfcensus3 = pd.read_csv("census.csv")
dfcensus3 = dfcensus3.set_index("STNAME")

def function1(item):
    if item[0]<"M":
        return 0
    elif item[0]<"Q":
        return 1
    else:
        return 2
        
for group3, frame3 in dfcensus3.groupby(function1):            
    print ("Topic 10.4.1:\n",str(group3))
    print ("Topic 10.4.2:\n",str(len(frame3)))
print("\n")
                           
#Topic 10.5: The "Split - Apply - Combine Pattern".Apparently, allow us to...
#...."split the data, apply some funcion and then combine the results". In...
#...other words, it is another way to group and apply segmentation of the...
#...data.

#"Agg Method": Is a function of the code "GroupBy". Also called "Aggregate...
#...Function", it can apply a function to a column or columns of dataframe...
#...and return a dataframe or a serie (The output from a "Groupby and...
#...Aggregation" operation varies between Pandas Series and Pandas Dataframes...
#...as a rule of thumb, if you calculate more than one column of results,...
#...your result will be a Dataframe. For a single column of results,...
#...the agg function, by default, will produce a Series.

#For a DataFrame, when we use the "Agg Method", we use the dictionary format...
#...if the "keys" (it means, dictionary keys) are "DataFrame column names" and...
#...the "function or functions" we want to apply to those "Dataframes...
#...column names" are the "values" (it means, dictionary values). However,...
#...other accepted combinations are:
    #...string function name.
    #...function.
    #...list of functions.
    #...dict of column names -> functions (or list of functions).

#In this case we use the dictionary combination ({column name: function}) and...
#...the end result is a Panda Series, where the index of the Panda Serie is...
#...column of "STNAME" (it is important to say that in this case the...
#...segmentation in the dataframe is due to the groupby"STNAME"), and the...
#...the other column is just the "CENSUS2010POP" averaged (it means, the...
#...column which receive the effect of the function).
                           
dfcensus4 = pd.read_csv("census.csv")
dfcensus4 = dfcensus4[dfcensus4["SUMLEV"] == 50]
        
SerieCensus4 = dfcensus4.groupby("STNAME").agg({"CENSUS2010POP":np.average})
print("Topic 10.5:\n",SerieCensus4)
print("\n")

#Topic 10.5.1:The aggregation dictionary syntax is flexible and can be...
#...defined before the operation.

#Important: We are applying just one function to one column.

dfcensus5 = pd.read_csv("census.csv")
dfcensus5 = dfcensus5[dfcensus5["SUMLEV"] == 50]

aggregationfunc1 = {"CENSUS2010POP":np.average}
        
SerieCensus5 = dfcensus5.groupby("STNAME").agg(aggregationfunc1)
print("Topic 10.5.1:\n",SerieCensus5)
print("\n")

#Topic 10.5.2:The "Apply Function" can be use as an alternative of the...
#..."Aggregate Function" when we use the Pandas code "GroupBy". 

#In a simple way, is the application of a function (being the the first argument)
#...in a dataframe (being the the second argument) of the GroupBy code. The...
#...main disavantage is that there is a bit slower than "Aggregate Function".

#...In the case of the first argument, we can set it previously, with the...
#...specific column (of the dataframa) in which we want to apply the function.
#...Thererefore, we can establish as a second argument of the "GroupBy.Apply"...
#...or the name of the datafram or the name of specific column...
#...(of the dataframa) in which we want to apply the function.

#...In the case of the second argument, that could be dataframe.

#The return of the "GroupBy.Apply" will be dataframe or a serie or even a...
#...scalar. 

#Important: We are applying just one function to one column.

dfcensus7 = pd.read_csv("census.csv")
dfcensus7 = dfcensus7[dfcensus7["SUMLEV"] == 50]

def function2(dfcensus7,Xnum):
    return sum (dfcensus7["CENSUS2010POP"])

SerieCensus7 = dfcensus7.groupby("STNAME").apply(function2,dfcensus7)
print("Topic 10.5.2:\n", SerieCensus7)
print("\n")

#Topic 10.5.3:The "Apply Function" can be use as an alternative of the...
#..."Aggregate Function" when we use the Pandas code "GroupBy". 

#In a simple way, is the application of a function (being the the first argument)
#...in a dataframe (being the the second argument) of the GroupBy code. The...
#...main disavantage is that there is a bit slower than "Aggregate Function".

#...In the case of the first argument, we can set it previously, with the...
#...specific column (of the dataframa) in which we want to apply the function.
#...Thererefore, we can establish as a second argument of the "GroupBy.Apply"...
#...or the name of the datafram or the name of specific column...
#...(of the dataframa) in which we want to apply the function.

#...In the case of the second argument, that could be dataframe or a ...
#...specific column or columns of dataframe.

#The return of the "GroupBy.Apply" will be dataframe or a serie or even a...
#...scalar. 

#Important: We are applying just one function to one column.

dfcensus8 = pd.read_csv("census.csv")
dfcensus8 = dfcensus8[dfcensus8["SUMLEV"] == 50]

def function3(dfcensus8,Ynum):
    return sum (dfcensus8["CENSUS2010POP"])

SerieCensus8 = dfcensus8.groupby("STNAME").apply(function3,"CENSUS2010POP")
print("Topic 10.5.3:\n", SerieCensus8)
print("\n")

#Topic 10.5.3: A potential issue and using the "Aggregate Method" of...
#...#Group By" objects, it is related with what you pass in the dictionary,...
#...because it can be used to either to identify the columns to apply a...
#...function on or to name an output column if there's multiple functions...
#...to be run. The difference depends on the keys that you pass in from the...
#...dictionary and how they're named. 

#In short, while much of the documentation and examples will talk about...
#...a single "GroupBy" object, there's really two different objects, that...
#..behave a little bit differently with aggregate: 
#...The Dataframe "GroupBy"...
#...The Series "GroupBy".

#Topic 10.5.3.1.:...
#For instance: we take our census data and convert it into a series with...
#...the state names as the index and only columns as the census 2010 population.
#And then we can group this by "Level". Then we call the "Agg Method" where the...
#...dictionary that has both the "Numpy Average" and the "Numpy Sum" functions.
#It is important to say that "Pandas" applies those functions to the...
#..."Series Object" and, since there's only one column of data, it apply...
#...both functions to that column and prints out the output. 

#It is important to say that the "GroupBy" by "Level" is related with the...
#...code:
    
#DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=<object object>, observed=False, dropna=True)[source]

#Where "Level": int, level name, or sequence of such, default None...
#....If the axis is a MultiIndex (hierarchical), "groupby" a particular level...
#...or levels.

dfcensus9 = pd.read_csv("census.csv")
dfcensus9 = dfcensus9.set_index("STNAME")

SerieCensus9 = dfcensus9.groupby(level=0)["CENSUS2010POP"].agg({"Average":np.average, "Sum":np.sum})
print("Topic 10.5.3.1.:\n",SerieCensus9)
print("\n")

#Topic 10.5.3.2.:...
#For instance: we take our census data and convert it into a Dataframe with...
#...the state names as the index and the columns (POPESTIMATE2010 and...
#...POPESTIMATE2011) in which we will apply the functions.
#And then we can group this by "Level". Then we call the "Agg Method" where the...
#...dictionary that has both the "Numpy Average" and the "Numpy Sum" functions.
#It is important to say that "Pandas" applies those functions to the...
#..."Dataframe Object" and, since there's two columns of data, it apply...
#...both functions to that column and prints out the output. 

#It is important to say that the "GroupBy" by "Level" is related with the...
#...code:
    
#DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=<object object>, observed=False, dropna=True)[source]

#Where "Level": int, level name, or sequence of such, default None...
#....If the axis is a MultiIndex (hierarchical), "groupby" a particular level...
#...or levels.

dfcensus10 = pd.read_csv("census.csv")
dfcensus10 = dfcensus10.set_index("STNAME")

SerieCensus10 = dfcensus10.groupby(level=0)["POPESTIMATE2010", "POPESTIMATE2011"].agg({"Average":np.average, "Sum":np.sum})
print("Topic 10.5.3.2.:\n",SerieCensus10)
print("\n")

#Topic 10.5.3.3.:...
#We apply the same o the Topic 10.5.3.2, but with a little twist (we apply...
#...one different function to every column).

dfcensus11 = pd.read_csv("census.csv")
dfcensus11 = dfcensus11.set_index("STNAME")

SerieCensus11 = dfcensus11.groupby(level=0)["POPESTIMATE2010", "POPESTIMATE2011"].agg({"POPESTIMATE2010":np.average, "POPESTIMATE2011":np.sum})
print("Topic 10.5.3.3.:\n",SerieCensus11)
print("\n")

###############################################################################

#The use of "Scales" in Pandas. 

#Topic 11.1: There are 4 different types of "Scales" in Pandas...

#...in which we can classify the data. The main importance of this topic...
#is that we need to deal (clean and/or handle) data with differente type of...
#...scales. Those "Scales" are the followings:
    
#...Ratio Scale: units are equally spaced and we can apply several math...
#...operations (+, -, *, /). For instance: height and weight data.

#...Interval Scale: units are equally spaced; however, we cannot apply...
#...some math operations (*, /) due to zero (0) have meaningful value...
#...for the scale. For instance: temperature and the compass.
    
#...Ordinal Scale: units are not equally spaced. The order of the units is...
#...really important. For instance: grades in the school (A+, B-, C,...). 
    
#...Nominal Scale or Categorical Scale: The order is no important between the...
#...categories. For instance: the names of my co-workers or the names of...
#...teams in a sport (there are a limited number of teams but changing their...
#...order or playing mathematical function to them is meaningless)....
#...Categorical values are very common and we generally refer to categories...
#...where there are only two possible values as binary. 

#Topic 11.2: The Pandas data types are called "dtypes".

#Data Type: is essentially an internal construct that a programming language...
#...uses to understand how to store and manipulate data.

#A possible confusing point about Pandas Data Types is that there is some...
#...overlap between Pandas, Python and Numpy. Therefore in the following lines...
#...we are going to show some of them for Pandas and Python:

    #Data usage: Text or mixed numeric and non-numeric values
        #Pandas dtype: object
        #Python type: str or mixed
        #Numpy type: string_, unicode_, mixed types
    
    #Data usage: Integer numbers
        #Pandas dtype: int64
        #Python type: int
        #Numpy type: int_, int8, int16, int32, int64, uint8, uint16, uint32, uint64
    
    #Data usage: Floating point numbers
        #Pandas dtype: float64
        #Python type: float
        #Numpy type: float_, float16, float32, float64

    #Data usage: True/False values
        #Pandas dtype: bool
        #Python type: bool
        #Numpy type: bool_

    #Data usage: Date and time values
        #Pandas dtype: datetime64
        #Python type: N/A
        #Numpy type: datetime64_

    #Data usage: Differences between two datetimes
        #Pandas dtype: timedelta[ns]
        #Python type: N/A
        #Numpy type: N/A

    #Data usage: Finite list of text values
        #Pandas dtype: category
        #Python type: N/A
        #Numpy type: N/A

#Topic 11.3.1: One way to find the Pandas data type is using the following code...
#...First, we create a Pandas Dataframe and then we figure out the kind of...
#...data type is the data that is part of the Pandas Dataframe through the...
#...code "....dtypes". It is important to say that with this code we only...
#...check the data and not the index of the dataframe.

dfgrades0 = pd.DataFrame(["A+","A","A-","B+","B","B-","C+",None,"C-","D+","D","D-"],index=["Excellent","Excellent","Excellent","Good","Good","Good","OK","OK","OK","Poor","Poor","Poor"])
dfgrades0.rename(columns={0:"Grades"}, inplace=True)
print("Topic 11.3.1:\n",dfgrades0)
print("\n") 

#Topic 11.3.2: In this case the Pandas' datatype of the column "Grades" is...
#...an object (it means is text or mixed numeric and non-numeric values).
TestDType1 = dfgrades0.dtypes
print("Topic 11.3.2:\n",TestDType1)
print("\n") 

#Topic 11.3.3: Other way to find the Pandas data type and even more info of...
#...the data is using the following code. First, we create a Pandas...
#...Dataframe and then we figure out all the info of the data that...
#...is part of the Pandas Dataframe through the function "....info()". It is..
#...important to say that with this function provide information about the...
#...data (like number of entries, number of columns of data, number of...
#...non-null object {null object = "None"}, type of data, and even the size...
#...of that kind of data in the memory) and not the index of the dataframe.

TestDType2 = dfgrades0.info()
print("Topic 11.3.3:\n",TestDType2)
print("\n") 

#Topic 11.4: There are functions to convert Panda's Data Type. Those...
#...functions are the followings:
    
    #Use astype() to force an appropriate dtype
    #Create a custom function to convert the data
    #Use pandas functions such as to_numeric() or to_datetime()

#Topic 11.5: The function "astype()" to convert Panda's Data Type is very...
#...simple. In this case we are going to transform some data from " float64"...
#...to "int64". First, we create the dataframe and then we check the type of...
#...data.

dfgrades00 = pd.DataFrame([1.5,2.9,3.8,8.5],index=["Excellent","Good","Regular","Bad"])
dfgrades00.rename(columns={0:"Grades"}, inplace=True)
print("Topic 11.5.1:\n",dfgrades00)
print("\n") 

TestDType3 = dfgrades00.info()
print("Topic 11.5.2:\n",TestDType3)
print("\n") 

#Topic 11.6.1: We transform the data from "float64" to "int64".

TestDType4= dfgrades00['Grades'].astype('int64')
print("Topic 11.6.1:\n",TestDType4)
print("\n") 

#Topic 11.6.2: If we print the original dataframe,  we will see that the...
#...dataframe still in "float64".

print("Topic 11.6.2:\n",dfgrades00)
print("\n") 

#Topic 11.6.3: It its important to say that in order to actually change the...
#...the original dataframe, make sure to assign it back since the astype()...
#...functions returns a copy.

dfgrades00['Grades'] = dfgrades00['Grades'].astype('int64')
print("Topic 11.6.3:\n",dfgrades00)
print("\n") 

#Topic 11.7: The function "astype()" to convert Panda's Data Type is very...
#...simple. However, we are going to be in trouble (it means that this...
#...function will not work well) if: the data is no clean or if the data is...
#...not homogeneous. 

#Topic 11.7.1: It is important to say that the function "astype()" works very...
#...well if the data is clean, homogeneous and:
    #If the data can be interpreted as a number (it means, without symbols,...
    #...other kind of data type, etc).
    #If we are going to transform from number to a string object.

#In this case we are going to transform some data from to "int64". Then we...
#...see that it will be a problem to work with this datafram3 because it is...
#...not homogeneous, and if we apply the function "astype()" the result will...
#...be an error message.

dfgrades000 = pd.DataFrame([1.5,2.9,3.8,"sdfs"],index=["Excellent","Good","Regular","Bad"])

#Topic 11.8.1: In order of what I described previously about the function...
#..."astype()", we also have the option of create a custom function to...
#...convert the data. One way to do that is the following: First, we create....
#...the dataframe (in this case there are string "objects") which will be
#...transformed in "float64". 

#In this moment the data is typed as string "object".

dfgrades01 = pd.DataFrame(["$1.6","$33.9","$107.8"],index=["Excellent","Good","Regular"])
dfgrades01.rename(columns={0:"Cost"}, inplace=True)
print("Topic 11.8.1.1:\n",dfgrades01)
print("\n")

TestDType5 = dfgrades01.dtypes
print("Topic 11.8.1.2:\n",TestDType5)
print("\n") 

#Topic 11.8.2: In order of what I described previously about the function...
#..."astype()", we also have the option of create a custom function to...
#...convert the data. To achieve this we need to create a custom function...
#...that eliminates the "$" symbol from the string "object" and then transform....
#...this to data type "float64".

#It is important to say that we will see how we use function code "apply" in...
#....case and in the same way, we also can use the function code "Lambda"..

def convert_cost(val):
    """
    Convert the string number value to a int
     - Remove $
     - Remove commas
     - Convert to int type
    """
    XXXX = val.replace('$', '')
    return float(XXXX)

Conversion = dfgrades01['Cost'].apply(convert_cost)
print("Topic 11.8.2:\n",Conversion)
print("\n")

#Topic 11.9: We can use another custom function that is very useful when we...
#...are dealing with data (to be specific, a column) which will be converted...
#...in booleans. This function is called "np.where ()".  It is important to...
#...say this function is related with "Numpy".

#This function allow us to set some value as True; therefore, the other values...
#...will be considered as False. 

#First, we create the dataframe.

dfgrades02 = pd.DataFrame(["Yes","No","No"],index=["Excellent","Good","Regular"])
dfgrades02.rename(columns={0:"Ans"}, inplace=True)
print("Topic 11.9.1:\n",dfgrades02)
print("\n")

TestDType6 = dfgrades02.dtypes
print("Topic 11.9.2:\n",TestDType6)
print("\n") 

#Topic 11.10: Then we transform the data from "string object" to "bool", and...
#...can check that with in the data type.

dfgrades02["Ans"] = np.where(dfgrades02["Ans"] == "Yes", True, False)
NewBool = dfgrades02["Ans"]
print("Topic 11.10:\n",NewBool)
print("\n") 


#$$$$$$$$$$$$

#Topic 11.2: There are functions to deal or convert Scales in Pandas. Those...
#...functions are the followings:
    
#"As Type Function": Allow us to convert the scale of some data in "Nominal...
#...Scale or Categorical Scale". Even, we can pass the scale of some data to...
#..."Ordinal Scale". To be specific, this function work for one column...
#...(it means, the column that show the scale of the data) and also allow us...
#...to print the values in logical order.

#Topic 11.1.1: We convert normal data to a "Nominal Scale or Categorical Scale"...
#...data in the DataFrame. To do that, we first write and print the DataFrame.

dfgrades1 = pd.DataFrame(["A+","A","A-","B+","B","B-","C+","C","C-","D+","D","D-"],index=["Excellent","Excellent","Excellent","Good","Good","Good","OK","OK","OK","Poor","Poor","Poor"])
print("Topic 11.1.1:\n",dfgrades1)
print("\n")

k = dfgrades1.dtypes
print(k)

#Topic 11.1.2: We convert normal data to a "Nominal Scale or Categorical Scale"...
#...data in the DataFrame. To do that, we first write and print the DataFrame....
#...However, after the printing, we will discover that the title o the column...
#...["A+","A","A-","B+","B","B-","C+","C","C-","D+","D","D-"] is zero (0);...
#...therefore, we proceeed to change the number the title of the column. It...
#...is important to remember that the other column is the index.

dfgrades2 = pd.DataFrame(["A+","A","A-","B+","B","B-","C+","C","C-","D+","D","D-"],index=["Excellent","Excellent","Excellent","Good","Good","Good","OK","OK","OK","Poor","Poor","Poor"])
dfgrades2.rename(columns={0:"Grades"}, inplace=True)
print("Topic 11.1.2:\n",dfgrades2)
print("\n") 

k = dfgrades2.dtypes
print(k)


#Topic 11.1.3: We convert normal data to a "Nominal Scale or Categorical Scale"...
#...data in the DataFrame. To do that, we apply the function "as type". As a...
#...result we will see that the printed text  show the phrase dtype:category"

dfgrades3 = dfgrades2["Grades"].astype("category")
print("Topic 11.1.3:\n",dfgrades3)
print("\n")

k = dfgrades3.dtypes
print(k)


#Topic 11.1.3: We convert normal data to a "Nominal Scale or Categorical Scale"...
#...data in the DataFrame and also put it in logical order. To do that, we...
#...apply the function "as type". As a result we will see that the printed...
#...text show the phrase "dtype:category"

#dfgrades4 = pd.DataFrame(["A+","A","A-","B+","B","B-","C+","C","C-","D+","D","D-"],index=["Excellent","Excellent","Excellent","Good","Good","Good","OK","OK","OK","Poor","Poor","Poor"])
#dfgrades4.rename(columns={0:"Grades"}, inplace=True)
#print("Topic 11.1.3:\n",dfgrades4)
#print("\n") 

#dfgrades5 = dfgrades4["Grades"].astype("category",categories=["D-","D","D+","C-","C","C+","B-","B","B+","A-","A","A+"],index=["Excellent","Excellent","Excellent","Good","Good","Good","OK","OK","OK","Poor","Poor","Poor"],ordered=True)
#print("Topic 11.1.3:\n",dfgrades5)
#print("\n") 

#4:00
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    











