class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1, i1 = num1.split("+")
        r2, i2 = num2.split("+")
        in1 = i1.rstrip("i")
        in2 = i2.rstrip("i")

        n1 = int(r1) * int(r2)
        n2 = int(r1) * int(in2) + int(in1) * int(r2)
        n3 = -1 * (int(in1) * int(in2))

        return f"{n1+n3}+{n2}i"
