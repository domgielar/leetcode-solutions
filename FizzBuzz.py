class Solution(object):
    def fizzBuzz(self, n):
        result = []
        for index in range(1, n+1):
            if index % 3 == 0 and index % 5 == 0:
                result.append("FizzBuzz")
            elif index % 3 == 0:
                result.append("Fizz")
            elif index % 5 == 0:
                result.append("Buzz")
            
            else:
                result.append(str(index))
        return result


sol = Solution()
print(sol.fizzBuzz(15))
