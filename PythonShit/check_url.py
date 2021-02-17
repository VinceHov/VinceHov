# import urllib2
import fnmatch
import os
import zipfile
import platform
platform = platform.system()
ahegao_path = "ahegao"
# if persistent.ahegao_path:
#     try:
#         findPath(persistent.ahegao_path, "_ahegao.png")
#     except:
#         persistent.ahegao_path = ""
# if not persistent.ahegao_path:
if platform == "Windows":
    def findPath(path, mode):
        matches = []
        matches.clear()
        for root, dirnames, filenames in os.walk(path):
            # print(root, dirnames, filenames)
            for filename in fnmatch.filter(filenames, '*' + mode):
                matches.append(os.path.join(root, filename))
        new_path = "/".join(matches[0].split("\\"))
        return new_path
            
    def findBase(ahegao_path):
        index = 0 
        new_path = ""
        for subfolder in ahegao_path.split("/"):
            if index < (len(ahegao_path.split("/")) - 3):
                new_path += subfolder + "/"
            index +=1
        new_path = new_path [0:-1]
        return new_path
    path = 'D:\\SteamLibrary\\steamapps\\common\\Everlasting Summer'
    rpyPath = 'sprite_ahegao.rpy'
    ahegaoPath = '_ahegao.png'
    try:
        new_path = findPath(path, ahegaoPath)
    except:
        new_path = findPath(path.split("common")[0] + "workshop\\content\\", ahegaoPath)
        # print(new_path)
                   
    try:
        ahegao_path = new_path.split('/Everlasting Summer/game/')[1]
    except: 
        # try:
        # print("/".join(path.split("\\")))
        ahegao_path = new_path.split('/workshop/content/')[1]
        ahegao_path = ahegao_path.split("/", maxsplit=2)[2]
        print(ahegao_path)




        # except:
            # rpyPath = findPath(path, rpyPath).split(rpyPath)[0][0:-1]
            # with open(rpyPath + "/ahegao.zip" ,'wb') as f:
            #     f.write(urllib2.urlopen("https://github.com/VinceHov/EverlastingSummer/blob/master/ahegao.zip?raw=true").read())
            #     f.close()
            
            # with zipfile.ZipFile(rpyPath + "/ahegao.zip", 'r') as zip_ref:
            #     zip_ref.extractall(rpyPath)
            #     try:
            #         ahegao_path = rpyPath.split('/Everlasting Summer/game/')[1]
            #     except:
            #         ahegao_path = rpyPath.split('/workshop/content/')[1]
            #         ahegao_path = "/".join(ahegao_path.split("/")[1:])
            #     ahegao_path += "/ahegao"
            #     persistent.ahegao_path = ahegao_path
            #     renpy.save_persistent()
            # os.remove(rpyPath + "/ahegao.zip")
        pass 
    ahegao_path = findBase(ahegao_path)