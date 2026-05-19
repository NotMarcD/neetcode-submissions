# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # divide step
        if len(pairs) <= 1:
            return pairs

        middle = len(pairs) // 2
        left = self.mergeSort(pairs[:middle])
        right = self.mergeSort(pairs[middle:])
        
        #conquer step
        merge_arr = self.merge(left, right)

        return merge_arr


    def merge(self,left: List[Pair], right: List[Pair]) -> List[Pair]:
        merged = []

        lpointer = 0
        rpointer = 0
        while lpointer < len(left) and rpointer < len(right):
            if left[lpointer].key <= right[rpointer].key:
                merged.append(left[lpointer])
                lpointer+=1
            else:
                merged.append(right[rpointer])
                rpointer+=1
        if lpointer == len(left):
            print(merged + right[rpointer:])
            return merged + right[rpointer:]
        else:
            print(merged + left[lpointer:])
            return merged + left[lpointer:]
