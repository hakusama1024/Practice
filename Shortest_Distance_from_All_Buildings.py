class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n, self.nth = len(grid), len(grid[0]), -1
        distance = [ [0]*n for dummy in xrange(m) ]

        for i,row in enumerate(grid):
            for j, num in enumerate(row):
                if num==1:
                    if self.helper(i,j,grid,distance)==False:
                        return -1


        return min([ distance[i][j]
                 for i, row in enumerate(grid)
                 for j, num in enumerate(row)
                 if num == (self.nth+1) ] or [-1] )

    def helper(self, i, j, grid, distance):
        m, n = len(grid), len(grid[0])
        queue, level, nth = collections.deque( [(i,j)] ), 1, self.nth

        count = 0
        while queue:
            for dummy in xrange(len(queue)):
                i, j = queue.popleft()

                for x, y in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nexti, nextj = i+x, j+y
                    if 0<= nexti <m and 0<=nextj<n and grid[nexti][nextj]==(nth+1):
                        count += 1
                        queue.append( (nexti,nextj) )

                        distance[nexti][nextj] += level
                        grid[nexti][nextj] = nth
            level += 1

        self.nth -= 1

        return True if count!=0 else False
