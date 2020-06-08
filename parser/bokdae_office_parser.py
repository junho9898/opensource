import requests
from bs4 import BeautifulSoup
import json
import os, sys
import pandas as pd
import plotly.express as px
import sqlite3
import webbrowser
from urllib.request import urlopen

def collect_lent(ym,lawd_cd):
 
    API_KEY = "p46H1V3Abg3ygD36c7sOWEmw8Tn9Am9SDuYngAkwpdqxxaMT6%2BeNOt0KpqEw7pGSYB71xZ3nSTcsD6MXxM4D0w%3D%3D"
 
    url="http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcOffiRent"
 
    # &numOfRows=1000"+
    url=url+"?&LAWD_CD="+lawd_cd+"&DEAL_YMD="+ym+"&serviceKey="+API_KEY
 
    #webbrowser.open(url)
    resultXML = urlopen(url)
    result = resultXML.read()
    xmlsoup = BeautifulSoup(result, 'lxml-xml')
 
    te=xmlsoup.findAll("item")
 
    sil=pd.DataFrame()
 
    for t in te:
        build_y=t.find("건축년도").text
        offi_nm=t.find("단지").text
        size=t.find("전용면적").text
        year=t.find("년").text
        month=t.find("월").text
        day=t.find("일").text
        dong=t.find("법정동").text
        bo_price=t.find("보증금").text
        mo_price=t.find("월세").text
        floor=t.find("층").text
        ji_code=t.find("지역코드").text
 
        temp = pd.DataFrame(([[build_y,offi_nm,size,year,month,day,dong,bo_price,mo_price,ji_code,floor]]), columns=["build_y","offi_nm","size","year","month","day","dong","bo_price","mo_price","ji_code","floor"])
 
        sil=pd.concat([sil,temp])

    sil=sil.reset_index(drop=True)
 
    return sil



if __name__ == '__main__':
    # 지역코드 가져오기
    code=pd.read_excel("KIKcd_B.20200515.xlsx")
    code_seo=code[(code["시도명"]=="충청북도") | (code["시도명"]=="충북")]
    code_seo=code_seo[code_seo["읍면동명"] == "복대동"]
    code_seo = code_seo[code_seo["시군구명"].isnull() == False]
    code_seo["ji_code"] = code_seo["법정동코드"].astype(str).str[0:5]
    sil_trade=pd.DataFrame()
 
    ym=list(["201901","201902","201903","201904","201905","201906","201907","201908","201909","201910","201911","201912","202001"])

    output_file = sys.argv[1]
 
    for m in ym:
        for co in code_seo["ji_code"]:
            temp =collect_lent(m,co)
            sil_trade=pd.concat([sil_trade,temp])
            print(co+", "+str(len(temp))+" is compleded")
        print("*"+str(m)+" is completed")

    jw_trade = sil_trade.loc[(sil_trade['dong'].str.contains('복대동')), :]
    jw_trade.to_csv(output_file, index=False)
 
#   con = sqlite3.connect("/opt/django_demo/db.sqlite3")
#   sil_trade.to_sql('lent', con, if_exists='replace', index=True)
#   con.close()
