# PyQRCode
This is a simple terminal script to create a QR Code out of user's input text (for example, a website).

Dependencies:
- Python (obviously)
- qrcode module (pip install qrcode[pil])

STEPS:
- The script will ask the user for the desired URL (of course, you can just input some text, but why would you?)
- The script will ask the user to give a name to the QR Code image (no extension as it's default is png), if the name already exists, the script will ask the user to write a different name
- The script will then tell the user where the image was saved
- The script will finally ask the user if he wants to open the newly created image, if the user presses 'N', the script will then ask if the user wants to create another one or simply exit. If the user presses 'R', the script will restart, if he presses 'E', the script terminates. If the user wants to open the image, the image will then be displayed on the screen and the script terminated

