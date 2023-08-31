class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        def is_bound(row,col):
            return (0<=row<len(image)) and (0<=col<len(image[0]))
        def helper(image,sr,sc):
            if is_bound(sr,sc) and image[sr][sc] == original_color:
                image[sr][sc]=color
                for row,col in direction:
                    helper(image,sr+row,sc+col)
        
        if original_color!=color:  
            helper(image,sr,sc)
        return image 
            
            
            
                
                
            