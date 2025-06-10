import FreeSimpleGUI as sg
from converters14 import convert

label1 = sg.Text("Enter feet:")
input1 = sg.Input(tooltip="enter value")


label2 = sg.Text("Enter inches:")
input2= sg.Input(tooltip="Enter Value")

convert_button = sg.Button("Convert")
o_l = sg.Text(" ",key= "output")

window = sg.Window("Converter",layout=[[label1,input1],
                                       [label2,input2],
                                       [convert_button,o_l]])

while True:
    event,values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet,inches)
    window["output"].update(value = f"{result} m",text_color="white")

window.read()
window.close()