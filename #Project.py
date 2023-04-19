#Project
# from bai 96

from tkinter import *

root = Tk()

root.title("Huy dang lam viec")
root.resizable(height= True, width=True)
# root.geometry(600x800)


# Label(root, text= "Muon thoat ha").pack(pady =10)
# Button(root, text="Khong").pack(side = RIGHT)
# Button(root, text="Co", command=root.quit).pack(side = RIGHT)# .quit la de thoat

Label(root, text= "Enter your name: ").pack(side=LEFT, padx=5, pady=10)
e = StringVar()
Entry(root, width=40, textvariable=e).pack(side=LEFT)
e.set("Vu Van Huy")
Button(root, text= "Say OK", command=root.quit).pack(side=LEFT)




root.mainloop()