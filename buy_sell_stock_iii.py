from typing import List
import json

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        total_max = 0
        #print("Next:")
        for i in range(0, n):
            local_max_j, local_max_k, min_j, min_k = 0, 0, prices[0], prices[i]
            for j in range(0, i):
                min_j = min(prices[j],min_j)
                local_max_j = max(local_max_j, prices[j] - min_j)
                #print("j", j, "local_max_j:", local_max_j, "min_j:", min_j )
            for k in range(i, n):
                min_k = min(prices[k],min_k)
                local_max_k = max(local_max_k, prices[k] - min_k)
                #print("k", k, "local_max_k:", local_max_k, "min_k:", min_k )
            local_max = local_max_j + local_max_k
            total_max = max(total_max, local_max)
        return total_max

def stringToIntegerList(input):
    return json.loads(input)

def main():
    import sys
    import io
    
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            prices = stringToIntegerList(line)       
            ret = Solution().maxProfit(prices)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()