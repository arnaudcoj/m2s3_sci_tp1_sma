class Environment(object):
    """docstring for Environment"""
    def __init__(self, gridSizeX, gridSizeY, torus):
        super(Environment, self).__init__()
        self.initGrid(gridSizeX, gridSizeY, torus)

    def initGrid(self, gridSizeX, gridSizeY, torus):
        self.grid = []
        for i in range(gridSizeX):
            self.grid.append([None] * gridSizeY)
        self.grid[0][1] = True
        print("The grid of size", gridSizeX, gridSizeY, "has successfully been created.")

    def getFreeCells(self):
        freeCells = []
        for i in range(self.getNbCol()):
            for j in range(self.getNbRow()):
                if self.grid[i][j] == None:
                    freeCells.append((i,j))
        return freeCells

    def getNbRow(self):
        return len(self.grid[0])

    def getNbCol(self):
        return len(self.grid)

    def printASCII(self):
        print(self.getNbCol(), self.getNbRow())

        #First Line
        print("+", end="")
        for i in range(self.getNbCol()):
            print("-+", end="")

        #Intermediate Lines
        for j in range(self.getNbRow()):
            print("\n|", end="")
            for i in range(self.getNbCol()):
                if self.grid[i][j] :
                    print("X", end="")
                else:
                    print(" ", end="")
                print("|", end="")
            print("\n+", end="")
            for i in range(self.getNbCol()):
                print("-+", end="")

        #End
        print("")

#env = Environment(4,2,True)
#env.printASCII()
#print(env.getFreeCells())