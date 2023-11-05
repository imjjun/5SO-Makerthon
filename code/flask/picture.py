import base64
import os

text_base64 = 'iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAAAAACoWZBhAAAAMklEQVR4nEXNwQkAMBACwfFI/y2bxwXia8FFUwF1pCCNJTIIwaD04ctsKRyaldI/9i8u1iwOE6FA880AAAAASUVORK5CYII='
bytes_base64 = text_base64.encode()
data = base64.b64decode(bytes_base64)
open('image.png', 'wb').write(data)
if os.path.isfile("image.png"):
    os.rename('image.png', '1.png')
elif os.path.isfile("image.png") and os.path.isfile("1.png"):
    os.rename('image.png', '2.png')
elif os.path.isfile("image.png")  and os.path.isfile("1.png") and os.path.isfile("2.png"):
    os.rename('image.png', '3.png')
elif os.path.isfile("image.png") and os.path.isfile("1.png")  and os.path.isfile("2.png")  and os.path.isfile("3.png"):
    os.rename('image.png', '4.png')
elif os.path.isfile("image.png") and os.path.isfile("1.png") and os.path.isfile("2.png") and os.path.isfile("3.png")  and os.path.isfile("4.png"):
    os.rename('image.png', '5.png')
else:
    None





