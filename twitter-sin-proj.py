#!/usr/bin/env python
# coding: utf-8

# In[1]:


from igraph import *
import pycario
import csv
import math

vinfile = "D://VIT//5th Sem//SAIN//Project//twitter-data//data//nba_v_small.csv"
einfile = "D://VIT//5th Sem//SAIN//Project//twitter-data//data//nba_e_small.csv"

V = []
E = []
scrn_names = []
full_names = []
teams = []

#for edges
with open(vinfile, 'r') as infile:
    reader = csv.reader(infile, delimiter=',')
    for row in reader:
        V.append(row[0])
        full_names.append(row[1])
        scrn_names.append(row[2])
        teams.append(row[3])

#for vertices
with open(einfile, 'r') as infile:
    reader = csv.reader(infile, delimiter=',')
    for row in reader:
        E.append((row[0], row[1]))

g = igraph.Graph(directed=True)
g.add_vertices(V)
g.add_edges(E)
g.vs["full_name"] = full_names
g.vs["screen_name"] = scrn_names

def process_edges(graph):
    for e in graph.es:
        src, targ = e.tuple
        if graph.are_connected(targ, src):
            e["color"] = "#90EE90" 
            e["arrow"] = 0        
            e["width"] = .75
        else:
            e["color"] = "#7FFFD4"
            e["arrow"] = 1
            e["width"] = 1
process_edges(g)
g.ecount()

def process_verts(graph):
    for v in graph.vs:
        if v.degree() == 0:
            v.delete()
process_verts(g)
g.vcount()

import math
ang = []
dis = []
flip = 1
for i in range(0, g.vcount()):
    dist = 5
    angle = -i*1.0/g.vcount()*2.0*math.pi
    diff = abs(abs(angle) % math.pi - math.pi/2.0)
    if diff < 0.2:
        dist += 1.5*flip
        flip *= -1
    ang.append(angle)
    dis.append(dist)
g.vs["ang"] = ang
g.vs["dis"] = dis

visual_style = {}
visual_style["layout"] = g.layout("circular")
visual_style["vertex_size"] = 3
visual_style["vertex_color"] = "white"
visual_style["vertex_shape"] = "square"
visual_style["vertex_frame_color"] = "white"
visual_style["vertex_label"] = g.vs["screen_name"]
visual_style["margin"] = 100
visual_style["bbox"] = (500, 500) # change to 5000, 5000 for full graph
visual_style["edge_curved"] = False
visual_style["edge_color"] = g.es["color"]
visual_style["edge_arrow_size"] = g.es["arrow"]
visual_style["vertex_label_angle"] = g.vs["ang"]
visual_style["vertex_label_dist"] = g.vs["dis"]
visual_style["vertex_label_size"] = 7
visual_style["edge_width"] = g.es["width"]

plot(g, **visual_style)


# In[2]:


import networkx as nx


# In[3]:


pip install networkx


# In[48]:


import networkx as nx
import csv
import math

vinfile = "D://VIT//5th Sem//SAIN//Project//twitter-data//data//nba_v_small.csv"
einfile = "D://VIT//5th Sem//SAIN//Project//twitter-data//data//nba_e_small.csv"

V = []
E = []
scrn_names = []
full_names = []
teams = []


#for edges
with open(vinfile, 'r') as infile:
    reader = csv.reader(infile, delimiter=',')
    for row in reader:
        V.append(row[0])
        full_names.append(row[1])
        scrn_names.append(row[2])
        teams.append(row[3])

#for vertices
with open(einfile, 'r') as infile:
    reader = csv.reader(infile, delimiter=',')
    for row in reader:
        E.append((row[0], row[1]))
        
G = nx.Graph()
G.add_nodes_from(V)
G.add_edges_from(E)

nx.draw(G, node_size=150, node_color='green')
list(nx.find_cliques(G))


# In[51]:


import igraph
import csv
import math
import networkx as nx

vinfile = "D://VIT//5th Sem//SAIN//Project//twitter-data//data//v429.csv"
einfile = "D://VIT//5th Sem//SAIN//Project//twitter-data//data//e429.csv"

V = []
E = []
scrn_names = []
full_names = []
teams = []

#for edges
with open(vinfile, 'r') as infile:
    reader = csv.reader(infile, delimiter=',')
    for row in reader:
        V.append(row[0])
        full_names.append(row[1])
        scrn_names.append(row[2])
        teams.append(row[3])

