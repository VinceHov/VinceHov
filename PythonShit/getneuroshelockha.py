import subprocess
import re 
cmdpath = "python3 E:\\нейросетки\\петончег\\нейросетка.py -t E:\\нейросетки\\петончег\\uv_sex.txt -o 100000 -g"
for i in range(1,51):
    output = open(("C:/neuroshelochka_" + str(i) + ".rpy"), "w")
    subpart = ("""
init:

    $ mods["test_neuroset""" + str(i) + """\"]=u"НейроЮля и её Киберщёлочка_""" + str(i) + """\"    
    
    $ Chan = Character(u'Я', color="ffd800", what_color="E2C778",)
    $ KOD = Character(u'Код', color="#FF0000", what_color="E2C778",)
    
    $ Beskonechnoe_Leto_OST = "music/Beskonechnoe_Leto_OST.mp3"
    

    image cg uv_grin1 = "18+/images/uv_grin.png"
    image cg uv_normal1 = "18+/images/uv_normal.png"
    image cg uv_sad1 = "18+/images/uv_sad.png"
    image cg uv_smile1 = "18+/images/uv_smile.png"
    image cg uv_laugh1 = "18+/images/uv_laugh.png"
    image cg uv_surprise1 = "18+/images/uv_surprise.png"
    image cg uv_shoked1 = "18+/images/uv_shoked.png"
    image cg uv_shokeds1 = "18+/images/uv_shokeds.png"
    image cg uv_shokеdr1 = "18+/images/uv_shokеdr.png"
    image cg uv_shy1 = "18+/images/uv_shy.png"
    image uvee = "18+/images/uvee.jpg"
    image cg uv_ch1 = "18+/images/uv_ch1.png"
    image cg uv_ch2 = "18+/images/uv_ch2.png"
    
    # секс рабыня Юля
    image cg uv_bog = "18+/images/uv18/uv_bog.png"
    image cg uv_grin = "18+/images/uv18/uv_grin.png"
    image cg uv_laugh = "18+/images/uv18/uv_laugh.png"
    image cg uv_normal = "18+/images/uv18/uv_normal.png"
    image cg uv_sad = "18+/images/uv18/uv_sad.png"
    image cg uv_shoked = "18+/images/uv18/uv_shoked.png"
    image cg uv_shokeds = "18+/images/uv18/uv_shokeds.png"
    image cg uv_shy = "18+/images/uv18/uv_shy.png"
    image cg uv_smile = "18+/images/uv18/uv_smile.png"
    image cg uv_surprise = "18+/images/uv18/uv_surprise.png"
    
    image cg 4890528 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "18+/images/4890528.png", (0,0), "18+/images/pustota.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900,1080), (0,0), "18+/images/4890528.png", (0,0), "18+/images/pustota.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900,1080), (0,0), "18+/images/4890528.png", (0,0), "18+/images/pustota.png") )      

    image cg uv_ch:
        "18+/images/uv_ch1.png" with Dissolve(0.4, alpha=True)
        pause 1.0
        "18+/images/uv_ch2.png" with Dissolve(0.4, alpha=True)  
        pause 1.0
        repeat
    
    image Spasti_Leny = "18+/images/Spasti_Leny.jpg"

    transform pr1_1:
        xalign 0.5 yalign 0.1
        linear 0.10 zoom 1.0 xalign 0.5 yalign 0.1
        linear 0.10 zoom 1.1 xalign 0.5 yalign 0.2
        linear 0.10 zoom 1.2 xalign 0.5 yalign 0.3
        linear 0.10 zoom 1.3 xalign 0.5 yalign 0.4
        linear 0.10 zoom 1.4 xalign 0.5 yalign 0.5
        linear 0.10 zoom 1.5 xalign 0.5 yalign 0.6
        linear 0.10 zoom 1.6 xalign 0.5 yalign 0.7
        linear 0.10 zoom 1.7 xalign 0.5 yalign 0.8
        linear 0.10 zoom 1.8 xalign 0.5 yalign 0.9
        linear 0.10 zoom 1.9 xalign 0.5 yalign 0.9
        linear 0.10 zoom 2.0 xalign 0.5 yalign 0.9
        linear 0.10 zoom 2.1 xalign 0.5 yalign 0.9
        linear 0.10 zoom 2.2 xalign 0.5 yalign 0.9
        linear 0.10 zoom 2.3 xalign 0.5 yalign 0.9
        linear 0.10 zoom 2.4 xalign 0.5 yalign 0.9
        linear 0.10 zoom 2.5 xalign 0.5 yalign 0.9
        linear 0.10 zoom 2.6 xalign 0.5 yalign 0.9
        linear 0.10 zoom 2.7 xalign 0.5 yalign 0.9
        linear 0.10 zoom 2.8 xalign 0.5 yalign 0.9
        linear 0.10 zoom 2.9 xalign 0.5 yalign 0.9
        linear 0.10 zoom 3.0 xalign 0.5 yalign 0.9
        linear 0.10 zoom 3.1 xalign 0.5 yalign 0.9
        linear 0.10 zoom 3.2 xalign 0.5 yalign 0.9
        linear 0.10 zoom 3.3 xalign 0.5 yalign 0.9
        linear 0.10 zoom 3.4 xalign 0.5 yalign 0.9
        linear 0.10 zoom 3.5 xalign 0.5 yalign 0.9
        linear 0.10 zoom 3.6 xalign 0.5 yalign 0.9
        linear 0.10 zoom 3.7 xalign 0.5 yalign 0.9
        linear 0.10 zoom 3.8 xalign 0.5 yalign 0.9
        linear 0.10 zoom 3.9 xalign 0.5 yalign 0.9
        linear 0.10 zoom 4.0 xalign 0.5 yalign 0.9  
        
    transform pr1_2:
        zoom 3.9 xalign 0.5 yalign 0.9
        linear 0.13 zoom 3.8 xalign 0.5 yalign 0.9  
        linear 0.13 zoom 3.7 xalign 0.5 yalign 0.9
        linear 0.13 zoom 3.6 xalign 0.5 yalign 0.9
        linear 0.13 zoom 3.5 xalign 0.5 yalign 0.9
        linear 0.13 zoom 3.4 xalign 0.5 yalign 0.9
        linear 0.13 zoom 3.3 xalign 0.5 yalign 0.9
        linear 0.13 zoom 3.2 xalign 0.5 yalign 0.9
        linear 0.13 zoom 3.1 xalign 0.5 yalign 0.9
        linear 0.13 zoom 3.0 xalign 0.5 yalign 0.9
        linear 0.13 zoom 2.9 xalign 0.5 yalign 0.9
        linear 0.13 zoom 2.8 xalign 0.5 yalign 0.9  
        linear 0.13 zoom 2.7 xalign 0.5 yalign 0.9
        linear 0.13 zoom 2.6 xalign 0.5 yalign 0.9
        linear 0.13 zoom 2.5 xalign 0.5 yalign 0.9
        linear 0.13 zoom 2.4 xalign 0.5 yalign 0.9
        linear 0.13 zoom 2.3 xalign 0.5 yalign 0.9
        linear 0.13 zoom 2.2 xalign 0.5 yalign 0.9
        linear 0.13 zoom 2.1 xalign 0.5 yalign 0.9
        linear 0.13 zoom 2.0 xalign 0.5 yalign 0.9
        linear 0.13 zoom 1.9 xalign 0.5 yalign 0.9
        
    transform pr1_3:
        zoom 1.9 xalign 0.5 yalign 0.9
        linear 0.13 zoom 1.8 xalign 0.5 yalign 0.9  
        linear 0.13 zoom 1.7 xalign 0.5 yalign 0.9
        linear 0.13 zoom 1.6 xalign 0.5 yalign 0.9
        linear 0.13 zoom 1.5 xalign 0.5 yalign 0.9
        linear 0.13 zoom 1.4 xalign 0.5 yalign 0.9
        linear 0.13 zoom 1.3 xalign 0.5 yalign 0.9
        linear 0.13 zoom 1.2 xalign 0.5 yalign 0.9
        linear 0.13 zoom 1.1 xalign 0.5 yalign 0.9
        linear 0.13 zoom 1.0 xalign 0.5 yalign 0.9 
        
    transform pr1_4:
        zoom 1.9 xalign 0.5 yalign 0.9
        linear 0.13 zoom 2.0 xalign 0.5 yalign 0.9 
        linear 0.13 zoom 2.1 xalign 0.5 yalign 0.9
        linear 0.13 zoom 2.2 xalign 0.5 yalign 0.9
        linear 0.13 zoom 2.3 xalign 0.5 yalign 0.9
        linear 0.13 zoom 2.4 xalign 0.5 yalign 0.9
        linear 0.13 zoom 2.5 xalign 0.5 yalign 0.9
        linear 0.13 zoom 2.6 xalign 0.5 yalign 0.9
        linear 0.13 zoom 2.7 xalign 0.5 yalign 0.9
        linear 0.13 zoom 2.8 xalign 0.5 yalign 0.9
        linear 0.13 zoom 2.9 xalign 0.5 yalign 0.9
        linear 0.13 zoom 3.0 xalign 0.5 yalign 0.9  
        linear 0.10 zoom 3.1 xalign 0.5 yalign 0.9
        linear 0.10 zoom 3.2 xalign 0.5 yalign 0.9
        linear 0.10 zoom 3.3 xalign 0.5 yalign 0.9
        linear 0.10 zoom 3.4 xalign 0.5 yalign 0.9
        linear 0.10 zoom 3.5 xalign 0.5 yalign 0.9
        linear 0.10 zoom 3.6 xalign 0.5 yalign 0.9
        linear 0.10 zoom 3.7 xalign 0.5 yalign 0.9
        linear 0.10 zoom 3.8 xalign 0.5 yalign 0.9
        linear 0.10 zoom 3.9 xalign 0.5 yalign 0.9
        linear 0.10 zoom 4.0 xalign 0.5 yalign 0.9 
        
    transform pr2_1:
        xalign 0.5 yalign 0.1
        linear 0.10 zoom 1.0 xalign 0.5 yalign 0.1
        linear 0.10 zoom 1.1 xalign 0.5 yalign 0.2
        linear 0.10 zoom 1.2 xalign 0.5 yalign 0.3
        linear 0.10 zoom 1.3 xalign 0.5 yalign 0.4
        linear 0.10 zoom 1.4 xalign 0.5 yalign 0.5
        linear 0.10 zoom 1.5 xalign 0.5 yalign 0.6
        linear 0.10 zoom 1.6 xalign 0.5 yalign 0.7
        linear 0.10 zoom 1.7 xalign 0.5 yalign 0.8
        linear 0.10 zoom 1.8 xalign 0.5 yalign 0.9
        linear 0.10 zoom 1.9 xalign 0.5 yalign 0.9
        
    transform pr3_1:
        zoom 2.0 xalign 0.5 yalign 0.9
        linear 0.5 zoom 2.0 xalign 0.5 yalign 0.9    
        linear 0.5 zoom 2.1 xalign 0.5 yalign 0.9 
        linear 0.5 zoom 2.0 xalign 0.5 yalign 0.9 
        linear 0.5 zoom 1.9 xalign 0.5 yalign 0.9 
        
    transform pr4_1:
        zoom 2.0 xalign 0.5 yalign 0.9
        linear 0.5 zoom 2.1 xalign 0.5 yalign 0.8    

        
    transform pr5_1:
        zoom 2.2 xalign 0.5 yalign 0.8
        linear 0.5 zoom 2.3 xalign 0.5 yalign 0.7    
        linear 0.5 zoom 2.4 xalign 0.5 yalign 0.6   
    transform pr6_1:
        zoom 2.5 xalign 0.5 yalign 0.6
        linear 0.5 zoom 2.6 xalign 0.5 yalign 0.6    
        linear 0.5 zoom 2.7 xalign 0.5 yalign 0.6  
        linear 0.5 zoom 2.8 xalign 0.5 yalign 0.6    
        linear 0.5 zoom 2.9 xalign 0.5 yalign 0.6     
        linear 0.5 zoom 3.0 xalign 0.5 yalign 0.6    
        linear 0.5 zoom 3.1 xalign 0.5 yalign 0.6  
    transform pr7_1:
        zoom 3.1 xalign 0.5 yalign 0.6
        linear 0.5 zoom 3.1 xalign 0.5 yalign 0.5       
    transform pr8_1:
        zoom 3.1 xalign 0.5 yalign 0.5
        linear 0.7 zoom 3.0 xalign 0.5 yalign 0.5    
        linear 0.7 zoom 2.9 xalign 0.5 yalign 0.6 
        linear 0.7 zoom 2.8 xalign 0.5 yalign 0.7
        linear 0.7 zoom 2.7 xalign 0.5 yalign 0.8
        linear 0.7 zoom 2.6 xalign 0.5 yalign 0.9
        linear 0.7 zoom 2.5 xalign 0.5 yalign 0.9
        linear 0.7 zoom 2.4 xalign 0.5 yalign 0.9
        linear 0.7 zoom 2.3 xalign 0.5 yalign 0.9
        linear 0.7 zoom 2.2 xalign 0.5 yalign 0.9
        linear 0.7 zoom 2.1 xalign 0.5 yalign 0.9
        linear 0.7 zoom 2.0 xalign 0.5 yalign 0.9
        linear 0.7 zoom 1.9 xalign 0.5 yalign 0.9 
    transform pr9_1:
        zoom 1.9 xalign 0.5 yalign 0.8
        linear 1.0 zoom 1.9 xalign 0.5 yalign 0.7    
        linear 1.0 zoom 1.9 xalign 0.5 yalign 0.8 
        repeat
    transform pr10_1:
        zoom 1.9 xalign 0.5 yalign 0.8
        linear 0.3 zoom 2.0 xalign 0.5 yalign 0.7    
        linear 0.3 zoom 2.1 xalign 0.5 yalign 0.6
        linear 0.3 zoom 2.2 xalign 0.5 yalign 0.5    
        linear 0.3 zoom 2.3 xalign 0.5 yalign 0.5   
        linear 0.3 zoom 2.4 xalign 0.5 yalign 0.5 
    transform pr11_1:
        zoom 2.4 xalign 0.5 yalign 0.5
        linear 0.3 zoom 2.5 xalign 0.5 yalign 0.5    
        linear 0.3 zoom 2.6 xalign 0.5 yalign 0.5
        linear 0.3 zoom 2.7 xalign 0.5 yalign 0.5    
        linear 0.3 zoom 2.8 xalign 0.5 yalign 0.5   
        linear 0.3 zoom 2.9 xalign 0.5 yalign 0.5      
    transform pr12_1:
        zoom 1.9 xalign 0.5 yalign 0.8  
    transform pr13_1:  
        zoom 1.9 xalign 0.5 yalign 0.8
        linear 1.07 zoom 1.9 xalign 0.5 yalign 0.7    
        linear 1.07 zoom 1.9 xalign 0.5 yalign 0.8 
        repeat      
    transform pr14_1:  
        zoom 1.9 xalign 0.5 yalign 0.8
        linear 0.07 zoom 2.0 xalign 0.5 yalign 0.6    
        linear 0.07 zoom 2.1 xalign 0.5 yalign 0.6     
        linear 0.07 zoom 2.2 xalign 0.5 yalign 0.6    
        linear 0.07 zoom 2.3 xalign 0.5 yalign 0.6 
        linear 0.07 zoom 2.4 xalign 0.5 yalign 0.6    
        linear 0.07 zoom 2.5 xalign 0.5 yalign 0.6 
        linear 0.07 zoom 2.6 xalign 0.5 yalign 0.6    
        linear 0.07 zoom 2.7 xalign 0.5 yalign 0.6
        linear 0.07 zoom 2.8 xalign 0.5 yalign 0.6    
        linear 0.07 zoom 2.9 xalign 0.5 yalign 0.6         
        linear 0.07 zoom 3.0 xalign 0.5 yalign 0.6    
        linear 0.07 zoom 3.1 xalign 0.5 yalign 0.6     
        linear 0.07 zoom 3.2 xalign 0.5 yalign 0.6    
        linear 0.07 zoom 3.3 xalign 0.5 yalign 0.6 
        linear 0.07 zoom 3.4 xalign 0.5 yalign 0.6    
        linear 0.07 zoom 3.5 xalign 0.5 yalign 0.6 
        linear 0.07 zoom 3.6 xalign 0.5 yalign 0.6    
        linear 0.07 zoom 3.7 xalign 0.5 yalign 0.6
        linear 0.07 zoom 3.8 xalign 0.5 yalign 0.6    
        linear 0.07 zoom 3.9 xalign 0.5 yalign 0.6
    transform pr15_1:  
        zoom 3.9 xalign 0.4 yalign 0.6
        linear 0.1 zoom 4.0 xalign 0.4 yalign 0.6    
        linear 0.1 zoom 4.1 xalign 0.4 yalign 0.6     
        linear 0.1 zoom 4.2 xalign 0.4 yalign 0.6    
        linear 0.1 zoom 4.3 xalign 0.4 yalign 0.6 
        linear 0.1 zoom 4.4 xalign 0.4 yalign 0.6    
        linear 0.1 zoom 4.5 xalign 0.4 yalign 0.6 
        linear 0.1 zoom 4.6 xalign 0.4 yalign 0.6    
        linear 0.1 zoom 4.7 xalign 0.4 yalign 0.6
        linear 0.1 zoom 4.8 xalign 0.4 yalign 0.6    
        linear 0.1 zoom 4.9 xalign 0.4 yalign 0.6         
    transform pr16_1:  
        zoom 4.9 xalign 0.5 yalign 0.6    
        linear 0.07 zoom 4.9 xalign 0.6 yalign 0.6        
    transform pr17_1:  
        zoom 4.9 xalign 0.4 yalign 0.6
        linear 0.5 zoom 4.9 xalign 0.5 yalign 0.6    
        linear 0.5 zoom 4.9 xalign 0.5 yalign 0.5     
        linear 0.5 zoom 4.9 xalign 0.5 yalign 0.4    
    transform pr18_1:  
        zoom 4.9 xalign 0.5 yalign 0.4
        linear 2.5 zoom 4.9 xalign 0.5 yalign 0.5    
        linear 2.5 zoom 4.9 xalign 0.5 yalign 0.4     
        repeat   
    transform pr19_1:  
        zoom 4.9 xalign 0.5 yalign 0.5
        linear 0.4 zoom 4.8 xalign 0.5 yalign 0.6    
        linear 0.4 zoom 4.7 xalign 0.5 yalign 0.7     
        linear 0.4 zoom 4.6 xalign 0.5 yalign 0.8    
        linear 0.4 zoom 4.5 xalign 0.5 yalign 0.9 
        linear 0.4 zoom 4.4 xalign 0.5 yalign 0.9    
        linear 0.4 zoom 4.3 xalign 0.5 yalign 0.9 
        linear 0.4 zoom 4.2 xalign 0.5 yalign 0.9    
        linear 0.4 zoom 4.1 xalign 0.5 yalign 0.9
        linear 0.4 zoom 4.0 xalign 0.5 yalign 0.9    
        linear 0.3 zoom 3.9 xalign 0.5 yalign 0.9         
        linear 0.3 zoom 3.8 xalign 0.5 yalign 0.9    
        linear 0.3 zoom 3.7 xalign 0.5 yalign 0.9     
        linear 0.3 zoom 3.6 xalign 0.5 yalign 0.9    
        linear 0.3 zoom 3.5 xalign 0.5 yalign 0.9 
        linear 0.3 zoom 3.4 xalign 0.5 yalign 0.9    
        linear 0.3 zoom 3.3 xalign 0.5 yalign 0.9 
        linear 0.3 zoom 3.2 xalign 0.5 yalign 0.9    
        linear 0.3 zoom 3.1 xalign 0.5 yalign 0.9
        linear 0.2 zoom 3.0 xalign 0.5 yalign 0.9    
        linear 0.2 zoom 2.9 xalign 0.5 yalign 0.9   
        linear 0.2 zoom 2.8 xalign 0.5 yalign 0.9    
        linear 0.2 zoom 2.7 xalign 0.5 yalign 0.9     
        linear 0.2 zoom 2.6 xalign 0.5 yalign 0.9    
        linear 0.2 zoom 2.5 xalign 0.5 yalign 0.9 
        linear 0.2 zoom 2.4 xalign 0.5 yalign 0.9    
        linear 0.1 zoom 2.3 xalign 0.5 yalign 0.9 
        linear 0.1 zoom 2.2 xalign 0.5 yalign 0.9    
        linear 0.1 zoom 2.1 xalign 0.5 yalign 0.9
        linear 0.1 zoom 2.0 xalign 0.5 yalign 0.9    
        linear 0.1 zoom 3.9 xalign 0.5 yalign 0.9         
        
    transform pr1_6:  
        zoom 2.5 xalign 0.5 yalign 0.2
    transform pr1_7:  
        zoom 2.5 xalign 0.5 yalign 0.2  
        linear 0.5 zoom 2.6 xalign 0.5 yalign 0.2
        linear 0.5 zoom 2.7 xalign 0.5 yalign 0.2    
        linear 0.5 zoom 2.8 xalign 0.5 yalign 0.2     
    transform pr1_8:  
        zoom 2.8 xalign 0.5 yalign 0.2  
        linear 0.5 zoom 2.7 xalign 0.5 yalign 0.2
        linear 0.5 zoom 2.6 xalign 0.5 yalign 0.2    
        linear 0.5 zoom 2.5 xalign 0.5 yalign 0.3             
        linear 0.5 zoom 2.4 xalign 0.5 yalign 0.3
        linear 0.5 zoom 2.3 xalign 0.5 yalign 0.3   
        linear 0.5 zoom 2.2 xalign 0.5 yalign 0.3  
        linear 0.5 zoom 2.1 xalign 0.5 yalign 0.3   
        linear 0.5 zoom 2.0 xalign 0.5 yalign 0.3     
        linear 0.5 zoom 1.9 xalign 0.5 yalign 0.3  
        linear 0.5 zoom 1.8 xalign 0.5 yalign 0.3   
        linear 0.5 zoom 1.7 xalign 0.5 yalign 0.3    
        linear 0.5 zoom 1.6 xalign 0.5 yalign 0.3    
        linear 0.5 zoom 1.5 xalign 0.5 yalign 0.3    

label test_neuroset""" + str(i) + """: 
""").encode('utf-8')
    subpart2 = re.split(r'Seed:.*', subprocess.check_output(cmdpath).decode('utf-8'))[1]
    if subpart2[-1] != "\"":
        subpart2 = subpart2[0:-2] + "\""
    subpart2 = subpart2.replace('chan', 'Chan')
    outputtext = (subpart.decode('utf-8') + "\n".join(re.split(r"\r\n", subpart2)))
    output.write(outputtext)
    output.close()
    print(i, "of", "50") 
