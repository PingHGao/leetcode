class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        lenT = len(T)
        ans = [0] * lenT
        
        for i in range(lenT - 2, -1, -1):
            j = i + 1
            while j < lenT:
                if T[j] > T[i]:
                    ans[i] = j - i
                    break
                elif ans[j] == 0:
                    ans[i] = 0
                    break
                else:
                    j += max(1, ans[j])
            else:
                ans[i] = 0
                
        return ans
