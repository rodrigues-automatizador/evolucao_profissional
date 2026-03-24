class HealCheck:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not HealCheck._instance:
            HealCheck._instance = super(HealCheck, cls).__new__(cls, *args, **kwargs)
            
        return HealCheck._instance
    
    def __init__(self):
        self._servers = []
        
    def addServer(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")
        
    def changeServer(self):
        self._servers.pop()
        self._servers.append("Server 5")
        
hc1 = HealCheck()
hc2 = HealCheck()

hc1.addServer()
print("Schedule health check for servers (1)...")

for i in range(4):
    print("Checking ", hc1._servers[i])
    
hc2.changeServer()
print("Schedule health check for servers (2)...")

for i in range(4):
    print("Checking ", hc2._servers[i])