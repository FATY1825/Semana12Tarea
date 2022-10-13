from source import email
from dotenv import load_dotenv
from ast import Delete
from email import message
from ensurepip import bootstrap
from pydoc import text
from turtle import clear
from os import environ
from tkinter import Button, Entry, Label  , Tk, dialog

load_dotenv()
mensaje = """

<!DOCYPE html>
<html>
<body>
<h1>LE SALUDAMOS DESDE PYTHON {}</h1>
<p>{}</p>
</body>
</html>
"""

def enviar():
   vari=desti.get()
   vari2=escrib2.get()
   varia3=escrib3.get()
   Correo = email.Correo()
   Correo.mandar_correo([vari],"PYTHON", message_format=mensaje.format(vari2,varia3), format="html")

ventana = Tk()
ventana.geometry("540x350")
ventana.title("ENVIAR CORREO")
ventana.configure(bg="blue")


#ESTABLECER MEDIDAS Y DISEÑO DE CUADROS DE TEXTO
label1=Label(ventana, text="DESTINATARIO:"  ,bg="lightblue")
desti=Entry(ventana )
nam=Label(ventana, text="Nombre:"  ,bg="lightblue")
escrib2=Entry(ventana)
escrib3=Entry(ventana)
mensaje=Label(ventana, text="Redactar mensaje:",bg="lightblue")
btn1=Button(ventana, text="ENVIAR",  bg="lightblue", command=enviar )

label1.place(x=40,y=40)
desti.place(x=200, y=40, width=200, height=20)
nam.place(x=40,y=70)
escrib2.place(x=200, y=70 , width=200, height=20)
mensaje.place(x=40 , y=100)
escrib3.place(x=40, y=140 , width=400, height=100)
btn1.place(x=400, y=300)
ventana.mainloop()