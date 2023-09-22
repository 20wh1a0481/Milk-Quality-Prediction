import tkinter as tk
import pandas as pd
import numpy as np
import pickle
#rom joblib import dump, load
from PIL import Image, ImageTk

#model = load('model.pkl')
model = pickle.load(open("model.pkl","rb"))
def credit_score():
    pH = float(e0.get())
    Temprature = int(e1.get())
    Taste = int(e2.get())
    Odor = int(e5.get())
    Fat = int(e3.get())
    Turbidity = int(e4.get())
    colour = int(e6.get())
    
    
    userInput = pd.DataFrame({'pH': [pH], 'Temprature': [Temprature], 'Taste': [Taste], 'Odor': [Odor], 'Fat ': [Fat], 'Turbidity': [Turbidity], 'Colour': [colour]})
    
    prediction = model.predict(userInput)
    if prediction[0]==0:
        ans="high"
    elif prediction[0]==1:
        ans="low"
    else:
        ans="medium"

    result_label.config(text=ans)
    return ans
    
m = tk.Tk()

m.title("Milk QUlity Predection")
m.geometry('350x300')

bg_image = Image.open("image.png")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(m, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_image = bg_image.resize((500, 500), Image.ANTIALIAS)
#m.iconbitmap('creditlogo.ico')


button = tk.Button(m, text="Milk Quality Prediction")
button.grid(row=0, column=50,padx=10,pady=10)


tk.Label(m, text="PH").grid(row=1,column =0,padx=50,pady=10)
e0 = tk.Entry(m)
e0.grid(row=1, column=1)

tk.Label(m, text="Temperature").grid(row=3,column =0,padx=50,pady=10)
e1 = tk.Entry(m)
e1.grid(row=3, column=1)

tk.Label(m, text="Taste").grid(row=5,column =0,padx=50,pady=10)
e2 = tk.Entry(m)
e2.grid(row=5, column=1)

tk.Label(m, text="fat").grid(row=7,column =0,padx=50,pady=10)
e3 = tk.Entry(m)
e3.grid(row=7, column=1)

tk.Label(m, text="Turbidity").grid(row=9,column =0,padx=50,pady=10)
e4 = tk.Entry(m)
e4.grid(row=9, column=1)

tk.Label(m, text="odur").grid(row=11,column =0,padx=50,pady=10)
e5 = tk.Entry(m)
e5.grid(row=11, column=1)

tk.Label(m, text="colour").grid(row=13,column =0,padx=50,pady=10)
e6 = tk.Entry(m)
e6.grid(row=13, column=1)



result_label = tk.Label(m, text="")
result_label.grid(row=25, column=0, columnspan=2)

#result_label = tk.Label(m, text="")
#result_label.grid(row=9, column=0, columnspan=2)

predict_button = tk.Button(m, text="Predict", command=credit_score)
predict_button.grid(row=27, column=6)
m.mainloop()