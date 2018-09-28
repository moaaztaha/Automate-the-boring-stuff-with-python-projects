# MCB (Multi Clipboard)
## an implementation of MCB from 'Automate the boring stuff with python' with some new features
Features:
=========
1. List all availabe keys and copy them to clipboard
    ```
    python mcb.py list
    ```
2. save to file with a key from clipboard or the command line(optional)
    ```
    python mcb.py save name moaz
    ```
3. get the value in the key and copy it to the clipboard
    ```
    python mcb.py key
    ```
4. delete a key and it's value
    ```
    python mcb.py delete key
    ```
5. empty the list of keys
    ```
    python mcb.py empty
    ```
----
Modules Used:
====
* **sys**: get command line arguments
* **pyperclip**: control clipboard
* **shelve**: save and resotre to an external file
* **os**: delete files