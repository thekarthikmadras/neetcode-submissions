class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            start = i 
            while stack and t > stack[-1][-1]:
                stackInd, stackTemp = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((i, t))
        return res