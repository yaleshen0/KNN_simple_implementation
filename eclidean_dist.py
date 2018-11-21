from matplotlib import pyplot as plt
import numpy as np
import collections
def euclidean(a,b):
	return np.linalg.norm(a-b)
def returnKNear(arr, targetP, k):
	dist = {}
	for i in arr:
		dist[euclidean(i[0],targetP[0])] = i[1]
	return {k: dist[k] for k in sorted(dist.keys())[:k]}
def orderdic(dic, reverse):
    ordered_list = sorted(
        dic.items(), key=lambda item: item[0], reverse=reverse)
    label_counts = {}
    for i in ordered_list:
    	label_counts[i[1]] = label_counts.get(i[1],0)+1
    # label, counts = np.unique(ordered_list, return_counts=True)
    return sorted(label_counts)[0]
    # for i in np.array(ordered_list)
    # print(collections.Counter(ordered_list))
# define data points and target point
a1 = [np.array([1,1]), 'A']
a2 = [np.array([1,2]), 'A']
b1 = [np.array([3,3]), 'B']
b2 = [np.array([3,4]), 'B']
# define points to corresponding class
p_arr = [a1,a2,b1,b2]
c = [np.array([2,1]), 'A']
first_k = returnKNear(p_arr,c,2)
find_label = orderdic(first_k, True)
if find_label == c[1]:
	print('KNN result is correct')