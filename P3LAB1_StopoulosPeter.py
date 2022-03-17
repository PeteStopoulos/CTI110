x = int(input())
y = int(input())
z = int(input())
rgb  = [x, y, z]
min = int(min(rgb))
rgb[0] = x - min
rgb[1] = y - min
rgb[2] = z - min
print (str(rgb[0]) + ' ' + str(rgb[1]) + ' ' + str(rgb[2]))