# App to merger multiple files together
# Author: Alayande Mustapha: alayandemustapha@gmail.com
import docx
import docmerge 
from  doc_name import docname
''' This Section Collects informations about hte files '''

output_file_name = "No document has been merged"
def FileLogic(merge_list, dftype):  
    dftype_list = ['Text Document', 'CSV Document','Word Document', 'Word Document']
     
    i = 0
    files_list = [] 
    # Output file name 
    global output_file_name
    output_file_name = docname()
    print("FL 1 " + output_file_name + " " + dftype)
    for file in merge_list:
        files_list.append(file)
    print("FL 2 Created list")
    if (dftype == dftype_list[0]):
        ''' Document type is Txt'''
        print("FL 3 doc type is defined")
        # call function to merge csv or txt
        docmerge.merge_txt_csv(output_file_name, files_list)
        print("Documents are merged")
        print ("The Name of the Merged Document is: {}".format(output_file_name) + ".txt")
        output_file_name = output_file_name + ".txt"
    elif dftype == dftype_list[1]:  
        ''' Document type is CSV '''
        # Call function to merge Word document
        print("FL 3 doc type is defined")
        docmerge.merge_txt_csv(output_file_name, files_list)
        print("Documents are merged")
        print("The Name of the Merged Document is: {}".format(output_file_name) + ".csv")
        output_file_name = output_file_name + ".csv"
    elif dftype == dftype_list[2]:  
        ''' Document type is word '''
        # Call function to merge Word document
        print("FL 3 doc type is defined")
        docmerge.merge_docx(output_file_name, files_list)
        print("Documents are merged")
        print("The Name of the Merged Document is: {}".format(output_file_name) + ".docx")
        output_file_name = output_file_name + ".docx"
    elif dftype == dftype_list[3]:  
        #call function to merge Excel spreadsheet
        print("FL 3 doc type is defined")
        docmerge.merger_xcel(files_list, output_file_name)
        print("Documents are merged")
        print ("The Name of the Merged Document is: {}".format(output_file_name) + '.xlsx')
        output_file_name = output_file_name + ".xlsx"
    else:
       return "Documnet type not listed"
    #return "The Name of the Merged Document is: {}".format(output_file_name)

def DOC_NAME():  
    if output_file_name:  
        return output_file_name
    else:
        return "No document has been merged"  
