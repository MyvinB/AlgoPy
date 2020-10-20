from typing import List

from pip._vendor.msgpack.fallback import xrange


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        r, record = set(), set()
        for i in xrange(len(s) - 9):
            substring = s[i:i + 10]
            [record, r][substring in record].add(substring)
        return list(r)


def main():
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT";
    print(Solution.findRepeatedDnaSequences(Solution, s))


if __name__ == "__main__":
    main()
