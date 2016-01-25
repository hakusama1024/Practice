class Solution(object):
    def numIslands2(self, m, n, positions):
    
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
    
        def union(a, b):
            x, y = find(a), find(b)
            if x != y:
                if rank[x] < rank[y]:
                    parent[x] = y
                else:
                    parent[y] = x
                    rank[x] += 1 if rank[x] == rank[y] else 0
            return x != y
    
        idx = lambda x, y: x * n + y
        parent = range(idx(m, n))
        rank = [0] * idx(m, n)
        matrix = [[0] * n for _ in xrange(m)]
    
        ret = []
        for a, b in positions:
            matrix[a][b] = 1
            cnt = ret[-1] + 1 if ret else 1
            for x, y in (a+1, b), (a-1, b), (a, b+1), (a, b-1):
                if 0 <= x < m and 0 <= y < n and matrix[x][y] and union(idx(a, b), idx(x, y)):
                    cnt -= 1
            ret.append(cnt)
    
        return ret
