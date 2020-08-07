# coronavirus daily data
 
from configparser import ConfigParser

file='Config.ini'
config=ConfigParser()
config.read(file)

print(config.sections())