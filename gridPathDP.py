grid = {}
def gridPaths(m,n):
    """This function tells all the possible ways to reach from (0,0) to (n,n)
        (m,n) --> Target & (x,y) -->hole """
    (x,y) = (2,4)
    if(m==2 and n==4):
        return 0
    if (m,n) in grid:
        return grid[(m,n)]
    if(m==0 or n==0):  # Boundary grid points
        return 1
    else:
        result = gridPaths(m-1,n) + gridPaths(m,n-1)
        grid[(m,n)] = result
        return(result)


print(gridPaths(5,10))