from tkinter import *
from gtts import gTTS # google text to speech python library
from playsound import playsound
import os

# window initializing
root=Tk()
root.geometry("500x500")
root.configure(bg = "white smoke")
root.title("Text to Speech Convertor")

Label(root, text = "TEXT TO SPEECH", font = "arial 20 bold", bg='white smoke').pack()
Label(text ="Manju Paryani", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')
Msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)
entry_field = Entry(root, textvariable = Msg ,width ='70')
entry_field.place(x=20,y=100)

#Function to Convert Text to Speech

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save(f'{Message}.mp3')
    playsound(f'{Message}.mp3')
    os.remove(f'{Message}.mp3') # isse ek hi text ko baar baar speech mai play kar sakte h

#function to reset
def Reset():
    Msg.set("")

#function to exit
def Exit():
    root.destroy()

Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4').place(x=25,y=140)
Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=100 , y = 140)
Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x=200, y = 140)


root.mainloop()
