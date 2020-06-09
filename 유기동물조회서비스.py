from tkinter import *
from tkinter import font
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

        self.LoadXMLFromFile()

    def LoadXMLFromFile(self):  # xml
        self.tree1 = ElementTree.fromstring(self.strXml1) #강아지
        self.tree2 = ElementTree.fromstring(self.strXml2) #고양이
        self.tree3 = ElementTree.fromstring(self.strXml3) #기타

        self.tree4 = ElementTree.fromstring(self.strXml4)  # 시도

        self.tree5 = ElementTree.fromstring(self.strXml5)  # 서울특별시
        self.tree6 = ElementTree.fromstring(self.strXml6)  # 부산광역시시

    def setLabel(self): # Label
        self.MainText = Label(text="유기동물 조회 서비스", width=24, height=1,  font=self.fontstyle, fg="black")
        self.MainText.place(x=80, y=50)

    def SearchBox(self): # 검색박스
        self.InputLabel = Entry(self.window, font=self.fontstyle2, width=36, borderwidth=10, relief='ridge')
        self.InputLabel.place(x=40, y=120)

    def setupButton(self): #버튼:검색버튼, 그래프 버튼(지역 / 품종)
        self.SearchButton = Button(self.window, text="검색", font=self.fontstyle2, borderwidth=5, command=self.SearchButtonAction)
        self.SearchButton.place(x=430, y=120)

        self.GraphAreaButton = Button(self.window, text="지역", width=20, font=self.fontstyle2, command=self.GraphCity)
        self.GraphAreaButton.place(x=40, y=400)

        self.GraphBreedButton = Button(self.window, text="품종", width=20, font=self.fontstyle2, command=self.GraphBreed)
        self.GraphBreedButton.place(x=270, y=400)

    def CategoryCity(self): #카테고리:지역(시도)
        self.CategoryCityList = ["시/도 선택"]

        self.itemElements4 = self.tree4.iter("item")

        for item in self.itemElements4:
            self.CategoryCityList.append(item.find("orgdownNm").text)

        self.variable1 = StringVar(self.window)
        self.variable1.set(self.CategoryCityList[0])

        self.opt1 = OptionMenu(self.window, self.variable1, *self.CategoryCityList)
        self.opt1.config(width=17, font=self.fontstyle2)
        self.opt1.place(x=40, y=200)

    def CategoryDistrict(self): #카테고리:지역(구)
        self.CategoryDistrictList = ["행정구역 선택"]

        self.variable2 = StringVar(self.window)
        self.variable2.set(self.CategoryDistrictList[0])

        self.opt2 = OptionMenu(self.window, self.variable2, *self.CategoryDistrictList)
        self.opt2.config(width=17, font=self.fontstyle2)
        self.opt2.place(x=270, y=200)

    def CategoryKind(self): #카테고리:품종(종류)
        self.CategoryKindList = ["종류 선택", "개", "고양이", "기타"]

        self.variable3 = StringVar(self.window)
        self.variable3.set(self.CategoryKindList[0])

        self.opt3 = OptionMenu(self.window, self.variable3, *self.CategoryKindList)
        self.opt3.config(width=17, font=self.fontstyle2)
        self.opt3.place(x=40, y=300)

    def CategoryBreed(self): #카테고리:품종(품종)
        self.CategoryBreedList = ["품종 선택"]

        self.variable4 = StringVar(self.window)
        self.variable4.set(self.CategoryBreedList[0])

        self.opt4 = OptionMenu(self.window, self.variable4, *self.CategoryBreedList)
        self.opt4.config(width=17, font=self.fontstyle2)
        self.opt4.place(x=270, y=300)

    def SearchBacktoMainButton(self):
        self.SearchBacktomainButton = Button(self.window, text="뒤로", font=self.fontstyle2, borderwidth=5, command=self.SearchBacktoMain)
        self.SearchBacktomainButton.place(x=430, y=585)

    def SearchBacktoMain(self):
        self.RenderText.destroy()
        self.RenderTextScrollbar.destroy()
        self.SearchBacktomainButton.destroy()
        self.mapButton.destroy()
        self.bookmarkButton.destroy()

        self.SearchBox()
        self.setupButton()
        self.CategoryCity()
        self.CategoryBreed()
        self.CategoryDistrict()
        self.CategoryKind()

    def SearchButtonAction(self):
        self.opt1.destroy()
        self.opt2.destroy()
        self.opt3.destroy()
        self.opt4.destroy()
        self.GraphAreaButton.destroy()
        self.GraphBreedButton.destroy()

        self.MapButton()
        self.BookMarkButton()
        self.SearchBacktoMainButton()

        self.RenderText = Text(self.window, font=self.fontstyle3, width=50, height=27, borderwidth=12, relief='ridge')
        self.RenderText.place(x=40, y=200)

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
        self.mapButton = Button(self.window, text="지도", font=self.fontstyle2, borderwidth=5, command=self.Map)
        self.mapButton.place(x=430, y=200)

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

    def BookMarkButton(self):
        self.bookmarkButton = Button(self.window, text="저장", font=self.fontstyle2, borderwidth=5, command=self.BookMark)
        self.bookmarkButton.place(x=430, y=250)

    def BookMark(self):
        pass

    def GraphBreedBacktoMainButton(self):
        self.GraphBacktomainButton = Button(self.window, text="뒤로", font=self.fontstyle2, borderwidth=5, command=self.GraphBreedBacktoMain)
        self.GraphBacktomainButton.place(x=430, y=585)

    def GraphBreedBacktoMain(self):
        self.GraphBacktomainButton.destroy()
        self.GraphBreedCanvas.destroy()

        self.SearchBox()
        self.setupButton()
        self.CategoryCity()
        self.CategoryBreed()
        self.CategoryDistrict()
        self.CategoryKind()

    def GraphCityBacktoMainButton(self):
        self.GraphBacktomainButton = Button(self.window, text="뒤로", font=self.fontstyle2, borderwidth=5, command=self.GraphCityBacktoMain)
        self.GraphBacktomainButton.place(x=430, y=585)

    def GraphCityBacktoMain(self):
        self.GraphBacktomainButton.destroy()
        self.GraphCityCanvas.destroy()

        self.SearchBox()
        self.setupButton()
        self.CategoryCity()
        self.CategoryBreed()
        self.CategoryDistrict()
        self.CategoryKind()

    def GraphCity(self):
        self.SearchButton.destroy()
        self.InputLabel.destroy()
        self.opt1.destroy()
        self.opt2.destroy()
        self.opt3.destroy()
        self.opt4.destroy()
        self.GraphAreaButton.destroy()
        self.GraphBreedButton.destroy()

        self.GraphCityBacktoMainButton()

        self.itemElements1 = self.tree1.iter("item")
        self.itemElements2 = self.tree2.iter("item")
        self.itemElements3 = self.tree3.iter("item")

        self.GraphCityCanvas = Canvas(self.window, width=500, height=200, relief="solid", bd=2)
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
        self.opt1.destroy()
        self.opt2.destroy()
        self.opt3.destroy()
        self.opt4.destroy()
        self.GraphAreaButton.destroy()
        self.GraphBreedButton.destroy()

        self.GraphBreedBacktoMainButton()

        self.itemElements1 = self.tree1.iter("item")
        self.itemElements2 = self.tree2.iter("item")
        self.itemElements3 = self.tree3.iter("item")

        self.GraphBreedCanvas = Canvas(self.window, width=500, height=200, relief="solid", bd=2)
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