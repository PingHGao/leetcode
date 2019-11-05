class Solution:
    def exist(self, B: List[List[str]], W: str) -> bool:
        m, n, l = len(B), len(B[0]), len(W)

        def DFS(i, j, c, pt):
            if B[i][j] != W[c]:
                return False
            pt.append([i, j])
            if c == l - 1:
                return True

            inrange = lambda x, l, r: (x >= l and x <= r)
            for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                if inrange(x, 0, m - 1) and inrange(y, 0, n - 1) and [x, y] not in pt:
                    if DFS(x, y, c + 1, pt):
                        return True
            else:
                del pt[-1]
                return False

        from itertools import product
        for x, y in product(range(m), range(n)):
            res = DFS(x, y, 0, [])
            if res:
                return True
        else:
            return False
