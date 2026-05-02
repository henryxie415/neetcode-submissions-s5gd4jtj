class Solution:
    def minOperations(self, logs: List[str]) -> int:
        total = 0
        for log in logs:
            if log == "../":
                if total > 0:
                    total -= 1
                else:
                    continue
            elif log == "./":
                continue
            else:
                total += 1
        return total 