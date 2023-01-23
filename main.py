from tkinter import *
import tkinter as tk
from tkinter import ttk

from src.bootstrapper import Bootstrapper

window = Tk()
window.title("Game Engine")

mainFrame = ttk.Frame(window, padding="125 125 125 125")

if __name__ == '__main__':
    app = Bootstrapper(window)
    
    app.run()