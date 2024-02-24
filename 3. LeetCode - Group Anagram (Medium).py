# Solution 1
def group_anagrams(strs):
    grouped_anagrams = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word in grouped_anagrams:
            grouped_anagrams[sorted_word].append(word)
        else:
            grouped_anagrams[sorted_word] = [word]
    return list(grouped_anagrams.values())

# Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))


# Solution 2

# Without the necessity to check upon keys in dictionary

from collections import defaultdict

def group_anagrams(strs):
    grouped_anagrams = defaultdict(list)
    for word in strs:
        grouped_anagrams[''.join(sorted(word))].append(word)
    return list(grouped_anagrams.values())

# Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))

