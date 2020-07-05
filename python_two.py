#第三方库的安装与使用
#点击下方的Terminal（终端），输入pip install 库的名称

#import random#random 官方自带的库
#print(random.randint(1,5))#生成随机数的

#能够将一段中文文本分割成中文词语的序列---jieba(结巴)
'''import jieba

s=jieba.lcut('能够将一段中文文本分割成中文词语的序列')
print(s)
'''

import jieba
from wordcloud import WordCloud
s='''
？？？？？
我靠瞬间去世
死因：天气不错
李荣浩 草
为下次做铺垫
为了下集，吃好了上路
四大名捕
？？？？？
哈哈哈
？？？？？
危
哈哈
人言否？
'''

cut_list=jieba.lcut(s)#分词
new_str=' '.join(cut_list)#用空格从新拼接成一个字符串
word=WordCloud(font_path='msyh.ttc').generate(new_str)#生成词云对象  fonr_path（指定字体）=msyh.ttc(字体)
word.to_file('煮鼠.png')#保存图片