import tkinter as ttk
import pandas as pd
model = pd.read_pickle('diabeticRF.pickle')
app = ttk.Tk()
app.geometry('400x400')
app.iconbitmap('sugar-blood-level.ico')
app.title('Diabetic Prediction')

ttk.Label(app,text='Please enter the following data',padx=15,pady=15).grid(row=1,column=0)
Glucose=ttk.Variable(app)
ttk.Label(app,text='Glucose',padx=15,pady=15).grid(row=2,column=0)
ttk.Entry(app,textvariable=Glucose,width=10).grid(row=2,column=1)

BMI=ttk.Variable(app)
ttk.Label(app,text='BMI',padx=15,pady=15).grid(row=4,column=0)
ttk.Entry(app,textvariable= BMI,width=10).grid(row=4,column=1)

Age=ttk.Variable(app)
ttk.Label(app,text='Age',padx=15,pady=15).grid(row=5,column=0)
ttk.Entry(app,textvariable=Age,width=10).grid(row=5,column=1)

BloodPressure=ttk.Variable(app)
ttk.Label(app,text='BloodPressure',padx=15,pady=15).grid(row=7,column=0)
ttk.Entry(app,textvariable=BloodPressure,width=10).grid(row=7,column=1)


result =ttk.Variable(app)
result.set('0')
def prediction():
    global model
    values = [[Glucose.get()],[BMI.get()],[Age.get()],[BloodPressure.get()]]
    cols = model.feature_names_in_
    query_df = pd.DataFrame(dict(zip(cols,values)))
    if(model.predict(pd.DataFrame(query_df))):pred = "YES DIABETIC "
    else:pred = "NOT DIABETIC"
    result.set(f'{pred}')

ttk.Button(app,text='Predict',command=prediction,font=('Arial',20)).grid(row=10,column=0,columnspan=2)


ttk.Label(app,textvariable=result,pady=15,font=('Arial',20),background='white').grid(row=12,column=0,columnspan=2)
app.mainloop()
