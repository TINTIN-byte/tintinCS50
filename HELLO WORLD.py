class Player:
    
    def __init__(self, gk,cb,m,st):
        self.gk=gk
        self.cb=cb
        self.m=m
        self.st=st
        
    def team(self):
        return'{} {} {} {}'.format(self.gk,self.cb,self.m,self.st)
        
team1=Player('Never','Alaba','Kaka', 'CR7')

print(team1.gk,'and',team1.st)



  
     


