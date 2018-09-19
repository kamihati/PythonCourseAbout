# codint=utf8

b_str = ""
with open("demo.jpg", 'rb') as f:
    b_str = f.read()
    

with open("demo_temp.jpg", 'wb') as f:
    f.write(b_str)
