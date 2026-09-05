INT_MAX = 2147483647
INT_MIN = -2147483648

class Solution:
    @staticmethod
    def trimWS(s: str) -> str:
        chars = list(s)
        while chars[0] == " ":
            chars.pop(0)
            if len(chars) == 0:
                break

        return "".join(chars)

    def trimZeroes(s: str) -> str:
        chars = list(s)
        while chars[0] == "0":
            chars.pop(0)
            if len(chars) == 0:
                break
        return "".join(chars)

    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0

        answer = 0
        positive_sign = True

        strNoWS = Solution.trimWS(s)

        if strNoWS == "":
            return 0

        if strNoWS[0] == "+":
            strNoWS = strNoWS.removeprefix("+")
        elif strNoWS[0] == "-":
            positive_sign = False
            strNoWS = strNoWS.removeprefix("-")

        if strNoWS == "":
            return 0

        if not strNoWS[0].isdecimal():
            # no digits
            return 0

        # if we get here, we have a decimal in chars[0]

        strNoWS = Solution.trimZeroes(strNoWS)

        if strNoWS == "":
            return 0

        # no more leading zeros after this point

        if not strNoWS[0].isdecimal():
            # answer is zero
            return 0

        last_digit_idx = 0

        for i in range(len(strNoWS)):
            if strNoWS[i].isdecimal() and i < 10:
                last_digit_idx = i
                continue
            elif i > 9:
                # over 10 chars exceeds int min/max (2147483647)
                if strNoWS[i].isdecimal():
                    last_digit_idx = i
                break
            else:
                break

        if last_digit_idx > 9:
            if positive_sign:
                return INT_MAX
            else:
                return INT_MIN

        validNumStr = strNoWS[0:last_digit_idx+1]
        length = len(validNumStr)

        for i in range(length):
            answer = answer + (10**i) * int(validNumStr[length-i-1])

        if positive_sign and answer > INT_MAX:
            return INT_MAX

        if not positive_sign:
            answer = -1 * answer
            if answer < INT_MIN:
                return INT_MIN

        return answer