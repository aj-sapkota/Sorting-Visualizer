from tkinter import *
from tkinter import ttk
import random 

from algorithm.bubbleSort import bubbleSort
from algorithm.insertionSort import insertionSort
from algorithm.mergeSort import mergeSort
from algorithm.quickSort import quickSort

from color import *

# Creating a basic window
window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 800)
window.config(bg = GRAY)

algorithm_name = StringVar()
algo_list = ['Bubble Sort', 'Merge Sort','Quick Sort','Insertion Sort']

random_data = []
timeValue = 0.02

def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 300
    x_width = canvas_width / (len(data) + 1)
    spacing = 3
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width  + spacing
        y0 = canvas_height - height * 280
        x1 = (i + 1) * x_width 
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()
    
    
def generate():
    global data
    data = []
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        data.append(random_value)

    drawData(data, [BLUE for x in range(len(data))])

def sort():
    global data 
    if algo_button_list.get() == 'Bubble Sort':
        bubbleSort(data,drawData,timeValue)
    elif algo_button_list.get() == 'Insertion Sort':
        insertionSort(data,drawData,timeValue)
    elif algo_button_list.get() == 'Merge Sort':
        mergeSort(data,0,len(data)-1,drawData,timeValue)
    elif algo_button_list.get() == 'Quick Sort':
        quickSort(0,len(data)-1,data,drawData,timeValue)
    else:
        pass
    


#user interface 
UI_frame = Frame(window,width=800,height=300,bg=GRAY)   
UI_frame.grid(row=0,column=0,padx=10,pady=5) 

#dropdown to select sorting alogrithm
l1 = Label(UI_frame,text="Algorithm: ",bg=GRAY)
l1.grid(row=0,column=0,padx=5,pady=5,sticky=W)
algo_button_list = ttk.Combobox(UI_frame,textvariable=algorithm_name,values=algo_list)
algo_button_list.grid(row=0,column=1,padx=5,pady=5)
algo_button_list.current(0)

#button to generate array
b1 = Button(UI_frame,text="Generate Array",command=generate,bg=YELLOW)
b1.grid(row=1,column=0,padx=5,pady=5)

#button to generate array
b2 = Button(UI_frame,text="Sort",command=sort,bg=YELLOW)
b2.grid(row=1,column=1,padx=5,pady=5)

canvas = Canvas(window, width=800, height=300, bg=GRAY)
canvas.grid(row=1, column=0, padx=10, pady=5)

window.mainloop()