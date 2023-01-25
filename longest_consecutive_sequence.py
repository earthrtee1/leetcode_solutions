class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest_sequence = 0
        for i in numSet:
            match (i + longest_sequence) in numSet:
                case True:
                    current_sequence = 0
                    while True:
                        print(current_sequence)
                        match (i+current_sequence) in numSet:
                            case True:
                                current_sequence += 1
                            case False:
                                if current_sequence > longest_sequence:
                                    longest_sequence = current_sequence
                                break
        return(longest_sequence)
