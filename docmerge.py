# Author: Alayande Mustapha: alayandemustapha@gmail.com
import docx
import pandas as pd

def merge_docx(new_file, doc_list):
	''' Merges Docx type of File '''
	if (type(doc_list) == list) or (type(doc_list) == tuple):
		pass
	else:
		doclist = list(doclist)
	if new_file.endswith('.docx'):
		pass
	else:
		new_file = new_file + '.docx'
	newdoc = docx.Document()
	for doc in doc_list:
		d_docx = docx.Document(doc)
		for element in d_docx.element.body:
			newdoc.element.body.append(element)
	newdoc.save(new_file)
	return  "Flies Merged Sucessfully"




def merge_txt_csv(new_file, files_list):
    ''' This section Merges txt or csv files '''
    if (type(files_list) == list) or (type(files_list) == tuple):
    	pass
    else:
    	files_list = list(files_list)
    if (new_file.endswith('.csv')) or (new_file.endswith('.txt')) :
    	pass
    else:
    	new_file = new_file + '.csv'
    nf = open(new_file, 'w')
    for afile in files_list:
        fm = open(afile, 'r')
        for line in fm:
            nf.write(line)
        fm.close()
    nf.close()
    return  "Files Merged Sucessfully"


def merge_xcel(file_list, newfile):
	'''This section merges Excel Spreasheets '''
	if (type(file_list) == list) or (type(file_list == tuple)):
		pass
	else:
		file_list = list(file_list)
	if new_file.endswith('.xlsx'):
		pass
	else:
		new_file = new_file + '.xlsx'
	excel_list = []
	not_excel = []
	for file in file_list:
		if file.endswith('xlsx'):
			excel_list.append(file)
		else:
			not_excel.append(file)
	df = pd.DataFrame()
	for file in excel_list:
		ef = pd.read_excel(file)
		df = df.append(ef, ignore_index = True)
	df.to_excel(newfile)
	return "Excel Files Succesfully Merged"
