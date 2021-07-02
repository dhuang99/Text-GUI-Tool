#! /usr/bin/env python3

import tkinter as tk
from tkinter import *
import subprocess
import os
import sys
 
LARGEFONT =("Verdana", 20)
SMALLFONT = ("arial", 9)
global name
name = "No Name Provided"

#################### WINDOWS SIZE #################### 
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 800

  



class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        self.title("Terrapin Tech Sales Text Expander Tool")
        self.geometry(str(WINDOW_WIDTH) +"x"+ str(WINDOW_HEIGHT) + "+600+200")
        container = tk.Frame(self)
        container.pack(side = "top",)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, mainmenu, quote,order,invoice,spss,tracking,LSnotes,repairpay):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, mainmenu, quote respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  

############################## Start Page ##############################

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.namevar = tk.StringVar()
        
        #Variables
        title = Label(self, text ="Welcome to the Sales Text Expander Tool", font = LARGEFONT)
        namestr = tk.Label(self, text = "Name")
        nameEntry = Entry(self, textvariable= self.namevar, justify='center')
        submit = Button(self, text="Submit", command = lambda : [controller.show_frame(mainmenu), self.submit()])

        #Postitioning
        title.grid(row=5, column=1) 
        namestr.grid(row=13, column = 1)
        nameEntry.grid(row=14, column = 1, pady=10)
        submit.grid(row=16, column=1)

        
        for rows in range(0,20):
            self.grid_rowconfigure(rows, weight =1)
            rows += 1
        self.grid_columnconfigure(1, weight=1)
    def submit(self):
        global name
        if len(self.namevar.get()) != 0:    
            name = self.namevar.get()
            self.namevar.set("")


        
############################## Main Menu ##############################  

class mainmenu(tk.Frame):
   
    def __init__(self, parent, controller):
   
        tk.Frame.__init__(self, parent)

        label = Label(self, text ="Main Menu", font = LARGEFONT)
        spacing1 = Label(self, text =" ")
        spacing2 = Label(self, text =" ")
        but1 = Button(self, text ="Quote", command = lambda : controller.show_frame(quote))
        but2 = Button(self, text ="Order", command = lambda : controller.show_frame(order))
        but3 = Button(self, text ="Invoice", command = lambda : controller.show_frame(invoice))
        but4 = Button(self, text ="SPSS", command = lambda : controller.show_frame(spss))
        but5 = Button(self, text ="Apple Order Tracking Link", command = lambda : controller.show_frame(tracking))
        but6 = Button(self, text ="Lightspeed Notes", command = lambda : controller.show_frame(LSnotes))
        but7 = Button(self, text ="Hardware Repair Payment", command = lambda : controller.show_frame(repairpay))
        back = Button(self, text ="Back to Start", command = lambda : controller.show_frame(StartPage))

        label.grid(row = 0, column = 1, padx = 10, pady = 10)
        spacing1.grid(row = 1, column = 1, padx = 10, pady = 10)
        spacing2.grid(row = 2, column = 1, padx = 10, pady = 10)
        but1.grid(row = 3, column = 1, padx = 10, pady = 10)
        but2.grid(row = 4, column = 1, padx = 10, pady = 10)
        but3.grid(row = 5, column = 1, padx = 10, pady = 10)
        but4.grid(row = 6, column = 1, padx = 10, pady = 10)
        but5.grid(row = 7, column = 1, padx = 10, pady = 10)
        but6.grid(row = 8, column = 1, padx = 10, pady = 10)
        but7.grid(row = 9, column = 1, padx = 10, pady = 10)
        back.grid(row = 10, column = 1, padx = 10, pady = 10)

        
        self.grid_columnconfigure(1, weight=1)

    def printname(self):
        global name
        print(name)


############################## PAGES ##############################  

