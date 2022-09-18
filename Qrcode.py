import qrcode
data = "Good Morning"
img = qrcode.make(data)
img.show()