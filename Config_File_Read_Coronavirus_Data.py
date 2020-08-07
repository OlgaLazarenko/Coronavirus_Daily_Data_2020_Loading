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
			34)life_expectancy: a positive decimal or integer,<150, zero or null is not allowed
				

Data Source: https://data.world/markmarkoh/coronavirus-data
Size: 1.74 MB
'''

import configparser



my_file="E:\_Python_Projects\GitHub_Coronavirus_Daily_Data\Variables_File.ini" # define the file you will read the initial file information

parser=configparser.RawConfigParser()

print('1')
parser.read(my_file)
print('2')
#to access the elements 
print(parser.sections())
print('3')
print(parser.sections())
print('4')
print(parser.get("coronavirus_data"))
print('5')
print(parser.has_section('coronavirus_data'))

# open and read the data file
input_file='E:\_Python_Projects_Data\Coronavirus_Data\Covid_Data.csv'
with open(input_file,'r') as data_file:
    line=data_file.readline() #read the header
    print(line)
    n=1
    while n<=10: # print the first 10 rows of the input file
        line=data_file.readline()
        print(line)
        n+=1
    
