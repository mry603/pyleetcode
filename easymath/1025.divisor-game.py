#
# @lc app=leetcode id=1025 lang=python3
#
# [1025] Divisor Game
#

# @lc code=start
class Solution:


    def divisorGame(self, n: int) -> bool:
        '''
     * Whomever can end up with playing the value = 2 will win because x = 1  forces the next player to get 1
     * which is unplayable.
     * Whomever ends up with an odd value must present the next player an even value
     * this is because an odd value can only be the product of 2 odd values.
     *       you can see this because any even number is 2n and any odd number is 2m+1
     *       so an even number times an even number is:
     *            2n * 2m = 4nm = 2*(2*nm) = 2k    which is even
     *       likewise an even number times an odd number is:
     *            2n * (2m +1) = 4nm + 2n = 2*(2*nm + n) = 2p  which is even
     *       only an odd number times an odd number yields an odd result:
     *            (2n+1)*(2m+1) = 4*nm + 2n + 2m + 1 = 2*(2*nm + n + m) + 1 = 2q +1  which is odd
     * this means that the next player will be presented with an odd value subtracted from another odd value
     * which can only be an even value.
     *     which you can see by:
     *           (2n + 1) - (2m + 1) = 2(n-m) + (1 - 1) = 2r  which is even
     * Whomever ends up with an even value can force the next player to take an odd value.
     * If no other odd factor is possible for example in the case of 4 = 2 * 2
     * one can resort to choosing x = 1 from 4 = 4 * 1.
     * This means that whomever starts even can ensure that they only get even numbers to play
     * by always forcing the other player to taken an odd number, which forces them to always return an even number.
     * This game plays all the way down to the even number 2, whose holder wins the game.
     * Thus whomever starts with an even number can force the game in their favor
     *
        '''
        return n%2 == 0

        
# @lc code=end

