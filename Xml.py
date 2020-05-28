import urllib
import http.client
from xml.etree import ElementTree

class xml():
    def __init__(self):
        self.conn1 = http.client.HTTPConnection("openapi.animal.go.kr")
        self.conn1.request("GET",
                     "/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?serviceKey=f%2FqounJa%2BfZ5Bv1YnJPiKcEcWrrfYur9FgrYkinR8t0m7sCjvWoey6inoG2PxEvBzgqEs%2Fchc29kokMbhkJdLg%3D%3D&bgnde=20190101&endde=20200527&upkind=417000&kind=&upr_cd=&org_cd=&care_reg_no=&state=notice&pageNo=1&numOfRows=10&neuter_yn=Y&")
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

        print(self.strXml1)
        print(self.strXml2)
        print(self.strXml3)

        itemElements = self.tree1.iter("item")
        itemElements = self.tree2.iter("item")
        itemElements = self.tree3.iter("item")

xml()