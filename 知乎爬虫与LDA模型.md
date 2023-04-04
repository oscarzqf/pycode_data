#### 1.知乎爬虫

- 获取某个话题下的全部评论

![](https://cdn.jsdelivr.net/gh/oscarzqf/typoraPictures/20221102171140.png)

```python
import requests
import json
url = 'https://www.zhihu.com/api/v4/comment_v5/answers/2720330164/root_comment?order_by=score&limit=20&offset='
while True:
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
         }
    res=requests.get(url,headers=headers).content.decode('utf-8')
    jsonfile=json.loads(res)
    next_page=jsonfile['paging']['is_end']
    url=jsonfile['paging']['next']#获取评论下一页的url
    print(next_page)
    for data in jsonfile['data']:
        id=data['id']
        content=data['content']
        author=data['author']['name']
        for data1 in data['child_comments']:
            content1 = data1['content']
            print(content1)
        print(id,content,author)

    if next_page==True:
        break
```

- 获取全部话题

![](https://cdn.jsdelivr.net/gh/oscarzqf/typoraPictures/20221102170936.png)

```python
import requests
import json
url_answers='https://www.zhihu.com/api/v4/questions/560526531/feeds?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Creaction_instruction%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cvip_info%2Cbadge%5B*%5D.topics%3Bdata%5B*%5D.settings.table_of_content.enabled&offset=&limit=3&order=default&platform=desktop'

while True:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        }
    res_answers = requests.get(url_answers, headers=headers).content.decode('utf-8')
    jsonfile_answers = json.loads(res_answers)
    next_page_answers = jsonfile_answers['paging']['is_end']
    url_answers=jsonfile_answers['paging']['next'] # 获取下一页的回答
    for data_answers in jsonfile_answers['data']:
        id_answers=data_answers['target']['id']
        content_answers=data_answers['target']['content']
        print(id_answers,content_answers)#打印回答内容
    if next_page_answers==True:
        break


```

- 获取全部话题以及对应评论,只要文本内容

  ```python
  import requests
  import json
  url_answers='https://www.zhihu.com/api/v4/questions/560526531/feeds?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Creaction_instruction%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cvip_info%2Cbadge%5B*%5D.topics%3Bdata%5B*%5D.settings.table_of_content.enabled&offset=&limit=3&order=default&platform=desktop'
  
  while True:
      headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
          }
      res_answers = requests.get(url_answers, headers=headers).content.decode('utf-8')
      jsonfile_answers = json.loads(res_answers)
      next_page_answers = jsonfile_answers['paging']['is_end']
      url_answers=jsonfile_answers['paging']['next'] # 获取下一页的回答
      for data_answers in jsonfile_answers['data']:
          id_answers=data_answers['target']['id']
          content_answers=data_answers['target']['content']
          print(content_answers)#打印回答内容
          #=========打印评论内容==============,不同回答评论的链接中只有id不同
          url = 'https://www.zhihu.com/api/v4/comment_v5/answers/{}/root_comment?order_by=score&limit=20&offset='.format(id_answers)
          while True:
              headers = {
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
                  }
              res = requests.get(url, headers=headers).content.decode('utf-8')
              jsonfile = json.loads(res)
              next_page = jsonfile['paging']['is_end']
              url = jsonfile['paging']['next']  # 获取评论下一页的url
              for data in jsonfile['data']:
                  content = data['content']
                  for data1 in data['child_comments']:
                      content1 = data1['content']
                      print(content1)
                  print(content)
  
              if next_page == True:
                  break
      if next_page_answers==True:
          break
  
  
  ```

- 最终

  ```python
  import requests
  import json
  f=open('zhihu.txt','w',encoding='utf-8')
  url_answers='https://www.zhihu.com/api/v4/questions/560526531/feeds?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Creaction_instruction%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cvip_info%2Cbadge%5B*%5D.topics%3Bdata%5B*%5D.settings.table_of_content.enabled&offset=&limit=3&order=default&platform=desktop'
  while True:
      headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
          }
      res_answers = requests.get(url_answers, headers=headers).content.decode('utf-8')
      jsonfile_answers = json.loads(res_answers)
      next_page_answers = jsonfile_answers['paging']['is_end']
      url_answers=jsonfile_answers['paging']['next'] # 获取下一页的回答
      for data_answers in jsonfile_answers['data']:
          id_answers=data_answers['target']['id']
          content_answers=data_answers['target']['content']
          print(content_answers)#打印回答内容
          f.write(content_answers)
          #=========打印评论内容==============,不同回答评论的链接中只有id不同
          url = 'https://www.zhihu.com/api/v4/comment_v5/answers/{}/root_comment?order_by=score&limit=20&offset='.format(id_answers)
          while True:
              headers = {
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
                  }
              res = requests.get(url, headers=headers).content.decode('utf-8')
              jsonfile = json.loads(res)
              next_page = jsonfile['paging']['is_end']
              url = jsonfile['paging']['next']  # 获取评论下一页的url
              for data in jsonfile['data']:
                  content = data['content']
                  for data1 in data['child_comments']:
                      content1 = data1['content']
                      print(content1)
                      f.write(content1)
                  print(content)
                  f.write(content)
  
              if next_page == True:
                  break
      if next_page_answers==True:
          break
  f.close()
  
  ```



#### 2.中文分词

​		结巴分词是一种优秀的中文分词方法，支持精确模式、全模式、搜索引擎模式和paddle模式等四种模式，支持繁体分词、自定义词典以及MIT授权协议。算法：基于前缀词典实现高效的词图扫描，生成句子中汉字所有可能成词情况所构成的有向无环图 (DAG)；采用了动态规划查找最大概率路径, 找出基于词频的最大切分组合；对于未登录词，采用了基于汉字成词能力的 HMM 模型，使用了 Viterbi 算法。（github介绍）

```python
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
outputs = open('./zhihu0.txt', 'w', encoding='utf-8')

for line in inputs:
    line_seg = seg_sentence(line)  # 这里的返回值是分词后字符串
    outputs.write(line_seg + '\n')
outputs.close()
inputs.close()

```

#### 3.LDA模型与可视化

主题挖掘算法主要基于Gibbs采样的隐含狄利克雷分配（Latent Dirichlet Allocation,LDA）主题模型

```python
import pyLDAvis.gensim_models
from gensim import corpora#语料库
from gensim.models import LdaModel#lda模型

#gensim是python的一个可以创建和查询语料库的自然语言处理库
train = []#存放要分类的词

fp = open('./zhihu0.txt','r',encoding='utf-8')
for line in fp:#加载词
    if line != '':
        line = line.split()
        train.append([w for w in line])

dictionary = corpora.Dictionary(train)#词典

corpus = [dictionary.doc2bow(text) for text in train]#文档词频率矩阵（稀疏矩阵），词袋

lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=10, passes=50)#计算好的话题模型
# num_topics：主题数目
# passes：训练伦次
# num_words：每个主题下输出的term的数目

for topic in lda.print_topics(num_words = 20):
    termNumber = topic[0]
    print(topic[0], ':', sep='')
    listOfTerms = topic[1].split('+')
    for term in listOfTerms:
        listItems = term.split('*')
        print('  ', listItems[1], '(', listItems[0], ')', sep='')

d=pyLDAvis.gensim_models.prepare(lda, corpus, dictionary,mds='mmds')#mds='mmds'必须加，否则会报错，不能使用缺省的js pcoa mds
pyLDAvis.save_html(d,"lda_pass1.html")


```

#### 4.词云图

```python
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 20:11:01 2022

@author: 22837
"""
from wordcloud import WordCloud
train = ''#分词后的文件直接连接成字符串使用
fp = open('./zhihu0.txt','r',encoding='utf-8')
for line in fp:#加载词
    if line != '':
       train=train+line
#print(train)       
wordcloud = WordCloud(font_path ="msyh.ttc",mode='RGBA',background_color='white').generate(train)
wordcloud.to_file('中文词云图.png')

```

