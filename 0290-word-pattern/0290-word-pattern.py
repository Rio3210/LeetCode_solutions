class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list1=s.split(' ')
        print(list1)
        print(len(pattern))
        print(len(list1))
        
        # if len(pattern)!=len(list1):
        #     return False
        ind = [[] for i in range(len(pattern))]
        indices = [[] for i in range(len(list1))]
        for item_to_find in range(len(list1)):          
            for idx, value in enumerate(list1):
                if value == list1[item_to_find]:
                    indices[item_to_find].append(idx)
        print(indices)
        
        # indices = [[] for i in range(len(list1))]
        
        for item_to_find in range(len(pattern)):          
            for idx, value in enumerate(list(pattern)):
                if value == list(pattern)[item_to_find]:
                    ind[item_to_find].append(idx)
                    
        print(ind)
        return indices==ind
        
#         ind = [[0] for i in range(len(pattern))]
#         for item_to_find in range(len(list(pattern)):
                                  
                                  
#             for idx, value in enumerate(list(pattern)):
                                  
#                 if value == list(pattern)[item_to_find]:
                                  
#                     ind[item_to_find].append(idx)
#         print(ind)
        # for i in range(len(pattern)):
            