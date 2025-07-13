from collections import defaultdict
import heapq
class WeightedGraph:
    def __init__(self):
        self.graph=defaultdict(list)
        
    
    def add_user(self,user):
       pass
            
    def add_connection(self,user1,user2,weight=1):
       
        self.graph[user1].append((user2,weight))
        self.graph[user2].append((user1,weight))
    
    def get_connections(self,user):
        return self.graph.get(user,[])
    
    def get_weighted_suggestions(self,user,k=5):
        mutual_suggestion=defaultdict(int)
        
        user_friends={friend for friend,_ in self.get_connections(user)}
        
        
        for friend,w1 in self.get_connections(user):
            for mutual,w2 in self.get_connections(friend):
                if mutual==user or mutual in user_friends:
                    continue
                mutual_suggestion[mutual]+=(w1+w2)
        # print(mutual_suggestion)
        heap=[(-score,users) for users,score in mutual_suggestion.items()]
        heapq.heapify(heap)
        # print(heap)
        top_k=[]
        
        for _ in range(min(k,len(heap))):
            score,person=heapq.heappop(heap)
            top_k.append([person,-score])
        return top_k
                
                
                    
        