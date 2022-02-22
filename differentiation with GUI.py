import math
from re import A
import PySimpleGUI as sg
def differentiation(A: float, N: float) -> str:
   if N==1:
      return A
   elif n==0 or a==0:
      return 0
   else:
      an1=A*N
      b=N-1
      return f"{an1}x^{b}"
#UI
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Differentiation Calculator')],
            [sg.Text('Enter value "a"'), sg.InputText()],
            [sg.Text('Enter value "n"'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Differentiation',layout)
# Window 
while True:
    event,values = window.read()
    a=values[0]
    n=values[1]
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if not(str.isnumeric(a)) and not(str.isnumeric(n)):
       sg.popup(f"Neither {a} or {n} are numerical responses")
    elif not(str.isnumeric(a)):
       sg.popup(f"{a} is not a numerical response")
    elif not(str.isnumeric(n)):
       sg.popup(f"{n} is not a numerical response")
    elif (str.isnumeric(a)) and (str.isnumeric(n)):
       a=float(a)
       n=float(n)
       sg.popup(f"answer is {differentiation(a,n)}")
window.close()
