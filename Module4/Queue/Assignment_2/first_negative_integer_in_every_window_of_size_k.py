from collections import deque


def printFirstNegativeInteger(A, N, K):
    q = deque()
    ans = []
    for i in range(K):
        if A[i] < 0:
            q.append(i)

    for i in range(K, N):
        if len(q) == 0:
            ans.append(0)
        else:
            ans.append(A[q[0]])

        if len(q) != 0 and q[0] == i - K:
            q.popleft()

        if A[i] < 0:
            q.append(i)

    if len(q) == 0:
        ans.append(0)
    else:
        ans.append(A[q[0]])

    return ans
