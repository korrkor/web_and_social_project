import pandas as pd
import ast 
import numpy as np
import matplotlib.pyplot as plt
from pyspark.sql import SparkSession, HiveContext
<<<<<<< HEAD
from pyts.approximation import PAA
=======
>>>>>>> e46e9dcb4fe6e33657ec794c6117870a90b42b3f
# import display
class TopicTracing:
    
    def __init__(self, dictionary):
        self.filename = r"dataset/ds-1.tsv"
        self.dict = dictionary
        # self.spark = self.get_Spark_Session("")
        self.read_csv() 
        
        # print("this si spark ", self.spark)
    

    def get_Spark_Session(self,nome):
        spark=(SparkSession.builder.appName(nome).enableHiveSupport().getOrCreate())
        return spark

    def read_csv(self):
        # sc = SparkContext(conf=conf)
        # sqlCtx = SQLContext(sc)

        final_df = pd.DataFrame({'keyword': [], 'year': [], 'count': []})
        pd.set_option('display.max_columns', 30)
        pd.set_option('display.expand_frame_repr', False)
        df_orig = pd.read_csv(self.filename, sep='\t', names=["year", "keywords_1", "keywords_2", "authors"])
        
        # print(df["year"])
        is_greater = df_orig['year'] > 1999
        df = df_orig[is_greater]
        # df = df[df["year"] !=0].reset_index(drop=True)

        # df = df.filter(lambda x: x['year'] > 1999)
        print(type(df))
        for keyword_list in self.dict.values():
            for keyword in keyword_list:
                # df['new_keyword'] = np.where(df["keywords_1"]==keyword[0]) | (df["keywords_2"]==keyword[0]), keyword[0], 'red')
                # print("thia is the key word" , keyword[0])
                df_filter = df[(df["keywords_1"]==keyword[0]) | (df["keywords_2"]==keyword[0])]
                if(df_filter.size > 0):
                # df_filter = df_filter[(df_filter["year"]) > 1999]
                    df_filter['new_keyword'] =  keyword[0]
                    print(df_filter.columns)
                    print("**********************************************************************************************************************************************")
                    # print(df_filter)
                    
                    df_filter_years = df_filter[["year","authors", "new_keyword"]].copy()
                    print("666666666666666666666")
                    # df_filter_years['new_count'] = df_filter_years["authors"].map(self.get_author_count(df_filter_years["authors"][0][0]))
                    df_filter_years['count'] = df_filter_years["authors"].apply(lambda x : self.get_author_count(ast.literal_eval(x)))
                    
                    print("******2222222222222222222222222222222222222222**************")
                    print(df_filter_years)
                    df_finale = df_filter_years.groupby(['new_keyword',"year"]).sum()[["count"]].sort_values(by = "year").reset_index()
                    print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
                    years = [pd.year for year in df_finale["year"].tolist() ]
                    plt.plot(df_finale["year"].tolist(), df_finale["count"].tolist(), label=keyword[0])
          
                    plt.legend()          # plt.show()
                    plt.show()
        
                # plt.plot([0.1, 0.2, 0.3, 0.4], [1, 4, 9, 16], label='second plot')
                # print("******233333333333333333333333333333333333333333333333333333333333333333333333333322222**************")
                # final_df = final_df.append({'keyword': keyword[0], 'year': df_finale["year"] , 'count': df_finale["count"]}, ignore_index=True)
        # self.spark.createDataFrame(final_df).show()
        
        # plot_df = final_df.groupby(['keyword'])
        
        # print("the colssssssssssssssssssssss ")
        # print(df_finale.head())
        # print( df_finale["year"].tolist())
        # plt.plot(df_finale["year"].tolist(), df_finale["count"].tolist(), label=keyword[0])
        
        # x axis values 
        # x = [1,2,3] 
        # # corresponding y axis values 
        # y = [2,4,1] 
        
        # # plotting the points  
        # plt.plot(x, y) 
        
        # # naming the x axis 
        # plt.xlabel('x - axis') 
        # # naming the y axis 
        # plt.ylabel('y - axis') 
        
        # # giving a title to my graph 
        # plt.title('My first graph!') 
        
        # # function to show the plot 
        # plt.show() 
        

        # final_df = final_df.pivot(index='year', columns='keyword', values='count')

        # df.plot()
        # fig, ax = plt.subplots()
        # for key, grp in final_df.groupby(['keyword']):
        #     print("this si the key ", key)
        #     ax = grp.plot(ax=ax, kind='line', x='year', y='count', c=key, label=key)

        # plt.legend(loc='best')
        # plt.show() 


                
                                # print(df_filter_years.head())


    def get_author_count(self,dictionary):
        return sum(dictionary.values())
                # group by years

                # print(df_filter)

            # is_year = df['keywords_i'] == int(key) ||  
            



            
            # 
            # print("this si the key ************************888888", key)
            # print(df_filter)

        
            
        # print("hello")

