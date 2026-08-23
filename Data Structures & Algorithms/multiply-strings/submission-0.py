class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        to_ascii = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
        }       

        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):

                product = to_ascii[num1[i]] * to_ascii[num2[j]]

                p1 = i + j
                p2 = i + j + 1

                # There may already be a value here
                total = product + res[p2]

                # ones digit
                res[p2] = total % 10

                # carry
                res[p1] += total // 10

        # remove leading zero
        if res[0] == 0:
            res = res[1:]

        return "".join(str(digit) for digit in res)