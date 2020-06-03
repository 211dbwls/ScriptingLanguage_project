from tkinter import *
from tkinter import font
import tkinter.messagebox
import urllib
import http.client
from xml.etree import ElementTree

class Main:
    def __init__(self):
        self.window = Tk()
        self.window.title("유기동물 조회 서비스")
        self.window.geometry("500x700")
        self.fontstyle = font.Font(self.window, size=20, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=14, weight='bold', family='Consolas')
        self.fontstyle3 = font.Font(self.window, size=10, weight='bold', family='Consolas')
        self.xml()
        self.setLabel()
        self.SearchBox()
        self.setupButton()
        self.CategoryCity()
        self.CategoryDistrict()
        self.CategoryKind()
        self.CategoryBreed()

        self.window.mainloop()

    def xml(self):
        self.conn1 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn1.request("GET",
                     "/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&bgnde=20190101&endde=20200604&upkind=417000&kind=&upr_cd=&org_cd=&care_reg_no=&state=notice&pageNo=1&numOfRows=100&neuter_yn=Y&")
        self.req1 = self.conn1.getresponse()
        self.strXml1 = self.req1.read().decode('utf-8')  # 강아지

        self.conn2 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn2.request("GET",
                     "/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&bgnde=20190101&endde=20200527&upkind=422400&kind=&upr_cd=&org_cd=&care_reg_no=&state=notice&pageNo=1&numOfRows=10&neuter_yn=Y&")
        self.req2 = self.conn2.getresponse()
        self.strXml2 = self.req2.read().decode('utf-8')  # 고양이

        self.conn3 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn3.request("GET",
                     "/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&bgnde=20190101&endde=20200527&upkind=429900&kind=&upr_cd=&org_cd=&care_reg_no=&state=notice&pageNo=1&numOfRows=10&neuter_yn=Y&")
        self.req3 = self.conn3.getresponse()
        self.strXml3 = self.req3.read().decode('utf-8')  # 기타

        self.LoadXMLFromFile()

    def LoadXMLFromFile(self):  # xml
        self.tree1 = ElementTree.fromstring(self.strXml1)
        self.tree2 = ElementTree.fromstring(self.strXml2)
        self.tree3 = ElementTree.fromstring(self.strXml3)

    def setLabel(self): # Label
        self.MainText = Label(text="유기동물 조회 서비스", width=24, height=1,  font=self.fontstyle, fg="black")
        self.MainText.place(x=80, y=50)

    def SearchBox(self): # 검색박스
        self.InputLabel = Entry(self.window, font=self.fontstyle2, width=36, borderwidth=10, relief='ridge')
        self.InputLabel.place(x=40, y=120)

    def setupButton(self): #버튼:검색버튼, 그래프 버튼(지역 / 품종)
        self.SearchButton = Button(self.window, text="검색", font=self.fontstyle2, borderwidth=5, command=self.SearchButtonAction)
        self.SearchButton.place(x=430, y=120)

        self.GraphAreaButton = Button(self.window, text="지역", width=20, font=self.fontstyle2, command=self.GraphArea)
        self.GraphAreaButton.place(x=40, y=400)

        self.GraphBreedButton = Button(self.window, text="품종", width=20, font=self.fontstyle2,command=self.GraphBreed)
        self.GraphBreedButton.place(x=270, y=400)

    def CategoryCity(self): #카테고리:지역(시도)
        self.CategoryCityList = ["서울특별시", "인천광역시", "경기도"]

        self.variable1 = StringVar(self.window)
        self.variable1.set(self.CategoryCityList[0])

        self.opt1 = OptionMenu(self.window, self.variable1, *self.CategoryCityList)
        self.opt1.config(width=17, font=self.fontstyle2)
        self.opt1.place(x=40, y=200)

    def CategoryDistrict(self): #카테고리:지역(구)
        self.CategoryDistrictList = ["강서구", "양천구", "영등포구"]

        self.variable2 = StringVar(self.window)
        self.variable2.set(self.CategoryDistrictList[0])

        self.opt2 = OptionMenu(self.window, self.variable2, *self.CategoryDistrictList)
        self.opt2.config(width=17, font=self.fontstyle2)
        self.opt2.place(x=270, y=200)

    def CategoryKind(self): #카테고리:품종(종류)
        self.CategoryKindList = ["강아지", "고양이", "기타"]

        self.variable3 = StringVar(self.window)
        self.variable3.set(self.CategoryKindList[0])

        self.opt3 = OptionMenu(self.window, self.variable3, *self.CategoryKindList)
        self.opt3.config(width=17, font=self.fontstyle2)
        self.opt3.place(x=40, y=300)

    def CategoryBreed(self): #카테고리:품종(품종)
        self.CategoryBreedList = ["골든 리트리버", "말티즈", "불독"]

        self.variable4 = StringVar(self.window)
        self.variable4.set(self.CategoryBreedList[0])

        self.opt4 = OptionMenu(self.window, self.variable4, *self.CategoryBreedList)
        self.opt4.config(width=17, font=self.fontstyle2)
        self.opt4.place(x=270, y=300)

    def BacktoMainButton(self):
        self.BacktomainButton = Button(self.window, text="뒤로", font=self.fontstyle2, borderwidth=5, command=self.BacktoMain)
        self.BacktomainButton.place(x=430, y=585)

    def BacktoMain(self):
        self.RenderText.destroy()
        self.RenderTextScrollbar.destroy()
        self.BacktomainButton.destroy()
        self.mapButton.destroy()
        self.bookmarkButton.destroy()

        self.SearchBox()
        self.setupButton()
        self.CategoryCity()
        self.CategoryBreed()
        self.CategoryDistrict()
        self.CategoryKind()

    def SearchButtonAction(self):
        self.GraphAreaButton.destroy()
        self.GraphBreedButton.destroy()
        self.opt1.destroy()
        self.opt2.destroy()
        self.opt3.destroy()
        self.opt4.destroy()

        self.MapButton()
        self.BookMarkButton()
        self.BacktoMainButton()

        self.RenderTextScrollbar = Scrollbar(self.window)
        self.RenderTextScrollbar.place(x=415, y=200)

        self.RenderText = Text(self.window, font=self.fontstyle3, width=50, height=27, borderwidth=12, relief='ridge', yscrollcommand=self.RenderTextScrollbar.set)
        self.RenderText.place(x=40, y=200)
        self.RenderTextScrollbar.config(command=self.RenderText.yview)

        self.RenderText.configure(state='disabled')

        self.RenderText.configure(state='normal')
        self.RenderText.delete(0.0, END)

        self.Search()

        self.RenderText.configure(state='disabled')

    def Search(self):
        self.retlist = []

        self.itemElements1 = self.tree1.iter("item")
        self.itemElements2 = self.tree2.iter("item")
        self.itemElements3 = self.tree3.iter("item")

        num1 = 0

        for item in self.itemElements1:
            self.strTitle = item.find("careNm")
            if (self.strTitle.text == self.InputLabel.get()):
                self.age = item.find("age")
                self.happenDt = item.find("happenDt")
                self.happenPlace = item.find("happenPlace")
                self.sexCd = item.find("sexCd")
                self.specialMark = item.find("specialMark")

                self.retlist.append([])

                self.retlist[num1].append(self.age.text)
                self.retlist[num1].append(self.happenDt.text)
                self.retlist[num1].append(self.happenPlace.text)
                self.retlist[num1].append(self.sexCd.text)
                self.retlist[num1].append(self.specialMark.text)

                num1 += 1

        for item in self.itemElements2:
            self.strTitle = item.find("careNm")
            if (self.strTitle.text == self.InputLabel.get()):
                self.age = item.find("age")
                self.happenDt = item.find("happenDt")
                self.happenPlace = item.find("happenPlace")
                self.sexCd = item.find("sexCd")
                self.specialMark = item.find("specialMark")

                self.retlist.append([])

                self.retlist[num1].append(self.age.text)
                self.retlist[num1].append(self.happenDt.text)
                self.retlist[num1].append(self.happenPlace.text)
                self.retlist[num1].append(self.sexCd.text)
                self.retlist[num1].append(self.specialMark.text)

                num1 += 1

        for item in self.itemElements3:
            self.strTitle = item.find("careNm")
            if (self.strTitle.text == self.InputLabel.get()):
                self.age = item.find("age")
                self.happenDt = item.find("happenDt")
                self.happenPlace = item.find("happenPlace")
                self.sexCd = item.find("sexCd")
                self.specialMark = item.find("specialMark")

                self.retlist.append([])

                self.retlist[num1].append(self.age.text)
                self.retlist[num1].append(self.happenDt.text)
                self.retlist[num1].append(self.happenPlace.text)
                self.retlist[num1].append(self.sexCd.text)
                self.retlist[num1].append(self.specialMark.text)

                num1 += 1

        for i in range(len(self.retlist)):
            self.RenderText.insert(INSERT, "\n나이:")
            self.RenderText.insert(INSERT, self.retlist[i][0])
            self.RenderText.insert(INSERT, "\n발견 날짜:")
            self.RenderText.insert(INSERT, self.retlist[i][1])
            self.RenderText.insert(INSERT, "\n발견 장소:")
            self.RenderText.insert(INSERT, self.retlist[i][2])
            self.RenderText.insert(INSERT, "\n성:")
            self.RenderText.insert(INSERT, self.retlist[i][3])
            self.RenderText.insert(INSERT, "\n특징:")
            self.RenderText.insert(INSERT, self.retlist[i][4])
            self.RenderText.insert(INSERT, "\n---------------------------------------")

            num1 = 0

    def MapButton(self):
        self.mapButton = Button(self.window, text="지도", font=self.fontstyle2, borderwidth=5, command=self.Map)
        self.mapButton.place(x=430, y=200)

    def Map(self):
        pass

    def BookMarkButton(self):
        self.bookmarkButton = Button(self.window, text="저장", font=self.fontstyle2, borderwidth=5, command=self.BookMark)
        self.bookmarkButton.place(x=430, y=250)

    def BookMark(self):
        pass

    def GraphArea(self):
        pass

    def GraphBreed(self):
        pass


Main()