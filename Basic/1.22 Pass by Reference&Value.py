class Solution:
    def passedBy(self, a, b):
        # Pass by value simulation: a is modified but won't affect the original variable
        a += 1
        
        # Pass by reference simulation: b is modified and the change is returned
        b += 2
        
        return a, b

sol = Solution()
a = 10
b = 20
result = sol.passedBy(a, b)
print(result)  # Output: (11, 22)
