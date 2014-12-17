print("-------------")
def clearlist(thelist, val):
	return [value for value in thelist if value != val]

def findinlist(thelist, val):
	try:
		index = thelist.index(val)
		return index
	except ValueError:
		return -1
import csv
# Step : 1 Merges the training and the test sets to create one data set
# __________training data set___________ 
localfiletrain = open(".\\train\\X_train.txt")
csvtrain = csv.reader(localfiletrain,delimiter=" ")
listtrain = list(csvtrain)
localfiletrain.close()

index = 0
#clearing spaces
for e in listtrain:
	#listtrain[index] = list(filter(('').__ne__,e))
	listtrain[index] = clearlist(e,"")
	index += 1
listtrain = clearlist(listtrain,"")
print('training set loaded')

#temp
#e = listtrain[0]
#print(e[0:5])


#____________test data set_______________
localfiletest = open(".\\test\\X_test.txt")
csvtest = csv.reader(localfiletest,delimiter=" ")
listtest = list(csvtest)
localfiletrain.close()
index = 0
#clearing spaces
for e in listtest:
	listtest[index] = list(filter(('').__ne__,e))
	index += 1
print('test set loaded')


#____________merged data set____________
#listnet = listtrain + listtest
listnet = []
for e in listtrain:
	listnet.append(e)
for e in listtest:
	listnet.append(e)


# Step : 2 Extracts only the measurements on the mean and standard deviation for each measurement
#feature labels
labelsfile = open(".\\features.txt")
listlabel = list(labelsfile)
index = 0
indexmean = []
indexstd = []
for e in listlabel:
	templabel = e[len(str(index+1))+1:-1]
	if(e.find('mean')!=-1):
		indexmean.append(index)
	if(e.find('std')!=-1):
		indexstd.append(index)
	index += 1
#length is 561  print(index)
cols = len(listnet[0])
rows = len(listnet)

listmean = []
liststd = []
for i in range(rows):
	tempmean = []
	tempstd = []
	for e in indexmean:
		tempmean.append(listnet[i][e])
	for e in indexstd:
		tempstd.append(listnet[i][e])
	listmean.append(tempmean)
	liststd.append(tempstd)

# merging the train and temp
extractedlist = []
for i in range(len(listmean)):
	extractedlist.append(listmean[i]+liststd[i])
#temp
#print(len(extractedlist[0]))



# Step : 3 Uses descriptive activity names to name the activities in the data set
#_______________activity labels_______________
activitylabel = open(".\\activity_labels.txt")
activitylabels = list(activitylabel)
#cleaning labelled activities
index = 0
for e in activitylabels:
	activitylabels[index] = e[2:-1]
	index += 1
activitylabels[0] = "Walking"
activitylabels[1] = "Walking Upstairs"
activitylabels[2] = "Walking Downstairs"
activitylabels[3] = "Sitting"
activitylabels[4] = "Standing"
activitylabels[5] = "Laying"
print("Various Activities are :")
print(activitylabels)


localfile = open(".\\train\\y_train.txt")
csvtrain = csv.reader(localfile,delimiter=" ")
listtrain_label = list(csvtrain)
localfile = open(".\\test\\y_test.txt")
csvtest = csv.reader(localfile,delimiter=" ")
listtest_label = list(csvtest)
netlabels = listtrain_label + listtest_label

#naming the activities with the help of labels 
newlist_labels = []
for i in range(len(netlabels)):
	index_ = int(netlabels[i][0]) - 1
	newlist_labels.append(activitylabels[index_])
#merging the labels into data
for i in range(len(extractedlist)):
	extractedlist[i].insert(0,newlist_labels[i])

# Step : 4 Appropriately labels the data set with descriptive variable names
label_mean = []
label_std = []
for e in indexmean:
	label_mean.append(listlabel[e][len(str(e))+1:-1])
for e in indexstd:
	label_std.append(listlabel[e][len(str(e))+1:-1])
netlabels = label_mean + label_std
#merging labels into the data
netlabels = ['Body Activity'] + netlabels
extractedlist.insert(0,netlabels)
#showing top ten data set
for i in range(10):
	print(extractedlist[i][0:5])

# Step : 5 Independent tidy data set with the average of each variable for each activity and each subject
tidylist = []
for i in range(6):
	temp = []
	for j in range(len(extractedlist[0])-1):
		temp.append(0)
	tidylist.append(temp)

countofactivities = [0,0,0,0,0,0]
for e in extractedlist[1:]:
	indexofactivity = activitylabels.index(e[0])
	#print(indexofactivity)
	countofactivities[indexofactivity] += 1
	index = 1
	for j in range(len(e)-1):
		element = e[index]
		tidylist[indexofactivity][index-1] += float(element)
		index += 1

#averaging data and formatting upto five places of decimal
print(countofactivities)
for i in range(6):
	e = tidylist[i]
	for j in range(len(e)):
		tidylist[i][j] = tidylist[i][j] / countofactivities[i]
		tidylist[i][j] = "{:5e}".format(tidylist[i][j])

# merging labels and activities
tidylist.insert(0,netlabels)
activitylabels[0] = "Walking            "
activitylabels[1] = "Walking Upstairs   "
activitylabels[2] = "Walking Downstairs "
activitylabels[3] = "Sitting            "
activitylabels[4] = "Standing           "
activitylabels[5] = "Laying             "
for i in range(1,len(tidylist)):
	tidylist[i].insert(0,activitylabels[i-1])

for i in range(6):
	print(tidylist[i][0:8])

localfile = open('tidydata.txt','wb')
localfile = open('tidydata.txt','r+')
for e in tidylist:
	for i in e:
		localfile.write("%s\t"%i)
	localfile.write("\n")