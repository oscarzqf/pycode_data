import pyLDAvis.gensim_models
from gensim import corpora#语料库
from gensim.models import LdaModel#lda模型

#gensim是python的一个可以创建和查询语料库的自然语言处理库
train = []#存放要分类的词

fp = open('./zanjuke.txt','r',encoding='utf-8')
for line in fp:#加载词
    if line != '':
        line = line.split()
        train.append([w for w in line])

dictionary = corpora.Dictionary(train)#词典

corpus = [dictionary.doc2bow(text) for text in train]#文档词频率矩阵（稀疏矩阵），词袋

lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=5, passes=100)#计算好的话题模型
# num_topics：主题数目
# passes：训练伦次
# num_words：每个主题下输出的term的数目

for topic in lda.print_topics(num_words = 10):
    termNumber = topic[0]
    print(topic[0], ':', sep='')
    listOfTerms = topic[1].split('+')
    for term in listOfTerms:
        listItems = term.split('*')
        print('  ', listItems[1], '(', listItems[0], ')', sep='')

d=pyLDAvis.gensim_models.prepare(lda, corpus, dictionary,mds='mmds')
pyLDAvis.save_html(d,"lda_pass1.html")