#Quote Page
class quote(tk.Frame):
    def __init__(self, parent, controller):
        #Variables
        tk.Frame.__init__(self, parent)
        self.custname = tk.StringVar()
        self.printstr_var = tk.StringVar()
        self.printstring = "Copy to Clipboard for a Preview"
        self.printstr_var.set(self.printstring)
        
        #Objects
        label = Label(self, text ="Quote", font = LARGEFONT)
        custlabel = Label(self, text= "Customer Name")
        self.customer = Entry(self, textvariable=self.custname, justify='center')
        self.quotestr = Label(self, textvariable = self.printstr_var, justify="left", wraplength=600, font=SMALLFONT)
        copy = Button(self, text= "Copy to Clipboard", command = lambda: self.makestr())
        clear = Button(self, text= "Clear", command = lambda: self.clear())
        back = Button(self, text ="Back to Menu", command = lambda : controller.show_frame(mainmenu))

        #Object Positioning
        label.grid(row=0, column=1, pady =10)
        custlabel.grid(row=5, column=1, sticky=W)
        self.customer.grid(row =5, column=1)
        self.quotestr.grid(row=10, column=1)
        copy.grid(row=16, column = 1)
        clear.grid(row = 18, column = 1, padx = 10, pady = 10, sticky= E)
        back.grid(row = 18, column = 1, padx = 10, pady = 10)

        #Weighting Row/Columns
        for rows in range(0,20):
            self.grid_rowconfigure(rows, weight =1)
            rows += 1
        self.grid_columnconfigure(1, weight=1)

    def clipboard(self):
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(self.printstring)
        r.update()
        r.destroy()
    def clear(self):
        self.customer.delete(0, 'end')
        self.printstring = "Copy to Clipboard for a Preview"
        self.printstr_var.set(self.printstring)
    def makestr(self):
        global name
        file = open(os.path.join(sys.path[0], "./texts/quote.txt"), encoding = "utf-8")
        self.printstring = file.read()
        self.printstring = self.printstring.replace("[customer]", self.custname.get())
        self.printstring = self.printstring.replace("[name]", name)
        self.printstr_var.set(self.printstring)
        self.clipboard()
        file.close()            


#Order Page
class order(tk.Frame):
    def __init__(self, parent, controller):
        #Variables
        tk.Frame.__init__(self, parent)
        self.custname = tk.StringVar()
        self.printstr_var = tk.StringVar()
        self.printstring = "Copy to Clipboard for a Preview"
        self.printstr_var.set(self.printstring)
        
        #Objects
        label = Label(self, text ="Order", font = LARGEFONT)
        custlabel = Label(self, text= "Customer Name")
        self.customer = Entry(self, textvariable=self.custname, justify='center')
        self.quotestr = Label(self, textvariable = self.printstr_var, justify="left", wraplength=600, font=SMALLFONT)
        copy = Button(self, text= "Copy to Clipboard", command = lambda: self.makestr())
        clear = Button(self, text= "Clear", command = lambda: self.clear())
        back = Button(self, text ="Back to Menu", command = lambda : controller.show_frame(mainmenu))

        #Object Positioning
        label.grid(row=0, column=1, pady =10)
        custlabel.grid(row=5, column=1, sticky=W)
        self.customer.grid(row =5, column=1)
        self.quotestr.grid(row=10, column=1)
        copy.grid(row=16, column = 1)
        clear.grid(row = 18, column = 1, padx = 10, pady = 10, sticky= E)
        back.grid(row = 18, column = 1, padx = 10, pady = 10)

        #Weighting Row/Columns
        for rows in range(0,20):
            self.grid_rowconfigure(rows, weight =1)
            rows += 1
        self.grid_columnconfigure(1, weight=1)

    def clipboard(self):
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(self.printstring)
        r.update()
        r.destroy()
    def clear(self):
        self.customer.delete(0, 'end')
        self.printstring = "Copy to Clipboard for a Preview"
        self.printstr_var.set(self.printstring)
    def makestr(self):
        global name
        file = open(os.path.join(sys.path[0], "./texts/order.txt"), encoding = "utf-8")
        self.printstring = file.read()
        self.printstring = self.printstring.replace("[customer]", self.custname.get())
        self.printstring = self.printstring.replace("[name]", name)
        self.printstr_var.set(self.printstring)
        self.clipboard()
        file.close()

