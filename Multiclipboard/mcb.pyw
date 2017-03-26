#! python3
# Usage: python3 mcb.pyw save <keyword> - Saves clipboard to keyword.
#        python3 mcb.pyw <keyword> - Loads keyword to clipboard.
#        python3 mcb.pyw list - Loads all keywords and corresponding values to clipboard.
import shelve,pyperclip,sys
user_shelf=shelve.open('mcb')
arguments=sys.argv
if len(arguments)==1 or len(arguments)>3:
    print("Invalid arguments. Please Try Again")
    sys.exit()
if arguments[1]=='save':
    user_shelf[arguments[2]]=pyperclip.paste()
    print("Success! Clipboard content saved under keyword '%s'"%(arguments[2]))
else:
    if arguments[1].lower()=='list':
        pyperclip.copy(str(list(user_shelf.items())))
        print("Success! All keywords and corresponding values copied to clipboard")
    elif arguments[1] in user_shelf:
        pyperclip.copy(user_shelf[arguments[1]])
        print("Success! Value under keyword '%s' copied to clipboard."%arguments[1])
    else:
        print("Invalid keyword. Please try again")
    
    
