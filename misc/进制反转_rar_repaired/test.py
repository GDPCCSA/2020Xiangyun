# coding: utf-8

with open("flag.wav","rb") as f:
    print(f.read())
    
with open("flag.wav","rb") as f:
    content = f.read()
    
def reverse(s):
    return ''.join(str(1^int(c)) for c in s)
    
with open("flag2.wav","wb") as fi:
    fi.write(reverse(content))
    
with open("flag2.wav","wb") as fi:
    print(type((reverse(content))))
    
    
with open("flag2.wav","wb") as fi:
    fi.write(bytes(reverse(content)))
    
    
    
type(content)
reverse(content)
type(reverse(content))
bin(content)
bincontent = bytes.fromhex(content)
bincontent = bytes.fromhex(str(content))
str(content)
content
byte_binary = bin(ord(content))
get_ipython().run_line_magic('ls', '')
with open("flag2.wav","wb") as fi:
    fi.tell()
       
    
with open("flag2.wav","wb") as fi:
    a = fi.tell()
       
    
a
content[0]
a = 256 content[0]
a = 256 - content[0]
a
a = 255 - content[0]
a
bytes(a)
ascii(a)
a
ord(a)
get_ipython().run_line_magic('pinfo', 'ord')
get_ipython().run_line_magic('pinfo', 'ascii')
type(a)
hexdump
ascii(82)
ascii(83)
ascii(69)
chr(69(
))
chr(6)
chr(69)
chr(82)
new = ''
for c in content:
    _c = 255 - c
    new += chr(_c)
    
with open("flag2.wav","w",encoding='utf-8') as fi:
    fi.write(new)
    
       
    
0xA9
chr(255-0xA9)
chr(255-0xA8)
chr(255-0xA8)
new[0:44]
n = 'RIFFäÀY\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x02\x00\x80\x00\x00\x00î\x02\x00\x04\x00\x10\x00data\x00ÀY\x00'
n
new = ''
new = bytes(new)
print(new,type(new))
for c in content:
    _c = 255 - c
    new += bytes(_c)
    
new = ''
bytes(new)
new = 'a'
bytes(new)
bytes(new,encoding = "utf-8")
new = ''
print(new,type(new))
for c in content:
    _c = 255 - c
    new += bytes(_c,"utf-8")
    
new = ''
print(new,type(new))
for c in content:
    _c = 255 - c
    new += bytes(_c,encoding = "utf-8")
    
bytes([3])
bytes([a])
new = ''
print(new,type(new))
for c in content:
    _c = 255 - c
    new += bytes([_c])
    
new = '\xFF'

print(new,type(new))
for c in content:
    _c = 255 - c
    new += bytes([_c])
    
new = b''

print(new,type(new))
for c in content:
    _c = 255 - c
    new += bytes([_c])
    
new = b''

print(new,type(new))
for c in content:
    _c = 255 - c
    new += bytes([_c])
    print(new)
    
new = b''

print(new,type(new))
for c in content:
    _c = 255 - c
    new += bytes([_c])
    # print(new)
    
new = b''

print(new,type(new))
for c in content:
    _c = 255 - c
    new += bytes([_c])
    print(bytes([_c]))
    
len(content)
with open("flag.wav","rb") as f:
    
    content = f.read()
    
len(content)
new = b''

print(new,type(new))
for id,c in enumerate(content):
    _c = 255 - c
    new += bytes([_c])
    print(f'\r{id}//{len(content)}')
    
    
new = b''

print(new,type(new))
for id,c in enumerate(content):
    _c = 255 - c
    new += bytes([_c])
    print(f"{id}/{len(content)}\r")
    
    
    
print  (u'前面的内容\r只显示后面的内容')
new = b''

print(new,type(new))
for id,c in enumerate(content):
    _c = 255 - c
    new += bytes([_c])
    print(f"\r{id}/{len(content)}\r")
    
    
    
new
with open("flag5.wav","wb",encoding='utf-8') as fi:
    fi.write(new)
    
       
    
with open("flag5.wav","wb") as fi:
    fi.write(new)
    
       
    
get_ipython().run_line_magic('save', 'test.py 0-76')
