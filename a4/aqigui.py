from tkinter import *
from tkinter import ttk

title = "Air Assessor 9000" #Better title than aqigui, follows naming scheme.
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
    # This functions gets the values from the entry boxes, converted them
    # to floats and then use a standard value dicionary to perform
    # the correct calculations
    # The largest aqi is then converted to have 2 decimal points and is set
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
        formattedAQI = "{:.2f}".format(largestAQI)
        AQI.set(formattedAQI)

    except ValueError:
        pass
    

# The tkinter work
# using row/column configure commands to allow for resizing
# Would have like to resize each object but decided it was not needed
# and this gui looks fine anyway.
root = Tk()
root.title(title)
frame = ttk.Frame(root, padding='3 3 12 12')
frame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight = 1, minsize = 20)
frame.rowconfigure(3, weight = 1, minsize = 20)
frame.rowconfigure(4, weight = 1, minsize = 20)
frame.columnconfigure(0,weight = 1)
frame.columnconfigure(1,weight = 1)
frame.columnconfigure(2, weight = 1)
frame.columnconfigure(3, weight = 1)
frame.columnconfigure(4, weight = 1)
frame.columnconfigure(5, weight = 1)

#entry box strings
ozone = StringVar()
sulfurDioxide = StringVar()
ozone = StringVar()
otherParticles = StringVar()
AQI = StringVar()

ozone_entry=ttk.Entry(frame, width=6, textvariable=ozone)
ozone_entry.grid(column=2, row=1, sticky=(W, E))

sulfurDioxide_entry=ttk.Entry(frame, width=6, textvariable=sulfurDioxide)
sulfurDioxide_entry.grid(column=2, row=2, sticky=(W, E))

otherParticles_entry=ttk.Entry(frame, width=6, textvariable=otherParticles)
otherParticles_entry.grid(column=2, row=3, sticky=(W, E))


aqi_label = ttk.Label(frame, textvariable=AQI)
aqi_label.grid(column=2, row=5, sticky=(N, E, S, W))

g_button = ttk.Button(frame, text='Calculate AQI', command=calculate)
g_button.grid(column=2, row=4, sticky=W)

ozone_label = ttk.Label(frame, text='Ozone:')
ozone_label.grid(column=1, row=1, sticky=E)
ozone_labelinfo = ttk.Label(frame, text='Parts per hundred million')
ozone_labelinfo.grid(column=3, row=1, sticky=W)

sulfurDioxide_label = ttk.Label(frame, text='Sulfur Dioxide:')
sulfurDioxide_label.grid(column=1, row=2, sticky=E)
sulfurDioxide_labelinfo = ttk.Label(frame, text='Parts per hundred million')
sulfurDioxide_labelinfo.grid(column=3, row=2, sticky=W)


otherParticles_label = ttk.Label(frame, text='Particles less than 2.5 micrometer diamter:')
otherParticles_label.grid(column=1, row=3, sticky=E)
otherParticlesinfo_label = ttk.Label(frame, text='Micrograms per cubic metre')
otherParticlesinfo_label.grid(column=3, row=3, sticky=W)


aqi_label = ttk.Label(frame, text='AQI:')
aqi_label.grid(column=1, row=5, sticky=E)

# Padding and the return key
for child in frame.winfo_children():
   child.grid_configure(padx=5, pady=6)
ozone_entry.focus()
sulfurDioxide_entry.focus()
root.bind('<Return>', calculate)
root.mainloop()