from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list) 
        for w in strs:
            key = "".join(sorted(w))
            hashMap[key].append(w)
        
        res = []

        for arr in hashMap.values():
            res.append(arr)
        return res


'''
what if we stored the string and that strs chars freq in a hashmap

act:[a:1, c:1, t: 1]
cat: [a:1, c:1, t: 1]
its the same so group them as anangram

time and space too slow on this approach

wait what if we flipped it

freq as key and word as val

then grouping becomes simpler

[a:1, c: 1, t: 1] : ["cat"], [o:1,p:1,s:1,t:1] : ["pots", "tops"]

counter as key is not hashable
so sorting the word and making it the key is better
"act" : ["cat", "act"]
this is much simpler



'''