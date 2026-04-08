class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Step 1: Length check
        if len(s) != len(t):
            return False

        freq = {}

        # Step 2: Add frequency from the first word
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Step 3: Subtract frequency using the second word
        for ch in t:
            if ch not in freq:
                return False  # character not present at all
            freq[ch] -= 1
            if freq[ch] < 0:
                return False  # character used too many times

        # Step 4: If everything balanced, it's an anagram
        return True

