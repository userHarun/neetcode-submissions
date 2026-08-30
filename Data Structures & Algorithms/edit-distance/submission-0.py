class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N, M = len(word1), len(word2)

        dp = [[0] * (M + 1) for _ in range(N + 1)]
        # initial row and col
        for i in range(N + 1):
            dp[i][0] = i

        for j in range(M + 1):
            dp[0][j] = j
        # [print(row) for row in dp]
        for i in range(1,N + 1):
            for j in range(1, M  + 1):
                # same ch use diag
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] =  1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
                


        [print(row) for row in dp]
        return dp[-1][-1]


'''

recursive solution,  you have 3 choices at each index in word1.
time complexity would be super slow though.
so dfs(i,j)

if word1[i] == word2[j]: do nothing
then do your 3 choices.
replace: dfs(i + 1, j + 1) because we can just skip the indices since we know the replacement makes them equal
delete:  dfs(i + 1, j), we are just deleting the word1 index (skip it)
insert:  dfs(i,  j + 1), if we are inserting we just inserting a word into word 1 , so we only need to move j index forward


DP :

first start with building the grid. the first row and column will be the length of the word 1, and len of
word 2 respectively. and the actual values of them would be the minimum number of operations to match
an empty string to the character. Thus, first row and first col would be i_1,i_2,... len(word1) and
j_1,j_2,.. len(word2)

then we build the rest of the grid based off of it.
if they are equal its just taking diagonal value
if its not the same char:
we look at the dp[i-1][j-1] the val diagonal, dp[i - 1][j] the val abpve it, and to the left is, dp[i][j - 1]. and ADD + 1 to take into the replacement of the curr char
this builds us to the minimum num of operations based on the insert, replace, and delete to get the words
the same


Each DP cell answers: "What's the minimum number of edits to turn word1[:i] into word2[:j]?"

'''