class Solution(object):
    def prisonAfterNDays(self, cells, n):
        
        record=[]
        seen,count=0,0
        while seen==0:
            temp=[]
            temp.append(0)
            for i in range(1,7):
                if cells[i-1]==cells[i+1]:
                    val=1
                else:
                    val=0
                temp.append(val)
            temp.append(0)
            cells=tuple(temp)
            if cells in record:
                seen=1
            else:
                record.append(cells)
                count+=1
        
        return record[(n-1)%count]
        
        """
        
        
        :type cells: List[int]
        :type n: int
        :rtype: List[int]
        """
        