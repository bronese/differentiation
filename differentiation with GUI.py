import math
from re import A
import PySimpleGUI as sg
def differentiation(A,N):
   if N==1:
      return A
   elif n==0 or a==0:
      return 0
   else:
      an1=A*N
      an1=str(an1)
      b=N-1
      b=str(b)
      return an1+"x^"+b
   
def error_code(a):
   if not(str.isnumeric(a)):
      print(f"{a} is not a numerical response")
      
def error_code(n):
   if not(str.isnumeric(n)):
      print(f"{n} is not a numerical response")

a=int
n=int
#UI
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Differentiation Calculator')],
            [sg.Text('Enter value "a"'), sg.InputText(key=a)],
            [sg.Text('Enter value "n"'), sg.InputText(key=n)],
            [sg.Text](key=reult)
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Differentiation', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read(a)
    event, values = window.read(n)
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
result=print(differentiation(a,n))

window.close()
