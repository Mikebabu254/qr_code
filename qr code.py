import qrcode

img = qrcode.make('https://github.com/Mikebabu254')

img.save('mikegit.png')

img.show()