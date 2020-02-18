from tkinter import *
from keras.models import load_model
from auxillary import generate_prediction, generate_seq
from keras.preprocessing.text import Tokenizer
import pickle

num_epochs = 20

NUMBER_OF_WORDS = 15

with open("../saved_models/ra_top_{}.pickle".format(num_epochs), "rb") as f:
    list_of_params = pickle.load(f)
    tokenizer = list_of_params[0]
    max_length = list_of_params[1]


model_path = "../saved_models/ra_top_{}.h5".format(num_epochs)
model = load_model(model_path)

window = Tk()
window.title("Welcome text_gen")
window.geometry('650x400')
 
lbl = Label(window, text="Insert your two words here: ")
#lbl.grid(column=0, row=0)
lbl.pack()

txt = Entry(window, width=15)
txt.focus()
#txt.grid(column=1, row=0)
txt.pack()

def clicked():
    res =  generate_prediction(str(txt.get()), NUMBER_OF_WORDS, model, tokenizer, max_length)
    result.configure(text=res)

result = Label(window)
#result.grid(column=0, row=2)
result.pack()

btn = Button(window, text="Create Text", command=clicked)
#btn.grid(column=2, row=0)
btn.pack()

window.mainloop()