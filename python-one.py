'''
f=open('任飘渺',encoding='utf-8')#打开文件f接,指定编码格式
s=f.read()#读取s接收
print(s)
f.close()
'''
#write 文件写入
f=open('write_test',mode='w',encoding='utf-8')#mode是写入模式，w是写入
f.write('飘散\n')
f.write('谷歌商店\n')
f.close()
