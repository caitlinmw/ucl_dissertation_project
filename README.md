# ucl_dissertation_project
Network Analysis Project: The Goupil Stock Books

The Python scripts in this repo formed a part of my Disseration Project during my MA Digital Humantities degree (2020-21).

Using the digitised Goupil Stock Books, I conducted Network Analysis of sales relationships between European and American contacts in the 'long' nineteenth century (1780s-1920s).
To create network graphs with Gephi software, I required the dataset to be transformed: I would need a Node table (with information about the individual buyers and sellers) and an Edge table (with information about the transactions between these individuals).

I am publicly sharing the scripts I wrote to transform the raw data, in case they are of use for anyone else conducting research on this topic using digital methods.
The process_goupil.py script should be run before edge_table_loop.py

The original dataset can be found on the Getty Provenance Index's github repo here: https://github.com/thegetty/provenance-index-csv/tree/main/
