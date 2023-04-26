import networkx as nx
import numpy as np

# GMmodel
def GMmodel(G, risk):
	N = len(G.nodes)
	Node = G.nodes()
	S = np.zeros((N, N))
	result = [0 for i in range(N)]
	# 在全部节点中标记哪些节点为已知重要节点
	vital = [0 for i in range(N)]
	for i, num in enumerate(Node):
		if num in risk:
			vital[i] = 1
	# 计算得分矩阵S
	for i, item1 in enumerate(Node):  # 创建图G的邻接矩阵，即为a
		for j, item2 in enumerate(Node):
			if i != j:
				S[i][j] = nx.degree(G, item1) * nx.degree(G, item2) / nx.shortest_path_length(G, source=item1, target=item2)
			else:
				S[i][j] = 0
	# 计算result
	for i, item1 in enumerate(S):
		for j, item2 in enumerate(S):
			if vital[j] == 0:
				result[i] += S[i][j]
	return result

# GMmodel_plus(NEGM)
def GMmodel_plus(G, risk, vector):
	# 计算欧式距离
	def dist(x, y):
		res1 = np.array(x)
		res2 = np.array(y)
		return np.sqrt(sum((res1 - res2) ** 2))

	N = len(G.nodes)
	Node = G.nodes()
	S = np.zeros((N, N))
	result = [0 for i in range(N)]
	# 在全部节点中标记哪些节点为已知重要节点
	vital = [0 for i in range(N)]
	for i, num in enumerate(Node):
		if num in risk:
			vital[i] = 1
	# 计算得分矩阵S
	for i, item1 in enumerate(Node):  # 创建图G的邻接矩阵，即为a
		for j, item2 in enumerate(Node):
			if i != j:
				S[i][j] = nx.degree(G, item1) * nx.degree(G, item2) / dist(vector[i], vector[j])
			else:
				S[i][j] = 0
	# 计算result
	for i, item1 in enumerate(S):
		for j, item2 in enumerate(S):
			if vital[j] == 0:
				result[i] += S[i][j]
	return result