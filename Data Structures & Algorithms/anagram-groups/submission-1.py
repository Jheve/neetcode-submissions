class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        # defaultdict(list) acts like a normal dict, but automatically creates
        # an empty list for any new key —> don't have to manually check
        # "if key not in dict" before appending.
        output = defaultdict(list)

        for s in strs:
            # use sorted version of string as a fingerprint (key) to group
            sorted_str = ''.join(sorted(s))
            # append the ORIGINAL string (not the sorted one) under that key
            output[sorted_str].append(s)
        
        return list(output.values())