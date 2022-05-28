import PySimpleGUI as sg
#list of students
list_of_students = ['Crash Overload', 'Cereal Killer', 'Zero cool','john']

sg.theme('DarkAmber')   # Add a touch of color
layout = [[sg.Text("Header")]]

for i in list_of_students:
    item = [sg.Text(i), sg.Button("present",key = i)]
    layout.append(item)

layout.append([sg.Output(size=(20, 20))])
layout.append([sg.Button('Cancel')])

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    print(event)

window.close()