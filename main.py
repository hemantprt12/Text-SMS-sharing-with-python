#Importing Required Modules
import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror

# calling function for 2 arguments (1 is mobile no. & 2 is text massage)
def send_sms(number, message):
    url="https://www.fast2sms.com/dev/bulkV2"
    params = {
        'authorization': 'ipJvVSIZLDuAaTwlejf2RknPKrWt6XoE7H5NcxgYqhs9G08b13P6xbMDqfgQVGHULT3uEKveawXOko92',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'q',
        'numbers': number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)
    return dic.get('return')

#Creating GUI
def btn_click():
    num = textNumber.get()
    msg = textMsg.get("1.0", END)
    r = send_sms(num, msg)
    if r:
        showinfo("Send Success", "Successfully sent...")
    else:
        showerror("Error", "Something went wrong...!")

# Creating GUI
root = Tk()
root.title("Message Sender ")
root.geometry("400x550")
font = ("Helvetica", 20, "italic")
textNumber = Entry(root, font=font)
textNumber.pack(fill=X, pady=20)
textMsg = Text(root)
textMsg.pack(fill=X)
sendBtn = Button(root, text="SEND SMS", command=btn_click)
sendBtn.pack()
root.mainloop()