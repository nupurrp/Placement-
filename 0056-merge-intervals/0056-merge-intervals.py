class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return intervals
        intervals.sort()
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][1]:
                pass
            elif result[-1][1] < intervals[i][1] and result[-1][1] >= intervals[i][0]:
                result[-1][1] = intervals[i][1]
            else:
                result.append(intervals[i])
        return result       
        