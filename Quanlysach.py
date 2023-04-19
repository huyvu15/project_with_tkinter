#101:Quanlysach

from tkinter import *
from XuLyfile import *
from PIL import Image, ImageTk
import os

def themAction():
    line = stringMa.get()+";"+stringTen.get()+";"+stringNam.get()
    saveFile(line)
    stringTen.set("")
    stringMa.set("")
    stringNam.set("")
    showSach()

def delete_book():
    ma = stringMa.get()
    ten = stringTen.get()
    nam = stringNam.get()
    arrSach = readFile()
    with open("database.txt", "r") as f:
        lines = f.readlines()
    # new_lines = [line for line in lines if ma or ten or nam not in line]
    new_lines = [line for line in lines if ma + '\n' not in line and ten + '\n' not in line and nam + '\n' not in line]

    with open("database.txt", "w") as f:
        f.writelines(new_lines)
    showSach()



    
    
def showSach():
    arrSach = readFile()
    listbox.delete(0, END)
    for item in arrSach:
        listbox.insert(END, item)
    print(arrSach)

def sapXep():
    arrSach = readFile()
    print(len(arrSach))
    for i in range(len(arrSach)):
        for j in range(len(arrSach)):
            a = arrSach[i]
            b = arrSach[j]
            if a[2] > b[2]:
                arrSach[i] = b
                arrSach[j] = a
    listbox.delete(0, END)
    for item in arrSach:
        listbox.insert(END, item)

def Find():
    arrSach = readFile()
    ma = stringMa.get()
    found = False
    for sach in arrSach:
        if sach[0] == ma:
            found = True
            break
    if found:
        print("có cuốn này ")
    else:
        print("Éo tìm thấy")

root = Tk()

# Mở và hiển thị hình ảnh
img = Image.open("D:\image\had.png")
background_image = ImageTk.PhotoImage(img)

# Tạo đối tượng Label với hình ảnh nền
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.configure(bg='cyan')

stringMa = StringVar()
stringTen = StringVar()
stringNam = StringVar()

root.title("Quản lý sách")
root.minsize(height=300, width=500)
# root.re

Label(root, text="Quản lý sách", fg="red", font=("cambria", 16)).grid(row=0, columnspan=2)
listbox = Listbox(root, width=70)
listbox.grid(row =1, columnspan=2)
showSach()
Label(root, text = "Mã sách").grid(row=2, columnspan=1)
Entry(root, width=50, textvariable=stringMa).grid(row=2, column=1)

Label(root, text = "Tên sách").grid(row=3, columnspan=1)
Entry(root, width=50, textvariable=stringTen).grid(row=3, column=1)


Label(root, text = "Năm XB").grid(row=4, columnspan=1)
Entry(root, width=50, textvariable=stringNam).grid(row=4, column=1)

frameButton = Frame(root)
Button(frameButton, text = "Thêm", command=themAction).pack(side = LEFT)
Button(frameButton, text = "Xóa", command=delete_book).pack(side = LEFT)
Button(frameButton, text = "Tìm", command=Find).pack(side = LEFT)
Button(frameButton, text = "Sắp xếp", command=sapXep).pack(side = LEFT)
Button(frameButton, text = "Thoát", command=root.quit).pack(side = LEFT)
frameButton.grid(row=5, columnspan=2)


root.mainloop()