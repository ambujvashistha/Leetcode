class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        gb=[]
        prev_start=intervals[0][0]
        prev_end=intervals[0][1]
        gb.append([prev_start,prev_end])
        for i in range(1,len(intervals)):
            start,end=intervals[i][0],intervals[i][1]
            if start<=prev_end and end>=prev_end and start>=prev_start:
                prev_end=end
                gb[-1][1]=end
            elif start<=prev_end and end<=prev_end:
                pass
            else:
                gb.append([start,end])
                prev_start=start
                prev_end=end
        return gb