#Invoice Page
class invoice(tk.Frame):
    def __init__(self, parent, controller):
        #Variables
        tk.Frame.__init__(self, parent)
        self.custname = tk.StringVar()
        self.printstr_var = tk.StringVar()
        self.printstring = "Copy to Clipboard for a Preview"
        self.printstr_var.set(self.printstring)
        
        #Objects
        label = Label(self, text ="Invoice", font = LARGEFONT)
        custlabel = Label(self, text= "Customer Name")
        self.customer = Entry(self, textvariable=self.custname, justify='center')
        self.quotestr = Label(self, textvariable = self.printstr_var, justify="left", wraplength=600, font=SMALLFONT)
        copy = Button(self, text= "Copy to Clipboard", command = lambda: self.makestr())
        clear = Button(self, text= "Clear", command = lambda: self.clear())
        back = Button(self, text ="Back to Menu", command = lambda : controller.show_frame(mainmenu))

        #Object Positioning
        label.grid(row=0, column=1, pady =10)
        custlabel.grid(row=5, column=1, sticky=W)
        self.customer.grid(row =5, column=1)
        self.quotestr.grid(row=10, column=1)
        copy.grid(row=16, column = 1)
        clear.grid(row = 18, column = 1, padx = 10, pady = 10, sticky= E)
        back.grid(row = 18, column = 1, padx = 10, pady = 10)

        #Weighting Row/Columns
        for rows in range(0,20):
            self.grid_rowconfigure(rows, weight =1)
            rows += 1
        self.grid_columnconfigure(1, weight=1)

    def clipboard(self):
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(self.printstring)
        r.update()
        r.destroy()
    def clear(self):
        self.customer.delete(0, 'end')
        self.printstring = "Copy to Clipboard for a Preview"
        self.printstr_var.set(self.printstring)
    def makestr(self):
        global name
        file = open(os.path.join(sys.path[0], "./texts/invoice.txt"), encoding = "utf-8")
        self.printstring = file.read()
        self.printstring = self.printstring.replace("[customer]", self.custname.get())
        self.printstring = self.printstring.replace("[name]", name)
        self.printstr_var.set(self.printstring)
        self.clipboard()
        file.close()
        
#SPSS Page
class spss(tk.Frame):
    def __init__(self, parent, controller):
        #Variables
        tk.Frame.__init__(self, parent)
        self.custname = tk.StringVar()
        self.printstr_var = tk.StringVar()
        self.printstring = "Copy to Clipboard for a Preview"
        self.printstr_var.set(self.printstring)
        
        #Objects
        label = Label(self, text ="SPSS Purchase", font = LARGEFONT)
        custlabel = Label(self, text= "Customer Name")
        self.customer = Entry(self, textvariable=self.custname, justify='center')
        self.quotestr = Label(self, textvariable = self.printstr_var, justify="left", wraplength=600, font=SMALLFONT)
        copy = Button(self, text= "Copy to Clipboard", command = lambda: self.makestr())
        clear = Button(self, text= "Clear", command = lambda: self.clear())
        back = Button(self, text ="Back to Menu", command = lambda : controller.show_frame(mainmenu))

        #Object Positioning
        label.grid(row=0, column=1, pady =10)
        custlabel.grid(row=5, column=1, sticky=W)
        self.customer.grid(row =5, column=1)
        self.quotestr.grid(row=10, column=1)
        copy.grid(row=16, column = 1)
        clear.grid(row = 18, column = 1, padx = 10, pady = 10, sticky= E)
        back.grid(row = 18, column = 1, padx = 10, pady = 10)

        #Weighting Row/Columns
        for rows in range(0,20):
            self.grid_rowconfigure(rows, weight =1)
            rows += 1
        self.grid_columnconfigure(1, weight=1)

    def clipboard(self):
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(self.printstring)
        r.update()
        r.destroy()
    def clear(self):
        self.customer.delete(0, 'end')
        self.printstring = "Copy to Clipboard for a Preview"
        self.printstr_var.set(self.printstring)
    def makestr(self):
        global name
        file = open(os.path.join(sys.path[0], "./texts/spss.txt"), encoding = "utf-8")
        self.printstring = file.read()
        self.printstring = self.printstring.replace("[customer]", self.custname.get())
        self.printstring = self.printstring.replace("[name]", name)
        self.printstr_var.set(self.printstring)
        self.clipboard()
        file.close()
        
        
