import jieba
import re
# 定义停用词列表
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords
# 对句子进行分词
def seg_sentence(sentence):
    sentence = re.sub('[^\u4e00-\u9fa5]+', '', sentence)#正则表达式去掉特殊字符

    jieba.add_word('租售并举')  # 这里是加入用户自定义的词来补充jieba词典。
    jieba.add_word('租房')  # 想要删除的词语就先把它加上然后放进停用词表

    sentence_seged = jieba.lcut(sentence.strip())#使用三种模式之一的精确模式
    stopwords = stopwordslist('./stopwords.txt')  # 这里加载停用词的路径
    outstr = ''#输出变量
    for word in sentence_seged:#不在停用表中的词就拼接到outstr
        if word not in stopwords and word.__len__() > 1:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

#  inputs即是读入原文本，outputs即是新建一个文本，统一用utf-8
inputs = open('./zhihu.txt', 'r', encoding='utf-8')
outputs = open('./zanjuke.txt', 'w', encoding='utf-8')

for line in inputs:
    line_seg = seg_sentence(line)  # 这里的返回值是分词后字符串
    outputs.write(line_seg + '\n')
outputs.close()
inputs.close()
