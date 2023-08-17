class Solution:
    def intToRoman(self, num: int) -> str:
        read = str(num)
        n = len(read)
        ans = ''
        # 9, 4, 5, 1
        convert = [['IX', 'IV', 'V', 'I'], ['XC', 'XL', 'L', 'X'], ['CM', 'CD', 'D', 'C']]
        for i in reversed(range(n)):
            # 3 - 0
            digit = int(read[n - 1 - i])
            print(i, digit)
            if i == 3:
                ans += digit * 'M'
            else:
                roms = convert[i]
                if digit == 9:
                    ans += roms[0]
                elif digit == 4:
                    ans += roms[1]
                else:
                    if digit >= 5:
                        ans += roms[2]
                        digit -= 5
                    ans += digit * roms[3]
        return ans
# Comment: Dictionary would have been way easier, although this is not the worst...?

