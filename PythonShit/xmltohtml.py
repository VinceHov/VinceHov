import os
for filename in os.listdir("C:/Users/User/lmao/"):
    if ".xml" in filename:
        os.rename("C:/Users/User/lmao/" + filename, "C:/Users/User/lmao/" + filename.split(".xml")[0] + ".html")