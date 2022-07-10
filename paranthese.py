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
