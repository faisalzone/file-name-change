import os, xlrd

path = 'C:/users/faisal.ahmed/documents/mystuffs/python-projects/filenamechange' #path to jpg files
path1 = 'c:/users/faisal.ahmed/Documents/mystuffs/python-projects/filenamechange/somefilename.xlsx'

data =[] #list of jpg filenames in folder

#lets create a filenames list without the jpg extension
for name in os.listdir(path):
    fileName, fileExtension = os.path.splitext(name)
    if fileExtension =='.png':
        data.append(fileName)

#lets create a list of old filenames in the excel column a

book = xlrd.open_workbook(path1)
sheet = book.sheet_by_index(0)
oldNames =[]
for row in range(sheet.nrows):
    oldNames.append(sheet.cell_value(row,0))


#lets create a list with the new names in column b
newNames =[]
for row in range(sheet.nrows):
    newNames.append(sheet.cell_value(row,1))


# now create a dictionary with the old name in a and the corresponding new name in b

fileNames = dict(zip(oldNames,newNames))
fileNameNotFound = 'not found'

print(fileNames)

#lastly rename your jpg files

for f in data:
    if f in fileNames.keys():
        os.rename(path+'/'+f+'.png', path+'/'+fileNames[f]+'.png')
    if f not in fileNames.keys():
        os.rename(path+'/'+f+'.png', path+'/'+fileNameNotFound+'-'+f+'.png')
