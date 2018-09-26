# Community Detection Algorithm Implementation
In the Program (CommunityDetectionAlgorithmOnKarateClubGraph.py and CommunityDetectionAlgorithmImplementation.py),  I have implemented the Hierarchical Clustering using Jaccard Coefficient for similarity measurement along with single linkage method.

The Algorithm suffers from Chaining Problem i.e. it is trying to create only one super cluster until and unless a certain threshold value is reached. When the threshold value is reached then all the other nodes which are not part of the super cluster till now as regarded as clusters themselves . 

The program NEEDS the following python libraries for running -
1) Networkx
2) matplotlib and its dependencies.

# On Karate Club Graph as provided in Networkx Library

Program - CommunityDetectionAlgorithmOnKarateClubGraph.py

Some png files are attached to show the output -
1) Karate_club_graph.png - This is the original Karate Club Graph before applying the Algorithm on it
2) with_threshold_value0.1.png - This is the graph with clusters detected when the threshold value is kept as 0.1 on Karate Club Graph.
3) with_threshold_value0.2.png - This is the graph with clusters detected when the threshold value is kept as 0.2 on Karate Club Graph.
4) with_threshold_value0.3.png - This is the graph with clusters detected when the threshold value is kept as 0.3 on Karate Club Graph.
5) with_threshold_value0.4.png - This is the graph with clusters detected when the threshold value is kept as 0.4 on Karate Club Graph.
5) with_threshold_value0.5.png - This is the graph with clusters detected when the threshold value is kept as 0.5 on Karate Club Graph.

The Program does the following -
1) It shows the original Graph G in a separate window. You have to close this window to proceed with the program further.
2) It asks you choose a Threshold Value based on the Jaccard Coefficients of each edge.
3) It shows the cluster number that each Node belongs to . If the cluster Number is -1 for a Node i . It means that the Node i is itself a cluster
4) It shows you the clusters with labels in a separate window.

# On any Graph 

Program - CommunityDetectionAlgorithmImplementation.py

Report.xlsx : This report shows how the running time varies with repect to the number of nodes and edges in the Graph.
