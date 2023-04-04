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
