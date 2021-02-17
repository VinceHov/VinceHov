from PIL import Image
import requests 
from io import BytesIO
import numpy as np

def image_to_byte_array(image:Image):
  imgByteArr = BytesIO()
  image.save(imgByteArr, format=image.format)
  imgByteArr = imgByteArr.getvalue()
  return imgByteArr

def repixel_image(image_url, coeff_rgb, on_coeff=1.3):
    
    # image_url = "https://sun9-22.use  rapi.com/4qWDIR5pGnxB_seA5-s01FuIetoZ2a3KMZUKVA/wxulWPOTNms.jpg"
    img = Image.open(BytesIO(requests.get(image_url).content)) #Image.open('C:/alice.jpg')#(BytesIO(requests.get(image_url).content)) #('C:/alice.jpg')
    
    pixels = img.load() # pixelmap
    
    R_low, R_hig = (100, 255)
    G_low, G_hig = (30, 156)
    B_low, B_hig = (0, 128)
    
    R_colmap = range(R_low, R_hig)
    G_colmap = range(G_low, G_hig)
    B_colmap = range(B_low, B_hig)
    
    # on_coeff = 1.3
    coeff_r, coeff_g, coeff_b = coeff_rgb

    for x_pixel in range(img.size[0]):
        stroka = ""
        for y_pixel in range(img.size[1]):
            # stroka += ("R" + str(pixels[x_pixel, y_pixel][0]) + "G" + str(pixels[x_pixel, y_pixel][1]) + "B" + str(pixels[x_pixel, y_pixel][2]) + " " )
            # print(pixels[x_pixel, y_pixel])
            pixel = pixels[x_pixel, y_pixel]
            # if (pixels[x_pixel, y_pixel][0] in range(110, 248)) and (pixels[x_pixel, y_pixel][1] in range(30, 128) and (pixels[x_pixel, y_pixel][2] in range(14, 85))):
            #     pixels[x_pixel, y_pixel] = (int(pixel[0] * 1.1) , pixel[1] , 240)
    
            try:
                diffR = pixel[0] / pixel[1]
                diffG = pixel[1] / pixel[2]
            except:
                diffR = (pixel[0] + 1) / (pixel[1] + 1)
                diffG = (pixel[1] + 1) / (pixel[2] + 1)
            finally:
                # print(diffR, diffG)
                # print(diffR / 0.8)
                if ((pixel[0] > pixel[1] > pixel[2]) and (diffR > on_coeff) and (diffG > on_coeff) and (pixel[0] in R_colmap) and (pixel[1] in G_colmap) and (pixel[2] in B_colmap)):
                    # print("TRUE")
                    pixels[x_pixel, y_pixel] = (int(pixel[0] * coeff_r) , int(pixel[1] * coeff_g) , int(pixel[2] * coeff_b))
            # exit(0)
    
                # if ((pixel[0] > pixel[1] > pixel[2]) and (pixel[0] / pixel[1] > 0.8) and (pixel[1] / pixel[2] > 0.8)):
        # print(stroka + "\n")
    return img #image_to_byte_array(img)
# for b in range(230,256):
# b = 245
index = 1
for r in np.arange(0.2, 1.6, 0.1):
    for g in np.arange(0.2, 1.6, 0.1):
        for b in np.arange(0.2, 20.6, 0.1):
            img = repixel_image("https://sun9-73.userapi.com/lJUUCoK03p5w_M8zP_ltU_H9F5dc39TElqTI2g/j3wXIYSkTnE.jpg", (r,g,b))
            img.save('D:/alice4/%3f_%3f_%3f.jpg' % (r,g,b))
            print("Saved:%d of %d" % (index, 16464))
            index += 1