
class Bootstrapper:
    
    def __init__(self, window):
        print("Initializing...")
        self.window = window
        
        print("Initialized successfull")
        
    def __del__(self):
        print("Closing application...")  
    
    
    def run(self):
        self.window.mainloop()