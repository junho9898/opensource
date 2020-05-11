from tkinter import *
from tkinter.filedialog import *

## 함수 선언 부분 ##
def loadImage(fname):
    global inImage, XSIZE, YSIZE
    fp = open(fname, 'rb')

    for i in range(0, XSIZE):
        tmpList = []
        for k in range(0, YSIZE):
            data = int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)
    displayImage(inImage)

    fp.close()


def displayImage(image):
    global XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE):
        tmpString = ""
        for k in range(0, YSIZE):
            data = image[i][k]
            tmpString += "#%02x%02x%02x " % (data, data, data)  # x 뒤에 한칸 공백
        rgbString += "{" + tmpString + "} "  # } 뒤에 한칸 공백
    paper.put(rgbString)


def loadNewImage():
    global inImage
    inImage.clear()
    filename = askopenfilename(parent=window, filetypes=(("RAW 파일", "*.raw"), ("모든 파일", "*.*")))
    loadImage(filename)

def toBright() :
    global inImage
    global XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE):
        tmpString = ""
        for k in range(0, YSIZE):
            data = inImage[i][k]
            inImage[i][k] = data + 20
            tmpString += "#%02x%02x%02x " % (inImage[i][k], inImage[i][k], inImage[i][k])  # x 뒤에 한칸 공백
        rgbString += "{" + tmpString + "} "  # } 뒤에 한칸 공백
    paper.put(rgbString)

def toDark():
    global inImage
    global XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE):
        tmpString = ""
        for k in range(0, YSIZE):
            data = inImage[i][k]
            if data-20 < 0 :
                inImage[i][k] = 0
            else :
                inImage[i][k] = data - 20
            tmpString += "#%02x%02x%02x " % (inImage[i][k], inImage[i][k], inImage[i][k])  # x 뒤에 한칸 공백
        rgbString += "{" + tmpString + "} "  # } 뒤에 한칸 공백
    paper.put(rgbString)

def toReverse() :
    global inImage
    global XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE):
        tmpString = ""
        for k in range(0, YSIZE):
            inImage[i][k] = 255 - inImage[i][k]
            tmpString += "#%02x%02x%02x " % (inImage[i][k], inImage[i][k], inImage[i][k])  # x 뒤에 한칸 공백
        rgbString += "{" + tmpString + "} "  # } 뒤에 한칸 공백
    paper.put(rgbString)

def func_exit():
    window.quit()
    window.destroy()


## 전역 변수 선언 부분 ##
window = None
canvas = None
XSIZE, YSIZE = 256, 256
inImage = []  # 2차원 리스트 (메모리)

## 메인 코드 부분 ##
window = Tk()
window.title("흑백 사진 보기")
canvas = Canvas(window, height=XSIZE, width=YSIZE)
paper = PhotoImage(width=XSIZE, height=YSIZE)
canvas.create_image((XSIZE / 2, YSIZE / 2), image=paper, state="normal")

if not inImage :
    filename = 'D:\수업\오픈소스기초프로젝트\\tree.raw'
    loadImage(filename)

# 파일 --> 메모리
#filename = 'D:\수업\오픈소스기초프로젝트\\tree.raw'  # C:/CookPython/RAW/tree.raw
#loadImage(filename)

mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(window)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=loadNewImage)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

imageEffectMenu = Menu(window)
mainMenu.add_cascade(label = "사진효과", menu = imageEffectMenu)
imageEffectMenu.add_command(label = "밝게하기", command = toBright)
imageEffectMenu.add_separator()
imageEffectMenu.add_command(label = "어둡게하기", command = toDark)
imageEffectMenu.add_separator()
imageEffectMenu.add_command(label = "반전 이미지", command = toReverse)
# 메모리 --> 화면
#displayImage(inImage)

canvas.pack()
window.mainloop()
