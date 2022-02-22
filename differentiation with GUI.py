import math
import PySimpleGUI as sg
import numpy as np
def differentiation(A: float, N: float) -> str:
   if N==1:
      return A
   elif n==0 or a==0:
      return 0
   else:
      an1=A*N
      b=N-1
      return f"{an1}x^{b}"

def error_code(f):
   try:
      f=float(f)
   except ValueError as float_conversion_err:
      sg.popup(f"{f} is not a numerical response")

def nanerror(g):
   if math.isnan(g):
      sg.popup("what in God's green Earth are you attempting to do???")
   

#UI
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside window.
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
   if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
   try:
      a=float(a)
      n=float(n)
   except ValueError as float_conversion_err:
      error_code(a)
      error_code(n)
   else:
      if math.isnan(a) or math.isnan(n):
         nanerror(a)
         nanerror(n)
      else:
         sg.popup(f"Answer is {differentiation(a,n)}")
window.close()
