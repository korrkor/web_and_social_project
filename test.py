from pyspark.sql.functions import *
from itertools import chain
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random


G=nx.DiGraph()

pages = ["1","2","3","4"]
G.add_nodes_from(pages)
G.add_edges_from([('1','2'), ('1','4'),('1','3'), ('4','1'),('2','3'),('2','4'),('3','1'),('4','3')])

print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())

nx.draw(G, with_labels = True)
plt.show() # display

# filename = r"dataset/ds-1.tsv"
# # G=nx.DiGraph()

# df_1 = pd.read_csv(filename, sep='\t', names=["year", "keywords_1", "keywords_2", "authors"])
# print(df_1.head())
# df_distinct_years = df_1['year'].unique()
# # print(sorted(df_distinct_years))

# for year in df_distinct_years:
#     is_year = df_1["year"] == year
#     df_filter = df_1[is_year]
#     # print(df_filter)
# # get list of keywords fr each year
#     list_keywords = df_filter['keywords_1'].unique().tolist() + df_filter['keywords_2'].unique().tolist()
#     g=nx.DiGraph(directed = True)
#     g.add_nodes_from(list_keywords)
#     # g= nx.gnp_random_graph(10,0.5,directed = True)
#     nx.draw(g, with_labels=True)
#     plt.show()