# -*- coding: utf-8 -*-
# test = \\\\"Р—РђРћ \\\\\"РќРР¦ \\\\".encode('cp1251')

import re
# reg = b'\xd0'
test= b' \xe2\x80\x99\xd1\x81\xd0\xba\xd0\xb0\xd0\xb6\xd0\xb8 \xd0\xbc\xd0\xbd\xd0\xb5\xe2\x80\x99.<br><br>\xd0\xa1\xd0\xbe\xd1\x82\xd1\x80\xd1\x83\xd0\xb4\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb8 \xd0\xbd\xd0\xb0 \xc2\xab\xd1\x85\xd0\xbe\xd1\x80\xd0\xbe\xd1\x88\xd0\xbe\xc2\xbb \xd0\xbe\xd1\x86\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xbb\xd0\xb8 HR \xd1\x81\xd0\xb5\xd1\x80\xd0\xb2\xd0\xb8\xd1\x81\xd1\x8b (\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81 2010 \xd0\xb3\xd0\xbe\xd0\xb4\xd0\xb0 - TS CIS 7,0 \xd0\xb1\xd0\xb0\xd0\xbb\xd0\xbe\xd0\xb2, \xd0\xb2 \xd1\x81\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbd\xd0\xb5\xd0\xbc \xd0\xbf\xd0\xbe \xd0\xba\xd0\xbe\xd1\x80\xd0\xbf\xd0\xbe\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8 - 5,9). <br>\xd0\xa0\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb0 \xd1\x81 HR \xd0\xba\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb4\xd0\xbe\xd0\xb9, \xd0\xbd\xd0\xb0\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xb0\xd1\x8f \xd0\xbd\xd0\xb0 \xd0\xbf\xd0\xbe\xd0\xb2\xd1\x8b\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x83\xd1\x80\xd0\xbe\xd0\xb2\xd0\xbd\xd1\x8f \xd1\x81\xd0\xb5\xd1\x80\xd0\xb2\xd0\xb8\xd1\x81\xd0\xb0 \xd0\xb8 \xd0\xb2\xd0\xbd\xd0\xb5\xd0\xb4\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 3-\xd1\x85 \xd1\x83\xd1\x80\xd0\xbe\xd0\xb2\xd0\xbd\xd0\xb5\xd0\xb2\xd0\xbe\xd0\xb9 \xd1\x81\xd1\x82\xd1\x80\xd1\x83\xd0\xba\xd1\x82\xd1\x83\xd1\x80\xd1\x8b \xd0\xbe\xd1\x82\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb0: <br>1.\n HR \xd0\x91\xd0\xb8\xd0\xb7\xd0\xbd\xd0\xb5\xd1\x81 \xd0\xbf\xd0\xb0\xd1\x80\xd1\x82\xd0\xbd\xd0\xb5\xd1\x80 \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbb\xd0\xb0\xd0\xb3\xd0\xb0\xd0\xb5\xd1\x82 \xd0\xa2\xd0\xbe\xd0\xbf - \xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xb4\xd0\xb6\xd0\xb5\xd1\x80\xd1\x83 \xd1\x81\xd0\xbe\xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xb8 \n\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xbd\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x80 HR \xd1\x81\xd0\xb5\xd1\x80\xd0\xb2\xd0\xb8\xd1\x81\xd0\xbe\xd0\xb2, \xd0\xb1\xd0\xb0\xd0\xb7\xd0\xb8\xd1\x80\xd1\x83\xd1\x8e\xd1\x89\xd0\xb8\xd0\xb9\xd1\x81\xd1\x8f \xd0\xbd\xd0\xb0 \xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xb4\xd0\xb6\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb5: \xd0\xba\xd0\xb0\xd0\xb4\xd1\x80\xd0\xbe\xd0\xb2\xd1\x8b\xd1\x85\n \xd1\x80\xd0\xb5\xd1\x81\xd1\x83\xd1\x80\xd1\x81\xd0\xbe\xd0\xb2, \xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb9, \xd0\xb2\xd0\xbe\xd0\xb7\xd0\xbd\xd0\xb0\xd0\xb3\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb9, \xd1\x86\xd0\xb5\xd0\xbb\xd0\xb5\xd0\xb9, \xd0\xb4\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb9, \xd1\x83\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb8 \n\xd1\x82\xd0\xb0\xd0\xbb\xd0\xb0\xd0\xbd\xd1\x82\xd0\xb0\xd0\xbc\xd0\xb8, HR \xd0\xb1\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb4\xd0\xbe\xd0\xbc. \xd0\x9e\xd1\x81\xd1\x83\xd1\x89\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbb\xd1\x8f\xd0\xb5\xd1\x82 HR \xd0\xba\xd0\xbe\xd0\xbd\xd1\x81\xd0\xb0\xd0\xbb\xd1\x82\xd0\xb8\xd0\xbd\xd0\xb3, \xd1\x83\xd1\x87\xd0\xb0\xd1\x81\xd1\x82\xd0\xb2\xd1\x83\xd0\xb5\xd1\x82 \xd0\xb2 \n\xd0\xba\xd0\xbe\xd0\xbb\xd0\xbb\xd0\xb5\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd1\x8b\xd1\x85  \xd0\xbf\xd0\xb5\xd1\x80\xd0\xb5\xd0\xb3\xd0\xbe\xd0\xb2\xd0\xbe\xd1\x80\xd0\xb0\xd1\x85, \xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb5\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb8 \xd0\xba\xd0\xbe\xd0\xbd\xd1\x84\xd0\xbb\xd0\xb8\xd0\xba\xd1\x82\xd0\xbe\xd0\xb2. \xd0\x97\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xbc\xd0\xb0\xd0\xb5\xd1\x82\xd1\x81\xd1\x8f \xd0\xb2\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xb0\xd0\xbc\xd0\xb8 \n\xd0\xb4\xd0\xb8\xd1\x81\xd1\x86\xd0\xb8\xd0\xbf\xd0\xbb\xd0\xb8\xd0\xbd\xd0\xb0\xd1\x80\xd0\xbd\xd1\x8b\xd1\x85 \xd0\xb2\xd0\xb7\xd1\x8b\xd1\x81\xd0\xba\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb9, \xd0\xbf\xd0\xb5\xd1\x80\xd0\xb5\xd1\x81\xd0\xbc\xd0\xbe\xd1\x82\xd1\x80\xd0\xbe\xd0\xbc \xd0\xbc\xd0\xbe\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb5\xd0\xb9 \xd0\xbf\xd1\x80\xd0\xb5\xd0\xbc\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f, \n\xd0\xb3\xd1\x80\xd0\xb5\xd0\xb9\xd0\xb4\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5\xd0\xbc, \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xb3\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb2\xd0\xba\xd0\xbe\xd0\xb9 \xd0\xba \xd1\x80\xd0\xb5\xd1\x81\xd1\x82\xd1\x80\xd1\x83\xd0\xba\xd1\x82\xd1\x83\xd1\x80\xd0\xb8\xd0\xb7\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8, \xd0\xb1\xd0\xbb\xd0\xb8\xd0\xb6\xd0\xb0\xd0\xb9\xd1\x88\xd0\xb8\xd0\xbc \xd0\xba\xd1\x80\xd1\x83\xd0\xbf\xd0\xbd\xd1\x8b\xd0\xbc \n\xd1\x81\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xba\xd0\xb0\xd0\xbc, \xd0\xb2\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xb0\xd0\xbc\xd0\xb8 \xd0\xbc\xd0\xbe\xd1\x82\xd0\xb8\xd0\xb2\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8 \xd0\xb8 \xd1\x80\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb8\xd1\x82\xd0\xb8\xd1\x8f \xd0\xba\xd0\xb0\xd1\x80\xd1\x8c\xd0\xb5\xd1\x80\xd1\x8b, \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb5\xd0\xba\xd1\x82\xd0\xbe\xd0\xbc \xd0\xba\xd0\xbe\xd1\x80\xd0\xbf\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd0\xbe\xd0\xb9 \n\xd0\xb1\xd0\xb0\xd0\xb7\xd1\x8b \xd0\xb7\xd0\xbd\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb9. \xd0\x9a\xd0\xbe\xd0\xbd\xd1\x82\xd1\x80\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x80\xd1\x83\xd0\xb5\xd1\x82 \xc2\xab\xd0\xbd\xd0\xb0\xd1\x81\xd1\x82\xd1\x80\xd0\xbe\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f\xc2\xbb, \xd1\x83\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xbd\xd1\x8c \xd0\xbb\xd0\xb8\xd0\xb4\xd0\xb5\xd1\x80\xd1\x81\xd1\x82\xd0\xb2\xd0\xb0. \xd0\xa1\xd0\xb0\xd0\xbc \n\xd0\xbe\xd1\x81\xd1\x83\xd1\x89\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbb\xd1\x8f\xd0\xb5\xd1\x82 \xd1\x85\xd0\xb5\xd0\xb4\xd1\x85\xd0\xb0\xd0\xbd\xd1\x82\xd0\xb8\xd0\xbd\xd0\xb3, \xd0\xb0 \xd1\x82\xd0\xb0\xd0\xba \xd0\xb6\xd0\xb5 \xd0\xb2\xd0\xb5\xd0\xb4\xd0\xb5\xd1\x82 \xd0\xbb\xd0\xb8\xd1\x87\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb0 \xd0\xb8 \xd0\xbe\xd0\xb1\xd1\x81\xd0\xbb\xd1\x83\xd0\xb6\xd0\xb8\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x82\xd0\xbe\xd0\xbf -\n \xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xb4\xd0\xb6\xd0\xb5\xd1\x80\xd0\xbe\xd0\xb2 \xd0\xbf\xd0\xbe \xd0\xb2\xd1\x81\xd0\xb5\xd0\xbc HR \xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb7\xd0\xb0\xd0\xba\xd1\x86\xd0\xb8\xd1\x8f\xd0\xbc. \xd0\xa4\xd0\xbe\xd1\x80\xd0\xbc\xd1\x83\xd0\xbb\xd0\xb8\xd1\x80\xd1\x83\xd0\xb5\xd1\x82 \xd0\xb7\xd0\xb0\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8 \xd0\xb8 \xd0\xba\xd0\xbe\xd0\xbd\xd1\x82\xd1\x80\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x80\xd1\x83\xd0\xb5\xd1\x82 \n\xd0\xba\xd0\xb0\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe HR \xd1\x81\xd0\xb5\xd1\x80\xd0\xb2\xd0\xb8\xd1\x81\xd0\xbe\xd0\xb2, \xd0\xbe\xd0\xbf\xd1\x82\xd0\xb8\xd0\xbc\xd0\xb8\xd0\xb7\xd0\xb8\xd1\x80\xd1\x83\xd0\xb5\xd1\x82 \xd0\xb3\xd0\xbe\xd0\xb4\xd0\xbe\xd0\xb2\xd1\x83\xd1\x8e \xd0\xb7\xd0\xb0\xd0\xb3\xd1\x80\xd1\x83\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c \xd1\x81\xd0\xbe\xd1\x82\xd1\x80\xd1\x83\xd0\xb4\xd0\xbd\xd0\xb8\xd0\xba\xd0\xbe\xd0\xb2 HR \n\xd0\xbe\xd1\x82\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb0. <br>2. \xd0\xa1\xd1\x82\xd0\xb0\xd1\x80\xd1\x88\xd0\xb8\xd0\xb9 \xd1\x81\xd0\xbf\xd0\xb5\xd1\x86\xd0\xb8\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x81\xd1\x82 \xd1\x86\xd0\xb5\xd0\xbd\xd1\x82\xd1\x80\xd0\xb0 HR \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb5\xd1\x82\xd0\xb5\xd0\xbd\xd1\x86\xd0\xb8\xd0\xb9 \xd0\xb0\xd0\xb4\xd0\xb0\xd0\xbf\xd1\x82\xd0\xb8\xd1\x80\xd1\x83\xd0\xb5\xd1\x82 \xd0\xb8 \n\xd0\xbe\xd0\xb1\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xbb\xd1\x8f\xd0\xb5\xd1\x82 HR \xd0\xbf\xd1\x80\xd0\xbe\xd1\x86\xd0\xb5\xd1\x81\xd1\x81\xd1\x8b, \xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x82\xd0\xb8\xd0\xba\xd0\xb8, \xd0\xbe\xd1\x82\xd1\x87\xd0\xb5\xd1\x82\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c, HR IT \xd1\x81\xd0\xb8\xd1\x81\xd1\x82\xd0\xb5\xd0\xbc\xd1\x8b; \xd0\xbe\xd1\x82\xd0\xb2\xd0\xb5\xd1\x87\xd0\xb0\xd0\xb5\xd1\x82 \xd0\xb7\xd0\xb0 \n\xd0\xbe\xd0\xb4\xd0\xbd\xd0\xbe \xd0\xb8\xd0\xb7 HR \xd0\xbd\xd0\xb0\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb9, \xd0\xbd\xd0\xb0\xd0\xbf\xd1\x80\xd0\xb8\xd0\xbc\xd0\xb5\xd1\x80, \xd0\xb7\xd0\xb0 \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xb1\xd0\xbe\xd1\x80 \xd0\xb8 \xd1\x80\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb8\xd1\x82\xd0\xb8\xd0\xb5 \xd0\xb8\xd0\xbb\xd0\xb8 \xd0\xb7\xd0\xb0 \xd0\xba\xd0\xb0\xd0\xb4\xd1\x80\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb5 \n\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5.<br>\xd0\x9e\xd0\xb1\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xbb\xd1\x8f\xd0\xb5\xd1\x82 \xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd0\xba\xd0\xb8 \xd1\x81\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8, \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb0\xd0\xb5\xd1\x82 \xd1\x81 \xd0\xb3\xd0\xbe\xd1\x81\xd0\xbe\xd1\x80\xd0\xb3\xd0\xb0\xd0\xbd\xd0\xb0\xd0\xbc\xd0\xb8. \xd0\x9e\xd0\xb1\xd1\x83\xd1\x87\xd0\xb0\xd0\xb5\xd1\x82 \xd0\xb8 \xd0\xba\xd0\xbe\xd0\xbd\xd1\x82\xd1\x80\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x80\xd1\x83\xd0\xb5\xd1\x82 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x83 \xd0\xbc\xd0\xbb\xd0\xb0\xd0\xb4\xd1\x88\xd0\xb8\xd1\x85 \xd1\x81\xd0\xbf\xd0\xb5\xd1\x86\xd0\xb8\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x81\xd1\x82\xd0\xbe\xd0\xb2. <br>3.\n \xd0\x9c\xd0\xbb\xd0\xb0\xd0\xb4\xd1\x88\xd0\xb8\xd0\xb9 \xd1\x81\xd0\xbf\xd0\xb5\xd1\x86\xd0\xb8\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x81\xd1\x82 HR \xd1\x81\xd0\xb5\xd1\x80\xd0\xb2\xd0\xb8\xd1\x81 \xd1\x86\xd0\xb5\xd0\xbd\xd1\x82\xd1\x80\xd0\xb0 \xd0\xbe\xd1\x81\xd1\x83\xd1\x89\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbb\xd1\x8f\xd0\xb5\xd1\x82 \xd1\x81\xd1\x82\xd0\xb0\xd0\xbd\xd0\xb4\xd0\xb0\xd1\x80\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb5 HR \n\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb7\xd0\xb0\xd0\xba\xd1\x86\xd0\xb8\xd0\xb8: \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xb1\xd0\xbe\xd1\x80 (\xd1\x80\xd0\xb5\xd1\x81\xd0\xb5\xd1\x87\xd0\xb8\xd0\xbd\xd0\xb3), \xd0\xbe\xd0\xb1\xd1\x83\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5, \xd0\x9a\xd0\x94\xd0\x9f, \xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x85\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5, \xd0\xbe\xd1\x82\xd1\x87\xd0\xb5\xd1\x82\xd1\x8b, \n\xd0\xb3\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb2\xd0\xb8\xd1\x82 \xd0\xba\xd0\xbe\xd0\xbf\xd0\xb8\xd0\xb8 \xd0\xb4\xd0\xbe\xd0\xba\xd1\x83\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xbe\xd0\xb2, \xd1\x81\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb8 \xd0\xb8 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82 \xd0\xb4\xd1\x80\xd1\x83\xd0\xb3\xd0\xb8\xd0\xb5 \xd1\x80\xd0\xb5\xd0\xb3\xd0\xbb\xd0\xb0\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5 \n\xd0\xbf\xd1\x80\xd0\xbe\xd1\x86\xd0\xb5\xd0\xb4\xd1\x83\xd1\x80\xd1\x8b. <br><br>T-Systems CIS \xd1\x81\xd1\x82\xd0\xb0\xd0\xbb \xd0\xbf\xd1\x80\xd0\xb8\xd0\xb7\xd0\xbd\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xbc \xd1\x87\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xbe\xd0\xbc \xd0\xbc\xd0\xb5\xd0\xb6\xd0\xb4\xd1\x83\xd0\xbd\xd0\xb0\xd1\x80\xd0\xbe\xd0\xb4\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xbe\xd0\xb1\xd1\x8a\xd0\xb5\xd0\xb4\xd0\xb8\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f HR\xd0\xbe\xd0\xb2 \xd0\xba\xd0\xbe\xd1\x80\xd0\xbf\xd0\xbe\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8 \xd0\xb1\xd0\xbb\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x80\xd1\x8f: <br>- \xd0\xb2\xd0\xbd\xd0\xb5\xd0\xb4\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8e \xd0\xbc\xd0\xb5\xd0\xb6\xd0\xb4\xd1\x83\xd0\xbd\xd0\xb0\xd1\x80\xd0\xbe\xd0\xb4\xd0\xbd\xd1\x8b\xd1\x85 HR \xd0\xbf\xd1\x80\xd0\xbe\xd1\x86\xd0\xb5\xd1\x81\xd1\x81\xd0\xbe\xd0\xb2, S-OX, compliance, HR Due Diligence, \xd1\x83\xd1\x87\xd0\xb0\xd1\x81\xd1\x82\xd0\xb8\xd1\x8e \xd0\xb2 \xd1\x82\xd1\x80\xd0\xb5\xd1\x85 \xd0\xbf\xd0\xb8\xd0\xbb\xd0\xbe\xd1\x82\xd0\xbd\xd1\x8b\xd1\x85 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb5\xd0\xba\xd1\x82\xd0\xb0\xd1\x85;<br>-\n \xd0\xb0\xd0\xb4\xd0\xb0\xd0\xbf\xd1\x82\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8 \xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x82\xd0\xb8\xd0\xba \xd1\x88\xd1\x82\xd0\xb0\xd0\xb1 \xd0\xba\xd0\xb2\xd0\xb0\xd1\x80\xd1\x82\xd0\xb8\xd1\x80\xd1\x8b \xd1\x81 \xd1\x83\xd1\x87\xd0\xb5\xd1\x82\xd0\xbe\xd0\xbc \xd0\xbb\xd0\xbe\xd0\xba\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd1\x85 \xd0\xbf\xd0\xbe\xd1\x82\xd1\x80\xd0\xb5\xd0\xb1\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd0\xb5\xd0\xb9 \xd0\xb1\xd0\xb8\xd0\xb7\xd0\xbd\xd0\xb5\xd1\x81\xd0\xb0\n \xd0\xb8 \xd0\xba\xd0\xbe\xd0\xbd\xd0\xba\xd1\x83\xd1\x80\xd0\xb5\xd0\xbd\xd1\x82\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xbe\xd0\xba\xd1\x80\xd1\x83\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f, \xd1\x81 \xd1\x83\xd1\x87\xd0\xb5\xd1\x82\xd0\xbe\xd0\xbc \xd1\x80\xd0\xbe\xd1\x81\xd1\x81\xd0\xb8\xd0\xb9\xd1\x81\xd0\xba\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb8 \xd0\xbc\xd0\xb5\xd0\xb6\xd0\xb4\xd1\x83\xd0\xbd\xd0\xb0\xd1\x80\xd0\xbe\xd0\xb4\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \n\xd0\xb7\xd0\xb0\xd0\xba\xd0\xbe\xd0\xbd\xd0\xbe\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd1\x81\xd1\x82\xd0\xb2\xd0\xb0; <br>- \xd1\x83\xd1\x87\xd0\xb0\xd1\x81\xd1\x82\xd0\xb8\xd1\x8e \xd0\xb2 \xd0\xb3\xd0\xbb\xd0\xbe\xd0\xb1\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd1\x85 HR \xd0\xba\xd0\xbe\xd0\xbd\xd1\x84\xd0\xb5\xd1\x80\xd0\xb5\xd0\xbd\xd1\x86\xd0\xb8\xd1\x8f\xd1\x85, \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8e C&amp;B \xd0\xb2\xd0\xbe\xd1\x80\xd0\xba\xd1\x88\xd0\xbe\xd0\xbf\xd0\xb0 \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xba\xd0\xbe\xd0\xbb\xd0\xbb\xd0\xb5\xd0\xb3 \xd0\xb8\xd0\xb7 \xd0\xb1\xd0\xbe\xd0\xbb\xd0\xb5\xd0\xb5 \xd1\x87\xd0\xb5\xd0\xbc 40 \xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd.<br><br>\xd0\x94\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8\xd0\xb3\xd0\xbd\xd1\x83\xd1\x82 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb5\xd1\x81\xd1\x81 \xd0\xb2\xd0\xbe \xd0\xb2\xd0\xbd\xd0\xb5\xd0\xb4\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb8 \xd0\xa1\xd1\x82\xd1\x80\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xb8\xd0\xb8 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb8 (\xd0\x9e\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81 \xd1\x81\xd0\xbe\xd1\x82\xd1\x80\xd1\x83\xd0\xb4\xd0\xbd\xd0\xb8\xd0\xba\xd0\xbe\xd0\xb2 2011 \xd0\xb3\xd0\xbe\xd0\xb4\xd0\xb0, 55% \xd0\xb8 39%) \xd0\xb2 \xd1\x80\xd0\xb5\xd0\xb7\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd1\x82\xd0\xb5:<br>- \xd0\xbf\xd1\x80\xd0\xb8\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xb2 \xd0\xba\xd0\xb0\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xb5 \xd0\xb1\xd0\xb0\xd0\xb7\xd0\xb8\xd1\x81\xd0\xb0 \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xb2\xd1\x81\xd0\xb5\xd1\x85 HR \xd0\xbf\xd1\x80\xd0\xbe\xd1\x86\xd0\xb5\xd1\x81\xd1\x81\xd0\xbe\xd0\xb2 \xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xb8 \xd0\xbe\xd1\x80\xd0\xb8\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xb9 \xd0\xbc\xd0\xbe\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb8 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb5\xd1\x82\xd0\xb5\xd0\xbd\xd1\x86\xd0\xb8\xd0\xb9;<br>- \xd0\xb2\xd0\xbd\xd0\xb5\xd0\xb4\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd1\x86\xd0\xb5\xd0\xbd\xd1\x82\xd1\x80\xd0\xb0 \xd0\xbe\xd1\x86\xd0\xb5\xd0\xbd\xd0\xba\xd0\xb8 \xd0\xbf\xd0\xbe \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb5\xd1\x82\xd0\xb5\xd0\xbd\xd1\x86\xd0\xb8\xd1\x8f\xd0\xbc \xd0\xb8 \xd0\xbc\xd0\xb5\xd1\x82\xd0\xbe\xd0\xb4\xd0\xb8\xd0\xba\xd0\xb8 360\xc2\xb0 \xd0\xb4\xd0\xbb\xd1\x8f \xd1\x80\xd1\x83\xd0\xba\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd0\xb9. <br><br>\xd0\xa3\xd0\xb4\xd0\xbe\xd0\xb2\xd0\xbb\xd0\xb5\xd1\x82\xd0\xb2\xd0\xbe\xd1\x80\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c \xd1\x81\xd0\xbe\xd1\x82\xd1\x80\xd1\x83\xd0\xb4\xd0\xbd\xd0\xb8\xd0\xba\xd0\xbe\xd0\xb2 \xd0\xbf\xd0\xbe\xd0\xb2\xd1\x8b\xd1\x81\xd0\xb8\xd0\xbb\xd0\xb0\xd1\x81\xd1\x8c \xd0\xbd\xd0\xb0 8% (\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81 2011 \xd0\xb3\xd0\xbe\xd0\xb4\xd0\xb0) \xd0\xb7\xd0\xb0 \xd1\x81\xd1\x87\xd0\xb5\xd1\x82: <br>- \xd0\xb2\xd0\xbd\xd0\xb8\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xba \xd0\xbd\xd0\xb5\xd0\xbe\xd1\x84\xd0\xb8\xd1\x86\xd0\xb8\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xbc \xd0\xbb\xd0\xb8\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb0\xd0\xbc, \xd0\xb2\xd0\xbe\xd0\xb2\xd0\xbb\xd0\xb5\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd1\x82\xd0\xbe\xd0\xbf-\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xb4\xd0\xb6\xd0\xb5\xd1\x80\xd0\xbe\xd0\xb2 \xd0\xb4\xd0\xbb\xd1\x8f \xd1\x83\xd1\x87\xd0\xb0\xd1\x81\xd1\x82\xd0\xb8\xd1\x8f \xd0\xb2 \xd1\x80\xd0\xb5\xd0\xb3\xd1\x83\xd0\xbb\xd1\x8f\xd1\x80\xd0\xbd\xd1\x8b\xd1\x85 \xd1\x81\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f\xd1\x85 \xd0\xbe\xd1\x82\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xbe\xd0\xb2;<br>- \xd0\xba\xd0\xbe\xd1\x80\xd0\xbf\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd1\x8b\xd1\x85 \xd0\xbc\xd0\xb5\xd1\x80\xd0\xbe\xd0\xbf\xd1\x80\xd0\xb8\xd1\x8f\xd1\x82\xd0\xb8\xd0\xb9, \xd1\x82\xd0\xb8\xd0\xbc-\xd0\xb1\xd0\xb8\xd0\xbb\xd0\xb4\xd0\xb8\xd0\xbd\xd0\xb3\xd0\xbe\xd0\xb2, \xd0\xb2\xd0\xbd\xd1\x83\xd1\x82\xd1\x80\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xb8\xd1\x85 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbc\xd1\x83\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb9 (\xd0\xba\xd0\xbe\xd1\x80\xd0\xbf\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd0\xb0\xd1\x8f \xd0\xb3\xd0\xb0\xd0\xb7\xd0\xb5\xd1\x82\xd0\xb0, \xd0\xb8\xd0\xbd\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb5\xd1\x82 \xd0\xbf\xd0\xbe\xd1\x80\xd1\x82\xd0\xb0\xd0\xbb); <br>- \xd1\x80\xd0\xb0\xd1\x81\xd1\x88\xd0\xb8\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xb2\xd0\xbe\xd0\xb7\xd0\xbc\xd0\xbe\xd0\xb6\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd0\xb5\xd0\xb9 \xd0\xbf\xd1\x80\xd0\xbe\xd1\x84\xd0\xb5\xd1\x81\xd1\x81\xd0\xb8\xd0\xbe\xd0\xbd\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb8 \xd0\xba\xd0\xb0\xd1\x80\xd1\x8c\xd0\xb5\xd1\x80\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd1\x80\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0, \xd0\xbd\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb4\xd0\xb8\xd0\xb7\xd0\xb0\xd0\xb9\xd0\xbd\xd0\xb0 \xd0\xbe\xd1\x84\xd0\xb8\xd1\x81\xd0\xb0, \xd0\xb7\xd0\xb0\xd0\xba\xd1\x83\xd0\xbf\xd0\xba\xd0\xb8 \xd1\x82\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb0\xd0\xb6\xd0\xb5\xd1\x80\xd0\xbe\xd0\xb2 \xd0\xb8 \xd0\xbe\xd1\x82\xd0\xba\xd1\x80\xd1\x8b\xd1\x82\xd0\xb8\xd1\x8f \xd0\xbd\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xba\xd0\xb0\xd1\x84\xd0\xb5.\n\t\t\t                    </dd>\n\t\t\t                  \n\t\t\t                    <dt class="b-resume-pinfo-label">\n\t\t\t\t                    <span class="b-resume-pinfo-exp-date">09.2007 -\n\t\t\t                      \n\t\t\t                        12.2009\n\t\t\t                        \n\t\t\t                      </span>,\n\t\t\t\t                    <span class="b-resume-pinfo-org">\xd0\x9c\xd0\xbe\xd1\x81\xd0\xba\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd1\x80\xd1\x86-\xd0\xbb\xd0\xb8\xd0\xb7\xd0\xb8\xd0\xbd\xd0\xb3 (\xd0\xbb\xd0\xb8\xd0\xb7\xd0\xb8\xd0\xbd\xd0\xb3 \xd0\xb8 \xd1\x81\xd1\x82\xd1\x80\xd0\xbe\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb0\xd1\x8f \xd1\x81\xd0\xbf\xd0\xb5\xd1\x86\xd1\x82\xd0\xb5\xd1\x85\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb0, 200 \xd1\x81\xd0\xbe\xd1\x82\xd1\x80\xd1\x83\xd0\xb4\xd0\xbd\xd0\xb8\xd0\xba\xd0\xbe\xd0\xb2, 7 \xd0\xbe\xd1\x84\xd0\xb8\xd1\x81\xd0\xbe\xd0\xb2)</span><br>\n\t\t\t\t                    \n\t\t\t\t                      <div class="b-resume-pinfo-industry">\xd0\x91\xd0\xb0\xd0\xbd\xd0\xba\xd0\xb8/\xd0\xba\xd1\x80\xd0\xb5\xd0\xb4\xd0\xb8\xd1\x82\xd1\x8b/\xd0\xb8\xd0\xbd\xd0\xb2\xd0\xb5\xd1\x81\xd1\x82\xd0\xb8\xd1\x86\xd0\xb8\xd0\xb8/\xd0\xbb\xd0\xb8\xd0\xb7\xd0\xb8\xd0\xbd\xd0\xb3</div>\n\t\t\t\t                    \n\t\t\t\t                    <strong>\xd0\x94\xd0\xb8\xd1\x80\xd0\xb5\xd0\xba\xd1\x82\xd0\xbe\xd1\x80 \xd0\xbf\xd0\xbe \xd0\xbf\xd0\xb5\xd1\x80\xd1\x81\xd0\xbe\xd0\xbd\xd0\xb0\xd0\xbb\xd1\x83, \xd1\x81 \xd0\x9e\xd0\xba\xd1\x82\xd1\x8f\xd0\xb1\xd1\x80\xd1\x8f 2008 \xd0\xbf\xd0\xbe \xd1\x81\xd0\xbe\xd0\xb2\xd0\xbc\xd0\xb5\xd1\x81\xd1\x82\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd1\x81\xd1\x82\xd0\xb2\xd1\x83</strong>\n\t\t\t                    </dt>\n\t\t\t                    <dd class="b-resume-pinfo-value">\n\t\t\t                      \n\t\t\t                      \xd0\x9e\xd1\x81\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xb4\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f: \xd0\xbf\xd0\xbe\xd1\x81\xd1\x82\xd1\x80\xd0\xbe\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb2\xd1\x81\xd0\xb5\xd1\x85 HR \n\xd0\xbf\xd1\x80\xd0\xbe\xd1\x86\xd0\xb5\xd1\x81\xd1\x81\xd0\xbe\xd0\xb2 \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xbb\xd0\xb8\xd0\xb7\xd0\xb8\xd0\xbd\xd0\xb3\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb9 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb8 \xd0\xb8 \xd0\xbd\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x80 \xd0\xbf\xd0\xb5\xd1\x80\xd1\x81\xd0\xbe\xd0\xbd\xd0\xb0\xd0\xbb\xd0\xb0 \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xb4\xd0\xb8\xd0\xbb\xd0\xb5\xd1\x80\xd0\xb0 \xd0\xba\xd0\xb8\xd1\x82\xd0\xb0\xd0\xb9\xd1\x81\xd0\xba\xd0\xbe\xd0\xb9\n \xd1\x81\xd0\xbf\xd0\xb5\xd1\x86\xd1\x82\xd0\xb5\xd1\x85\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb8 \xd1\x81 "0". \xd0\xa3\xd1\x81\xd0\xbf\xd0\xb5\xd1\x88\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xb7\xd0\xb0\xd0\xb2\xd0\xb5\xd1\x80\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd1\x81\xd1\x83\xd0\xb4\xd0\xb5\xd0\xb1\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xbf\xd1\x80\xd0\xbe\xd1\x86\xd0\xb5\xd1\x81\xd1\x81\xd0\xb0 \xd1\x81 \xd0\xb1\xd1\x8b\xd0\xb2\xd1\x88\xd0\xb8\xd0\xbc \n\xd1\x81\xd0\xbe\xd1\x82\xd1\x80\xd1\x83\xd0\xb4\xd0\xbd\xd0\xb8\xd0\xba\xd0\xbe\xd0\xbc. \xd0\x9c\xd0\xb8\xd0\xbd\xd0\xb8\xd0\xbc\xd0\xb8\xd0\xb7\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f \xd1\x80\xd0\xb8\xd1\x81\xd0\xba\xd0\xbe\xd0\xb2 \xd0\xb2\xd0\xbe \xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd1\x80\xd0\xb5\xd0\xbe\xd1\x80\xd0\xb3\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb7\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8 \xd0\xbf\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb5 \xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb0 \n\xd1\x84\xd0\xb8\xd0\xbd\xd0\xb0\xd0\xbd\xd1\x81\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xba\xd1\x80\xd0\xb8\xd0\xb7\xd0\xb8\xd1\x81\xd0\xb0.\n\t\t\t                    </dd>\n\t\t\t                  \n\t\t\t                    <dt class="b-resume-pinfo-label">\n\t\t\t\t                    <span class="b-resume-pinfo-exp-date">08.2005 -\n\t\t\t                      \n\t\t\t                        08.2007\n\t\t\t                        \n\t\t\t                      </span>,\n\t\t\t\t                    <span class="b-resume-pinfo-org">Nicko Travel Group (\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb9 \xd1\x82\xd1\x83\xd1\x80\xd0\xb8\xd0\xb7\xd0\xbc, \xd0\xb2\xd0\xb8\xd0\xb7\xd1\x8b, \xd0\xbf\xd1\x80\xd0\xb8\xd0\xb3\xd0\xbb\xd0\xb0\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xb8 \xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb5\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xbd\xd0\xb0 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x83, \xd0\xba\xd0\xbe\xd0\xbd\xd1\x84\xd0\xb5\xd1\x80\xd0\xb5\xd0\xbd\xd1\x86\xd0\xb8\xd0\xb8, VIP \xd1\x82\xd1\x83\xd1\x80\xd1\x8b, 6 \xd0\xbe\xd1\x84\xd0\xb8\xd1\x81\xd0\xbe\xd0\xb2, 350 \xd1\x81\xd0\xbe\xd1\x82\xd1\x80\xd1\x83\xd0\xb4\xd0\xbd\xd0\xb8\xd0\xba\xd0\xbe\xd0\xb2))</span><br>\n\t\t\t\t                    \n\t\t\t\t                      <div class="b-resume-pinfo-industry">\xd0\xa2\xd1\x83\xd1\x80\xd0\xb8\xd0\xb7\xd0\xbc/\xd0\xb3\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x86\xd1\x8b/\xd1\x80\xd0\xb5\xd1\x81\xd1\x82\xd0\xbe\xd1\x80\xd0\xb0\xd0\xbd\xd1\x8b</div>\n\t\t\t\t                    \n\t\t\t\t                    <strong>\xd0\xa0\xd1\x83\xd0\xba\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c \xd0\xbe\xd1\x82\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb0 \xd0\xbf\xd0\xb5\xd1\x80\xd1\x81\xd0\xbe\xd0\xbd\xd0\xb0\xd0\xbb\xd0\xb0, \xd1\x82\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xbd\xd0\xb3 \xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xb4\xd0\xb6\xd0\xb5\xd1\x80 \xd0\xb4\xd0\xbe \xd0\x98\xd1\x8e\xd0\xbb\xd1\x8f 2006.</strong>\n\t\t\t                    </dt>\n\t\t\t                    <dd class="b-resume-pinfo-value">\n\t\t\t                      \n\t\t\t                      \xd0\x9e\xd1\x81\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xb4\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f. \xd0\xa1\xd0\xb0\xd0\xbc\xd0\xbe\xd1\x81\xd1\x82\xd0\xbe\xd1\x8f\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xb7\xd0\xb0\xd0\xba\xd1\x80\xd1\x8b\xd1\x82\xd0\xb8\xd0\xb5 \n&gt;20 \xd0\xbf\xd0\xbe\xd0\xb7\xd0\xb8\xd1\x86\xd0\xb8\xd0\xb9 \xd0\xb2 \xd0\xbc\xd0\xb5\xd1\x81\xd1\x8f\xd1\x86, \xd0\xb2\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\x9a\xd0\x94\xd0\x9f,  \xd0\xb7\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbc \xd0\xbf\xd1\x80\xd0\xb8\xd0\xb5\xd0\xbc \xd0\xb8 \xd0\xbe\xd0\xb1\xd1\x83\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbd\xd0\xbe\xd0\xb2\xd1\x8b\xd1\x85 HR \n\xd1\x81\xd0\xbe\xd1\x82\xd1\x80\xd1\x83\xd0\xb4\xd0\xbd\xd0\xb8\xd0\xba\xd0\xbe\xd0\xb2. \xd0\xa3\xd1\x87\xd0\xb0\xd1\x81\xd1\x82\xd0\xb8\xd0\xb5 \xd0\xb2 \xd1\x81\xd0\xbe\xd0\xb2\xd0\xb5\xd1\x89\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f\xd1\x85 \xd1\x80\xd1\x83\xd0\xba\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb4\xd1\x81\xd1\x82\xd0\xb2\xd0\xb0. \xd0\x9e\xd1\x80\xd0\xb3\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb7\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f Nicko \nUniversity \xd0\xb8 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb2\xd0\xbd\xd1\x83\xd1\x82\xd1\x80\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xb8\xd1\x85 \xd0\xb8 \xd0\xb2\xd0\xbd\xd0\xb5\xd1\x88\xd0\xbd\xd0\xb8\xd1\x85 \xd1\x82\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xbd\xd0\xb3\xd0\xbe\xd0\xb2 \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xb4\xd0\xb6\xd0\xb5\xd1\x80\xd0\xbe\xd0\xb2 \xd0\xb8 \n\xd1\x81\xd0\xbe\xd1\x82\xd1\x80\xd1\x83\xd0\xb4\xd0\xbd\xd0\xb8\xd0\xba\xd0\xbe\xd0\xb2, \xd1\x80\xd1\x83\xd0\xba\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd0\xb9 \xd0\xbd\xd0\xbe\xd0\xb2\xd1\x8b\xd1\x85 \xd0\xbe\xd1\x84\xd0\xb8\xd1\x81\xd0\xbe\xd0\xb2.\n\t\t\t                    </dd>\n\t\t\t                  \n\t\t\t                    <dt class="b-resume-pinfo-label">\n\t\t\t\t                    <span class="b-resume-pinfo-exp-date">12.2003 -\n\t\t\t                      \n\t\t\t                        03.2005\n\t\t\t                        \n\t\t\t                      </span>,\n\t\t\t\t                    <span class="b-resume-pinfo-org">Roservice / Rostik group (\xd0\xbf\xd0\xb8\xd1\x89\xd0\xb5\xd0\xb2\xd0\xbe\xd0\xb5 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb8\xd0\xb7\xd0\xb2\xd0\xbe\xd0\xb4\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe \xd0\xb8 \xd0\xb4\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd0\xb1\xd1\x83\xd1\x86\xd0\xb8\xd1\x8f, 250 \xd1\x81\xd0\xbe\xd1\x82\xd1\x80\xd1\x83\xd0\xb4\xd0\xbd\xd0\xb8\xd0\xba\xd0\xbe\xd0\xb2)</span><br>\n\t\t\t\t                    \n\t\t\t\t                      <div class="b-resume-pinfo-industry">\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb4\xd1\x83\xd0\xba\xd1\x82\xd1\x8b \xd0\xbf\xd0\xb8\xd1\x82\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f</div>\n\t\t\t\t                    \n\t\t\t\t                    <strong>\xd0\xa2\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xbd\xd0\xb3-\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xb4\xd0\xb6\xd0\xb5\xd1\x80, \xd0\xbf\xd0\xbe\xd0\xb4\xd1\x87\xd0\xb8\xd0\xbd\xd1\x8f\xd0\xbb\xd1\x81\xd1\x8f \xd0\xb2\xd0\xbd\xd0\xb5\xd1\x88\xd0\xbd\xd0\xb5\xd0\xbc\xd1\x83 \xd0\xba\xd0\xbe\xd0\xbd\xd1\x81\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd0\xbd\xd1\x82\xd1\x83 \xd0\xb8\xd0\xb7 \xd0\xa1\xd0\xa8\xd0\x90.</strong>\n\t\t\t                    </dt>\n\t\t\t                    <dd class="b-resume-pinfo-value">\n\t\t\t                      \n\t\t\t                      \xd0\x9e\xd1\x81\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xb4\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f. \xd0\x9f\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb2\xd0\xbd\xd1\x83\xd1\x82\xd1\x80\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xb8\xd1\x85 \n\xd1\x82\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xbd\xd0\xb3\xd0\xbe\xd0\xb2 \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb6\xd0\xb8\xd0\xb2\xd0\xb0\xd1\x8e\xd1\x89\xd0\xb8\xd1\x85 \xd0\xb2\xd0\xbd\xd0\xb5\xd0\xb4\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 ISO, HACCP, TQM, Lean Manufacturing \n(\xd0\xb1\xd0\xb5\xd1\x80\xd0\xb5\xd0\xb6\xd0\xbb\xd0\xb8\xd0\xb2\xd0\xbe\xd0\xb5 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb8\xd0\xb7\xd0\xb2\xd0\xbe\xd0\xb4\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe), \xd1\x88\xd0\xb5\xd1\x81\xd1\x82\xd1\x8c \xd1\x81\xd0\xb8\xd0\xb3\xd0\xbc \xd0\xb8 \xd0\xba\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd1\x83\xd1\x80\xd1\x8b \xd0\x9a\xd0\xb0\xd0\xb9\xd0\xb4\xd0\xb7\xd0\xb5\xd0\xbd. \xd0\xa3\xd1\x87\xd0\xb0\xd1\x81\xd1\x82\xd0\xb8\xd0\xb5 \xd0\xb2 \n\xd1\x81\xd0\xbe\xd0\xb2\xd0\xb5\xd1\x89\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f\xd1\x85 \xd1\x80\xd1\x83\xd0\xba\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb4\xd1\x81\xd1\x82\xd0\xb2\xd0\xb0. \xd0\x9e\xd1\x80\xd0\xb3\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb7\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f \xd0\xbf\xd1\x80\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xb8 \xd0\xbe\xd1\x80\xd0\xb8\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \n\xd1\x87\xd0\xb5\xd1\x82\xd1\x8b\xd1\x80\xd0\xb5\xd1\x85\xd0\xbd\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb2\xd0\xb2\xd0\xbe\xd0\xb4\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd1\x82\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xbd\xd0\xb3\xd0\xb0 \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xbd\xd0\xbe\xd0\xb2\xd1\x8b\xd1\x85 \xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xb4\xd0\xb6\xd0\xb5\xd1\x80\xd0\xbe\xd0\xb2 \xd0\xbf\xd0\xbe \xd0\xb2\xd1\x81\xd0\xb5\xd0\xbc \n\xd0\xbf\xd1\x80\xd0\xbe\xd1\x86\xd0\xb5\xd1\x81\xd1\x81\xd0\xb0\xd0\xbc: \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb4\xd0\xb0\xd0\xb6\xd0\xb8, \xd0\xb7\xd0\xb0\xd0\xba\xd1\x83\xd0\xbf\xd0\xba\xd0\xb8, \xd1\x81\xd0\xba\xd0\xbb\xd0\xb0\xd0\xb4, \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb8\xd0\xb7\xd0\xb2\xd0\xbe\xd0\xb4\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe, \xd0\xb4\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd0\xb1\xd1\x83\xd1\x86\xd0\xb8\xd1\x8f \xd0\xb8 \n\xd0\xb2\xd1\x81\xd0\xbf\xd0\xbe\xd0\xbc\xd0\xbe\xd0\xb3\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xbf\xd1\x80\xd0\xbe\xd1\x86\xd0\xb5\xd1\x81\xd1\x81\xd1\x8b.\n\t\t\t                    </dd>\n\t\t\t                  \n\t\t\t                </dl>\n\t\t\t              \n\t\t\t            </div>\n\t\t\t            \n\t\t\t            \n\t\t\t              <div class="b-resume-profinfo b-resume-recommendations">\n\t\t\t                <h3>\xd0\xa0\xd0\xb5\xd0\xba\xd0\xbe\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb4\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8</h3>\n\t\t\t                \n\t\t\t                  \n\t\t\t                    <ul class="b-resume-profinfo-data b-resume-pinfo-recommendations">\n\t\t\t                      \n\t\t\t                        <li class="b-resume-pinfo-recomm-person">\n\t\t\t                          <span class="b-resume-pinfo-org">Nicko Travel Group</span><br>\n\t\t\t                          \n\t\t\t                          Roman Gorokhov,\n\t\t\t                          Director<br>\n\t\t\t                          on demand\n\t\t\t                        </li>\n\t\t\t                      \n\t\t\t                    </ul>\n\t\t\t                  \n\t\t\t                  \n\t\t\t                \n\t\t\t              </div>\n\t\t\t            \n\t\t\t            \n\t\t\t            <div class="b-resume-profinfo b-resume-additional">\n\t\t\t              \n\t\t\t              <h3>\n\t\t\t                \xd0\x94\xd0\xbe\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb0\xd1\x8f \xd0\xb8\xd0\xbd\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f\n\t\t\t              </h3>\n\t\t\t              <table class="b-forma-table">\n\t\t\t                \n\t\t\t                  <tbody><tr>\n\t\t\t                    <td class="b-forma-narrowcell">\n\t\t\t                      <label>\n\t\t\t                        <span>\xd0\x93\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb4\xd0\xb0\xd0\xbd\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe:</span>\n\t\t\t                      </label>\n\t\t\t                    </td>\n\n\t\t\t                    <td class="b-forma-widecell">\n\t\t\t                      <ul>\n\t\t\t                        \n\t\t\t                          <li>\n\t\t\t                            \xd0\xa0\xd0\xbe\xd1\x81\xd1\x81\xd0\xb8\xd1\x8f\n\t\t\t                          </li>\n\t\t\t                        \n\t\t\t                      </ul>\n\t\t\t                    </td>\n\t\t\t                  </tr>\n\t\t\t                \n\t\t\t                \n\t\t\t                  <tr>\n\t\t\t                    <td class="b-forma-narrowcell">\n\t\t\t                      <label>\n\t\t\t                        <span>\xd0\xa0\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb5\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbd\xd0\xb0 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x83 \xd0\xb2 \xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb0\xd1\x85:</span>\n\t\t\t                      </label>\n\t\t\t                    </td>\n\n\t\t\t                    <td class="b-forma-widecell">\n\t\t\t                      <ul>\n\t\t\t                        \n\t\t\t                          <li>\n\t\t\t                            \xd0\xa0\xd0\xbe\xd1\x81\xd1\x81\xd0\xb8\xd1\x8f\n\t\t\t                          </li>\n\t\t\t                        \n\t\t\t                      </ul>\n\t\t\t                    </td>\n\t\t\t                  </tr>\n\t\t\t                \n\t\t\t                <tr>\n\t\t\t                  <td class="b-forma-narrowcell">\n\t\t\t                    <label>\n\t\t\t                      <span>\xd0\xaf\xd0\xb7\xd1\x8b\xd0\xba\xd0\xb8</span>\n\t\t\t                    </label>\n\t\t\t                  </td>\n\n\t\t\t                  <td class="b-forma-widecell">\n\t\t\t                    <ul><li>\xd0\xa0\xd0\xbe\xd0\xb4\xd0\xbd\xd0\xbe\xd0\xb9 \xd1\x8f\xd0\xb7\xd1\x8b\xd0\xba \xe2\x80\x94 \xd0\xa0\xd1\x83\xd1\x81\xd1\x81\xd0\xba\xd0\xb8\xd0\xb9</li><li>\xd0\x90\xd0\xbd\xd0\xb3\xd0\xbb\xd0\xb8\xd0\xb9\xd1\x81\xd0\xba\xd0\xb8\xd0\xb9,\n        \xd1\x81\xd0\xb2\xd0\xbe\xd0\xb1\xd0\xbe\xd0\xb4\xd0\xbd\xd0\xbe \xd0\xb2\xd0\xbb\xd0\xb0\xd0\xb4\xd0\xb5\xd1\x8e</li><li>\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x8c\xd1\x81\xd0\xba\xd0\xb8\xd0\xb9,\n          \xd0\xb1\xd0\xb0\xd0\xb7\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb5 \xd0\xb7\xd0\xbd\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f</li></ul>\n\t\t\t                  </td>\n\t\t\t                </tr>\n\t\t\t              </tbody></table>\n\t\t\t            </div>\n\t\t\t            \n\t\t\t              <div class="b-resume-profinfo b-resume-keywords">\n\t\t\t                <h3>\n\t\t\t                  \xd0\x9a\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xb2\xd1\x8b\xd0\xb5 \xd0\xbd\xd0\xb0\xd0\xb2\xd1\x8b\xd0\xba\xd0\xb8\n\t\t\t                </h3>\n\t\t\t                <p class="b-resume-profinfo-data">\n\t\t\t                  \n\t\t\t                  <br>\n\t\t\t                  \xd0\x9e\xd1\x82\xd1\x80\xd0\xb0\xd1\x81\xd0\xbb\xd0\xb8: \xd0\x98\xd0\xa2, \xd1\x84\xd0\xb8\xd0\xbd\xd0\xb0\xd0\xbd\xd1\x81\xd1\x8b, \xd1\x81\xd0\xbf\xd0\xb5\xd1\x86\xd1\x82\xd0\xb5\xd1\x85\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb0, \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb4\xd0\xb0\xd0\xb6\xd0\xb8, \xd0\xb4\xd0\xb5\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb9 \xd1\x82\xd1\x83\xd1\x80\xd0\xb8\xd0\xb7\xd0\xbc, \xd0\xbf\xd0\xb8\xd1\x89\xd0\xb5\xd0\xb2\xd0\xbe\xd0\xb5 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb8\xd0\xb7\xd0\xb2\xd0\xbe\xd0\xb4\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe.<br><br>\xd0\x9f\xd1\x80\xd0\xbe\xd1\x84\xd0\xb5\xd1\x81\xd1\x81\xd0\xb8\xd0\xbe\xd0\xbd\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xbd\xd0\xb0\xd0\xb2\xd1\x8b\xd0\xba\xd0\xb8<br>\xd0\x91\xd0\xbe\xd0\xbb\xd0\xb5\xd0\xb5\n 7 \xd0\xbb\xd0\xb5\xd1\x82 HR \xd0\xbe\xd0\xbf\xd1\x8b\xd1\x82\xd0\xb0, 5 \xd0\xb8\xd0\xb7 \xd0\xbd\xd0\xb8\xd1\x85 \xd0\xb2 \xd1\x80\xd0\xbe\xd0\xbb\xd0\xb8 HR \xd0\xbb\xd0\xb8\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb0, \xd0\xbf\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb5\xd0\xb4\xd0\xbd\xd0\xb8\xd0\xb5 3 \xd0\xb3\xd0\xbe\xd0\xb4\xd0\xb0 \xd0\xb2 \xd0\xba\xd1\x80\xd1\x83\xd0\xbf\xd0\xbd\xd0\xbe\xd0\xb9 \n\xd0\xbc\xd0\xb5\xd0\xb6\xd0\xb4\xd1\x83\xd0\xbd\xd0\xb0\xd1\x80\xd0\xbe\xd0\xb4\xd0\xbd\xd0\xbe\xd0\xb9 \xd0\xba\xd0\xbe\xd1\x80\xd0\xbf\xd0\xbe\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8 \xd1\x81 \xd0\xbf\xd0\xb5\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xbc\xd0\xb8 HR \xd1\x82\xd0\xb5\xd1\x85\xd0\xbd\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb3\xd0\xb8\xd1\x8f\xd0\xbc\xd0\xb8. \xd0\x9e\xd1\x80\xd0\xb8\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f \xd0\xbd\xd0\xb0 \n\xd0\xb1\xd0\xb8\xd0\xb7\xd0\xbd\xd0\xb5\xd1\x81 \xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x8e \xd0\xb8 \xd1\x83\xd0\xb4\xd0\xbe\xd0\xb2\xd0\xbb\xd0\xb5\xd1\x82\xd0\xb2\xd0\xbe\xd1\x80\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c HR \xd0\xba\xd0\xbb\xd0\xb8\xd0\xb5\xd0\xbd\xd1\x82\xd0\xbe\xd0\xb2; \xd0\xb0\xd0\xbd\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x82\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xb8\xd0\xb9 \xd1\x81\xd0\xba\xd0\xbb\xd0\xb0\xd0\xb4 \n\xd1\x83\xd0\xbc\xd0\xb0 \xd1\x81 \xd0\xbe\xd1\x80\xd0\xb8\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb5\xd0\xb9 \xd0\xbd\xd0\xb0 \xd1\x80\xd0\xb5\xd0\xb7\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd1\x82, \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbc\xd1\x83\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb0\xd1\x86\xd0\xb8\xd0\xbe\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xb8 \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb7\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x86\xd0\xb8\xd0\xbe\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5 \n\xd0\xbd\xd0\xb0\xd0\xb2\xd1\x8b\xd0\xba\xd0\xb8; \xd0\xbd\xd0\xb0\xd0\xb2\xd1\x8b\xd0\xba \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b \xd0\xb2 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb4\xd0\xb5 - \xd0\xbd\xd0\xb5 \xd1\x82\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xba\xd0\xbe \xd1\x83\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5, \xd0\xbd\xd0\xbe \xd0\xb8 \xd0\xbf\xd1\x80\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xb8\xd0\xb9\n \xd0\xbd\xd0\xb0\xd0\xb2\xd1\x8b\xd0\xba \xd0\xb2\xd1\x8b\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xb2\xd1\x81\xd0\xb5\xd1\x85 \xd0\xb2\xd0\xb8\xd0\xb4\xd0\xbe\xd0\xb2 HR \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b \xd1\x81\xd0\xb2\xd0\xbe\xd0\xb8\xd0\xbc\xd0\xb8 \xd1\x80\xd1\x83\xd0\xba\xd0\xb0\xd0\xbc\xd0\xb8.  <br>\xd0\x94\xd0\xbe\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb5\n \xd0\xbd\xd0\xb0\xd0\xb2\xd1\x8b\xd0\xba\xd0\xb8. \xd0\x9f\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c SAP R3 (HR), 1\xd0\xa1 7.7, 8.0 \xe2\x80\x9c\xd0\x97\xd0\xb0\xd1\x80\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb8 \xd0\xba\xd0\xb0\xd0\xb4\xd1\x80\xd1\x8b\xe2\x80\x9d, \nPeople Click, E-Staff, MS Office etc. \xd0\x9f\xd1\x80\xd0\xb0\xd0\xb2\xd0\xb0 \xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb8 "B" (\xd0\xbe\xd0\xbf\xd1\x8b\xd1\x82 \xd1\x81 2000).\n\t\t\t                </p>\n\t\t\t              </div>\n\t\t\t            \n            </index></div></td></tr><!--EndFragment-->\n</body>\n</html> '
# test1 = re.findall(b'\xd0[%s]' % reg , test)
# for byte in test1:
# 	if byte 
# test2 = b'\xd0'.join(test.split(b'\xd0'))
print(test.decode('utf-8'))