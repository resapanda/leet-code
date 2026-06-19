# NeetCode Problem #0004: [Group Anagrams]
# Difficulty: [Medium]
# Date: [06/18/2026]
# Time: [24m]
# Topic: [Array & Hashing]

## Intuition & Approach
# The Core Idea: Sort each string and store it hashmap from sorted string to original word.
## Complexity Analysis
# Time Complexity: O(N log N * M)
# Why: We use sroted() for M strings and the worst case of sort time complexity is n log n.
# Space Complexity: O(N * M)
# Why: sorted() create a new list for M strings.

# Code
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        word_map = {}
        res = []

        for s in strs:
            key = ''.join(sorted(s))
            word_map[key] = word_map.get(key, [])
            word_map[key].append(s)

        for key in word_map:
            res.append(word_map[key])

        return res

# Solution - using hash table
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] +=1
            res[tuple(count)].append(s)
        return list(res.values())
'''

# previpus solution
'''
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        check = {}

        # counts each alphabet and make a hashtable -> e.g. {a:1, b:1}
        for idx in range(len(strs)):
            counts = {}
            for i in range(len(strs[idx])):
                counts[strs[idx][i]] = 1 + counts.get(strs[idx][i], 0)

            # sort the map alphabetically
            sorted_counts = dict(sorted(counts.items()))

            # hash the counts -> key: counts, val: values of strs
            check[tuple(sorted_counts.items())] = check.get(tuple(sorted_counts.items()), [])
            check[tuple(sorted_counts.items())].append(strs[idx])

        # iterate the hashtable and make it as an array
        result = []
        for key in check:
            result.append(check.get(key))

        return result
'''

if __name__ == "__main__":
    s = Solution()
    strs1 = ["act","pots","tops","cat","stop","hat"]
    print(f"Test 1 Result: {s.groupAnagrams(strs1)}")  # Expected Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

    strs2 = ["x"]
    print(f"Test 2 Result: {s.groupAnagrams(strs2)}")  # Expected Output: [["x"]]

    strs3 = [""]
    print(f"Test 2 Result: {s.groupAnagrams(strs3)}")  # Expected Output: [[""]]