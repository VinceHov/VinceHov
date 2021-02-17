from PIL import Image
import os
baseDir = "D:/siga/"
destDir = "D:/newsiga/"
index = 0
for filename in os.listdir(baseDir):
    img = Image.open(baseDir + filename)
    x,y = img.size

    im = img.crop((1228.0, 0.0, 1728.0, 1080.0))
    # im.show()
    im.save(destDir + filename)
    print(index, len(os.listdir(baseDir)))
    index +=1 
    # exit()

    # pixels = img.load()
    # x_size, y_size = img.size
    # x_max = 0
    # have_non_x = True
    # for x in range(x_size):
    #     for y in range(y_size):
    #         r,g,b,have = pixels[x,y]
    #         if have == 0 and x >= x_max and have_non_x == True:
    #             x_max = x 
    #         else:
    #             have_non_x = False
    # print(x_max)


# Image.open("D:/siga%s")