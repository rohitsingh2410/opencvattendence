
def start():
    import tkinter 
    from tkinter import BOTTOM
    from dataSet import data
    from newDetectorTry import detect
    from trainer import train
    
    window = tkinter.Tk()
    window.title("Facial recognition system")
    window.geometry("500x700")
    #
    photo = tkinter.PhotoImage(file='logo.gif')
    w = tkinter.Label(window, image=photo)
    w.pack()
    image1 = tkinter.PhotoImage(file="background.gif")
    w = image1.width()
    h = image1.height()
    #window.geometry("%dx%d+0+0" % (w, h))
    panel1 = tkinter.Label(window, image=image1)
    panel1.pack(side='top', fill='both', expand='yes')

    #button2 = tkinter.Button(panel1, text='button2')
    #button2.pack(side='right')

    detect = tkinter.Button(window, text = "Detect",bg='#383a39',fg='#a1dbcd' , command =detect)
    detect.pack(padx=5, pady=10, side=BOTTOM)

    tra = tkinter.Button(window, text = "train data",bg='#383a39',fg='#a1dbcd' , command =train)
    tra.pack(padx=5, pady=10, side=BOTTOM)
    
    data = tkinter.Button(window, text = "Create Dataset",bg='#383a39',fg='#a1dbcd' , command =data)
    data.pack(padx=5, pady=10, side=BOTTOM)
    
    window.mainloop()


if __name__ == "__main__":
    start()
