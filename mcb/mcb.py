#! Python 3
# mcb.py help : view all features

# import modules
import sys # to get the arguments
import pyperclip as pc # control the clipboard
import shelve # save variable to external files
import os # to delete data files

# Keywords Dictionary
keys = shelve.open('keywords')    # use a shelve file insted keywords = {'test':'test'} 


# Remove shelve files
def empty():
    os.remove('keywords.bak')
    os.remove('keywords.dat')
    os.remove('keywords.dir')

# Start the program by checking the arguments 
if len(sys.argv) > 1:
    # The list option
    if sys.argv[1].lower() == 'list':   # if sys.argv[1] == 'list' or sys.argv[1] == 'List':
        # Save the list to the clipboard
        text = ''
        for key in list(keys):
            text = text + key + '\t'
        
        if text == '':
            print('The list is empty, tpye help')
        else:
            pc.copy(text)
            print('List of keys have been copied to clipboard.')
            print(text)

    # The save option
    elif sys.argv[1].lower() == 'save':
        # checking if there is the text argument
        try:
            keys[sys.argv[2]] = sys.argv[3]
            print(sys.argv[3] + ' copied to clipboard as ' + sys.argv[2])
        except IndexError:
            keys[sys.argv[2]] = pc.paste()
            print(pc.paste() + ' copied to clipboard as ' + sys.argv[2])
    
    # Search the keys
    elif sys.argv[1] in list(keys):
        pc.copy(keys[sys.argv[1]])
        print(keys[sys.argv[1]] + ' copied to clipboard')

    # Delete a key
    elif sys.argv[1].lower() in ['del','delete']:
        if sys.argv[2] in list(keys):
            del keys[sys.argv[2]]
            print(sys.argv[2] + ' is deleted')
        else:
            print(sys.argv[2] + ' is not found -_-')
    
    # Empty the keys
    elif sys.argv[1].lower() == 'empty':
        empty()
        print('All data has been deleted')

    # Seeking help
    elif sys.argv[1].lower() == 'help':
        print('*'*40)
        print('1.list: show all keys')
        print('2.save <key> <text>(optional): save text(optional) or clipboard as key')
        print('3.<key> :  print the value save in that key')
        print('4.delete <key>: delete the <key> from the keys list')
        print('5.empty: deletes all the data')
        print('*'*40)

    else:
        print('Wrong choice -_-')

else:
    print("Add the argument 'list' to show the list of keywords")

keys.close()
