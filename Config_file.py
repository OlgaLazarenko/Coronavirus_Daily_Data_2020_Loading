# coronavirus daily data

import configparser
my_file= 'E:\_Python_Projects\GitHub_Coronavirus_Daily_Data_2020_Loading\Variables_File.ini'
config = configparser.ConfigParser() # initialize a ConfigParser object
config.read(my_file)
print(config.sections())

print(config.get('files','input_file'))
print(config.get('files','output_file'))
print(config.get('files','errors_file'))