#Hardware Repair Payment Page
class repairpay(tk.Frame):
    def __init__(self, parent, controller):
        #Variables
        tk.Frame.__init__(self, parent)
        self.link = tk.StringVar()
        self.printstr_var = tk.StringVar()
        self.printstring = "Copy to Clipboard for a Preview"
        self.printstr_var.set(self.printstring)
        
        #Objects
        label = Label(self, text ="Hardware Repair Payment Link", font = LARGEFONT)
        custlabel = Label(self, text= "Payment Link")
        self.elink = Entry(self, textvariable=self.link, justify='center')
        self.quotestr = Label(self, textvariable = self.printstr_var, justify="left", wraplength=600, font=SMALLFONT)
        copy = Button(self, text= "Copy to Clipboard", command = lambda: self.makestr())
        clear = Button(self, text= "Clear", command = lambda: self.clear())
        back = Button(self, text ="Back to Menu", command = lambda : controller.show_frame(mainmenu))

        #Object Positioning
        label.grid(row=0, column=1, pady =10)
        custlabel.grid(row=5, column=1, sticky=W)
        self.elink.grid(row =5, column=1)
        self.quotestr.grid(row=10, column=1)
        copy.grid(row=16, column = 1)
        clear.grid(row = 18, column = 1, padx = 10, pady = 10, sticky= E)
        back.grid(row = 18, column = 1, padx = 10, pady = 10)

        #Weighting Row/Columns
        for rows in range(0,20):
            self.grid_rowconfigure(rows, weight =1)
            rows += 1
        self.grid_columnconfigure(1, weight=1)

    def clipboard(self):
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(self.printstring)
        r.update()
        r.destroy()
    def clear(self):
        self.elink.delete(0, 'end')
        self.printstring = "Copy to Clipboard for a Preview"
        self.printstr_var.set(self.printstring)
    def makestr(self):
        global name
        file = open(os.path.join(sys.path[0], "./texts/repairpayment.txt"), encoding = "utf-8")
        self.printstring = file.read()
        self.printstring = self.printstring.replace("[link]", self.elink.get())
        self.printstring = self.printstring.replace("[name]", name)
        self.printstr_var.set(self.printstring)
        self.clipboard()
        file.close()


#Tracking Link Page
class tracking(tk.Frame):
    def __init__(self, parent, controller):
        #Variables
        tk.Frame.__init__(self, parent)
        options = ["Willie", "Autumn"]
        self.link = tk.StringVar()
        self.customer = tk.StringVar()
        self.order = tk.StringVar()
        self.default = StringVar()
        self.default.set(options[0])
        self.person = ""
        self.printstr_var = tk.StringVar()
        self.printstring = "Copy to Clipboard for a Preview"
        self.printstr_var.set(self.printstring)
        
        #Objects
        label = Label(self, text ="Apple Order Tracking Link", font = LARGEFONT)
        custlabel = Label(self, text = "Customer")
        linklabel = Label(self, text= "Apple Order Number")
        orderlabel = Label(self, text = "Lightspeed Order Number")
        self.ecustomer = Entry(self, textvariable=self.customer, justify='center')
        self.elink = Entry(self, textvariable=self.link, justify='center')
        self.eorder = Entry(self, textvariable=self.order, justify='center')
        self.personoption = OptionMenu(self, self.default, *options, command = lambda x: self.checkperson())
        self.quotestr = Label(self, textvariable = self.printstr_var, justify="left", wraplength=600, font=SMALLFONT)
        copy = Button(self, text= "Copy to Clipboard", command = lambda: self.makestr())
        clear = Button(self, text= "Clear", command = lambda: self.clear())
        back = Button(self, text ="Back to Menu", command = lambda : controller.show_frame(mainmenu))

        #Object Positioning
        label.grid(row=1, column=1, pady =10)
        custlabel.grid(row=3, column=1, sticky=W)
        self.ecustomer.grid(row =3, column=1)
        linklabel.grid(row=4, column=1, stick=W)
        self.elink.grid(row =4, column=1)
        orderlabel.grid(row =5, column=1, stick=W)
        self.eorder.grid(row =5, column=1)
        self.personoption.grid(row=6, column=1)
        self.quotestr.grid(row=10, column=1)
        copy.grid(row=17, column = 1)
        clear.grid(row = 18, column = 1, padx = 10, pady = 10, sticky= E)
        back.grid(row = 18, column = 1, padx = 10, pady = 10)

        #Weighting Row/Columns
        for rows in range(0,20):
            self.grid_rowconfigure(rows, weight =1)
            rows += 1
        self.grid_columnconfigure(1, weight=1)

    def clipboard(self):
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(self.printstring)
        r.update()
        r.destroy()
    def clear(self):
        self.elink.delete(0, 'end')
        self.eorder.delete(0, 'end')
        self.ecustomer.delete(0, 'end')
        self.printstring = "Copy to Clipboard for a Preview"
        self.printstr_var.set(self.printstring)
    def checkperson(self):
        if self.default.get() == "Willie":
            self.person = "wtam26%2540umd.edu"
        elif self.default.get() == "Autumn":
            self.person = "aschomis%2540umd.edu"
        else:
            self.person = ""
    def makestr(self):
        global name
        file = open(os.path.join(sys.path[0], "./texts/appletracking.txt"), encoding = "utf-8")
        self.printstring = file.read()
        aorw = "https://secure.store.apple.com/us/order/guest/[number]/[person]"
        aorw = aorw.replace("[number]", self.elink.get()).replace("[person]", self.person)
        self.printstring = self.printstring.replace("[link]", aorw)
        self.printstring = self.printstring.replace("[customer]", self.ecustomer.get())
        self.printstring = self.printstring.replace("[order]", self.eorder.get())
        self.printstring = self.printstring.replace("[name]", name)
        self.printstr_var.set(self.printstring)
        self.person = ""
        self.clipboard()
        file.close()

