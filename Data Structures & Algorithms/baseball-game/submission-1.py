class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        total = 0

        for op in operations:
            if op == "+":
                tmp = record[-1] + record[-2]
                record.append(tmp)
                total += tmp
            elif op == "C":
                total -= record[-1]
                record.pop()
            elif op == "D":
                tmp = record[-1]*2
                record.append(tmp)
                total += tmp
            else:
                record.append(int(op))
                total += int(op)

        return total