# to do
# - Skill check app
# - import the required libraries
# - make simple gui
# - import pdfs from dir pdfs
# - functionality for dm

import json
import tabula #lib for json formatting of pdf
import glob #for searching files in dir
from pathlib import Path
import PyPDF2


class Player:
    def __init__(self, name, level):
        self._name = name
        self._level = level
    def showinfo(self):
        print(self.__dict__)

# filename = Path("source_data/text_files/raw_data.txt")
# filename.stem


pdfpathlist = glob.glob('pdfs/*.pdf')
pdf_dict = {}  # dict of form: { Name: [Path object, {Data dict}]}
for paths in pdfpathlist:
    x = Path(paths)  # makes PATH object for each path
    pdf_dict[x.stem] = [x, None]  # stores the path in a list in a dict with key filename

i = 0
for pdf in pdf_dict:
    print(str(i) + ': ' + pdf + '\n')  # removes path indicators and file ext from file name and prints the name
    i += 1

#  read pdf as JSON and store in pdf dicts data dict


f = PyPDF2.PdfFileReader(pdfpathlist[0])
ff = f.getFields()
for key in ff:
    print(key)

karel = Player(ff["Character_Name"]["/V"], ff["CR_Levels_Total"]["/V"])

karel.showinfo()
# i = 0
# for pdf in pdf_dict:

    #  print(tabula.read_pdf(pdf_dict[pdf][0], pages="all", multiple_tables="True", output_format="json"))
    # jsondata = json.loads(tabula.read_pdf(pdf_dict[pdf][0], output_format="json"))
    # pdf_dict[pdf][1] = jsondata
#
# for pdf in pdf_dict:
#     print(pdf_dict[pdf][1])


