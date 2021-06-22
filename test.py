import colourpick as cp

img = cp.processimage(cp.importimage("green.jpg"))
col = cp.findcolour(img, 2)
print(cp.checkcolour(col[0]))