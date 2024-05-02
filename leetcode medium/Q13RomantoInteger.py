class Solution:
    @staticmethod
    def romanToInt(s: str) -> int:
        # Mapping Roman numerals to their integer values
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        # Process each character except the last one
        for i in range(len(s) - 1):
            current_value = roman_values[s[i]]
            next_value = roman_values[s[i + 1]]
            # If current value is less than next, we know we have to subtract
            if current_value < next_value:
                total -= current_value
            else:
                total += current_value
        
        # Add the value of the last numeral
        total += roman_values[s[-1]]
        
        return total

# Examples of using the class and method
solution = Solution()
print(solution.romanToInt("III"))    # Output: 3
print(solution.romanToInt("LVIII"))  # Output: 58
print(solution.romanToInt("MCMXCIV"))# Output: 1994
