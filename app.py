# to do
# - Skill check app
# - import the required libraries
# - make simple gui
# - import pdfs from dir pdfs
# - functionality for dm

import glob  # for searching files in dir
from pathlib import Path
import PyPDF2


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

f = PyPDF2.PdfFileReader(pdfPathList[0])
ff = f.getFields()
for key in ff:
    print(key)

karel = Player(ff["Character_Name"]["/V"], ff["CR_Levels_Total"]["/V"])

karel.showinfo()


