import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from file_logic import FileLogic
from file_logic import DOC_NAME


howto = ''' How to use Simple Document Merger(SDM).\n 
Simple Document Merger can merge as may documents as possible, only documents of the following types
<> Word Documents (with .docx Extension)
<> Excel Documents (with .xlsx Extension)
<> CSV Documents (with .csv Extension)
<> Text Documents (Wuth .txt Extension)
SDM hasn't being extended to merge other document types this will be implemented in future versions
To merge Documents Do the following
1. Select the type of Documents you want to merge
2. Click "Select document" and select all the documents you want to merge from the file explorer

After words SDM will merge your documents and save them with a random name containing the Date and Time of Merging 
Example Name: " 2021-03-30 16-02-17-Kelugi "

Saved in the same location of the files
        '''
aboutsdm = '''Simple Document Merger (SDM) is a desktop app, meant to help with the merging of multple document of the 
same type (Word documents, Excel document, text files and CSV files).
\nSimple Document Merger can merge 100's of document in few minutes, it is still under development this version 0.1.0 is a quick release, for futher information, suggestion, assitance, complaints or feature request please \
contact the developer Alayande Mustapha Tel: +2349035077346, Email: alayandemustapha@gmail.com
         '''
class sdmui:
    ''' A class to create the user interface fo the document merger '''
    def __init__(self, master):
        ''' The class style and structures the user interface '''
        self.welcome = "Simple Document Merger"
        self.frame = ttk.Frame(master)
        master.title("Simple Document Merger")
        self.style = ttk.Style(master)
        self.style.theme_use('clam')
        self.frame.pack()
        ttk.Label(self.frame,
                  ).grid(row = 0, column = 0, rowspan = 2)
        self.frame.config(height = 9000, width = 9000, relief = RIDGE)
        ttk.Label(self.frame, text = self.welcome, wraplength = 500, font = ('Courier', 24, 'bold'), padding =(20, 10), justify = CENTER, foreground = 'green',
                  ).grid(row =0, column = 0, #rowspan = 4, columnspan = 4
                         )
        
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()
        self.frame_content.config(height = 3000, width = 3000, relief = RIDGE)
        self.second_frame = ttk.Frame(master)
        self.second_frame.config(height = 3000, width = 3000, relief = RIDGE)
        self.second_frame.pack()
        file_type = StringVar() 
        doclist = ['txt', 'csv', 'doc', 'xlsx']
        ttk.Label(self.second_frame, text = "1. Select File Type to be Merged", justify = CENTER).grid(row = 1, column = 1) 
        self.doctype = StringVar()
        combobox = ttk.Combobox(self.second_frame, textvariable = self.doctype, \
            values = ('Word Document', 'Excel Document', 'CSV Document', 'Text Document')
        ).grid(row = 1, column = 0, padx = 5, pady = 5, )
        
        
        def about():  
            root = Tk()
            root.title('About Simple Document Merger')
            label = ttk.Label(root, text = aboutsdm,  wraplength = 800, font = ('Courier', 18, 'bold'), padding =(20, 10), justify = LEFT, foreground = 'green'  ).grid(row = 0, column = 0)
            root.mainloop()
            
        def tutorial():  
            root = Tk()
            root.title('SDM Tutorial')
            label = ttk.Label(root, text = howto, wraplength = 800, font = ('serif', 18, 'bold'), padding =(20, 10), justify = LEFT, foreground = 'green'  ).grid(row = 0, column = 0)
            root.mainloop()
            
        def doc_name(): 
            root = Tk()
            root.title("Your Document")
            label = ttk.Label(root, text = "The name of the merged document is: " + DOC_NAME(), wraplength = 800, font = ('serif', 18, 'bold'), padding =(20, 10), justify = LEFT, foreground = 'green' )
            label.pack()
            
        def opendoc():  
            if ('.' in DOC_NAME()):  
                os.startfile(DOC_NAME())
            else:
                root = Tk()
                root.title("Your Document")
                label = ttk.Label(root, text = "You haven't merged any document ", wraplength = 800, font = ('serif', 18, 'bold'), padding =(20, 10), justify = LEFT, foreground = 'green' )
                label.pack()  
                pass
              
        ttk.Button(self.frame, text = 'About SDM', style = 'Alarm.TButton', padding = (2,2), command = about, ).grid(row = 1, column = 1)
        ttk.Button(self.frame, text = 'Tutorial', style = 'Alarm.TButton', padding = (2,2), command = tutorial, ).grid(row = 1, column = 0)
        
        self.frame.config(padding = (5,5))
        
       
        def file_open():
            o = 1
            rep = filedialog.askopenfilenames(
                parent=self.frame, 
                initialdir = '/', 
                initialfile = 'tmp', 
                filetype = [
                    ('DOC', '*docx'), ('EXCEL', '*.xlsx'), ('CSV', '*.csv'), ('TEXT', '*.txt'), ('ALL FILES', '*')
                    ]
            )
            return FileLogic(rep, self.doctype.get())
            
        ttk.Button(self.frame_content, text = '2. Select Documents', command = file_open, ).grid(row = 0, column = 0, padx = 4, pady = 4, sticky = 'w') 
        ttk.Button(self.frame_content, text = "3. Merge Documents", padding = (5,5), command = doc_name).grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'e')
        ttk.Button(self.frame_content, text = "4. Open Merged Document", padding = (5,5), command = opendoc).grid(row = 0, column = 1, padx = 5, pady = 5, sticky = 'nw')


def main():  
    root = Tk()
    interface = sdmui(root)
    root.mainloop()
    
if __name__ == '__main__':  main()
