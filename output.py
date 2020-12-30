Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
==== RESTART: C:/Users/lenovo/AppData/Local/Programs/Python/Python39/code.py ===
>>> import code as y
>>> y.create("keerthana",25)
>>> y.create("esha",2)
>>> y.create("kiran",24)
>>> y.create("kiran",3)
error: this key already exists
>>> y.read("kiran")
'kiran:24'
>>> y.delete("esha")
key is successfully deleted
>>> y.delete("honey")
error: given key does not exist in database. Please enter a valid key
>>> y.create("kiran05",5)
error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers
>>> y.modify("kiran",24)
>>> y.modify("kiran",15)
>>> y.read("kiran")
'kiran:15'
>>> #the value is modified
>>> y.delete("keerthana")
key is successfully deleted
>>> 