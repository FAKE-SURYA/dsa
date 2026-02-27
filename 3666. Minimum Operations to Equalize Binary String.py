class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z0 = s.count('0')
        if z0 == 0:
            return 0

        from collections import deque
        INF = 10**9
        dist = [INF] * (n + 1)

        # build parity sets
        import bisect
        even = [x for x in range(n + 1) if x % 2 == 0]
        odd  = [x for x in range(n + 1) if x % 2 == 1]
        S = [even, odd]

        # helper: remove element from list by index; we will erase ranges
        # but in practice you want to scan in range and pop by index.

        # mark start as visited: remove z0 from its parity list
        p0 = z0 & 1
        arr = S[p0]
        idx = bisect.bisect_left(arr, z0)
        if idx < len(arr) and arr[idx] == z0:
            arr.pop(idx)

        dist[z0] = 0
        q = deque([z0])

        while q:
            z = q.popleft()
            if z == 0:
                return dist[z]

            L = max(0, k - (n - z))
            R = min(k, z)
            if L > R:
                continue

            z_max = z + k - 2 * L
            z_min = z + k - 2 * R

            p = (z + k) & 1
            arr = S[p]

            # find all unvisited states v in [z_min, z_max] in arr
            # arr is sorted, so use bisect to get left index and then walk
            left = bisect.bisect_left(arr, z_min)
            # then while left < len(arr) and arr[left] <= z_max:
            #   v = arr[left]
            #   dist[v] = dist[z] + 1
            #   q.append(v)
            #   arr.pop(left)  # careful: popping shifts indices, so do not increment left

            i = left
            while i < len(arr) and arr[i] <= z_max:
                v = arr[i]
                dist[v] = dist[z] + 1
                q.append(v)
                arr.pop(i)
                # don't increment i, because the next element has moved into position i

        return -1
