'''
Sherlock and Watson have recently enrolled in a computer programming course. Today, the tutor taught them about the balanced parentheses problem. A string S consisting only of characters ( and/or ) is balanced if:
It is an empty string, or:
It has the form (S), where S is a balanced string, or:
It has the form S1S2, where S1 is a balanced string and S2 is a balanced string.
Sherlock coded up the solution very quickly and started bragging about how good he is, so Watson gave him a problem to test his knowledge. He asked Sherlock to generate a string S of `L + R` characters, in which there are a total of L left parentheses ( and a total of R right parentheses ). Moreover, the string must have as many different balanced non-empty substrings as possible. (Two substrings are considered different as long as they start and end at different indexes of the string, even if their content happens to be the same). Note that S itself does not have to be balanced.
Sherlock is sure that once he knows the maximum possible number of balanced non-empty substrings, he will be able to solve the problem. Can you help him find that maximum number?

Input
The first line of the input gives the number of test cases, T. T test cases follow.
Each test case consists of one line with two integers: L and R.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the answer, as described above.

Limits
Time limit: 20 seconds.
Memory limit: 1 GB.
1≤T≤100.
Test Set 1
0≤L≤20.
0≤R≤20.
1≤L+R≤20.
Test Set 2
0≤L≤105.
0≤R≤105.
1≤L+R≤105.

Sample Input

3
1 0
1 1
3 2


Sample Output

Case #1: 0
Case #2: 1
Case #3: 3

'''


def find_max_num_balanced_substrings(l, r):
    remain = r

    if(l < r):
        remain = l
    if(remain < 1):
        return 0
    if(remain == 1):
        return 1

    max_substring = (remain*(remain+1))/2

    return int(max_substring)


def main():
    # Get number of test cases
    # for i in range(1, 20):
    #     for j in range(1, 20):

    #         print(f'{i}, {j} ->{ find_max_num_balanced_substrings(i, j)}')

    test_cases = int(input())
    for test_case in range(1, test_cases + 1):
        # Get total of left and right parentheses
        l, r = map(int, input().split())
        ans = find_max_num_balanced_substrings(l, r)
        print("Case #%d: %d" % (test_case, ans))


if __name__ == "__main__":
    main()
