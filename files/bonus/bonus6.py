'''contents = ['All carrots are to bo sliced longitudinally',
            'the carrots were reportedly sliced',
            'the slicing process was well presented']

filenames = ['doc.txt','report.txt','presentation.txt']

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}",'w')
    file.write(content)'''
# NOTE: This script runs only on your local IDE
import FreeSimpleGUI as sg
from converters14 import convert

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input(key="inches")

button = sg.Button("Convert")
output_label = sg.Text("", key="output")

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button, output_label]])

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")


window.close()