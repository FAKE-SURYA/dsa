class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        ans = 0

        for i in range(m):
            # update heights for this row
            for j in range(n):
                if matrix[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            # sort heights in descending order to simulate best column rearrangement
            sorted_heights = sorted(heights, reverse=True)

            # try all possible widths
            for width in range(n):
                h = sorted_heights[width]
                if h == 0:
                    break  # no more area possible in this row
                area = h * (width + 1)
                if area > ans:
                    ans = area

        return ans
