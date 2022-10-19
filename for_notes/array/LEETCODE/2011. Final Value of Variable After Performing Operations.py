class Solution:
    # def finalValueAfterOperations(self, operations: List[str]) -> int:
    def finalValueAfterOperations(operation):
        x = 0
        for i in operation:
            if "+" in i:
                x += 1
            if "-" in i:
                x -= 1
        return x
    operations = ["--X", "X++", "X++"]
    print(finalValueAfterOperations(operations))

