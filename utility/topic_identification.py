from pyspark.sql.functions import *
from itertools import chain
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random
import copy
# import Tkinter as tk


class TopicIdentification:
    # read file into dataframe
    def __init__(self):
        self.filename = r"dataset/ds-1.tsv"
        self.dict = dict()
        
    def get_distinct_years(self):
        pd.set_option('display.max_columns', 5)
        df_1 = pd.read_csv(self.filename, sep='\t', names=["year", "keywords_1", "keywords_2", "authors"])
        # print(df_1.head())
        df_distinct_years = df_1['year'].unique()
        # print(sorted(df_distinct_years))
        df_distinct_years = sorted(df_distinct_years)
        return df_1, df_distinct_years

    def create_dictionary(self,list_keywords, df_filter):
        dictionary = dict()
        for keyword in list_keywords:
            is_rc = df_filter['keywords_1'] == keyword
            df_edge_list = df_filter[is_rc]
            df_edge_list = df_edge_list["keywords_2"].unique().tolist()
            dictionary[keyword] = df_edge_list 
        return dictionary 
    
    def show_graph(self,dictionary): 
        g = nx.DiGraph()
        g.add_nodes_from(dictionary.keys())
        for k, v in dictionary.items():
            g.add_edges_from(([(k, t) for t in v]))
        nx.draw(g, with_labels=True)
        # plt.show()  
        plt.close()
        return g
    
    def show_page_rank(self,g):
        pr = nx.pagerank(g, alpha=0.85)
        return pr  
    
    def get_top_k(self, page_rank, k):
        return sorted(page_rank.items(), key=lambda x: x[1], reverse=True)[:k]

    def linear_threshold(self,g,s):
        for n in nx.nodes(g):
            g.nodes[n]['threshoold'] = random.random()
        wave = 0
        diffusion={}
        diffusion[0] = copy.deepcopy(s)
        active = copy.deepcopy(s)
        # until convergence
        while True:
            added = []
            wave +=1
            print("this si the wave ", wave)

            for n in nx.nodes(g):
                if n not in active:
                    print("not in nodes")
                    influence = 0
                    for edge in g.in_edges(n, data=True):
                        if edge[0] in active:
                            print("edge active")
                            influence += float(edge[2]["weight"])
                            if influence >= g.nodes[n]["threshold"]:
                                print("this is the influence ", influence)
                                active.append(n)
                                added.append(n)
                print("in nodes")
            if len(added) == 0:
                break
            else:
                diffusion[wave] = added
        return diffusion
    
    def top_k_dictionary(self, year,top_list):  
        # print(year, top_list)
        self.dict[year] = top_list
        return self.dict





   


        



            




        # print("this is tcccc***************",rc)
        # print ("thsi is df edge list********,", df_edge_list)


        # get edges for each starting node
        
        
        
        # print(list_keywords)
        # G=nx.DiGraph(directed = True)
        # G.add_nodes_from(list_keywords)
        # pr = nx.pagerank(G, alpha=0.9)
        # # print(pr)
        # nx.draw(G, with_labels=False)
        # plt.show()
        # rc = random.choice([keyword for keyword in list_keywords])
        # dict_count = {}
        # for keyword in list_keywords:
        #     dict_count[keyword] = 0
        # dict_count[rc] = dict_count[rc]+1

        # for i in range(1000000):
        #     list_n = list(G.neighbors(rc))
        #     print(list_n)
        #     if len(list_n) == 0:
        #         rc = random.choice([keyword for keyword in list_keywords])
        #         dict_count[rc] = dict_count[rc]+1
        #     else:
        #         rc = random.choice(list_n)
        #         dict_count[rc] = dict_count[rc]+1


        # # print("Nodes of graph: ")
        # # print(G.nodes())
        # # print("Edges of graph: ")
        # # print(G.edges(list_keywords))
        # print("********************", year,"***********************************")
    

