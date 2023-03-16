

from graphviz import Digraph
import pandas as pd

# read the csv file into a pandas dataframe
df = pd.read_csv('orgchart.csv')

# create a new Digraph object
dot = Digraph()

# add nodes to the graph for each company and set their label to be the company name
for index, row in df.iterrows():
    dot.node(row['Company Name'], label=row['Company Name'])

# add edges to the graph to connect each parent company to its subsidiaries
for index, row in df.iterrows():
    if pd.notna(row['Parent Company']):
        edge_label = f"{row['Share Percentage']} / {row['Voting Rights']}"
        dot.edge(row['Parent Company'], row['Company Name'], label=edge_label)

# render the graph and view it
dot.render('organizational_chart.gv', view=True)

