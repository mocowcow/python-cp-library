
"""
數位 dp (digit dp)

在區間 [L, R] 內找滿足限制的數字
限制與填入的數字相關，包括但不限於：
- 奇數/偶數出出現次數
- 各數位出現次數
- 數位和
- 完整數值 mod 後餘 k


定義 solve(num)：求 [1, num] 滿足限制的填法個數。
根據排容原理，先求 [1, R] 的個數，然後扣掉 [1, L-1] 的個數，即 [L, R] 的個數。

有時範圍是以非常大的字串表示，對 python 沒有影響，可以直接大數求 L-1。
其他語言可以先求 [1, R] - [1, R]，然後單獨判斷 L 是否滿足限制，若滿足則再減 1。

dp(i) 代表當前填幾 i 位，搭配常用狀態有：
- is_limit：代表 ans[i] 是否受限於 s[i]
- is_num：代表是否為非零數，用於處理前導零
- sm：數位和
- prod：數位積
- mask：某數是否使用過
- cnt1：填 1 的次數
- remainder：上次填完剩的餘數

其中 is_limit 最為關鍵！！！
例如：
> s = "2234"
> 求不超過 s 的填法有幾種  

最初什麼都沒填，第 ans[0] 肯定不得超過 s[0]，只能填 0,1,2。
如果 s[0] 填 2，則 ans[1] 同樣會受限於 s[1]，因為填更大的數會超過 s。
反之，若 s[0] 填 0 或 1，則答案至多只能是 "1###" 剩下怎麼填都不會超過 s。
所以根據當前可填的數字範圍 [down, up]，若當前 ans[i] 受限且又填了上限 up，則 i+1 會持續受限；反之不受限。  

第二常用的是 is_num。
通常用於處理前導零，控制填入非零數字後才開始計入限制。
例如：
> s = "2234"
> 求填入奇偶數相同的填法有幾種

若填入 0012 忽略前導零，實際上數字只有 12，奇偶數各一次，合法。
因此只有在第一次填入非 0 時才設置 is_num = true，並開始計算奇偶。  

"""


# LC 233 (數 1) https://leetcode.com/problems/number-of-digit-one/description/
# LC 600 (轉 2 進制) https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/
# LC 902  https://leetcode.com/problems/numbers-at-most-n-given-digit-set/description/
# LC 1012 https://leetcode.com/problems/numbers-with-repeated-digits/description/
# LC 2376 https://leetcode.com/problems/count-special-integers/description/
# LC 2719 https://leetcode.com/problems/count-of-integers/submissions/
# LC 2801 https://leetcode.com/problems/count-stepping-numbers-in-range/submissions/
# LC 2827 https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/description/
# LC 2999 https://leetcode.com/problems/count-the-number-of-powerful-integers/
# LC 3007 https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/description/
# LC 3352 https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/description/
# LC 3448 (維護下界) https://leetcode.com/problems/count-substrings-divisible-by-last-digit/description/
# LC 3490 (乘積) https://leetcode.com/problems/count-beautiful-numbers/description/
# LC 3519 (轉 b 進制) https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/description/

from functools import cache
MOD = 10 ** 9 + 7
L, R = 1, 100000


def digit_dp():

    def solve(num):
        s = str(num)
        N = len(s)

        @cache
        def dp(i, is_limit, is_num):
            if i == N:
                # 全部填完，判斷是否合法
                return 1 if is_num else 0

            res = 0
            if not is_num:  # 特判前導零
                res = dp(i+1, False, False)

            down = 0 if is_num else 1  # 可填的最小值
            up = 9 if not is_limit else int(s[i])  # 可填的最大值
            for j in range(down, up+1):
                new_limit = is_limit and j == up
                new_is_num = is_num or (j > 0)
                res += dp(i+1, new_limit, new_is_num)
            return res % MOD

        res = dp(0, True, False)
        dp.cache_clear()  # prevent MLE
        return res

    ans = solve(R) - solve(L-1)
    ans %= MOD

    return ans
