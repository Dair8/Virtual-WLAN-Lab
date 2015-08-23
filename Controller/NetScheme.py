class NetScheme:
    netList={}
    
    def __init__(self,hosts,neighbors):
        j=0
        for i in hosts:
            self.setNeighbors(i,neighbors[j])
            j=j+1
        
    
    def addHost(self,host):
        self.netList[host]=[]
	
    def getHost(self,i):
	return self.netList(i)    
   
    def delHost (self,host):
        self.netList.pop(host)	
	
    def getHosts (self):
	return self.netList.keys()
                    
    def printHosts(self):
        print(self.netList.keys())
            
    def setNeighbors(self,host,neighbors):
        self.netList[host]=[neighbors]
            
    def getNeighbors(self,host):
        return self.netList[host]

    def delNeighbors(self,host):
        self.netList[host]=[]
            
    def printScheme(self):
        for j in self.netList:
            print"Host: %i" %j + " Neighbors: ", self.netList[j]
