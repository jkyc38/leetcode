class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        hashset = {}
        grouped_lists = []
        for str in strs:
            sortedstr = ''.join(sorted(str))
            hashset[sortedstr] = []
            
        for str in strs:
            sortedstr = ''.join(sorted(str))
            if sortedstr in hashset:
                hashset[sortedstr].append(str)
            
        for key in hashset:
            grouped_lists.append(hashset[key])

        return grouped_lists
       




sol = Solution()
case = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
print(f'Test Case: {case}')
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

