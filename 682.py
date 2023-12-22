# Logic:
# This ones pretty simple, but the idea is that it's a stack problem. Adding items to the stack and certain items rely on the stack items before it (+ and D).
# Remember to cast operation as int since they're strings in the operations array

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        
        for op in operations:
            if op == '+':
                record.append(record[-1] + record[-2])
            elif op == 'D':
                record.append(2 * record[-1])
            elif op == 'C':
                record.pop()
            else:
                record.append(int(op))
                
        return sum(record)