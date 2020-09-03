from tkinter import *

def main():
    root = Tk()
    root.geometry("225x200")  

    box_size = (40,20,165,130)

    def change_color():
        color = entry_1.get()
        print(f'Changed to {color}')
        try:
            canvas.create_rectangle(box_size, fill=color)
        except:
            canvas.create_rectangle(box_size, fill="white")
            canvas.create_text(105, 55,text="NOT FOUND!", font=50)
        entry_1.delete(0, END)

    canvas = Canvas(root, width=200, height=350)
    canvas.pack()

    canvas.create_rectangle(box_size, fill="blue")
    entry_1 = Entry(root)
    entry_1.place(x=50, y=140)
    button_1  = Button(root, text="Change", command=change_color)
    button_1.place(x=85, y=165)

    mainloop()

if __name__ == "__main__":
    main()