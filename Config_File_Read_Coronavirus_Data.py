#!/usr/bin/env python3
'''
Project Name: Coronavirus_Daily_Data_2020_Loading
Date started: Aug 05, 2020
Author: Olga Lazarenko
Description: the purpose of the program:
			- read csv file containing coronavirus daily data of 2020 year;
            - use the configuration file to provide the initilal data file path, the path for the output validated data,
              the path of the data with errors/ validation failed 
			- validate the data: the rows with errors will be removed and saved at a special file;
			- count the rows at the initial data file/s, the output file, the errors file;
			  count the rows with errors for each field			 
			 	
Specification:
			1)iso_code: not null 
			2)continent: the name of a continent, a string, not null
			3)location: the name of a country, not null 
			4)date at the format M/D/YYYY, not null 
			5)total cases: a positive integer, zero or null are allowed
			6)new cases: a positive integer, zero or null are allowed
			7)total deaths: a positie integer, zero or null are allowed
			8)new_deaths: a positive integer, zero or null are allowed
			9)total_cases_per_million: a positive integer, zero or null are allowed
			10)new_cases_per_million: a positive integer, zero or null are allowed
			11)total_deaths_per_million: a positive integer, zero or null are allowed
			12)new_deaths_per_million: a positive integer, zero or null are allowed
			13)new_tests:a positive integer, zero or null are allowed
			14)total_testes: a positive integer,zero or null are allowed
			15)total_tests_per_fhousand: a positive integer, zero or null are allowed
			16)new_tests_smoothed: a positive integer, zero or null are allowed
			17)new_tests_smoothed_per_thousand: a positive integer, zero or null are allowed
			18)tests_units
			19)stringency_index:a positive decimal or integer,zero or null are allowed
			20)population: a positive integer, zero or null are not allowed
			21)population_density: a positive decimal or integer, zero or null are not allowed
			23)median_age: a positive integer, zero or null are not allowed
			24)aged_65_older: a positive decimal or integer,<100, zero or null are  not allowed
			25)aged_70_older: a positive decimal or integer, <100, zero or null are not alloed
			26)gdp_per_capita: a positive decimal or integer, zero or null are not allowed
			27)extrime_poverty: a positive decimal or ingter, <100, zero or null are allowed
			28)cordiovasc_death_rate: a positive decimal or integer, zero or nul are not allowed
			29)diabetes_prevalance: a positive decimal or integer,<100, zero or null are not alloed 
			30)female_smokers: a positive decimal or integer,<100
			31)male_smokers: a positive decimal or integer, <100
			32)hand_washing_facilities: a positive decimal or integer
			33)hospital_beds_per_thousand: a positive decimal or integer, zero or null is not allowed
			34)life_expectancy: a positive decimal or integer, zero or null is not allowed
				

Data Source: https://data.world/markmarkoh/coronavirus-data
Size: 1.74 MB
'''

import configparser #import modules
import csv
import os,sys,datetime 

# check if the initial file exists
os.chdir(r'E:\_Python_Projects')
print()
print(open(r'E:\_Python_Projects\GitHub_Coronavirus_Daily_Data_2020_Loading\Variables_File.ini'))
print()
print("The initial file exists:  " + str(os.path.exists("E:\\_Python_Projects\\GitHub_Coronavirus_Daily_Data_2020_Loading\Variables_File.ini")))
print()

my_file= 'E:\_Python_Projects\GitHub_Coronavirus_Daily_Data_2020_Loading\Variables_File.ini'

config = configparser.ConfigParser() # initialize a ConfigParser object
config.read(my_file)
print('*-----------------*')
print(config.sections())

#get the files from the configuration file Variables_File.ini
file_input= config.get('files','input_file')
file_output= config.get('files','output_file')
file_errors= config.get('files','errors_file')


print()
file_input = file_input[1:]
file_input = file_input[:-1]

file_output = file_output[1:]
file_output = file_output[:-1]

file_errors = file_errors[1:]
file_errors = file_errors[:-1]
print('---------------------')
print(file_input)
print(file_output)
print(file_errors)

#  declare the variable for the fields/ the columns 



num_loop = 1
# open and read the data file
print()
print('-------------------------------------------------')
with open(file_input,'rt') as file1:
	with open(file_output,'w') as file2:
		with open (file_errors,'w') as file3:
			line = file1.readline() #  read the names of the fields/ the header 
			file2.write(line) #  write the header to the output file 
			file3.write(line)
			
			while line:
				line = file1.readline()
				item_list = line.split(',') #  split the read line by the commas into a list


				#  Validate the fields
				iso_code = item_list[0]
				if iso_code == '' :
					file3.write(line) # write to the errors file
					continue

				continent = item_list[1]
				if continent == '' :
					file3.write(line)
					continue


				location = item_list[2]
				if location == '' :
					file3.write(line)
					continue
				
				
				#  validate the date field
				date = item_list[3]
				try:
					datetime.datetime.strptime(date, '%m/%d/%Y')
				except:
					file3.write(line)
					continue
				
					
				# validate the following fields
				total_cases = item_list[4]
				new_cases = item_list[5]
				total_deaths = item_list[6]
				new_deathes = item_list[7]
				total_cases_per_million = item_list[8]
				new_cases_per_million = item_list[9]
				total_deaths_per_million = item_list[10]
				new_deather_per_million  = item_list[11]
				new_tests = item_list[12]
				total_tests = item_list[13]
				total_tests_per_thousand = item_list[14]
				new_tests_per_thousand = item_list[15]
				new_tests_smoothed = item_list[16]
				new_tests_smoothed_per_thousand = item_list[17]

				#  create a function
				def validate_cases(num):
					num = num.strip() # remove leading and trailing whitespaces
					if not num.isdigit() or num != '' :
						file3.write(line)

				#  call the function to validate the fields
				validate_cases(total_cases)
				validate_cases(new_cases)
				validate_cases(total_cases)
				validate_cases(new_deathes)
				validate_cases(total_cases_per_million)
				validate_cases(new_cases_per_million)
				validate_cases(total_deaths_per_million)
				validate_cases(new_deather_per_million)
				validate_cases(new_tests)
				validate_cases(total_tests)
				validate_cases(total_tests_per_thousand)
				validate_cases(new_tests_per_thousand)
				validate_cases(new_tests_smoothed)
				validate_cases(new_tests_smoothed_per_thousand)

				
				file2.write(line)

				



 # print sample data from the input file and the output file 		
print('The initial file (sample):')
print()				
with open(file_input,'rt') as file1: # read the initial file
	for i in range(0,6):# print the first ten rows
		text=file1.readline()
		print(text,end='')
print()
print('-------------------------')


print()
print('The output file (sample):')
print()				
with open(file_output,'rt') as file2: # read the initial file
	for i in range(0,11):# print the first ten rows
		text = file2.readline()
		print(text,end = '')
print()
print('-----------------------------')
print('errors_file')
with open(file_errors, 'rt') as file3:
	for a in range(0,11):
		text = file3.readline()
		print(text, end = '')

