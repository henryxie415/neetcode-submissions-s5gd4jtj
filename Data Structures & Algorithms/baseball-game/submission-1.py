class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        total = 0
        mult = 1
        j = 0
        for i in range(len(operations)):

            try:
                num = int(operations[i])
                arr.append(num)
            except ValueError:
                pass
            #if + add the last two to form number and add to list
            if operations[i] == "+":
                total = arr[- 1] + arr[- 2]
                arr.append(total)
            #if C pop from result
            elif operations[i] == "C":
                arr.pop()
            #if D add double the previous result 
            elif operations[i] == "D":
                mult = arr[- 1] * 2
                arr.append(mult)
            #go through the new list and sum all the numbers
            print(arr)
        combined = sum(arr)
        return combined