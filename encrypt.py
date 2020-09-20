from tkinter import *
import tkinter as tk
from tkinter import messagebox,filedialog
import base64

root=tk.Tk()
root.title("Base 64 Encoder & Decoder | Manjunathan C")
root.geometry("400x250")
ico=PhotoImage(file="icon.png")
root.iconphoto(True,ico)
root.config(bg="#0000ff")

def Encoder():
	def Encode():
		text.delete("1.0",END)

		string=entry.get()
		convert=string.encode("ascii")
		byte_convert=base64.b64encode(convert)
		base64str=byte_convert.decode("ascii")
		
		text.insert(tk.END,base64str)		

	root=tk.Tk()
	root.title("Base 64 Encoder | Manjunathan C")
	root.geometry("800x600")
	root.config(bg="#0000ff")

	label1=Label(root,text="Encode",font=("font awesome",18,"bold italic"),bg="#0000ff",fg="#f5873b").pack()

	entry=Entry(root,font=("fontawesome",12,"bold italic"),bg="#f5873b",width=50,fg="#0000ff",borderwidth=10)
	entry.place(x=100,y=50)

	text=Text(root,font=("fontawesome",15,"bold italic"),bg="#f5873b",width=40,height=10,fg="#0000ff",borderwidth=5)
	text.place(x=100,y=170)

	buttonclear=Button(root,text="clear",font=("fontawesome",15,"bold italic"),bg="#f5873b",width=7,fg="#0000ff",borderwidth=5,command=lambda: text.delete("1.0",END))
	buttonclear.place(x=320,y=420)

	buttonex=Button(root,text="Exit",font=("fontawesome",15,"bold italic"),bg="#f5873b",width=7,fg="#0000ff",borderwidth=5,command=root.destroy)
	buttonex.place(x=320,y=480)
		
	buttonenc=Button(root,text="Encode",font=("fontawesome",15,"bold italic"),bg="#f5873b",width=7,fg="#0000ff",borderwidth=5,command=Encode)
	buttonenc.place(x=320,y=110)
	
def Decoder():
	def Decode():
		text.delete("1.0",END)
		string=entry.get()

		try:
			convert=string.encode("ascii")
			byte_convert=base64.b64decode(convert)
			base64str=byte_convert.decode("ascii")

			text.insert(tk.END,base64str)

		except:
			messagebox.showerror("Wrong Input","The encrypted text is not look like Base64 value ")

	root=tk.Tk()
	root.title("Base 64 Decoder | Manjunathan C")
	root.geometry("800x600")
	root.config(bg="#0000ff")
	
	label1=Label(root,text="Decode",font=("font awesome",18,"bold italic"),bg="#0000ff",fg="#f5873b").pack()
	
	entry=Entry(root,font=("fontawesome",12,"bold italic"),bg="#f5873b",width=50,fg="#0000ff",borderwidth=10)
	entry.place(x=100,y=50)
	
	text=Text(root,font=("fontawesome",15,"bold italic"),bg="#f5873b",width=40,height=10,fg="#0000ff",borderwidth=5)
	text.place(x=100,y=170)
	
	buttonclear=Button(root,text="clear",font=("fontawesome",15,"bold italic"),bg="#f5873b",width=7,fg="#0000ff",borderwidth=5,command=lambda: text.delete("1.0",END))
	buttonclear.place(x=320,y=420)

	buttonex=Button(root,text="Exit",font=("fontawesome",15,"bold italic"),bg="#f5873b",width=7,fg="#0000ff",borderwidth=5,command=root.destroy)
	buttonex.place(x=320,y=480)
			
	buttondec=Button(root,text="Decode",font=("fontawesome",15,"bold italic"),bg="#f5873b",width=7,fg="#0000ff",borderwidth=5,command=Decode)
	buttondec.place(x=320,y=110)
	
def main():

	labelTitle=Label(root,text="Choose The Operation\nYou Want to Perform",font=("font awesome",14,"bold italic"),bg="#0000ff",fg="#f5873b").pack()

	buttonEnc=Button(root,text="Encoder",font=("fontawesome",15,"bold italic"),bg="#f5873b",width=7,fg="#0000ff",borderwidth=5,command=Encoder)
	buttonEnc.place(x=130,y=60)
	
	buttonDec=Button(root,text="Decoder",font=("fontawesome",15,"bold italic"),bg="#f5873b",width=7,fg="#0000ff",borderwidth=5,command=Decoder)
	buttonDec.place(x=130,y=110)
	
	buttonEx=Button(root,text="Exit",font=("fontawesome",15,"bold italic"),bg="#f5873b",width=7,fg="#0000ff",borderwidth=5,command=root.quit)
	buttonEx.place(x=130,y=160)

main()

root.mainloop()