class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = []

        def combinate(output, s, n, l, r):
            if l == n:
                while r < n:
                    s += ')'
                    r += 1
                if r == n:
                    output.append(s)
                    return
            else:
                if r > l:
                    print('error')
                elif r == l:
                    combinate(output, s + '(', n, l+1, r)
                else: 
                    combinate(output, s + '(', n, l+1, r)
                    combinate(output, s + ')', n, l, r+1)
        combinate(output, '', n, 0, 0)
        return output

# Runtime: Details 36ms - Beats 93.92%of users with Python3
# Memory: Details 16.48mb - Beats 99.05%of users with Python3