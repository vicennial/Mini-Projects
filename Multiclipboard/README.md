# Introduction
This project,'Multiclipboard' is a copy from the book 'Automate the boring stuff with python'.   
I am implementing this to gain experience with File I/O in python as well as getting accustomed to git and GitHub commands.   

# Description     
The program will save each piece of clipboard text under a keyword. For example, when
you run  py mcb.pyw save spam , the current contents of the clipboard will be saved with
the keyword spam. This text can later be loaded to the clipboard again by running  py
mcb.pyw spam . And if the user forgets what keywords they have, they can run  py mcb.pyw
list  to copy a list of all keywords and their corresponding values to the clipboard.   

# Usage
python3 mcb.pyw save <keyword> - Saves clipboard to keyword.  
python3 mcb.pyw <keyword> - Loads keyword to clipboard.  
python3 mcb.pyw list - Loads all keywords and correspoding values  to clipboard.  

If you get an error message that says: “Pyperclip could not find a copy/paste mechanism for your system.", You can fix it by    installing one of the copy/paste mechanisms:  
1.`sudo apt-get install xsel to install the xsel utility.`   
2.`sudo apt-get install xclip to install the xclip utility.`    
3.`pip install gtk to install the gtk Python module.`    
4.`pip install PyQt4 to install the PyQt4 Python module.`    

