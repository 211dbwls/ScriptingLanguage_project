from tkinter import *
from tkinter import font
import tkinter.messagebox
g_Tk = Tk()
g_Tk.geometry("500x700")


def InitTopText():
    TempFont = font.Font(g_Tk, size=20, weight='bold', family='Consolas')
    MainText = Label(g_Tk, font=TempFont, text="유기동물 조회 서비스")
    MainText.place(x=120, y=30)

def InitSearchLabel():
    global InputLabel
    TempFont = font.Font(g_Tk, size=16, weight='bold', family='Consolas')
    InputLabel = Entry(g_Tk, font=TempFont, width=30, borderwidth=12, relief='ridge')
    InputLabel.place(x=40, y=150)

def InitSearchButton():
    TempFont = font.Font(g_Tk, size=16, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="검색", command=SearchButtonAction)
    SearchButton.place(x=430, y=155)

def SearchButtonAction():
    pass

def InitCategoryArea():
    global CategoryArea
    ListBoxScrollbar = Scrollbar(g_Tk)
    ListBoxScrollbar.place(x=245, y=250)

    TempFont = font.Font(g_Tk, size=16, weight='bold', family='Consolas')
    CategoryArea = Listbox(g_Tk, font=TempFont, activestyle='none', width=15, height=1, borderwidth=12, relief='ridge', yscrollcommand=ListBoxScrollbar.set)

    CategoryArea.insert(1, "서울")
    CategoryArea.insert(2, "경기")
    CategoryArea.insert(3, "부산")
    CategoryArea.place(x=40, y=250)
    ListBoxScrollbar.config(command=CategoryArea.yview)

def InitCategoryBreed():
    global CategoryBreed
    ListBoxScrollbar = Scrollbar(g_Tk)
    ListBoxScrollbar.place(x=475, y=250)

    TempFont = font.Font(g_Tk, size=16, weight='bold', family='Consolas')
    CategoryBreed = Listbox(g_Tk, font=TempFont, activestyle='none', width=15, height=1, borderwidth=12, relief='ridge', yscrollcommand=ListBoxScrollbar.set)

    CategoryBreed.insert(1, "멍멍")
    CategoryBreed.insert(2, "야옹")
    CategoryBreed.insert(3, "왈왈")
    CategoryBreed.place(x=270, y=250)
    ListBoxScrollbar.config(command=CategoryBreed.yview)

def setupButton():
    TempFont = font.Font(g_Tk, size=16, weight='bold', family='Consolas')

    GraphAreaButton = Button(g_Tk, text="지역", width=15, font=TempFont, command=GraphArea, borderwidth=12, relief='ridge')
    GraphAreaButton.place(x=40, y=350)

    GraphBreedButton = Button(g_Tk, text="품종", width=15, font=TempFont, command=GraphBreed, borderwidth=12, relief='ridge')
    GraphBreedButton.place(x=270, y=350)

def GraphArea():
    pass

def GraphBreed():
    pass

InitTopText()
InitSearchLabel()
InitSearchButton()
InitCategoryArea()
InitCategoryBreed()
setupButton()

g_Tk.mainloop()