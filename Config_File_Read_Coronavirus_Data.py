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
			1)iso_code: an uppercase three letter word
			2)continent: the name of a continent
			3)location: the name of a country
			4)date at the format M/D/YYYY
			5)total cases: a positive integer, zero or null are allowed
			6)new cases: a positive integer, zero or null are allowed
			7)total deaths: a positie integer, zero or null are allowed
			8)new_deaths: a positive integer, zero or null are allowed
			9)total_cases_per_million: a positive decimal or integer number
			10)new_cases_per_million: a positive decimal or integer number
			11)total_deaths_per_million: a positive decimal or integer number
			12)new_deaths_per_million: a positivie decimal or integer number
			13)new_tests:a positive integer, zero or null are allowed
			14)total_testes: a positive integer,zero or null are allowed
			15)total_tests_per_fhousand: a positive integer, zero or null are allowed
			16)new_tests_smoothed: a positive integer, zero or null are allowed
			17)new_tests_smoothed: a positive integer, zero or null are allowed
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

import configparser

my_file= 'E:\_Python_Projects\GitHub_Coronavirus_Daily_Data_2020_Loading\Variables_File.ini'

config = configparser.ConfigParser() # initialize a ConfigParser object
config.read(my_file)
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

num_loop = 1
# open and read the data file
print()
print('-------------------------------------------------')
with open(file_input,'r') as file1:
	with open(file_output,'w+') as file2:
		with open (file_errors,'w+') as file3:
			header = file1.readline() # read the header 
			if num_loop==1: # the columns name should be written to the output and errors files only once 
				file2.write(header) #write the columns name to the output file 
				file3.write(header) #write  the columns names to the errors file
			num_loop+=1
		
			for line in file1:
				line = file1.readline()
				file2.write(line)
				
	
	