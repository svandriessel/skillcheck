# to do
# - Skill check app
# - import the required libraries
# - make simple gui
# - import pdfs from dir pdfs
# - functionality for dm

import glob  # for searching files in dir
from pathlib import Path
import PyPDF2
import random


class Player:
    def __init__(self, name, level):
        self._name = name
        self._level = level

    def showinfo(self):
        print(self.__dict__)


pdfPathList = glob.glob('pdfs/*.pdf')
pdf_dict = {}  # dict of form: { Name: [Path object, {Data dict}]}
for paths in pdfPathList:
    x = Path(paths)  # makes PATH object for each path
    pdf_dict[x.stem] = [x, None]  # stores the path in a list in a dict with key filename

i = 0
for pdf in pdf_dict:
    print(str(i) + ': ' + pdf + '\n')  # removes path indicators and file ext from file name and prints the name
    i += 1

with open(pdfPathList[0], 'rb') as pdf:
    f = PyPDF2.PdfFileReader(pdf)
    with open("fields.txt", 'w') as fieldsfile:
        ff = f.getFields(None, None, fieldsfile)
        with open("variables.txt", 'w') as file:
            for counter, (key, variable) in enumerate(ff.items()):
                print(counter, type(variable.value), variable.value)
                #  print("{}: {}".format(key, variable['/V']))
        karel = Player(ff["Character_Name"]["/V"], ff["CR_Levels_Total"]["/V"])

        karel.showinfo()


