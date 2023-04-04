# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 20:11:01 2022

@author: 22837
"""
from wordcloud import WordCloud
train = ''#分词后的文件直接连接成字符串使用
fp = open('./zanjuke.txt','r',encoding='utf-8')
for line in fp:#加载词
    if line != '':
       train=train+line
#print(train)       
wordcloud = WordCloud(font_path ="msyh.ttc",mode='RGBA',background_color='white').generate(train)
wordcloud.to_file('中文词云图.png')



