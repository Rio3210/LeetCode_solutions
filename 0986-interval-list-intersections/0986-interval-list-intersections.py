class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        i, j = 0, 0
        result = []
        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]
        
            if a_start <= b_end and b_start <= a_end:
          
                  result.append([max(a_start, b_start), min(a_end, b_end)])

            if a_end <= b_end:
                  i += 1
            else:
                  j += 1
        return result
            
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        