from .models import *


import csv

import sys
import os
import time



def read():
		lines = 0
		begin = time.time()
		# file = open("bank_branches.csv")
		file = open(os.path.join(sys.path[0], "api/bank_branches.csv"), encoding ="utf8")

		reader= csv.reader(file)
		# Bank.objects.all().delete()
		for row in reader:
			lines += 1
			# print(row[0],row[1], row[7])
		end = time.time()
		print("total time  : ",end-begin)
		print("total lines  : ", lines)



#populate banks

def populate_bank():
		begin = time.time()
		# file = open("bank_branches.csv")
		file = open(os.path.join(sys.path[0], "api/bank_branches.csv"), encoding ="utf8")

		reader= csv.reader(file)
		Bank.objects.all().delete()
		for row in reader:
			# lines += 1
			# print(row[1], row[7])
			if row[1].isdigit():
				new_bank, created = Bank.objects.get_or_create(id=int(row[1]), name=row[7])
				new_bank.save()
		end = time.time()

		print("toatl tim  : ",end-begin)
				
#populate branch

def populate_branches():
		# file = open("bank_branches.csv")
		begin = time.time()
		file = open(os.path.join(sys.path[0], "api/bank_branches.csv"), encoding ="utf8")

		reader= csv.reader(file)
		# Branch.objects.all().delete()
		for row in reader:
			print(row[0], row[1], row[7])
			begin1 = time.time()
			if row[1].isdigit():
				new_branch, created = Branch.objects.get_or_create(
																ifsc = row[0],
																bank_id = row[1],
																branch = row[2],
																address = row[3],
																city = row[4],
																district = row[5],
																state = row[6],
																 )
				new_branch.save()

			end1 = time.time()

			print("toatl tim  : ",end1-begin1)
		end = time.time()
		print("toal time : " ,end-begin)


# def run():
# 	fhand = open(os.path.join(sys.path[0], "api/bank_branches.csv"), encoding ="utf8")
# 	reader= csv.reader(fhand)
# 	# Bank.objects.all().delete()
# 	Branch.objects.all().delete()
# 	start = times.time()
# 	for row in reader:
# 		if row[1].isdigit():
# 			print(row[0], row[1], row[7])
# 			begin1 = time.time()
# 			# print(row[1])
# 			# ba, created = Banks.objects.get_or_create(id=row[1], name=row[7])
# 			# ba.save()
# 			Branch.objects.create(ifsc=row[0], bank_id=row[1], branch=row[2], address=row[3], city=row[4], district=row[5], state=row[6])
# 			# b.save()
# 			end1 = time.time()
# 			print("time : ",end1-begin1)
# 	end = time.time()
# 	print("Total time : ",end-start)

# fake = Faker()

def create_dict(row):
	return dict(
		ifsc=row[0], 
		bank_id=row[1], 
		branch=row[2], 
		address=row[3],
		city=row[4], 
		district=row[5], 
		state=row[6]
	)
  
n_things = 100

def run():
	start = time.time()
	fhand = open(os.path.join(sys.path[0], "api/bank_branches.csv"), encoding ="utf8")
	reader= csv.reader(fhand)
	# Bank.objects.all().delete()
	# Branch.objects.all().delete()
	start = time.time()

	things = [create_dict(row) for row in reader if row[1].isdigit() ]

	print(things[:10])
	print(len(things))

	thing_objects = []
	for thing in things:
		# print(thing['ifsc'],thing['branch'])
		if  Branch.objects.filter(ifsc = thing['ifsc']).exists():
			pass
		else:
			t = Branch(**thing)
			thing_objects.append(t)
	
	Branch.objects.bulk_create(thing_objects)
	end = time.time()
	print("total time : ",end-start)
