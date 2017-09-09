#!/usr/bin/python2.7
import qrcode
data = raw_input('Type something to create QRCode:') #gets input from user to encode into qrcode
print '\n'

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,) #initialize settings for Output Qrcode

qr.add_data(data) #adds the data to the qr cursor
qr.make(fit=True)

img = qr.make_image()
file_name = raw_input('Name for the Output image file, just the name without any extension:')
print '\n'

file_extension = raw_input('What type of Image? (PNG/JPEG): ')
file_name = file_name+'.'+file_extension
image_file = open(file_name,'w+') #will open the file, if file does not exist, it will be created and opened.
img.save(image_file,file_extension.upper()) #write qrcode encoded data to the image file.
image_file.close() #close the opened file handler.
