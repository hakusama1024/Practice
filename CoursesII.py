def findOrder(numCourses,prerequisites):
	d={}
	for i in prerequisites:
		if i[0] not in d:
			d[i[0]]=[i[1]]
			if i[1] not in d:
				d[i[1]]=[]
		else:
			d[i[0]].append(i[1])
	res=[]
	while d:
		for i in range(numCourses):
			if d[i] == []:
				res.append(d[i])
				tmp=d[i]
				del d[i]
				for j in d:
					if tmp in d[j]:
						del d[j][tmp]
	print res

p = [[1,0],[2,0],[3,1],[3,2]]
n = 4
findOrder(n, p)
