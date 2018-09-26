# Program - Community Detection using Hierchical Clustering using Jaccard coefficient 
# as a measure of similarity
# By - Rohan Bose (Jalpaiguri Govt. Engg. College)
import networkx
import matplotlib.pyplot as plt

def hierchical_clustering(G):
	E = list(G.edges())
	J = networkx.jaccard_coefficient(G, E)
	clusters= [-1]*len(G)
	cluster_number=-1
	print "Please choose a threshold value by looking at the jaccard similarity value"
	
	for u, v, k in J:
		print '(%d, %d) -> %.8f' % (u, v, k)

	threshold_value = float(raw_input())

	while(True):
		length = networkx.all_pairs_shortest_path_length(G)
		length = dict(length)
		value = 9000000 # set this as infinity
		final_s = -1
		final_t = -1
		for source in length:
			for target in length[source]:
				val = length[source][target]
				if val!=0 and value > val:
					value = val
					final_s = source
					final_t = target

		min_node = min(final_s, final_t)
		max_node = max(final_s, final_t)
		E = list(G.edges())
		
		# print "The min_node is %d", min_node
		# print "The max_node is %d", max_node		
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

		value = 900000 # set as infinity
		num=0
		for u, v, k in J:
			if k>threshold_value and k<value:
				value = k
				num+=1
		
		if num==0:
			break


	print "#"*60
	print "\n"*3
	print "The clusters are \n \n(If the cluster NUmber is shown as -1 , then it means that it itself is a cluster)"
	print "\n"*3
	print "#"*60
	print "\n"*3
	i=0
	for u in clusters:
		print 'The node ',i ,'belongs to the cluster number', u
		i+=1

	networkx.draw(G,  with_labels=1)
	plt.show()


G = networkx.karate_club_graph()
networkx.draw(G, with_labels=1)
plt.show()
hierchical_clustering(G)