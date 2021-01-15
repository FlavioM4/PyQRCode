import qrcode
import os
import os.path
from time import sleep
import sys
import subprocess



def exitRestartDef():
	exitRestart = input("Do you need to create another one or simply exit? (R/E) ")
	exitRestart = exitRestart.lower()
	if exitRestart == "r":
		print("Restarting...")
		os.execv(sys.argv[0], sys.argv)
	elif exitRestart == "e":
		sys.exit()


def openImg(imgName):
	subprocess.call(f'cmd /k {imgName}.png', shell=True)
	exitRestartDef()
	


def saveImg(img, imgName, cd):
	img.save(f'{imgName}.png')
	print("QRCode saved in: ", cd)
	openFile = input("Do you want to open the newly created QR Code? (Y/N) ")
	openFile = openFile.lower()
	if openFile == "y":
		openImg(imgName)
		
		
	else:
		exitRestartDef()

def nameImg(img):
	imgName = input("Choose a name for your QRCode file: ")
	cd = os.getcwd()
	checkFile = os.path.isfile(imgName + '.png')
	if checkFile == True:
		print("That file already exists, choose a different name, please.")
		nameImg(img)
	else:
		saveImg(img, imgName, cd)


def createQR(url):
	qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
	qr.add_data(url)
	qr.make(fit=True)
	img = qr.make_image(fill='black', back_color='white')
	nameImg(img)

def getInput():
	print("Waiting for user input...")
	urlUser = input("Which URL do you want to turn into a QR Code? ")
	createQR(urlUser)


getInput()




