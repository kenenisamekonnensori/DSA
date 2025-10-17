class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)
        # 1. Skip whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check if string is empty
        if i == n:
            return 0

        # 3. Check sign
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1

        # 4. Convert digits
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        # 5. Apply sign
        num *= sign

        # 6. Clamp to 32-bit signed integer
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num
