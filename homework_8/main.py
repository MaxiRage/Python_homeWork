from os.path import exists
from csv_create import create
from write import writing_scv
from write import writing_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    create()

writing_scv()
writing_txt()