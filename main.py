import tkinter as tk
from graph import Graph
from functools import partial

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("400x800")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.graph = Graph()

        self.frames = {}
        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("StartPage")
    
    def show_frame(self, page_name, text="Visitante"):
        frame = self.frames[page_name]
        if page_name == "PageOne":
            frame.change_text(text)
            frame.update_suggestions(sorted(list(self.graph.suggestion.items()), reverse=True, key=lambda x: x[1])[:10], 
                                     connected=bool( self.graph.graph.get(text) ))
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        welcome = tk.Label(self, text="Bem-Vindo")
        welcome.pack(side="top", pady=100)
        text = tk.Label(self, text="Digite seu nome para podermos inicar: ")
        text.pack(side="top", pady=10)
        self.ipt_txt = tk.Entry(self)
        self.ipt_txt.pack()

        button = tk.Button(self, text="Confirmar", command=self.next_page)
        button.pack(side="top", pady=15)

    def next_page(self):
        self.controller.show_frame("PageOne", text=self.ipt_txt.get())


class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.user = "Visitante"
        self.peoples = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.text = tk.StringVar()
        self.text.set("Ola")
        self.label = tk.Label(self, textvariable=self.text)
        self.label.pack(side="top", fill="x", pady=10)
        
        self.suggestion1 = tk.StringVar()
        self.suggestion2 = tk.StringVar()
        self.suggestion3 = tk.StringVar()
        self.suggestion4 = tk.StringVar()
        self.suggestion5 = tk.StringVar()
        self.suggestion6 = tk.StringVar()
        self.suggestion7 = tk.StringVar()
        self.suggestion8 = tk.StringVar()
        self.suggestion9 = tk.StringVar()
        self.suggestion10 = tk.StringVar()

        lb1 = tk.Label(self, textvariable=self.suggestion1)
        lb2 = tk.Label(self, textvariable=self.suggestion2)
        lb3 = tk.Label(self, textvariable=self.suggestion3)
        lb4 = tk.Label(self, textvariable=self.suggestion4)
        lb5 = tk.Label(self, textvariable=self.suggestion5)
        lb6 = tk.Label(self, textvariable=self.suggestion6)
        lb7 = tk.Label(self, textvariable=self.suggestion7)
        lb8 = tk.Label(self, textvariable=self.suggestion8)
        lb9 = tk.Label(self, textvariable=self.suggestion9)
        lb10 = tk.Label(self, textvariable=self.suggestion10)

        btn1 = tk.Button(self, text="Seguir", command=partial( self.follow, 0))
        btn2 = tk.Button(self, text="Seguir", command=partial( self.follow, 1))
        btn3 = tk.Button(self, text="Seguir", command=partial( self.follow, 2))
        btn4 = tk.Button(self, text="Seguir", command=partial( self.follow, 3))
        btn5 = tk.Button(self, text="Seguir", command=partial( self.follow, 4))
        btn6 = tk.Button(self, text="Seguir", command=partial( self.follow, 5))
        btn7 = tk.Button(self, text="Seguir", command=partial( self.follow, 6))
        btn8 = tk.Button(self, text="Seguir", command=partial( self.follow, 7))
        btn9 = tk.Button(self, text="Seguir", command=partial( self.follow, 8))
        btn10 = tk.Button(self, text="Seguir", command=partial( self.follow, 9))

        lb1.pack()
        btn1.pack()
        lb2.pack()
        btn2.pack()
        lb3.pack()
        btn3.pack()
        lb4.pack()
        btn4.pack()
        lb5.pack()
        btn5.pack()
        lb6.pack()
        btn6.pack()
        lb7.pack()
        btn7.pack()
        lb8.pack()
        btn8.pack()
        lb9.pack()
        btn9.pack()
        lb10.pack()
        btn10.pack()

    def change_text(self, text):
        self.user = text
        self.text.set(f"Olá {text}!\nAqui vão algumas sugestões de pessoas para você seguir:")

    def update_suggestions(self, names, connected=True):
        self.peoples = []
        for i in names:
            self.peoples.append(i[0])
        if connected:
            for i in range(10):
                names[i] = f'{names[i][0]}\nseguido(a) por {names[i][1]} das pessoas que você segue'
        else:
            for i in range(10):
                names[i] = f'{names[i][0]}\nseguido(a) por {names[i][1]} pessoas'

        self.suggestion1.set(names[0])
        self.suggestion2.set(names[1])
        self.suggestion3.set(names[2])
        self.suggestion4.set(names[3])
        self.suggestion5.set(names[4])
        self.suggestion6.set(names[5])
        self.suggestion7.set(names[6])
        self.suggestion8.set(names[7])
        self.suggestion9.set(names[8])
        self.suggestion10.set(names[9])

    def follow(self, pos):
        self.controller.graph.insert_edge(self.user, self.peoples[pos])
        self.update_suggestions( sorted( list(self.controller.graph.suggestion.items()), reverse=True, key=lambda x: x[1] )[:10] )


app = App()
app.mainloop()
