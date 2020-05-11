import requests
import xmltodict
import time



def collct_lent(ym,lawd_cd):
	API_KEY = IDLrC2ZOpQ6hWojQ29au/YxGNyFmfkpSy/2y11rqcTBuWjtYp7hkS/p3LnriQnWihHz6E8uxr20bc3f3W9cMNg==

	url="http://openapi.molit.go.kr:8081/OpenAPI_ToolinstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHRent

	# &numOfRows=1000"+
	url=url+"?&LAWD_CD="+lawd_cd+"&DEAL_YMD="+ym+"&serviceKey="+API_KEY

	# webbrowser.open(url)
	resultXML = urlopen(url)
	result = resultXML.read()
	xmlsoup = BeautifulSoup(result, 'lxml-xml')

	te=xmlsoup.findAll("item")

	sil=pd.DataFrame()

	for t in te :
		build_y=t.find("건축년도").text
		year=t.find("년").text
		month=t.find("월").text
		day=t.find("일").text
		
