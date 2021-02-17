import os
for filename in os.listdir("C:/TEST_SECTION"):
	filename_new = filename.split(".xml")
	os.rename("C:/TEST_SECTION/" + filename, "C:/TEST_SECTION/" + filename_new[0] + ".html")