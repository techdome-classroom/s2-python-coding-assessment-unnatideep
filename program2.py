class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Mapping of Roman numerals to their integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate over the Roman numeral string in reverse
        for char in reversed(s):
            current_value = roman_map[char]
            # Determine if we should add or subtract the current value
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value
        
        return total

# Example usage:
# sol = Solution()
# print(sol.romanToInt("III"))      # Output: 3
# print(sol.romanToInt("LVIII"))    # Output: 58
# print(sol.romanToInt("MCMXCIV"))  # Output: 1994
