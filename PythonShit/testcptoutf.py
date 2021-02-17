#coding: utf-8
# sourceEncoding = "utf-8"
# targetEncoding = "cp1251"
# word = "А".encode('utf-8')
# print(word.decode(targetEncoding))
# print(word.encode(sourceEncoding).decode(targetEncoding))
# print(word.encode(sourceEncoding).decode(targetEncoding, errors='ignore').encode(targetEncoding).decode(sourceEncoding, errors='ignore'))

# byte1 = 'А'.encode('utf-8')
# byte2 = 'И'.encode('utf-8')
# print(byte1, byte2)
# test1 = byte1.decode('cp1251')
# print(test1)
# # test2 = byte2.decode('cp1251')
# # print(test2)
# for byte in byte2:
#     print(str(byte).strip())
#     text = str(byte).decode('utf-8')
#     print(text.strip())



test1 = 'И'.encode('utf-8')
test = 'И'.encode('cp1251')
print(test1.split(b'0\x98')[0])
print(test)
# print(test1.decode('cp1251'))


test1 = '\x98'
print(test1)