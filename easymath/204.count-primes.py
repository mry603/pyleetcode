#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <=2: return 0
        '''
        numbers = {}
        for p in range(2, int(sqrt(n)) + 1):
            if p not in numbers:
                for multiple in range(p*p, n, p):
                    numbers[multiple] = 1
        
        # Exclude "1" and the number "n" itself.
        return n - len(numbers) - 2
        '''
        count = 0          
        primes = [True] * n#全1
        
        for i in range(2, int(n**0.5)+1):#外循环的范围是根号n，大于根号n的部分会被内循环删掉
            if not primes[i]:#如果这一位已经被标记为不是质数，跳过
                continue
            # mark all multiplies of i not prime
            for j in range(i * i, n, i):#内循环范围是i*i,i*(i+1)...
                primes[j] = False
        
        for i in range(2, n):
            if primes[i]:#统计质数
                count += 1          
        return count

# @lc code=end

