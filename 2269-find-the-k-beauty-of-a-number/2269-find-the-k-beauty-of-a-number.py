class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        digits=str(num)
        count=0
        for i in range(len(digits)):
            for j in range(i,len(digits)+1):
                sub=digits[i:j]
                if len(sub)==k:
                    div=int(sub)
                    if div!=0 and num%div==0:
                        count+=1
        return count