import webbrowser
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
import os

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
try:
    if not os.path.isfile(fr"{desktop}\WaterMark-App"):
        os.mkdir(fr"{desktop}\WaterMark-App")
except FileExistsError:
    pass
im = "img/logo_sm.png"
IMAGE_SIZE = (0, 0)
MARK_SIZE = (0, 0)
saved = False
windows = Tk("WaterMark")
windows.title("Water Mark App")
windows.geometry("520x450")
windows.config(bg="#392467")

# img = Image.open(fr"{desktop}\WaterMark-App\\1.png")
# draw = ImageDraw.Draw(img)
# font = ImageFont.truetype('Halogen.ttf', size=50)
# draw.text((1300, 640), 'hi', font)


def logo_select():
    global im, y
    try:
        if not os.path.isfile(fr"{desktop}\WaterMark-App"):
            os.mkdir(fr"{desktop}\WaterMark-App")
    except FileExistsError:
        pass
    t = Image.open("".join(filedialog.askopenfilenames())).resize((352, 188))
    t.save(fr"{desktop}\WaterMark-App\\1.png")
    im = fr"{desktop}\WaterMark-App\\1.png"
    y = Image.open(im).resize((300, 100))
    canvas.config(width=800, height=900, highlightthickness=0, bg='#392467')
    image.config(file=f"{fr"{desktop}\WaterMark-App\\1.png"}")
    canvas.create_image(250, 70, image=image)
    canvas.place(x=80, y=100)


canvas = Canvas(width=800, height=900, highlightthickness=0, bg='#392467')
image = PhotoImage(file=f"{im}")
canvas.create_image(250, 70, image=image)
canvas.place(x=80, y=100)

y = Image.open(im).resize((300, 100))


def update():
    try:
        if not os.path.isfile(fr"{desktop}\WaterMark-App"):
            os.mkdir(fr"{desktop}\WaterMark-App")
    except FileExistsError:
        pass
    # windows.withdraw()
    global IMAGE_SIZE, MARK_SIZE, saved
    try:
        if not v.get() and not int(image_x_size.get()):
            print((type(v.get())))
            messagebox.showinfo(title='WaterMark', message="Please Select a size!!!")
            return

        elif v.get() == 8:
            x_entry = int(image_x_size.get())
            y_entry = int(image_y_size.get())
            print(x_entry, y_entry)
            IMAGE_SIZE = (x_entry, y_entry)

        elif image_x_size.get() and v.get():
            messagebox.showinfo(title='WaterMark', message="A size has been selected!!!")
            image_x_size.delete(0, END)
            image_y_size.delete(0, END)
            return
        elif image_y_size.get() and v.get():
            messagebox.showinfo(title='WaterMark', message="A size has been selected!!!")
            image_x_size.delete(0, END)
            image_y_size.delete(0, END)
            return
    except ValueError:
        messagebox.showinfo(title="WaterMark", message='Please Enter or Select your preferred photo size!!!')
        return
    images = filedialog.askopenfilenames()
    files = [int(f.strip(".png")) for f in
             os.listdir(fr"{desktop}\WaterMark-App")]

    if not files:
        x = 0
    else:
        x = files[-1]
    for i in images:
        print(f"{i}")
        img = Image.open(i)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('BOD_B.TTF', size=90)
        draw.text((50, 250), text=text_entry.get(), font=font)
        try:
            img.thumbnail(IMAGE_SIZE)
        except ZeroDivisionError:
            img.thumbnail((int(image_x_size.get()), int(image_x_size.get())))
        y.thumbnail((200, 200))
        # if not text_entry.get():
        try:
            img.paste(y, box=MARK_SIZE, mask=y)
        except ValueError:
            img.paste(y, box=MARK_SIZE)



        x += 1
        img.save(fr"{desktop}\WaterMark-App\\{x}.png")

        saved = True
        print(saved)
        if saved:
            webbrowser.open(fr"{desktop}\WaterMark-App")


upload_btn = Button(text='Update Image', bg="#5D3587", fg="#FFD1E3",
                    font=("Elephant", 13, "normal"), highlightthickness=5, command=update)
upload_btn.place(x=150, y=350)

logo_btn = Button(text='Select Logo', bg="#5D3587", fg="#FFD1E3",
                  font=("Elephant", 13, "normal"), highlightthickness=5, command=logo_select)
logo_btn.place(x=325, y=350)

size_label = Label(text="Photo Size:", font=("Elephant", 20, "normal"), bg="#392467", fg='#FFD1E3')
size_label.place(x=20, y=50)

other_size_label = Label(text="Other Size:", font=("Elephant", 12, "normal"), bg="#392467", fg='#FFD1E3')
other_size_label.place(x=20, y=300)

x_label = Label(text="X", font=("Elephant", 10, "normal"), bg="#392467", fg='#FFD1E3')
x_label.place(x=20, y=335)
image_x_size = Entry(name="x", bg="#5D3587", fg='white', width=8, border=3)
image_x_size.place(x=50, y=335)

y_label = Label(text="Y", font=("Elephant", 10, "normal"), bg="#392467", fg='#FFD1E3')
y_label.place(x=20, y=370)
image_y_size = Entry(name="y", bg="#5D3587", fg='white', width=8, border=3)
image_y_size.place(x=50, y=370)

text_entry = Entry(name="text", bg="#5D3587", fg='white', width=48, border=3)
text_entry.place(x=150, y=265)


def radio_use():
    global IMAGE_SIZE, MARK_SIZE
    if v.get() == 1:
        IMAGE_SIZE = (300, 300)
    elif v.get() == 2:
        IMAGE_SIZE = (400, 400)
    elif v.get() == 3:
        IMAGE_SIZE = (500, 500)
    elif v.get() == 4:
        IMAGE_SIZE = (600, 600)
    elif v.get() == 5:
        IMAGE_SIZE = (700, 700)
    elif v.get() == 6:
        IMAGE_SIZE = (800, 800)
    elif v.get() == 7:
        IMAGE_SIZE = (900, 900)
    else:
        return False


axe_y = 70
v = IntVar()
values = {"300 * 300": "1",
          "400 * 400": "2",
          "500 * 500": "3",
          "600 * 600": "4",
          "700 * 700": "5",
          "800 * 800": "6",
          "900 * 900": "7",
          "Other": "8",
          }

# Loop is used to create multiple Radiobutton
# rather than creating each button separately
for (text, value) in values.items():
    axe_y += 25

    Radiobutton(text=text, variable=v,
                value=value, fg='brown',
                background="#392467", command=radio_use).place(x=15, y=axe_y)

windows.mainloop()
