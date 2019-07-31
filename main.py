import sys
sys.path.insert(1, '/home/kor/SCHOOL/web_and_social_project/utility')
from topic_identification import * 
from topic_tracing import * 
from operator import itemgetter
import random

# from utility.topic_identification import TopicIdentification
# from utility.topic_tracing import TopicTracing


# topic TopicIdentification************************************************************
ti = TopicIdentification()
df_target , df_distinct_years = ti.get_distinct_years()
for year in df_distinct_years:
    is_year = df_target["year"] == year
    df_filter = df_target[is_year]  
    # get list of keywords fr each year
    list_keywords = df_filter['keywords_1'].unique().tolist()
    dictionary = ti.create_dictionary(list_keywords,df_filter)
    graph = ti.show_graph(dictionary)
    page_rank = ti.show_page_rank(graph) 

    # k_list = [2,5,10]
    # rk = random.choice([k for k in k_list])
    top_ranked_list = ti.get_top_k(page_rank,3)   
    # print("this is the diffussion : ", ti.linear_threshold(graph,top_ranked_list))
    
    
    ti.top_k_dictionary(year,top_ranked_list)

# print(ti.dict)
print("topic tracing**************************************************")
# topic tracing************************************************************
tt = TopicTracing(ti.dict)




    

