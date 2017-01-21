# Code

## Description

https://leetcode.com/problems/island-perimeter/

## Python Solution
```
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if i == 0 or grid[i - 1][j] == 0:
                        perimeter += 1
                    if j == 0 or grid[i][j - 1] == 0:
                        perimeter += 1
                    if i == len(grid) - 1 or grid[i + 1][j] == 0:
                        perimeter += 1
                    if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                        perimeter += 1
        return perimeter
```

another way from discussion:
```
int islandPerimeter(vector<vector<int>>& grid) {
    int count=0, repeat=0;
    for(int i=0;i<grid.size();i++)
    {
        for(int j=0; j<grid[i].size();j++)
            {
                if(grid[i][j]==1)
                {
                    count ++;
                    if(i!=0 && grid[i-1][j] == 1) repeat++;
                    if(j!=0 && grid[i][j-1] == 1) repeat++;
                }
            }
    }
    return 4*count-repeat*2;
}
```
