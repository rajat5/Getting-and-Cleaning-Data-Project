Getting-and-Cleaning-Data-Project
=================================

Getting and Cleaning Data Project is done with help of a python script

These two functions are used clear the data and the finding some particular element in the list
clearlist(thelist, val),findinlist(thelist, val)

Details of the python script per each step is as follows:

Step : 1 Merges the training and the test sets to create one data set
training and test data is loaded independently and then merged together
Following lines of code simply creates a buffer and load file using help of csv
then loaded data is cleared meaning that erronous values of of null strings arer removed.
Then data set is finally merged as training + test i.e taining data set followed by the test data set.

Step : 2 Extracts only the measurements on the mean and standard deviation for each measurement
column labels are loaded in same way. After that with help of string search and data corresponding to that variables 
are stored in variables listmean , liststd and then combined to form a extractedlist.

Step : 3 Uses descriptive activity names to name the activities in the data set
Actvity names such as "Walking","Walking Upstairs","Walking Downstairs","Sitting","Standing","Laying"
and the data corresponding to that is also loaded and each entry is then labelled correspond to that variable.

Step : 4 Appropriately labels the data set with descriptive variable names
From the previously extracted data set and indicies corresponding to those variable values are used to load and 
extract the labels as label_mean , label_std and then merged together with the original data set.

Step : 5 Independent tidy data set with the average of each variable for each activity and each subject
In the end with the help of each data correspond to some activity its average is done for each subject.
And result is finally stored in variable tidylist.
Following line if code is used to  average data and formatt upto five places of decimal
tidylist[i][j] = "{:5e}".format(tidylist[i][j])
