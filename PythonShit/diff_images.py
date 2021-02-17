from PIL import Image
import requests 
from io import BytesIO

def image_to_byte_array(image:Image):
  imgByteArr = BytesIO()
  image.save(imgByteArr, format=image.format)
  imgByteArr = imgByteArr.getvalue()
  return imgByteArr

def repixel_image(image_url, on_coeff=1.3):

    img = Image.open(BytesIO(requests.get(image_url).content))
    
    pixels = img.load() # pixelmap
    
    R_low, R_hig = (100, 255)
    G_low, G_hig = (30, 156)
    B_low, B_hig = (0, 128)
    
    R_colmap = range(R_low, R_hig)
    G_colmap = range(G_low, G_hig)
    B_colmap = range(B_low, B_hig)

    return img, pixels 

def divide(pixelmap1, pixelmap2):
    try:
        a1 = pixelmap2[x_pixel, y_pixel][0] / pixelmap1[x_pixel, y_pixel][0]
    except:
        a1 = 0
    try:
        a2 = pixelmap2[x_pixel, y_pixel][1] / pixelmap1[x_pixel, y_pixel][1]
    except:
        a2 = 0
    try:
        a3 = pixelmap2[x_pixel, y_pixel][2] / pixelmap1[x_pixel, y_pixel][2]
    except:
        a3 = 0
    return a1, a2, a3

pics = []

pics.append(("https://sun9-7.userapi.com/8711NdHdpFNP0lgKWCFXCXBiNRpiHUE-YPigTw/W5TpRLtnEfU.jpg", "https://sun9-48.userapi.com/Rp760JiCYX_ymKFv55LdxKPmEzY2Hj_mnqGtdw/VkRaAe7bWpk.jpg"))
pics.append(("https://sun9-37.userapi.com/rvMnDEM7zc75evmujRQoqffd-fxkOHbC-ee0NA/Jak9iArbFQI.jpg", "https://sun9-19.userapi.com/od94OmuaUZzRYe0h1Of8FA23GwnzZumHxF3PMQ/4k1KyR40BJg.jpg"))
pics.append(("https://sun9-15.userapi.com/0QVft7Jrc6sj4lLtyUtSMeVAY2UqwxpfYd75hg/WYXQY490HAs.jpg", "https://sun9-47.userapi.com/N-UFeC7hkwhfgvF6ipahxL2yieCudfNmWIjCgg/cjYE6s7N57U.jpg"))
pics.append(("https://sun9-44.userapi.com/ESlOvNtuNrp0lyvukL9EhRgP1jAdtOtFesvUTw/W7hHCkx3u2s.jpg", "https://sun9-36.userapi.com/dARvKeWTcSxSeElDsO54EHSBKAueAOPF94fZdA/Pl56MEzVeiw.jpg"))
pics.append(("https://sun9-73.userapi.com/8fEJY8XSNw5DTnA86ZXr24cNmhIZzhKXYa8lBw/MbJA0G7ylec.jpg", "https://sun9-64.userapi.com/x421fxqrP27NxUE_fpsoP5Bc0baMBOOXK0pivg/7_05-Hm8IBg.jpg"))
pics.append(("https://sun9-62.userapi.com/WfaJ1hbVM759MgFcakGjKMiu6vC1VNa-nvjB9w/IT_vNBqWbYY.jpg", "https://sun9-49.userapi.com/4juQXv1PMKBWIAQ9weSDyJvxT6JiwsPHgeAq5w/iptTELcD1tM.jpg"))
pics.append(("https://sun9-46.userapi.com/Od6nmn2vVnxofCmWjGMVanwRHD9LeESunOaYLw/jpDOCy3HJ9Q.jpg", "https://sun9-31.userapi.com/_4aRo5JiexDykHsabPpNMksWmlrHzDSI0B2R7Q/V_AOtT7osCo.jpg"))

for pic1, pic2 in pics:
    
    img1, pixelmap1 = repixel_image(pic1)
    img2, pixelmap2 = repixel_image(pic2)
    
    diff_pixel = []
    R = 0
    G = 0 
    B = 0
    R_LOW = 255
    R_HIGH = 0
    G_LOW = 255
    G_HIGH = 0
    B_LOW = 255
    B_HIGH = 0
    R_AVERAGE = 0
    G_AVERAGE = 0
    B_AVERAGE = 0
    index = 0 
    for x_pixel in range(img1.size[0]):
        for y_pixel in range(img1.size[1]):
            if pixelmap1[x_pixel, y_pixel] != pixelmap2[x_pixel, y_pixel]:
                R_new, G_new, B_new = divide(pixelmap1, pixelmap2)
                R += R_new
                G += G_new
                B += B_new
                index += 1  
                if pixelmap1[x_pixel, y_pixel][0] < R_LOW:
                    R_LOW = pixelmap1[x_pixel, y_pixel][0]
                if pixelmap1[x_pixel, y_pixel][0] > R_HIGH:
                    R_HIGH = pixelmap1[x_pixel, y_pixel][0]

                if pixelmap1[x_pixel, y_pixel][1] < G_LOW:
                    G_LOW = pixelmap1[x_pixel, y_pixel][1]
                if pixelmap1[x_pixel, y_pixel][1] > G_HIGH:
                    G_HIGH = pixelmap1[x_pixel, y_pixel][1]

                if pixelmap1[x_pixel, y_pixel][2] < B_LOW:
                    B_LOW = pixelmap1[x_pixel, y_pixel][2]
                if pixelmap1[x_pixel, y_pixel][2] > B_HIGH:
                    B_HIGH = pixelmap1[x_pixel, y_pixel][2]

                R_AVERAGE += pixelmap1[x_pixel, y_pixel][0]
                G_AVERAGE += pixelmap1[x_pixel, y_pixel][1]
                B_AVERAGE += pixelmap1[x_pixel, y_pixel][2]

                # diff_pixel.append((
                #     str("X:" + str(x_pixel)), 
                #     str("Y:" + str(y_pixel)), 
                #     divide(pixelmap1, pixelmap2)
                #     ))
    
    print("R:%s G:%s B:%s R_LOW:%s R_HIGH:%s G_LOW:%s G_HIGH:%s B_LOW:%s B_HIGH:%s R_AVERAGE:%s G_AVERAGE:%s B_AVERAGE:%s" % (str(R / index), str(G / index), str(B / index), str(R_LOW), str(R_HIGH), str(G_LOW), str(G_HIGH), str(B_LOW), str(B_HIGH), str(R_AVERAGE / index), str(G_AVERAGE / index), str(B_AVERAGE / index)))

