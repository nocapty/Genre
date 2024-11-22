from tkinter import *

class Application(Frame):
    
    def __init__(self, master):
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()

    def create_widgets(self):
            
        
        Label(self,
              text = "Choose your favorite movie genre"
              ).grid(row = 0, column = 0, sticky = W)

        
        Label(self,
              text = "Select all that apply:"
              ).grid(row = 1, column = 0, sticky = W)
        
        
        self.likes_comedy = BooleanVar()
        Checkbutton(self,
                    text = "Comedy",
                    variable = self.likes_comedy,
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)

        
        self.likes_drama = BooleanVar()
        Checkbutton(self,
                    text = "Drama",
                    variable = self.likes_drama,
                    command = self.update_text
                    ).grid(row = 3, column = 0, sticky = W)

        
        self.likes_romance = BooleanVar()
        Checkbutton(self,
                    text = "Romance",
                    variable = self.likes_romance,
                    command = self.update_text
                    ).grid(row = 4, column = 0, sticky = W)
        
        self.likes_action = BooleanVar()
        Checkbutton(self,
                    text = "Action",
                    variable = self.likes_action,
                    command = self.update_text
                    ).grid(row = 5, column = 0, sticky = W)
        
        self.likes_horror = BooleanVar()
        Checkbutton(self,
                    text = "Horror",
                    variable = self.likes_horror,
                    command = self.update_text
                    ).grid(row = 6, column = 0, sticky = W)
        
        self.likes_thriller = BooleanVar()
        Checkbutton(self,
                    text = "Thriller",
                    variable = self.likes_thriller,
                    command = self.update_text
                    ).grid(row = 7, column = 0, sticky = W)

        
        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row = 8, column = 0, columnspan = 3)

    def update_text(self):
        
        likes = ""
        
        if self.likes_comedy.get():
            likes += "You like comedic movies.\n"

        if self.likes_drama.get():
            likes += "You like dramatic movies.\n"

        if self.likes_romance.get():
            likes += "You like romantic movies.\n"

        if self.likes_action.get():
            likes += "You like action movies.\n"

        if self.likes_horror.get():
            likes += "You like horror movies.\n"

        if self.likes_thriller.get():
            likes += "You like thriller movies.\n"
      
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, likes)

# main
root = Tk()
root.title("Movie Chooser")
app = Application(root)
root.mainloop()