#for vertices
with open(einfile, 'r') as infile:
    reader = csv.reader(infile, delimiter=',')
    for row in reader:
        E.append((row[0], row[1]))
#graph
g = igraph.Graph(directed=True)
g.add_vertices(V)
g.add_edges(E)
g.vs["full_name"] = full_names
g.vs["screen_name"] = scrn_names

def process_edges(graph):
    for e in graph.es:
        src, targ = e.tuple
        if graph.are_connected(targ, src):
            e["color"] = "#90EE90" 
            e["arrow"] = 0        
            e["width"] = .75
        else:
            e["color"] = "#7FFFD4"
            e["arrow"] = 1
            e["width"] = 1
process_edges(g)
g.ecount()

def process_verts(graph):
    for v in graph.vs:
        if v.degree() == 0:
            v.delete()
process_verts(g)
g.vcount()

import math
ang = []
dis = []
flip = 1
for i in range(0, g.vcount()):
    dist = 5
    angle = -i*1.0/g.vcount()*2.0*math.pi
    diff = abs(abs(angle) % math.pi - math.pi/2.0)
    if diff < 0.2:
        dist += 1.5*flip
        flip *= -1
    ang.append(angle)
    dis.append(dist)
g.vs["ang"] = ang
g.vs["dis"] = dis

visual_style = {}
visual_style["layout"] = g.layout("circular")
visual_style["vertex_size"] = 3
visual_style["vertex_color"] = "white"
visual_style["vertex_shape"] = "square"
visual_style["vertex_frame_color"] = "white"
visual_style["vertex_label"] = g.vs["screen_name"]
visual_style["margin"] = 100
visual_style["bbox"] = (500,500)
visual_style["edge_curved"] = False
visual_style["edge_color"] = g.es["color"]
visual_style["edge_arrow_size"] = g.es["arrow"]
visual_style["vertex_label_angle"] = g.vs["ang"]
visual_style["vertex_label_dist"] = g.vs["dis"]
visual_style["vertex_label_size"] = 7
visual_style["edge_width"] = g.es["width"]

plot(g, **visual_style)


# In[29]:


#plot kawhi graph with labels 
steph = g.vs(screen_name="StephenCurry30")[0]
v = steph.index
sg = g.subgraph_edges(g.es.select(_between = ([v], [i for i in range(0,g.vcount())])), delete_vertices=False)
sg.vs["screen_name"] = [None] * sg.vcount()
sg.vs[v]["screen_name"] = g.vs[v]["screen_name"]
for other in kawhi.neighbors():
    sg.vs[other.index]["screen_name"] = g.vs[other.index]["screen_name"]
visual_style["vertex_label"] = sg.vs["screen_name"]
visual_style["edge_color"] = sg.es["color"]
visual_style["edge_arrow_size"] = sg.es["arrow"]
visual_style["edge_width"] = sg.es["width"]

plot(sg,**visual_style)


# In[30]:


#analytics
h = g.degree_distribution()
plot(h)


# In[31]:


#FOLLOWERS-FOLLOWS DIFFERENTIAL 
deg = zip(g.degree(g.vs, OUT), g.degree(g.vs, IN))
res = []
for d in deg:
    res.append(d[1]-d[0])
res[:10]


# In[32]:


#CENTRALITY (EIGENVECTOR)
ec = sorted(zip(g.eigenvector_centrality(), g.vs["screen_name"]), reverse=True)
ec[:10]


# In[33]:


#PAGERANK
pr = sorted(zip(g.pagerank(), g.vs["screen_name"]), reverse=True)
pr[:10]


# In[34]:


#COMMUNITY DETECTION
sg = g.as_undirected(mode="MUTUAL")
process_verts(sg)
comm = sg.community_leading_eigenvector()
layout = sg.layout()
mem = sorted(zip(comm.membership, g.vs["screen_name"]))
mem
plot(comm, layout=layout, margin=50)


# In[37]:


#LARGEST CLIQUES
cls = g.as_undirected(mode="MUTUAL").largest_cliques()
cl = g.subgraph(cls[0].vs["screen_name"])
cl


# In[46]:


import networkx as nx
list(nx.find_cliques(g))


# In[ ]:




