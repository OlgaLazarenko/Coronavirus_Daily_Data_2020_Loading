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
			1)iso_code: not null, not number  
			2)continent: the name of a continent, a string, not null, not blank
			3)location: the name of a country, not null, not blank 
			4)date at the format M/D/YYYY, not null 

			5)total_cases: a positive integer or zero 
			6)new_cases: a positive integer or zero
			7)total_deaths: a positie integer or zero 
			8)new_deaths: a positive integer or zero

			9)total_cases_per_million: a positive number int/ decimal or zero
			10)new_cases_per_million: a positive number int/ decimal or zero
			11)total_deaths_per_million: a positive number int/ decimal or zero
			12)new_deaths_per_million: a positive number int/decimal or zero

			13)new_tests:a positive integer or zero, blank is allowed 
			14)total_testes_per_thousand: a positive integer or zero, blank is allowed 
			15)new_tests_per_fhousand: a positive number (can be int or float), or zero, blank is allowed 
			16)new_tests_smoothed: a positive integer or zero
			17)new_tests_smoothed_per_thousand: a positive number (int/or float), zero or blank

			18)tests_units
			19)stringency_index:a positive decimal or integer,zero, blank 
			20)population: a positive integer, zero or null are not allowed
			21)population_density: a positive decimal or integer, zero or blank
			
			22)median_age: a positive integer, zero or null are  allowed
			23)aged_65_older: a positive decimal or integer, zero or blank   
			24)aged_70_older: a positive decimal or integer, zero or blank 
			25)gdp_per_capita: a positive decimal or integer, zero or blank 
			26)extrime_poverty: a positive decimal or ingter, zero or blank 
			27)cordiovasc_death_rate: a positive decimal or integer 
			28)diabetes_prevalance: a positive decimal or integer, zero  or blank 
			29)female_smokers: a positive decimal or integer
			30)test_and_washing_facilities: a positive decimal or integer
			31)hospital_beds_per_thousand: a positive decimal or integer, zero or blank
			32)life_expectancy: a positive decimal or integer, zero or blank 
				

Data Source: https://data.world/markmarkoh/coronavirus-data
Size: 1.74 MB
'''

import configparser # import modules
import csv, numbers, decimal
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
size = os.path.getsize(file_input)
print('the file size: ' + str(size))
print()
print(file_output)
print(file_errors)
print()





# open and read the data file
print()
print('-------------------------------------------------')
with open(file_input,'rt') as file1:
	with open(file_output,'w') as file2:
		with open (file_errors,'w') as file3:
			line = file1.readline() #  read the names of the fields/ the header 
			file2.write(line) #  write the header to the output file 
			file3.write(line)

			
			lines = file1.readlines() # read all lines 
			
			for line in lines :
				item_list = line.split(',') #  split the line into the list by the commas
				
				iso_code = item_list[0]
				continent = item_list[1]
				location = item_list[2]
				
				
				iso_code = iso_code.strip()
				iso_code = iso_code.replace('_','')
				iso_code = iso_code.replace("(","")
				iso_code = iso_code.replace(")","")
				iso_code = iso_code.replace(' ','')
				if not iso_code.isalpha() :
					file3.write(line)
					continue
				

				continent = continent.strip() # remove leading and trailing whitespaces
				if continent != '' :
					if continent not in ('Asia', 'Europe','Oceania','North America','South America','Africa') :
						file3.write(line) # write to the errors file
						continue

								
				location = location.strip()
				# the name of a country can contain more than one word
				# as well the locaton can contain ' or - (for example Cote d'Ivoire, Guinea-Bissau)
				location = location.replace("'",'')
				location = location.replace("(","")
				location = location.replace(")","")
				location = location.replace('_','')
				location = location.replace('-','')
				location = location.replace(' ','')
				if not location.isalpha() :
					file3.write(line)
					continue

				#---------------------------------------------------------------------------------
				#  validate the date field
				my_date = item_list[3]
				# check if the format is correct
				dash_count = my_date.count('/')

				if dash_count == 2:
					# format is correct, continue the checking
					# split the value by the dashes, create a list
					list2 = my_date.split('/')
					# month, day, year values became the elements of the list
				else:
					# if the format is wrong, write the line to the errors file 
					file3.write(line)
					continue

				
				# when the format of the date value is OK, check each element of the list
				# check if the elements contains only numbers
				if not list2[0].isdigit() :
					file3.write(line)
					continue
				elif not list2[1].isdigit() :
					file3.write(line)
					continue
				elif not list2[2].isdigit() :
					file3.write(line)
					continue
				else:
					# the elements contain only numbers
					# now check if the values are in the correct range
					if not int(list2[0]) in range(1,13) :
						file3.write(line)
						continue
					elif not int(list2[1]) in range(1,32) :
						file3.write(line)
						continue
					elif not int(list2[2]) in range(2019, 2021) :
						file3.write(line)
						continue
				# the validation of the date field is over 
    			#*****--------------------------------------*****
				# create function to validate integer
				def validate_int(item) :
					item = item.strip() # remove whitespaces
					item = item.replace(',','')
					if item == '' :
						item = '0'
					result_int = item.isdigit()
					return result_int

				# create function to validate number (integer/or float)
				def validate_num(item) :
					item = item.strip()
					item = item.replace('.','')
					if item == '' :
						item ='0'
					result_num = item.isdigit()
					return result_num


				
				# validate the following fields (a positive number integer, zero or blank)
				# total_cases, new_cases, total_deaths, new_deaths 
				total_cases = item_list[4]
				new_cases = item_list[5]
				total_deaths = item_list[6]
				new_deaths = item_list[7]
				# call the function validate_int(item) and pass the parameters 
				result_int = validate_num(total_cases)
				if result_int == False :
					file3.write(line)
					continue


				result_int = validate_num(new_cases)
				if result_int == False :
					file3.write(line)
					continue


				
				result_int = validate_int(total_deaths)
				if result_int == False :
					file3.write(line)
					continue 

				result_int = validate_int(new_deaths)
				if result_int == False :
					file3.write(line)
					continue 
				
				# ---------------------------------------------------------------------------
				# the validation of the fields item_list[8:12], a positive number, decimal or integer, not zero
				total_cases_per_million = item_list[8]
				new_cases_per_million = item_list[9]
				total_deaths_per_million = item_list[10]
				new_deaths_per_million = item_list[11]
				# call the function validate_num(item) and pass the parameters 
	 

				# call the function 
				result_num = validate_num(total_cases_per_million)
				if result_num == False :
					file3.write(line)
					continue
				
				result_num = validate_num(new_cases_per_million)
				if result_num == False :
					file3.write(line)
					continue

				result_num = validate_num(total_deaths_per_million)
				if result_num == False :
					file3.write(line)
					continue

				result_num = validate_num(new_deaths_per_million)
				if result_num == False :
					file3.write(line)
					continue 
				# ---------------------------------------------------------

				# validate the following fields (integers)
				# new_tests, total_testes, total_tests_per_fhousand,
				# new_tests_smoothed, new_tests_smoothed_per_thousand 
				new_tests = item_list[12]
				total_tests = item_list[13]
				total_tests_thous = item_list[14]
				new_tests_thous = item_list[15]
				new_tests_sm = item_list[16]
				new_tests_sm_thous = item_list[17]

				
				
				result_int = validate_int(new_tests)
				if result_int == False :
					file3.write(line)
					continue
				
				result_int = validate_int(total_tests)
				if result_int == False :
					file3.write(line)
					continue
				
				result_int = validate_num(total_tests_thous)
				if result_int == False :
					file3.write(line)
					continue
				
				result_num = validate_num(new_tests_thous)
				if result_num == False :
					file3.write(line)
					continue
				
				result_int = validate_int(new_tests_sm)
				if result_int == False :
					file3.write(line)
					continue
				
				result_num = validate_num(new_tests_sm_thous)
				if result_num == False :
					file3.write(line)
					continue
				

				
				population = item_list[20]
				result_int = validate_int(population)
				if result_int == False :
					file3.write(line)
					continue
				
				population_dens = item_list[21]
				result_num = validate_num(population_dens)
				if result_num == False :
					file3.write(line)
					continue
				
			

				# validate the fields: 
				median_age = item_list[22]
				aged_65_older = item_list[23]
				aged_70_older = item_list[24]
				gdp_per_capita = item_list[25]
				extreme_poverty = item_list[26]
				cardio_death_rate = item_list[27]
				diabet_prev = item_list[28]
				female_smokers = item_list[29]
				male_smokers = item_list[30]


				# call the functions validate_int(item), validate_num(item)
				# to validate the mentioned above fields

				result_num = validate_num(median_age)
				if result_num == False :
					file3.write(line)
					continue
			
				result_num = validate_num(aged_65_older)
				if result_num == False :
					file3.write(line)
					continue

				result_num = validate_num(aged_70_older)
				if result_num == False :
					file3.write(line)
					continue

				result_num = validate_num(gdp_per_capita)
				if result_num == False :
					file3.write(line)
					continue

				result_num = validate_num(extreme_poverty)
				if result_num == False :
					file3.write(line)
					continue

				result_num = validate_num(cardio_death_rate)
				if result_num == False :
					file3.write(line)
					continue

				result_num = validate_num(diabet_prev)
				if result_num == False :
					file3.write(line)
					continue

				result_num = validate_num(female_smokers)
				if result_num == False :
					file3.write(line)
					continue

				result_num = validate_num(male_smokers)
				if result_num == False : 
					file3.write(line)
					continue
			
						




			file2.write(line)


			
				

				



 # print sample data from the input file and the output file 		
print('The initial file (sample):')
print()				
with open(file_input,'rt') as file1: # read the initial file
	for i in range(0,26):# print rows
		text=file1.readline()
		print(text,end='')
print()
print('-------------------------')


print()
print('The output file (sample):')
print()				
with open(file_output,'rt') as file2: # read the initial file
	for i in range(0,26):# print rows
		text = file2.readline()
		print(text,end = '')
print()
print('-----------------------------')
print('errors_file')
with open(file_errors, 'rt') as file3:
	for a in range(0,26):
		text = file3.readline()
		print(text, end = '')

