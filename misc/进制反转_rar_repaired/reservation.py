# coding: utf-8

with open("flag.wav","rb") as f:
    content = f.read()


new = b''

print(new,type(new))
for id,c in enumerate(content):
    _c = 255 - c
    new += bytes([_c])
    print(f"\r{id}/{len(content)}",end='')		# 大概跑了两小时（算法太拉跨）


with open("flag5.wav","wb") as fi:
    fi.write(new)