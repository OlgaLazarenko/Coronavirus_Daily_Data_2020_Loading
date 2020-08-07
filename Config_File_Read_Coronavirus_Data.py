'''
Project Name: Coronavirus_Daily_Data_2020
Date started: Aug 05, 2020
Author: Olga Lazarenko
Description: the purpose of the program:
			- read csv file containing coronavirus daily data of 2020 year;
            - user the configuration file to provide the initilal data file path, the path for the output validated data,
              the path of the data with errors/ validation failed 
			- validate the data: the rows with errors will be removed and saved at a special file;
			- count the rows at the initial data file, at the output file, at the errors file;
			- count the rows at the initial data file/s, the output file, the errors file;
			  count the rows with errors for each field			 
			 	
Specification: 1)dispatching_base_num: the values should be in the form 'B00123', the first character should be a letter and the following five
				characters should be numbers;
				2)pickup_datetime: the values should be in the format "%d/%m/%Y %H:%M" (ex: '02/15/2019 16:07')
				3)dropoff_datetime: the values should be in the format "%d/%m/%Y %H:%M"
				4)PULocation: the values should be three or less characters long, only positive decimals are allowed
				5)DOLocation: the values shold be three or less characters long, only positive decimals are allowed
				6)flag: the values can be either 1 or blank
				

Data Source: https://data.cityofnewyork.us/Transportation/2019-High-Volume-FHV-Trip-Records/4p5c-cbgn/data
			a sample of data was used to check if the code performes properly
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
    
