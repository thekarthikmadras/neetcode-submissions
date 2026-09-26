class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            store[nums[i]] = 1 + store.get(nums[i], 0)
        freq = [[] for i in range(len(nums)+1
        )]
        for number, count in store.items():
            freq[count].append(number)
        print(freq)
        res = []
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res