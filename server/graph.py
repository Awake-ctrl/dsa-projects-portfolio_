
class Graph:
    def __init__(self):
        self.graph={}
        
    
    def add_user(self,user):
        if user not in self.graph:
            self.graph[user]=[]
            
    def add_connection(self,user1,user2):
        if user1 in self.graph and user2 in self.graph:
            self.graph[user1].append(user2)
            self.graph[user2].append(user1)
    
    def get_connections(self,user):
        return self.graph.get(user,[])
    
    def get_suggestions(self,user):
        suggestion=set()
        
        for friend in self.get_connections(user):
            for potential_friend in self.get_connections(friend):
                if potential_friend!=user and potential_friend not in self.get_connections(user):
                    suggestion.add(potential_friend)
        return list(suggestion)
                
                    
        