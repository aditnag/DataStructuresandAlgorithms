def generate_valid_brackets(N, M, curr_str='', open_p=0, close_p=0, open_b=0, close_b=0):
    if len(curr_str) == N + M:
        print(curr_str)
        return

    if open_p < N:
        generate_valid_brackets(N, M, curr_str + '(', open_p + 1, close_p, open_b, close_b)

    if close_p < open_p:
        generate_valid_brackets(N, M, curr_str + ')', open_p, close_p + 1, open_b, close_b)

    if open_b < M:
        generate_valid_brackets(N, M, curr_str + '{', open_p, close_p, open_b + 1, close_b)

    if close_b < open_b:
        generate_valid_brackets(N, M, curr_str + '}', open_p, close_p, open_b, close_b + 1)


if __name__ == "__main__":
    N, M = map(int, input().split())
    generate_valid_brackets(N, M)
