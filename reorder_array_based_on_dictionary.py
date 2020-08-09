import collections
def reorder(employees, order):
	p_map = collections.defaultdict(list)
	c_map = collections.defaultdict(list)
	d = collections.defaultdict(list)

	for item in order:
		p_map[item[0]].append(item[1])
		c_map[item[1]].append(item[0])
	print(p_map)
	print(c_map)

	for name,rank in employees:
		d[rank].append(name)


	root = ""
	for rank in d.keys():
		if(rank not in p_map.keys()):
			root = rank

	print(d)
	print(root)
	q=[root]

	res=[]
	while(q):
		print(q)
		node = q.pop(0)
		res+=([(x,node) for x in d[node]])

		if(node in c_map):
			for child in c_map[node]:
				q.append(child)

	print(res[::-1])

print(reorder([('John', 'Manager'), ('Sally', 'CTO'), ('Sam', 'CEO'), ('Drax', 'Engineer'), ('Bob', 'CFO'), ('Daniel', 'Engineer')], [['CTO', 'CEO'], ['Manager', 'CTO'], ['Engineer', 'Manager'], ['CFO', 'CEO']]))