#Lightspeed Notes Page
class LSnotes(tk.Frame):
    def __init__(self, parent, controller):
        #Variables
        tk.Frame.__init__(self, parent)
        self.quote = tk.StringVar()
        self.order = tk.StringVar()
        self.po = tk.StringVar()
        self.kfs = tk.StringVar()
        self.shipto = tk.StringVar()
        self.printstr_var = tk.StringVar()
        self.printstring = "Copy to Clipboard for a Preview"
        self.printstr_var.set(self.printstring)
        
        #Objects
        label = Label(self, text ="Lightspeed Notes", font = LARGEFONT)
        quotelabel = Label(self, text= "Quote")
        orderlabel = Label(self, text= "Order")
        polabel = Label(self, text= "PO")
        kfslabel = Label(self, text= "KFS Number")
        shiptolabel = Label(self, text= "Ship to")
        self.equote = Entry(self, textvariable=self.quote, justify='center')
        self.eorder = Entry(self, textvariable=self.order, justify='center')
        self.epo = Entry(self, textvariable=self.po, justify='center')
        self.ekfs = Entry(self, textvariable=self.kfs, justify='center')
        self.eshipto = Entry(self, textvariable=self.shipto, justify='center')
        self.quotestr = Label(self, textvariable = self.printstr_var, justify="left", wraplength=600, font=SMALLFONT)
        copy = Button(self, text= "Copy to Clipboard", command = lambda: self.makestr())
        clear = Button(self, text= "Clear", command = lambda: self.clear())
        back = Button(self, text ="Back to Menu", command = lambda : controller.show_frame(mainmenu))

        #Object Positioning
        label.grid(row=0, column=1, pady =10)
        quotelabel.grid(row=1, column=1, sticky=W)
        orderlabel.grid(row=2, column=1, sticky=W)
        polabel.grid(row=3, column=1, sticky=W)
        kfslabel.grid(row=4, column=1, sticky=W)
        shiptolabel.grid(row=5, column=1, sticky=W)
        self.equote.grid(row =1, column=1)
        self.eorder.grid(row =2, column=1)
        self.epo.grid(row =3, column=1)
        self.ekfs.grid(row =4, column=1)
        self.eshipto.grid(row =5, column=1)
        self.quotestr.grid(row=10, column=1)
        copy.grid(row=16, column = 1)
        clear.grid(row = 18, column = 1, padx = 10, pady = 10, sticky= E)
        back.grid(row = 18, column = 1, padx = 10, pady = 10)

        #Weighting Row/Columns
        for rows in range(0,20):
            self.grid_rowconfigure(rows, weight =1)
            rows += 1
        self.grid_columnconfigure(1, weight=1)

    def clipboard(self):
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(self.printstring)
        r.update()
        r.destroy()
    def clear(self):
        self.equote.delete(0, 'end')
        self.eorder.delete(0, 'end')
        self.epo.delete(0, 'end')
        self.ekfs.delete(0, 'end')
        self.eshipto.delete(0, 'end')
        self.printstring = "Copy to Clipboard for a Preview"
        self.printstr_var.set(self.printstring)
    def makestr(self):
        global name
        file = open(os.path.join(sys.path[0], "./texts/lightspeednotes.txt"), encoding = "utf-8")
        self.printstring = file.read()
        self.printstring = self.printstring.replace("[quote]", self.equote.get())
        self.printstring = self.printstring.replace("[order]", self.eorder.get())
        self.printstring = self.printstring.replace("[po]", self.epo.get())
        self.printstring = self.printstring.replace("[kfs]", self.ekfs.get())
        self.printstring = self.printstring.replace("[shipto]", self.eshipto.get())
        self.printstr_var.set(self.printstring)
        self.clipboard()
        file.close()

#Driver Code
app = tkinterApp()
app.mainloop()
