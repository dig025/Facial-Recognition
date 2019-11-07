import os
import shutil
import random

source = '/home/wintermute/Desktop/University/face-recognition/images'
test = '/home/wintermute/Desktop/University/face-recognition/Data/Test'
train = '/home/wintermute/Desktop/University/face-recognition/Data/Train'
valid = '/home/wintermute/Desktop/University/face-recognition/Data/Validation'

#Get all the directories that contain the images
files = os.listdir(source)

for f in files:
	#Get all the images in the current directory
	img = os.listdir(source + '/' + f)
	
	#Percent full numbers
	test_full = 0
	train_full = 0
	valid_full = 0

	#Random number from 0 to 10
	rand = 0

	#Number of images in directory
	num = len(img)

	#Number of files equivalent to the percent of total files
	p1 = num * .7
	p2 = num * .1
	p3 = num * .2

	
	for i in img:
		#Generate random num 0 - 10
		rand = random.randint(1, 10)
		
		#If the random was 7 or less(70%)
		if(rand <= 7):
			if(train_full < p1):
				shutil.copy(source + '/'+ f + '/' + i, train + '/' + f + '/' + i)
				train_full += 1
			elif(valid_full < p2):
				shutil.copy(source + '/' + f + '/' + i, valid + '/' + f + '/' + i)
				valid_full += 1
			else:
				shutil.copy(source + '/' + f + '/' + i, test + '/' + f + '/' + i)
				test_full += 1

		#This is the 20% range
		elif(rand > 7 and rand <= 9):
			if(valid_full < p2):
				shutil.copy(source + '/' + f + '/' + i, valid + '/' + f + '/' + i)
				valid_full += 1
			elif(train_full < p1):
				shutil.copy(source + '/'+ f + '/' + i, train + '/' + f + '/' + i)
				train_full += 1
			else:
				shutil.copy(source + '/' + f + '/' + i, test + '/' + f + '/' + i)
				test_full += 1

		#This is the 10% range
		else:
			if(test_full < p3):
				shutil.copy(source + '/' + f + '/' + i, test + '/' + f + '/' + i)
				test_full += 1
			elif(train_full < p1):
				shutil.copy(source + '/'+ f + '/' + i, train + '/' + f + '/' + i)
				train_full += 1
			else:
				shutil.copy(source + '/' + f + '/' + i, valid + '/' + f + '/' + i)
				valid_full += 1
