class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, it's impossible for s2 to contain a permutation of s1
        if len(s1) > len(s2):
            return False

        # Frequency arrays for characters 'a' to 'z'
        s1Count, s2Count = [0] * 26, [0] * 26

        # Initialize counts for s1 and the first window of s2 (same length as s1)
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # Count how many character frequencies currently match between s1Count and s2Count
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # Left pointer of the sliding window
        l = 0
        # Expand window from len(s1) to len(s2)
        for r in range(len(s1), len(s2)):
            # If all 26 characters match, we found a valid permutation
            if matches == 26:
                return True

            # Add new character on the right side of the window
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            # Update matches count based on this new character
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # Remove old character on the left side of the window
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            # Update matches count based on this removed character
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            # Move the left pointer forward
            l += 1

        # Final check after sliding through entire s2
        return matches == 26
