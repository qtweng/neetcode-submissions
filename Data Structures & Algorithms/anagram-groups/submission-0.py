class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for i in strs:
            sort = "".join(sorted(i))
            groups[sort].append(i)
        return list(groups.values())
            