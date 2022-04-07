from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename


def open_file():

    image_path = askopenfilename()
    img = Image.open(image_path)
    wm = Image.open('watermark-logo.jpg').resize(img.size)
    wmm = wm.copy()
    wmm.putalpha(20)
    img.paste(wmm, mask=wmm)
    img.show()
    img_name = image_path.split('/')[-1]
    img.save(f"C:/Users/hassa/Desktop/Ibrahim/watermarking/watermarked_images/{img_name}")


window = Tk()
window.title("Watermarking App")
window.config(width=300, height=200, bg="#826F66", padx=20, pady=20)

canvas = Canvas(window, width=300, height=200, bg="#826F66", bd=0, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

logo = ImageTk.PhotoImage(Image.open("logo.png"))
canvas.create_image(150, 100, image=logo)

upload_button = Button(text="Browse", width=10, height=2, bg='#C69B7B', command=open_file, highlightthickness=0)
upload_button.grid(column=0, row=1)

exit_button = Button(text="Exit", width=10, height=2, bg='#C69B7B', command=window.destroy, highlightthickness=0)
exit_button.grid(column=1, row=1)
window.mainloop()
