# Program - Community Detection using Hierchical Clustering using Jaccard coefficient 
# as a measure of similarity
# By - Rohan Bose (Jalpaiguri Govt. Engg. College)
import networkx
import matplotlib.pyplot as plt
import time

def hierchical_clustering(G):
	E = list(G.edges())
	J = networkx.jaccard_coefficient(G, E)
	clusters= [-1]*len(G)
	cluster_number=-1

	# print "Please choose a threshold value by looking at the jaccard similarity value"
	# You can make the below threshold value as an input value also

	threshold_value = 0.4
	total_number_of_iterations = 0

	while(True):
		total_number_of_iterations+=1
		all_nodes = list(G.nodes())
		final_s = -1
		final_t = -1

		parent_mini=9999999999999999999999
		# start of for
		for source in all_nodes:
			# print source
			lengths = networkx.single_source_shortest_path_length(G, source)
			mini = 999999999999999999
			dest = -1
			for j in lengths:
				if lengths[j]<mini and lengths[j]!=0:
					mini = lengths[j]
					dest = j

			if mini<parent_mini:
				parent_mini=mini
				final_s = source
				final_t = dest

		# end of for		
		min_node = min(final_s, final_t)
		max_node = max(final_s, final_t)
		
		print "min_node=", min_node
		print "max_node=", max_node


		E = list(G.edges())
		
		if clusters[min_node]==-1 and clusters[max_node]==-1:
			cluster_number+=1
			clusters[min_node]=cluster_number
			clusters[max_node]=cluster_number
		elif clusters[min_node]==-1:
			clusters[min_node]=clusters[max_node]
		elif clusters[max_node]==-1:
			clusters[max_node]=clusters[min_node]
		else:
			cluster_max_node_belongs_to = clusters[max_node]
			clusters[max_node]=clusters[min_node]
			for u in clusters:
				if u==cluster_max_node_belongs_to:
					u=clusters[min_node]

		for u, v in E:
			if u==max_node and v!=min_node:
				G.add_edge(min_node, v)
			elif v==max_node and u!=min_node:
				G.add_edge(min_node, u)

		G.remove_node(max_node)
		E = list(G.edges())
		J = networkx.jaccard_coefficient(G, E)

		value = 9999999999999999 # set as infinity
		num=0
		for u, v, k in J:
			if k>threshold_value and k<value:
				value = k
				num+=1
		
		if num==0:
			break


	i=0
	unique_clusters = set()
	for u in clusters:
		i+=1
		if u==-1:
			unique_clusters.add(i)
		else :
			unique_clusters.add(u)


	print "The total number of unique clusters is", len(unique_clusters)
	print "The total number of iterations", total_number_of_iterations


start_time = time.time()
f = open("datafinal.txt")
G = networkx.Graph()
for line in f:
	num1, num2 = line.split()
	num1 = int(num1)
	num2 = int(num2)
	G.add_edge(num1, num2)
	
hierchical_clustering(G)
print("--- %s seconds ---" % (time.time() - start_time))