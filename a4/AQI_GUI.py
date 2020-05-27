from tkinter import *
from tkinter import ttk

title = "Air Assessor 9000"
author = "Mitchell Charity"

standard = {"o":8.0,"s": 20,"p": 25} # Dictionary for standard values

def largest(AQIA,a): 
  
    # Initialize maximum element 
    max = AQIA[0] 
  
    # Traverse array elementss
    # and compare every element with  
    # current max 
    for i in range(1, a): 
        if AQIA[i] > max: 
            max = AQIA[i] 
    return max

def calculate(*args):
    try:
        ozoneVal = float(ozone.get())
        sulfurDioxideVal = float(sulfurDioxide.get())
        otherParticlesVal = float(otherParticles.get())

        AQIO =100 * (ozoneVal / standard["o"] )
        round(AQIO)
        AQIS = 100 * ( sulfurDioxideVal / standard["s"] )
        round(AQIS)
        AQIP = 100 * ( otherParticlesVal / standard["p"] )
        round(AQIP)

        AQIA = [AQIO, AQIS, AQIP] # Array of results of AQI for O, S & P

        a = len(AQIA) # Length of array AQIA into variable a


        largestAQI = largest(AQIA, a)  # Make largest number AQI

        AQI.set(largestAQI)

    except ValueError:
        pass
    
root = Tk()
root.title(title)
frame = ttk.Frame(root, padding='3 3 12 12')
frame.grid(column=0, row=0, sticky=(N, W, E, S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

ozone = StringVar()
sulfurDioxide = StringVar()
ozone = StringVar()
otherParticles = StringVar()
AQI = StringVar()

ozone_entry=ttk.Entry(frame, width=8, textvariable=ozone)
ozone_entry.grid(column=3, row=1, sticky=(W, E))

sulfurDioxide_entry=ttk.Entry(frame, width=8, textvariable=sulfurDioxide)
sulfurDioxide_entry.grid(column=3, row=2, sticky=(W, E))

otherParticles_entry=ttk.Entry(frame, width=8, textvariable=otherParticles)
otherParticles_entry.grid(column=3, row=3, sticky=(W, E))


aqi_label = ttk.Label(frame, textvariable=AQI)
aqi_label.grid(column=3, row=4, sticky=(W, E))

g_button = ttk.Button(frame, text='Go', command=calculate)
g_button.grid(column=4, row=6, sticky=W)

ozone_label = ttk.Label(frame, text='Ozone')
ozone_label.grid(column=2, row=1, sticky=W)
sulfurDioxide_label = ttk.Label(frame, text='Sulfur Dioxide')
sulfurDioxide_label.grid(column=2, row=2, sticky=W)
otherParticles_label = ttk.Label(frame, text='Particles less than 2.5 micrometer diamter:')
otherParticles_label.grid(column=2, row=3, sticky=W)


d_label = ttk.Label(frame, text='AQI:')
d_label.grid(column=2, row=4, sticky=W)


for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)
ozone_entry.focus()
sulfurDioxide_entry.focus()
root.bind('<Return>', calculate)
root.mainloop()