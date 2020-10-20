def minDominoRotations(A, B):
    for x in [A[0], B[0]]:
        if all(x in d for d in zip(A, B)):
            return len(A) - max(A.count(x), B.count(x))
    return -1


def main():
    A = [2, 1, 2, 4, 2, 2]
    B = [5, 2, 6, 2, 3, 2]
    print(minDominoRotations(A, B))


class Solution:
    if __name__ == "__main__":
        main()