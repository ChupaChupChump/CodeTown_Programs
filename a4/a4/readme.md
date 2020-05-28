# CodeTown_Programs
Python programs for an imaginary client called CodeTown


## Installation and requirements
aqigui.py is a program made for Codetown as part of COSC110 Programming Task 3.
The purpose of the program is to calculate AQI using a graphical user interface

- Assure you have Python 3.8 installed
- Assure you have tkinter module installed



## Running the program
To open and run the program:
    - First assure you are in the same directory as a4.tgz 
    to access aqigui.py you will first have to run

```bash
tar -xzvf a4.tgz
cd a4/
```

After assuring you are in the same directory as aqigui.py run to start the program

```bash
python3 aqigui.py
```

if the above command does not work run
```bash
chmod a+x aqigui.py
```
then rerun the python3 command

## Usage
To use aqigui.py enter your values and click the "Calculate AQI" button.


## Further infomation

The calculate function is done as so

```python
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
        formattedAQI = "{:.2f}".format(largestAQI)
        AQI.set(formattedAQI)

    except ValueError:
        pass
```

to find the largest AQI from the reading I used a function called largest

```python
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
```
