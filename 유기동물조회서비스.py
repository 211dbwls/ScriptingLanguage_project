from tkinter import *
from tkinter import font
from tkinter import ttk
from io import BytesIO
import tkinter.messagebox
import urllib
import urllib.request
from PIL import Image,ImageTk
import http.client
from xml.etree import ElementTree
import folium
import webbrowser
import json
import requests
from bs4 import BeautifulSoup

# smtp 정보
host = "smtp.gmail.com" # Gmail SMTP 서버 주소.
port = "587"

class Main:
    def __init__(self):
        self.window = Tk()
        self.window.title("유기동물 조회 서비스")
        self.window.geometry("500x700")
        self.window.configure(bg='floral white')
        self.fontstyle = font.Font(self.window, size=20, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=14, weight='bold', family='Consolas')
        self.fontstyle3 = font.Font(self.window, size=10, weight='bold', family='Consolas')
        self.fontstyle4 = font.Font(self.window, size=8, weight='bold', family='Consolas')
        self.xml()
        self.setLabel()
        self.SearchBox()
        self.setupButton()
        self.CategoryCity()
        self.CategoryDistrictScreen()
        self.CategoryKind()
        self.CategoryBreedScreen()

        self.window.mainloop()

    def xml(self):
        # 강아지
        self.conn1 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn1.request("GET",
                     "/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&upkind=417000&pageNo=1&numOfRows=8000&")
        self.req1 = self.conn1.getresponse()
        self.strXml1 = self.req1.read().decode('utf-8')

        # 고양이
        self.conn2 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn2.request("GET",
                     "/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&&upkind=422400&pageNo=1&numOfRows=1000&")
        self.req2 = self.conn2.getresponse()
        self.strXml2 = self.req2.read().decode('utf-8')

        # 기타
        self.conn3 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn3.request("GET",
                     "/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&upkind=429900&pageNo=1&numOfRows=100&")
        self.req3 = self.conn3.getresponse()
        self.strXml3 = self.req3.read().decode('utf-8')

        # 시도
        self.conn4 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn4.request("GET",
                           "/openapi/service/rest/abandonmentPublicSrvc/sido?ServiceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&pageNo=1&numOfRows=50&")
        self.req4 = self.conn4.getresponse()
        self.strXml4 = self.req4.read().decode('utf-8')

        # 서울특별시
        self.conn5 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn5.request("GET",
                           "/openapi/service/rest/abandonmentPublicSrvc/sigungu?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&upr_cd=6110000&")
        self.req5 = self.conn5.getresponse()
        self.strXml5 = self.req5.read().decode('utf-8')

        # 부산광역시
        self.conn6 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn6.request("GET",
                           "/openapi/service/rest/abandonmentPublicSrvc/sigungu?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&upr_cd=6260000&")
        self.req6 = self.conn6.getresponse()
        self.strXml6 = self.req6.read().decode('utf-8')

        # 대구광역시
        self.conn7 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn7.request("GET",
                           "/openapi/service/rest/abandonmentPublicSrvc/sigungu?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&upr_cd=6270000&")
        self.req7 = self.conn7.getresponse()
        self.strXml7 = self.req7.read().decode('utf-8')

        # 인천광역시
        self.conn8 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn8.request("GET",
                           "/openapi/service/rest/abandonmentPublicSrvc/sigungu?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&upr_cd=6280000&")
        self.req8 = self.conn8.getresponse()
        self.strXml8= self.req8.read().decode('utf-8')

        # 광주광역시
        self.conn9 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn9.request("GET",
                           "/openapi/service/rest/abandonmentPublicSrvc/sigungu?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&upr_cd=6290000&")
        self.req9 = self.conn9.getresponse()
        self.strXml9 = self.req9.read().decode('utf-8')

        # 세종특별자치시
        self.conn10 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn10.request("GET",
                           "/openapi/service/rest/abandonmentPublicSrvc/sigungu?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&upr_cd=5690000&")
        self.req10 = self.conn10.getresponse()
        self.strXml10 = self.req10.read().decode('utf-8')

        # 대전광역시
        self.conn11 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn11.request("GET",
                           "/openapi/service/rest/abandonmentPublicSrvc/sigungu?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&upr_cd=6300000&")
        self.req11 = self.conn11.getresponse()
        self.strXml11 = self.req11.read().decode('utf-8')

        # 울산광역시
        self.conn12 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn12.request("GET",
                           "/openapi/service/rest/abandonmentPublicSrvc/sigungu?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&upr_cd=6310000&")
        self.req12 = self.conn12.getresponse()
        self.strXml12 = self.req12.read().decode('utf-8')

        # 경기도
        self.conn13 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn13.request("GET",
                           "/openapi/service/rest/abandonmentPublicSrvc/sigungu?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&upr_cd=6410000&")
        self.req13 = self.conn13.getresponse()
        self.strXml13 = self.req13.read().decode('utf-8')

        # 강원도
        self.conn14 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn14.request("GET",
                           "/openapi/service/rest/abandonmentPublicSrvc/sigungu?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&upr_cd=6420000&")
        self.req14 = self.conn14.getresponse()
        self.strXml14 = self.req14.read().decode('utf-8')

        # 충청북도
        self.conn15 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn15.request("GET",
                           "/openapi/service/rest/abandonmentPublicSrvc/sigungu?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&upr_cd=6430000&")
        self.req15 = self.conn15.getresponse()
        self.strXml15 = self.req15.read().decode('utf-8')

        # 충청남도
        self.conn16 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn16.request("GET",
                           "/openapi/service/rest/abandonmentPublicSrvc/sigungu?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&upr_cd=6440000&")
        self.req16 = self.conn16.getresponse()
        self.strXml16 = self.req16.read().decode('utf-8')

        # 전라북도
        self.conn17 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn17.request("GET",
                           "/openapi/service/rest/abandonmentPublicSrvc/sigungu?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&upr_cd=6450000&")
        self.req17 = self.conn17.getresponse()
        self.strXml17 = self.req17.read().decode('utf-8')

        # 전라남도
        self.conn18 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn18.request("GET",
                           "/openapi/service/rest/abandonmentPublicSrvc/sigungu?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&upr_cd=6460000&")
        self.req18 = self.conn18.getresponse()
        self.strXml18 = self.req18.read().decode('utf-8')

        # 경상북도
        self.conn19 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn19.request("GET",
                           "/openapi/service/rest/abandonmentPublicSrvc/sigungu?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&upr_cd=6470000&")
        self.req19 = self.conn19.getresponse()
        self.strXml19 = self.req19.read().decode('utf-8')

        # 경상남도
        self.conn20 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn20.request("GET",
                           "/openapi/service/rest/abandonmentPublicSrvc/sigungu?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&upr_cd=6480000&")
        self.req20 = self.conn20.getresponse()
        self.strXml20 = self.req20.read().decode('utf-8')

        # 제주특별자치도
        self.conn21 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn21.request("GET",
                            "/openapi/service/rest/abandonmentPublicSrvc/sigungu?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&upr_cd=6500000&")
        self.req21 = self.conn21.getresponse()
        self.strXml21 = self.req21.read().decode('utf-8')

        self.LoadXMLFromFile()

    def LoadXMLFromFile(self):  # xml
        self.tree1 = ElementTree.fromstring(self.strXml1) #강아지
        self.tree2 = ElementTree.fromstring(self.strXml2) #고양이
        self.tree3 = ElementTree.fromstring(self.strXml3) #기타

        self.tree4 = ElementTree.fromstring(self.strXml4)  # 시도

        self.tree5 = ElementTree.fromstring(self.strXml5)  # 서울특별시
        self.tree6 = ElementTree.fromstring(self.strXml6)  # 부산광역시
        self.tree7 = ElementTree.fromstring(self.strXml7)  # 대구광역시
        self.tree8 = ElementTree.fromstring(self.strXml8)  # 인천광역시
        self.tree9 = ElementTree.fromstring(self.strXml9)  # 광주광역시
        self.tree10 = ElementTree.fromstring(self.strXml10)  # 세종특별자치시
        self.tree11 = ElementTree.fromstring(self.strXml11)  # 대전광역시
        self.tree12 = ElementTree.fromstring(self.strXml12)  # 울산광역시
        self.tree13 = ElementTree.fromstring(self.strXml13)  # 경기도
        self.tree14 = ElementTree.fromstring(self.strXml14)  # 강원도
        self.tree15 = ElementTree.fromstring(self.strXml15)  # 충청북도
        self.tree16 = ElementTree.fromstring(self.strXml16)  # 충청남도
        self.tree17 = ElementTree.fromstring(self.strXml17)  # 전라북도
        self.tree18 = ElementTree.fromstring(self.strXml18)  # 전라남도
        self.tree19 = ElementTree.fromstring(self.strXml19)  # 경상북도
        self.tree20 = ElementTree.fromstring(self.strXml20)  # 경상남도
        self.tree21 = ElementTree.fromstring(self.strXml21)  # 제주특별자치도

    def setLabel(self): # Label
        self.MainText = Label(text="유기동물 조회 서비스", width=24, height=1,  font=self.fontstyle, fg="black", bg='floral white')
        self.MainText.place(x=80, y=50)

        self.CategoryCityLabel = Label(text="지역", width=4, height=1, font=self.fontstyle3, fg="black", bg='floral white')
        self.CategoryCityLabel.place(x=45, y=200)

        self.CategoryBreedLabel = Label(text="품종", width=4, height=1, font=self.fontstyle3, fg="black", bg='floral white')
        self.CategoryBreedLabel.place(x=45, y=300)

        self.GraphLabel = Label(text="그래프", width=6, height=1, font=self.fontstyle3, fg="black", bg='floral white')
        self.GraphLabel.place(x=45, y=400)

    def SearchBox(self): # 검색박스
        self.InputLabel = Entry(self.window, font=self.fontstyle3, width=53, borderwidth=3, relief='ridge', bg='white')
        self.InputLabel.place(x=50, y=135)

    def setupButton(self): #버튼:검색버튼, 그래프 버튼(지역 / 품종)
        self.SearchButton = Button(self.window, text="검색", font=self.fontstyle3, bg='floral white',command=self.SearchButtonAction)
        self.SearchButton.place(x=440, y=132)

        self.CategoryCityButton = Button(self.window, text="검색", font=self.fontstyle3, bg='floral white',command=self.CategoryCitySearchButtonAction)
        self.CategoryCityButton.place(x=440, y=198)

        self.CategoryBreedButton = Button(self.window, text="검색", font=self.fontstyle3, bg='floral white',command=self.CategoryBreedSearchButtonAction)
        self.CategoryBreedButton.place(x=440, y=298)

        self.GraphAreaButton = Button(self.window, text="지역", width=20, font=self.fontstyle3, bg='floral white',command=self.GraphCity)
        self.GraphAreaButton.place(x=100, y=400)

        self.GraphBreedButton = Button(self.window, text="품종", width=20, font=self.fontstyle3, bg='floral white',command=self.GraphBreed)
        self.GraphBreedButton.place(x=290, y=400)

    def CategoryCity(self): #카테고리:지역(시도)
        self.CategoryCityText = []
        self.itemElements4 = self.tree4.iter("item")

        for item in self.itemElements4:
            self.CategoryCityText.append(item.find("orgdownNm").text)

        self.City = StringVar()
        self.CategoryCityList = ttk.Combobox(self.window, width=20, textvariable=self.City)
        self.CategoryCityList['values'] = self.CategoryCityText

        self.CategoryCityList.place(x=90, y=200)
        self.CategoryCityList.current(0)

        self.CategoryCityList.bind("<<ComboboxSelected>>", self.CategoryDistrict)

    def CategoryDistrictScreen(self):  # 카테고리:지역(구)
        self.CategoryDistrictText = [" "]

        self.District = StringVar()
        self.CategoryDistrictList = ttk.Combobox(self.window, width=20, textvariable=self.District)
        self.CategoryDistrictList['values'] = self.CategoryDistrictText

        self.CategoryDistrictList.place(x=270, y=200)
        self.CategoryDistrictList.current(0)

    def CategoryDistrict(self, event):  # 카테고리:지역(구)
        self.CategoryDistrictText = [" "]

        if self.CategoryCityList.get() == "서울특별시":
            self.itemElements5 = self.tree5.iter("item")
            for item in self.itemElements5:
                if item.find("orgdownNm").text != "가정보호":
                    self.CategoryDistrictText.append(item.find("orgdownNm").text)
        elif self.CategoryCityList.get() == "부산광역시":
            self.itemElements6 = self.tree6.iter("item")
            for item in self.itemElements6:
                self.CategoryDistrictText.append(item.find("orgdownNm").text)
        elif self.CategoryCityList.get() == "대구광역시":
            self.itemElements7 = self.tree7.iter("item")
            for item in self.itemElements7:
                self.CategoryDistrictText.append(item.find("orgdownNm").text)
        elif self.CategoryCityList.get() == "인천광역시":
            self.itemElements8 = self.tree8.iter("item")
            for item in self.itemElements8:
                self.CategoryDistrictText.append(item.find("orgdownNm").text)
        elif self.CategoryCityList.get() == "광주광역시":
            self.itemElements9 = self.tree9.iter("item")
            for item in self.itemElements9:
                self.CategoryDistrictText.append(item.find("orgdownNm").text)
        elif self.CategoryCityList.get() == "세종특별자치시":
            self.itemElements10 = self.tree10.iter("item")
            for item in self.itemElements10:
                self.CategoryDistrictText.append(item.find("orgdownNm").text)
        elif self.CategoryCityList.get() == "대전광역시":
            self.itemElements11 = self.tree11.iter("item")
            for item in self.itemElements11:
                self.CategoryDistrictText.append(item.find("orgdownNm").text)
        elif self.CategoryCityList.get() == "울산광역시":
            self.itemElements12 = self.tree12.iter("item")
            for item in self.itemElements12:
                self.CategoryDistrictText.append(item.find("orgdownNm").text)
        elif self.CategoryCityList.get() == "경기도":
            self.itemElements13 = self.tree13.iter("item")
            for item in self.itemElements13:
                self.CategoryDistrictText.append(item.find("orgdownNm").text)
        elif self.CategoryCityList.get() == "강원도":
            self.itemElements14 = self.tree14.iter("item")
            for item in self.itemElements14:
                self.CategoryDistrictText.append(item.find("orgdownNm").text)
        elif self.CategoryCityList.get() == "충청북도":
            self.itemElements15 = self.tree15.iter("item")
            for item in self.itemElements15:
                self.CategoryDistrictText.append(item.find("orgdownNm").text)
        elif self.CategoryCityList.get() == "충청남도":
            self.itemElements16 = self.tree16.iter("item")
            for item in self.itemElements16:
                self.CategoryDistrictText.append(item.find("orgdownNm").text)
        elif self.CategoryCityList.get() == "전라북도":
            self.itemElements17 = self.tree17.iter("item")
            for item in self.itemElements17:
                self.CategoryDistrictText.append(item.find("orgdownNm").text)
        elif self.CategoryCityList.get() == "전라남도":
            self.itemElements18 = self.tree18.iter("item")
            for item in self.itemElements18:
                self.CategoryDistrictText.append(item.find("orgdownNm").text)
        elif self.CategoryCityList.get() == "경상북도":
            self.itemElements19 = self.tree19.iter("item")
            for item in self.itemElements19:
                self.CategoryDistrictText.append(item.find("orgdownNm").text)
        elif self.CategoryCityList.get() == "경상남도":
            self.itemElements20 = self.tree20.iter("item")
            for item in self.itemElements20:
                self.CategoryDistrictText.append(item.find("orgdownNm").text)
        elif self.CategoryCityList.get() == "제주특별자치도":
            self.itemElements21 = self.tree21.iter("item")
            for item in self.itemElements21:
                self.CategoryDistrictText.append(item.find("orgdownNm").text)

        self.District = StringVar()
        self.CategoryDistrictList = ttk.Combobox(self.window, width=20, textvariable=self.District)
        self.CategoryDistrictList['values'] = self.CategoryDistrictText

        self.CategoryDistrictList.place(x=270, y=200)
        self.CategoryDistrictList.current(0)

    def CategoryCitySearchButtonAction(self):
        self.CityName = self.CategoryCityList.get()
        self.DistrictName = self.CategoryDistrictList.get()

        self.SearchButton.destroy()
        self.InputLabel.destroy()
        self.GraphLabel.destroy()
        #self.CategoryCityLabel.destroy()
        #self.CategoryCityButton.destroy()
        self.CategoryCityList.destroy()
        self.CategoryDistrictList.destroy()
        self.CategoryBreedLabel.destroy()
        self.CategoryBreedButton.destroy()
        self.CategoryKindList.destroy()
        self.CategoryBreedList.destroy()
        self.GraphAreaButton.destroy()
        self.GraphBreedButton.destroy()

        self.CategoryCitySearchBacktoMainButton()

        self.CategoryCityLabel.place(x=45, y=120)
        self.CategoryCityButton.place(x=440, y=115)
        self.CategoryCity()
        self.CategoryCityList.place(x=90, y=120)
        self.CategoryDistrictScreen()
        self.CategoryDistrictList.place(x=270, y=120)

        self.RenderText = Text(self.window, font=self.fontstyle3, width=56, height=31, borderwidth=3, relief='ridge')
        self.RenderText.place(x=38, y=158)

        self.RenderTextScrollbar = Scrollbar(self.RenderText)
        self.RenderTextScrollbar.place(x=415, y=160)
        self.RenderTextScrollbar.config(command=self.RenderText.yview)

        self.RenderText.config(yscrollcommand=self.RenderTextScrollbar.set)

        self.retlist = []

        j = 0
        num1 = 0
        self.Citydic = dict()
        self.itemList = []

        self.itemElements1 = self.tree1.iter("item")
        self.itemElements2 = self.tree2.iter("item")
        self.itemElements3 = self.tree3.iter("item")

        for item in self.itemElements1:
            self.CitydicBNum = len(self.Citydic.keys())
            self.CategoryCitySearch = (item.find("orgNm"))
            self.CategoryCitySearchSplit = self.CategoryCitySearch.text.split()
            if(len(self.CategoryCitySearchSplit) == 1):
                self.CategoryCitySearchSplit.append(" ")
            self.CategoryCityCareNm = (item.find("careNm"))
            if (self.CityName == self.CategoryCitySearchSplit[0] and self.DistrictName == self.CategoryCitySearchSplit[1]) or (self.CityName == self.CategoryCitySearchSplit[0] and self.DistrictName == " "):
                self.Citydic[self.CategoryCityCareNm.text] = 0
            if (self.CitydicBNum+1) == len(self.Citydic.keys()):
                self.itemList.append(item)

        for item in self.itemElements2:
            self.CitydicBNum = len(self.Citydic.keys())
            self.CategoryCitySearch = (item.find("orgNm"))
            self.CategoryCitySearchSplit = self.CategoryCitySearch.text.split()
            if (len(self.CategoryCitySearchSplit) == 1):
                self.CategoryCitySearchSplit.append(" ")
            self.CategoryCityCareNm = (item.find("careNm"))
            if (self.CityName == self.CategoryCitySearchSplit[0] and self.DistrictName == self.CategoryCitySearchSplit[
                1]) or (self.CityName == self.CategoryCitySearchSplit[0] and self.DistrictName == " "):
                self.Citydic[self.CategoryCityCareNm.text] = 0
            if (self.CitydicBNum + 1) == len(self.Citydic.keys()):
                self.itemList.append(item)

        for item in self.itemElements3:
            self.CitydicBNum = len(self.Citydic.keys())
            self.CategoryCitySearch = (item.find("orgNm"))
            self.CategoryCitySearchSplit = self.CategoryCitySearch.text.split()
            if (len(self.CategoryCitySearchSplit) == 1):
                self.CategoryCitySearchSplit.append(" ")
            self.CategoryCityCareNm = (item.find("careNm"))
            if (self.CityName == self.CategoryCitySearchSplit[0] and self.DistrictName == self.CategoryCitySearchSplit[
                1]) or (self.CityName == self.CategoryCitySearchSplit[0] and self.DistrictName == " "):
                self.Citydic[self.CategoryCityCareNm.text] = 0
            if (self.CitydicBNum + 1) == len(self.Citydic.keys()):
                self.itemList.append(item)

        for i in self.Citydic.keys():
            item = self.itemList[j]
            self.careNm = item.find("careNm")
            self.careAddr = item.find("careAddr")
            self.careTel = item.find("careTel")

            self.retlist.append([])

            self.retlist[num1].append(self.careNm.text)
            self.retlist[num1].append(self.careAddr.text)
            self.retlist[num1].append(self.careTel.text)

            num1 += 1
            j += 1

        if len(self.Citydic.keys()) == 0:
            self.RenderText.insert(INSERT, "\n검색 결과가 없습니다. ")
        else:
            for i in range(len(self.retlist)):
                self.RenderText.insert(INSERT, "\n보호소 이름:")
                self.RenderText.insert(INSERT, self.retlist[i][0])
                self.RenderText.insert(INSERT, "\n주소:")
                self.RenderText.insert(INSERT, self.retlist[i][1])
                self.RenderText.insert(INSERT, "\n전화번호:")
                self.RenderText.insert(INSERT, self.retlist[i][2])
                self.RenderText.insert(INSERT, "\n---------------------------------------------")

                num1 = 0

    def CategoryCitySearchBacktoMainButton(self):
        self.CitySearchBacktoMainButton = Button(self.window, text="뒤로", font=self.fontstyle3, bg='floral white', command=self.CategoryCitySearchBacktoMain)
        self.CitySearchBacktoMainButton.place(x=445, y=600)

    def CategoryCitySearchBacktoMain(self):
        self.RenderText.destroy()
        self.RenderTextScrollbar.destroy()
        self.CitySearchBacktoMainButton.destroy()
        self.CategoryCityLabel.destroy()
        self.CategoryCityButton.destroy()
        self.CategoryCityList.destroy()
        self.CategoryDistrictList.destroy()

        self.SearchBox()
        self.setupButton()
        self.setLabel()
        self.CategoryCity()
        self.CategoryDistrictScreen()
        self.CategoryKind()
        self.CategoryBreedScreen()

    def CategoryKind(self): #카테고리:품종(종류)
        self.CategoryKindText = ["개", "고양이", "기타"]

        self.Kind = StringVar()
        self.CategoryKindList = ttk.Combobox(self.window, width=20, textvariable=self.Kind)
        self.CategoryKindList['values'] = self.CategoryKindText

        self.CategoryKindList.place(x=90, y=300)
        self.CategoryKindList.current(0)

        self.CategoryKindList.bind("<<ComboboxSelected>>", self.CategoryBreed)

    def CategoryBreedScreen(self):  # 카테고리:지역(구)
        self.CategoryBreedText = [" "]

        self.Breed = StringVar()
        self.CategoryBreedList = ttk.Combobox(self.window, width=20, textvariable=self.Breed)
        self.CategoryBreedList['values'] = self.CategoryBreedText

        self.CategoryBreedList.place(x=270, y=300)
        self.CategoryBreedList.current(0)

    def CategoryBreed(self, event): #카테고리:품종(품종)
        self.CategoryBreedDic = dict()
        self.CategoryBreedText = [" "]
        self.kindBreedText = ""
        self.kindBreedTextList = []

        if self.CategoryKindList.get() == "개":
            self.itemElements1 = self.tree1.iter("item")
            for item in self.itemElements1:
                self.kindBreed = item.find("kindCd")
                self.kindBreedSplit = self.kindBreed.text.split()

                for i in range(len(self.kindBreedSplit) - 1):
                    self.kindBreedText += self.kindBreedSplit[i + 1]
                self.kindBreedTextList.append(self.kindBreedText)

                self.kindBreedText = ""
            for i in range(len(self.kindBreedTextList)):
                self.CategoryBreedDic[self.kindBreedTextList[i]] = 0
            for i in self.CategoryBreedDic.keys():
                if i != '':
                    self.CategoryBreedText.append(i)
        elif self.CategoryKindList.get() == "고양이":
            self.itemElements2 = self.tree2.iter("item")
            for item in self.itemElements2:
                self.kindBreed = item.find("kindCd")
                self.kindBreedSplit = self.kindBreed.text.split()

                for i in range(len(self.kindBreedSplit)-1):
                    self.kindBreedText += self.kindBreedSplit[i+1]
                self.kindBreedTextList.append(self.kindBreedText)

                self.kindBreedText = ""
            for i in range(len(self.kindBreedTextList)):
                self.CategoryBreedDic[self.kindBreedTextList[i]] = 0
            for i in self.CategoryBreedDic.keys():
                if i != '':
                    self.CategoryBreedText.append(i)
        elif self.CategoryKindList.get() == "기타":
            self.itemElements3 = self.tree3.iter("item")
            for item in self.itemElements3:
                self.kindBreed = item.find("kindCd")
                self.kindBreedSplit = self.kindBreed.text.split()

                for i in range(len(self.kindBreedSplit) - 1):
                    self.kindBreedText += self.kindBreedSplit[i + 1]
                self.kindBreedTextList.append(self.kindBreedText)

                self.kindBreedText = ""
            for i in range(len(self.kindBreedTextList)):
                self.CategoryBreedDic[self.kindBreedTextList[i]] = 0
            for i in self.CategoryBreedDic.keys():
                if i != '':
                    self.CategoryBreedText.append(i)

        self.Breed = StringVar()
        self.CategoryBreedList = ttk.Combobox(self.window, width=20, textvariable=self.Breed)
        self.CategoryBreedList['values'] = self.CategoryBreedText

        self.CategoryBreedList.place(x=270, y=300)
        self.CategoryBreedList.current(0)

        self.CategoryBreedList.bind("<<ComboboxSelected>>")

    def CategoryBreedSearchButtonAction(self):
        self.BreedText = self.CategoryBreedList.get()

        self.SearchButton.destroy()
        self.InputLabel.destroy()
        self.GraphLabel.destroy()
        self.CategoryCityLabel.destroy()
        self.CategoryCityButton.destroy()
        self.CategoryCityList.destroy()
        self.CategoryDistrictList.destroy()
        #self.CategoryBreedLabel.destroy()
        #self.CategoryBreedButton.destroy()
        self.CategoryKindList.destroy()
        self.CategoryBreedList.destroy()
        self.GraphAreaButton.destroy()
        self.GraphBreedButton.destroy()

        self.CategoryBreedSearchBacktoMainButton()

        self.CategoryBreedLabel.place(x=45, y=120)
        self.CategoryBreedButton.place(x=440, y=115)
        self.CategoryKind()
        self.CategoryKindList.place(x=90, y=120)
        self.CategoryBreedScreen()
        self.CategoryBreedList.place(x=270, y=120)

        self.RenderText = Text(self.window, font=self.fontstyle3, width=56, height=31, borderwidth=3, relief='ridge')
        self.RenderText.place(x=38, y=158)

        self.RenderTextScrollbar = Scrollbar(self.RenderText)
        self.RenderTextScrollbar.place(x=415, y=160)
        self.RenderTextScrollbar.config(command=self.RenderText.yview)

        self.RenderText.config(yscrollcommand=self.RenderTextScrollbar.set)

        self.retlist = []

        num1 = 0

        self.itemElements1 = self.tree1.iter("item")
        self.itemElements2 = self.tree2.iter("item")
        self.itemElements3 = self.tree3.iter("item")

        for item in self.itemElements1:
            self.CategoryBreedSearch = (item.find("kindCd"))
            self.CategoryBreedSearchSplit = self.CategoryBreedSearch.text.split()
            if (len(self.CategoryBreedSearchSplit) == 1):
                self.CategoryBreedSearchSplit.append(" ")

            if self.CategoryBreedSearchSplit[0] == "[개]" and self.BreedText == self.CategoryBreedSearchSplit[1]:
                self.kindCd = item.find("kindCd")
                self.age = item.find("age")
                self.happenDt = item.find("happenDt")
                self.happenPlace = item.find("happenPlace")
                self.sexCd = item.find("sexCd")
                self.specialMark = item.find("specialMark")
                self.imageUrl = item.find("filename")
                self.processState = item.find("processState")

                self.retlist.append([])

                self.retlist[num1].append(self.kindCd.text)
                self.retlist[num1].append(self.age.text)
                self.retlist[num1].append(self.happenDt.text)
                self.retlist[num1].append(self.happenPlace.text)
                self.retlist[num1].append(self.sexCd.text)
                self.retlist[num1].append(self.specialMark.text)
                self.retlist[num1].append(self.imageUrl.text)
                self.retlist[num1].append(self.processState.text)

                num1 += 1

        for item in self.itemElements2:
            self.CategoryBreedSearch = (item.find("kindCd"))
            self.CategoryBreedSearchSplit = self.CategoryBreedSearch.text.split()
            if (len(self.CategoryBreedSearchSplit) == 1):
                self.CategoryBreedSearchSplit.append(" ")

            if self.CategoryBreedSearchSplit[0] == "[고양이]" and self.BreedText == self.CategoryBreedSearchSplit[1]:
                self.kindCd = item.find("kindCd")
                self.age = item.find("age")
                self.happenDt = item.find("happenDt")
                self.happenPlace = item.find("happenPlace")
                self.sexCd = item.find("sexCd")
                self.specialMark = item.find("specialMark")
                self.imageUrl = item.find("filename")
                self.processState = item.find("processState")

                self.retlist.append([])

                self.retlist[num1].append(self.kindCd.text)
                self.retlist[num1].append(self.age.text)
                self.retlist[num1].append(self.happenDt.text)
                self.retlist[num1].append(self.happenPlace.text)
                self.retlist[num1].append(self.sexCd.text)
                self.retlist[num1].append(self.specialMark.text)
                self.retlist[num1].append(self.imageUrl.text)
                self.retlist[num1].append(self.processState.text)

                num1 += 1

        for item in self.itemElements3:
            self.CategoryBreedSearch = (item.find("kindCd"))
            self.CategoryBreedSearchSplit = self.CategoryBreedSearch.text.split()
            if (len(self.CategoryBreedSearchSplit) == 1):
                self.CategoryBreedSearchSplit.append(" ")

            if self.CategoryBreedSearchSplit[0] == "[기타축종]" and self.BreedText == self.CategoryBreedSearchSplit[1]:
                self.kindCd = item.find("kindCd")
                self.age = item.find("age")
                self.happenDt = item.find("happenDt")
                self.happenPlace = item.find("happenPlace")
                self.sexCd = item.find("sexCd")
                self.specialMark = item.find("specialMark")
                self.imageUrl = item.find("filename")
                self.processState = item.find("processState")

                self.retlist.append([])

                self.retlist[num1].append(self.kindCd.text)
                self.retlist[num1].append(self.age.text)
                self.retlist[num1].append(self.happenDt.text)
                self.retlist[num1].append(self.happenPlace.text)
                self.retlist[num1].append(self.sexCd.text)
                self.retlist[num1].append(self.specialMark.text)
                self.retlist[num1].append(self.imageUrl.text)
                self.retlist[num1].append(self.processState.text)

                num1 += 1

        if num1 == 0:
            self.RenderText.insert(INSERT, "\n검색 결과가 없습니다. ")
        else:
            self.image = []
            for i in range(len(self.retlist)):
                with urllib.request.urlopen(self.retlist[i][6]) as u:
                    self.raw_data = u.read()
                self.im = Image.open(BytesIO(self.raw_data))

                self.image.append(ImageTk.PhotoImage(self.im))

            for i in range(len(self.retlist)):
                self.RenderText.image_create(END, image=self.image[i])

                self.RenderText.insert(INSERT, "\n품종:")
                self.RenderText.insert(INSERT, self.retlist[i][0])
                self.RenderText.insert(INSERT, "\n나이:")
                self.RenderText.insert(INSERT, self.retlist[i][1])
                self.RenderText.insert(INSERT, "\n성:")
                self.RenderText.insert(INSERT, self.retlist[i][4])
                self.RenderText.insert(INSERT, "\n발견 날짜:")
                self.RenderText.insert(INSERT, self.retlist[i][2])
                self.RenderText.insert(INSERT, "\n발견 장소:")
                self.RenderText.insert(INSERT, self.retlist[i][3])
                self.RenderText.insert(INSERT, "\n특징:")
                self.RenderText.insert(INSERT, self.retlist[i][5])
                self.RenderText.insert(INSERT, "\n현재 상태:")
                self.RenderText.insert(INSERT, self.retlist[i][7])

                self.RenderText.insert(INSERT, "\n---------------------------------------------")
                num1 = 0

    def CategoryBreedSearchBacktoMainButton(self):
        self.BreedSearchBacktoMainButton = Button(self.window, text="뒤로", font=self.fontstyle3, bg='floral white', command=self.CategoryBreedSearchBacktoMain)
        self.BreedSearchBacktoMainButton.place(x=445, y=600)

    def CategoryBreedSearchBacktoMain(self):
        self.RenderText.destroy()
        self.RenderTextScrollbar.destroy()
        self.BreedSearchBacktoMainButton.destroy()
        self.CategoryBreedLabel.destroy()
        self.CategoryBreedButton.destroy()
        self.CategoryKindList.destroy()
        self.CategoryBreedList.destroy()

        self.SearchBox()
        self.setupButton()
        self.setLabel()
        self.CategoryCity()
        self.CategoryDistrictScreen()
        self.CategoryKind()
        self.CategoryBreedScreen()

    def SearchBacktoMainButton(self):
        self.SearchBacktomainB = Button(self.window, text="뒤로", font=self.fontstyle3, bg='floral white', command=self.SearchBacktoMain)
        self.SearchBacktomainB.place(x=440, y=600)

    def SearchBacktoMain(self):
        self.SearchButton.destroy()
        self.InputLabel.destroy()
        self.RenderText.destroy()
        self.RenderTextScrollbar.destroy()
        self.SearchBacktomainB.destroy()
        self.InputLabel1.destroy()
        self.mailB.destroy()
        self.mapButton.destroy()
        self.MailLabel.destroy()

        self.SearchBox()
        self.setupButton()
        self.setLabel()
        self.CategoryCity()
        self.CategoryDistrictScreen()
        self.CategoryKind()
        self.CategoryBreedScreen()

    def SearchButtonAction(self):
        self.GraphLabel.destroy()
        self.CategoryCityLabel.destroy()
        self.CategoryCityButton.destroy()
        self.CategoryCityList.destroy()
        self.CategoryDistrictList.destroy()
        self.CategoryBreedLabel.destroy()
        self.CategoryBreedButton.destroy()
        self.CategoryKindList.destroy()
        self.CategoryBreedList.destroy()
        self.GraphAreaButton.destroy()
        self.GraphBreedButton.destroy()

        self.MapButton()
        self.MailBox()
        self.mailButton()
        self.SearchBacktoMainButton()

        self.RenderText = Text(self.window, font=self.fontstyle3, width=52, height=28, borderwidth=3, relief='ridge')
        self.RenderText.place(x=50, y=200)

        self.RenderTextScrollbar = Scrollbar(self.RenderText)
        self.RenderTextScrollbar.place(x=415, y=200)
        self.RenderTextScrollbar.config(command=self.RenderText.yview)

        self.RenderText.config(yscrollcommand=self.RenderTextScrollbar.set)

        self.Search()

    def Search(self):
        self.retlist = []

        self.itemElements1 = self.tree1.iter("item")
        self.itemElements2 = self.tree2.iter("item")
        self.itemElements3 = self.tree3.iter("item")

        num1 = 0

        for item in self.itemElements1:
            self.strTitle = item.find("careNm")
            if (self.strTitle.text == self.InputLabel.get()):
                self.kindCd = item.find("kindCd")
                self.age = item.find("age")
                self.happenDt = item.find("happenDt")
                self.happenPlace = item.find("happenPlace")
                self.sexCd = item.find("sexCd")
                self.specialMark = item.find("specialMark")
                self.imageUrl = item.find("filename")
                self.processState = item.find("processState")

                self.retlist.append([])

                self.retlist[num1].append(self.kindCd.text)
                self.retlist[num1].append(self.age.text)
                self.retlist[num1].append(self.happenDt.text)
                self.retlist[num1].append(self.happenPlace.text)
                self.retlist[num1].append(self.sexCd.text)
                self.retlist[num1].append(self.specialMark.text)
                self.retlist[num1].append(self.imageUrl.text)
                self.retlist[num1].append(self.processState.text)

                num1 += 1

        for item in self.itemElements2:
            self.strTitle = item.find("careNm")
            if (self.strTitle.text == self.InputLabel.get()):
                self.kindCd = item.find("kindCd")
                self.age = item.find("age")
                self.happenDt = item.find("happenDt")
                self.happenPlace = item.find("happenPlace")
                self.sexCd = item.find("sexCd")
                self.specialMark = item.find("specialMark")
                self.imageUrl = item.find("filename")
                self.processState = item.find("processState")

                self.retlist.append([])

                self.retlist[num1].append(self.kindCd.text)
                self.retlist[num1].append(self.age.text)
                self.retlist[num1].append(self.happenDt.text)
                self.retlist[num1].append(self.happenPlace.text)
                self.retlist[num1].append(self.sexCd.text)
                self.retlist[num1].append(self.specialMark.text)
                self.retlist[num1].append(self.imageUrl.text)
                self.retlist[num1].append(self.processState.text)

                num1 += 1

        for item in self.itemElements3:
            self.strTitle = item.find("careNm")
            if (self.strTitle.text == self.InputLabel.get()):
                self.kindCd = item.find("kindCd")
                self.age = item.find("age")
                self.happenDt = item.find("happenDt")
                self.happenPlace = item.find("happenPlace")
                self.sexCd = item.find("sexCd")
                self.specialMark = item.find("specialMark")
                self.imageUrl = item.find("filename")
                self.processState = item.find("processState")

                self.retlist.append([])

                self.retlist[num1].append(self.kindCd.text)
                self.retlist[num1].append(self.age.text)
                self.retlist[num1].append(self.happenDt.text)
                self.retlist[num1].append(self.happenPlace.text)
                self.retlist[num1].append(self.sexCd.text)
                self.retlist[num1].append(self.specialMark.text)
                self.retlist[num1].append(self.imageUrl.text)
                self.retlist[num1].append(self.processState.text)

                num1 += 1

        self.image = []
        for i in range(len(self.retlist)):
            with urllib.request.urlopen(self.retlist[i][6]) as u:
                self.raw_data = u.read()
            self.im = Image.open(BytesIO(self.raw_data))

            self.image.append(ImageTk.PhotoImage(self.im))

        for i in range(len(self.retlist)):
            self.RenderText.image_create(END, image=self.image[i])

            self.RenderText.insert(INSERT, "\n품종:")
            self.RenderText.insert(INSERT, self.retlist[i][0])
            self.RenderText.insert(INSERT, "\n나이:")
            self.RenderText.insert(INSERT, self.retlist[i][1])
            self.RenderText.insert(INSERT, "\n성:")
            self.RenderText.insert(INSERT, self.retlist[i][4])
            self.RenderText.insert(INSERT, "\n발견 날짜:")
            self.RenderText.insert(INSERT, self.retlist[i][2])
            self.RenderText.insert(INSERT, "\n발견 장소:")
            self.RenderText.insert(INSERT, self.retlist[i][3])
            self.RenderText.insert(INSERT, "\n특징:")
            self.RenderText.insert(INSERT, self.retlist[i][5])
            self.RenderText.insert(INSERT, "\n현재 상태:")
            self.RenderText.insert(INSERT, self.retlist[i][7])

            self.RenderText.insert(INSERT, "\n---------------------------------------")

            num1 = 0

    def MapButton(self):
        self.mapButton = Button(self.window, text="지도", font=self.fontstyle3, bg='floral white', command=self.Map)
        self.mapButton.place(x=440, y=200)

    def Map(self):
        # 주소를 위도 경도로 변환
        self.itemElements1 = self.tree1.iter("item")
        self.itemElements2 = self.tree2.iter("item")
        self.itemElements3 = self.tree3.iter("item")

        for item in self.itemElements1:
            self.strTitle = item.find("careNm")
            if (self.strTitle.text == self.InputLabel.get()):
                self.location = item.find("careAddr")

        for item in self.itemElements2:
            self.strTitle = item.find("careNm")
            if (self.strTitle.text == self.InputLabel.get()):
                self.location = item.find("careAddr")

        for item in self.itemElements3:
            self.strTitle = item.find("careNm")
            if (self.strTitle.text == self.InputLabel.get()):
                self.location = item.find("careAddr")

        url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + self.location.text
        headers = {"Authorization": "KakaoAK 0f311b32ad768ebcf668cb36214a66b1"}
        result = json.loads(str(requests.get(url, headers=headers).text))
        match_first = result['documents'][0]['address']
        lat = float(match_first['y'])
        lng = float(match_first['x'])

        self.map_osm = folium.Map(location=[lat, lng], zoom_start=13) # 위도 경도 지정
        folium.Marker([lat, lng], popup=self.InputLabel.get()).add_to(self.map_osm) # 마커 지정
        self.map_osm.save('osm.html') # html 파일로 저장
        webbrowser.open_new('osm.html')

    def mailButton(self):
        self.mailB = Button(self.window, text="메일", font=self.fontstyle3, bg='floral white', command=self.GMail)
        self.mailB.place(x=440, y=230)

    def GMail(self):
        global host, port
        html = ""
        title = str("유기동물 정보")
        senderAddr = str("noelvi1225@gmail.com")
        recipientAddr = self.InputLabel1.get()
        #메시지 쓰는데

        #msgtext = str("테스트용 메시지")
        passwd = str("choi1537")
        html = self.MakeHtmlDoc()

        import smtplib
        # MIMEMultipart의 MIME을 생성합니다.
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        # Message container를 생성합니다.
        msg = MIMEMultipart('alternative')

        # set message
        msg['Subject'] = title
        msg['From'] = senderAddr
        msg['To'] = recipientAddr

        msgPart = MIMEText(html, 'plain')
        bookPart = MIMEText(html, 'html', _charset='UTF-8')

        # 메세지에 생성한 MIME 문서를 첨부합니다.
        msg.attach(msgPart)
        msg.attach(bookPart)

        print("connect smtp server ... ")
        s = smtplib.SMTP(host, port)
        # s.set_debuglevel(1)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(senderAddr, passwd)  # 로긴을 합니다.
        s.sendmail(senderAddr, [recipientAddr], msg.as_string())
        s.close()

        print("Mail sending complete!!!")

    def MakeHtmlDoc(self):
        from xml.dom.minidom import getDOMImplementation
        # get Dom Implementation
        impl = getDOMImplementation()

        newdoc = impl.createDocument(None, "html", None)  # DOM 객체 생성
        top_element = newdoc.documentElement
        header = newdoc.createElement('header')
        top_element.appendChild(header)

        # Body 엘리먼트 생성.
        body = newdoc.createElement('body')
        # BR 태그 (엘리먼트) 생성.
        bre = newdoc.createElement('br')

        # create bold element
        b = newdoc.createElement('b')
        # create text node
        center = newdoc.createTextNode("보호소:" + self.InputLabel.get())
        b.appendChild(center)

        body.appendChild(b)
        body.appendChild(bre)  # line end

        for i in range(len(self.retlist)):
            # create bold element
            b = newdoc.createElement('b')
            # create text node
            kindCd = newdoc.createTextNode("품종:" + self.retlist[i][0])
            b.appendChild(kindCd)

            body.appendChild(b)

            # BR 태그 (엘리먼트) 생성.
            br = newdoc.createElement('br')

            body.appendChild(br)

            # create title Element
            p = newdoc.createElement('p')
            # create text node
            age = newdoc.createTextNode("나이:" + self.retlist[i][1]+ " ")
            p.appendChild(age)
            sexCd = newdoc.createTextNode("성: " + self.retlist[i][4]+ " ")
            p.appendChild(sexCd)
            happenDt = newdoc.createTextNode("발견 날짜: " + self.retlist[i][2]+ " ")
            p.appendChild(happenDt)
            happenPlace = newdoc.createTextNode("발견 장소: " + self.retlist[i][3]+ " ")
            p.appendChild(happenPlace)
            specialMark = newdoc.createTextNode("특징: " + self.retlist[i][5]+ " ")
            p.appendChild(specialMark)
            processState = newdoc.createTextNode("현재 상태: " + self.retlist[i][7]+ " ")
            p.appendChild(processState)


            body.appendChild(p)
            body.appendChild(br)  # line end

        # append Body
        top_element.appendChild(body)

        return newdoc.toxml()

    def MailBox(self): # 검색박스
        self.MailLabel = Label(text="이메일 주소", width=10, height=1, font=self.fontstyle3, bg='floral white', fg="black")
        self.MailLabel.place(x=45, y=650)

        self.InputLabel1 = Entry(self.window, font=self.fontstyle4, borderwidth=3, width=45, relief='ridge')
        self.InputLabel1.place(x=125, y=650)

    def GraphBreedBacktoMainButton(self):
        self.GraphBacktomainButton = Button(self.window, text="뒤로", font=self.fontstyle3, bg='floral white', command=self.GraphBreedBacktoMain)
        self.GraphBacktomainButton.place(x=440, y=600)

    def GraphBreedBacktoMain(self):
        self.GraphBacktomainButton.destroy()
        self.GraphBreedCanvas.destroy()

        self.SearchBox()
        self.setupButton()
        self.setLabel()
        self.CategoryCity()
        self.CategoryDistrictScreen()
        self.CategoryKind()
        self.CategoryBreedScreen()

    def GraphCityBacktoMainButton(self):
        self.GraphBacktomainButton = Button(self.window, text="뒤로", font=self.fontstyle3, bg='floral white', command=self.GraphCityBacktoMain)
        self.GraphBacktomainButton.place(x=440, y=600)

    def GraphCityBacktoMain(self):
        self.GraphBacktomainButton.destroy()
        self.GraphCityCanvas.destroy()

        self.SearchBox()
        self.setupButton()
        self.setLabel()
        self.CategoryCity()
        self.CategoryDistrictScreen()
        self.CategoryKind()
        self.CategoryBreedScreen()

    def GraphCity(self):
        self.SearchButton.destroy()
        self.InputLabel.destroy()
        self.GraphLabel.destroy()
        self.CategoryCityLabel.destroy()
        self.CategoryBreedLabel.destroy()
        self.CategoryCityButton.destroy()
        self.CategoryBreedButton.destroy()
        self.CategoryCityList.destroy()
        self.CategoryDistrictList.destroy()
        self.CategoryKindList.destroy()
        self.CategoryBreedList.destroy()
        self.GraphAreaButton.destroy()
        self.GraphBreedButton.destroy()

        self.GraphCityBacktoMainButton()

        self.itemElements1 = self.tree1.iter("item")
        self.itemElements2 = self.tree2.iter("item")
        self.itemElements3 = self.tree3.iter("item")

        self.GraphCityCanvas = Canvas(self.window, width=500, height=200, bd=2, bg='floral white')
        self.GraphCityCanvas.place(x=0, y=200)

        counts = [0] * 17
        self.CityList = ["서울", "부산", "대구", "인천", "광주", "세종", "대전", "경기", "울산", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]

        for item in self.itemElements1:
            self.orgNm = item.find("orgNm")
            self.orgNmsplit = self.orgNm.text.split()

            if(self.orgNmsplit[0] == "서울특별시"):
                counts[0] += 1
            elif(self.orgNmsplit[0] == "부산광역시"):
                counts[1] += 1
            elif (self.orgNmsplit[0] == "대구광역시"):
                counts[2] += 1
            elif (self.orgNmsplit[0] == "인천광역시"):
                counts[3] += 1
            elif (self.orgNmsplit[0] == "광주광역시"):
                counts[4] += 1
            elif (self.orgNmsplit[0] == "세종특별자치시"):
                counts[5] += 1
            elif (self.orgNmsplit[0] == "대전광역시"):
                counts[6] += 1
            elif (self.orgNmsplit[0] == "울산광역시"):
                counts[7] += 1
            elif (self.orgNmsplit[0] == "경기도"):
                counts[8] += 1
            elif (self.orgNmsplit[0] == "강원도"):
                counts[9] += 1
            elif (self.orgNmsplit[0] == "충청북도"):
                counts[10] += 1
            elif (self.orgNmsplit[0] == "충청남도"):
                counts[11] += 1
            elif (self.orgNmsplit[0] == "전라북도"):
                counts[12] += 1
            elif (self.orgNmsplit[0] == "전라남도"):
                counts[13] += 1
            elif (self.orgNmsplit[0] == "경상북도"):
                counts[14] += 1
            elif (self.orgNmsplit[0] == "경상남도"):
                counts[15] += 1
            elif (self.orgNmsplit[0] == "제주특별자치도"):
                counts[16] += 1

        for item in self.itemElements2:
            self.orgNm = item.find("orgNm")
            self.orgNmsplit = self.orgNm.text.split()

            if (self.orgNmsplit[0] == "서울특별시"):
                counts[0] += 1
            elif (self.orgNmsplit[0] == "부산광역시"):
                counts[1] += 1
            elif (self.orgNmsplit[0] == "대구광역시"):
                counts[2] += 1
            elif (self.orgNmsplit[0] == "인천광역시"):
                counts[3] += 1
            elif (self.orgNmsplit[0] == "광주광역시"):
                counts[4] += 1
            elif (self.orgNmsplit[0] == "세종특별자치시"):
                counts[5] += 1
            elif (self.orgNmsplit[0] == "대전광역시"):
                counts[6] += 1
            elif (self.orgNmsplit[0] == "울산광역시"):
                counts[7] += 1
            elif (self.orgNmsplit[0] == "경기도"):
                counts[8] += 1
            elif (self.orgNmsplit[0] == "강원도"):
                counts[9] += 1
            elif (self.orgNmsplit[0] == "충청북도"):
                counts[10] += 1
            elif (self.orgNmsplit[0] == "충청남도"):
                counts[11] += 1
            elif (self.orgNmsplit[0] == "전라북도"):
                counts[12] += 1
            elif (self.orgNmsplit[0] == "전라남도"):
                counts[13] += 1
            elif (self.orgNmsplit[0] == "경상북도"):
                counts[14] += 1
            elif (self.orgNmsplit[0] == "경상남도"):
                counts[15] += 1
            elif (self.orgNmsplit[0] == "제주특별자치도"):
                counts[16] += 1

        for item in self.itemElements3:
            self.orgNm = item.find("orgNm")
            self.orgNmsplit = self.orgNm.text.split()

            if (self.orgNmsplit[0] == "서울특별시"):
                counts[0] += 1
            elif (self.orgNmsplit[0] == "부산광역시"):
                counts[1] += 1
            elif (self.orgNmsplit[0] == "대구광역시"):
                counts[2] += 1
            elif (self.orgNmsplit[0] == "인천광역시"):
                counts[3] += 1
            elif (self.orgNmsplit[0] == "광주광역시"):
                counts[4] += 1
            elif (self.orgNmsplit[0] == "세종특별자치시"):
                counts[5] += 1
            elif (self.orgNmsplit[0] == "대전광역시"):
                counts[6] += 1
            elif (self.orgNmsplit[0] == "울산광역시"):
                counts[7] += 1
            elif (self.orgNmsplit[0] == "경기도"):
                counts[8] += 1
            elif (self.orgNmsplit[0] == "강원도"):
                counts[9] += 1
            elif (self.orgNmsplit[0] == "충청북도"):
                counts[10] += 1
            elif (self.orgNmsplit[0] == "충청남도"):
                counts[11] += 1
            elif (self.orgNmsplit[0] == "전라북도"):
                counts[12] += 1
            elif (self.orgNmsplit[0] == "전라남도"):
                counts[13] += 1
            elif (self.orgNmsplit[0] == "경상북도"):
                counts[14] += 1
            elif (self.orgNmsplit[0] == "경상남도"):
                counts[15] += 1
            elif (self.orgNmsplit[0] == "제주특별자치도"):
                counts[16] += 1

        width = 500  # 캔버스의 전체 크기
        height = 200
        maxCounts = max(counts)  # 빈도수가 높은 최대값
        heightBar = height * 0.75  # canvas 크기의 75%가 최대 막대 바의 높이
        widthBar = width - 10  # canvas 전체 너비에서 좌 10 우 10을 뺀 값
        for i in range(17):
            self.GraphCityCanvas.create_rectangle(i * widthBar / 17 + 10, height - heightBar * counts[i] / maxCounts - 20, (i + 1) * widthBar / 17, height-20)#, fill=feels[i])
            self.GraphCityCanvas.create_text(i * widthBar / 17 + 10 + 0.5 * widthBar/17, height-10, text=self.CityList[i])
            self.GraphCityCanvas.create_text(i * widthBar / 17 + 10 + 0.5 * widthBar / 17, height-180, text=counts[i])

    def GraphBreed(self):
        self.SearchButton.destroy()
        self.InputLabel.destroy()
        self.GraphLabel.destroy()
        self.CategoryCityLabel.destroy()
        self.CategoryBreedLabel.destroy()
        self.CategoryCityButton.destroy()
        self.CategoryBreedButton.destroy()
        self.CategoryCityList.destroy()
        self.CategoryDistrictList.destroy()
        self.CategoryKindList.destroy()
        self.CategoryBreedList.destroy()
        self.GraphAreaButton.destroy()
        self.GraphBreedButton.destroy()

        self.GraphBreedBacktoMainButton()

        self.itemElements1 = self.tree1.iter("item")
        self.itemElements2 = self.tree2.iter("item")
        self.itemElements3 = self.tree3.iter("item")

        self.GraphBreedCanvas = Canvas(self.window, width=500, height=200,  bg='floral white', bd=2)
        self.GraphBreedCanvas.place(x=0, y=200)

        counts = [0] * 3  # [0,0,...]
        breed = ["개","고양이","기타"]
        feels = ["red", "yellow", "green"]
        for _ in self.itemElements1:
            counts[0] += 1
        for _ in self.itemElements2:
            counts[1] += 1
        for _ in self.itemElements3:
            counts[2] += 1

        width = 500  # 캔버스의 전체 크기
        height = 200
        maxCounts = max(counts)  # 빈도수가 높은 최대값
        heightBar = height * 0.75  # canvas 크기의 75%가 최대 막대 바의 높이
        widthBar = width - 10  # canvas 전체 너비에서 좌 10 우 10을 뺀 값
        for i in range(3):
            self.GraphBreedCanvas.create_rectangle(i * widthBar / 3 + 10, height - heightBar * counts[i] / maxCounts - 20, (i + 1) * widthBar / 3, height-20, fill=feels[i])
            self.GraphBreedCanvas.create_text(i * widthBar / 3 + 10 + 0.5 * widthBar/3, height-10, text=breed[i])
            self.GraphBreedCanvas.create_text(i * widthBar / 3 + 10 + 0.5 * widthBar / 3, height-180, text=counts[i])

Main()