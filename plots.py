from tkinter import Tk


from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('Plots')
root.iconbitmap('Images/WillRagB.ico')
root.geometry('400x200')

def graphs():
    # Average house price of $200,000, $25,000 variation, and 5000 data points
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()

my_button = Button(root, text="Graph it", command=graphs)
my_button.pack()

root.mainloop()