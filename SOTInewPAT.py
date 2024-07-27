# Largest Binary Number

def largest_bn(M, N, A):
    MOD = 1000000007

    binary_list = [A[i][j] for i in range(M) for j in range(N)]
    binary_list.sort(reverse=True)

    # This 2 indicates to converting the interger into the Binary number
    # to convert int into string while join , map func is used
    sol = int("".join(map(str, binary_list)),2)
    return sol % MOD

M = 3
N = 2
A = [[0,0], [0, 0], [0, 1]]
print(largest_bn(M, N, A))





# Minimum Explosion

def min_explosion(M, H, G):
    # if any one mountain in B is larger than A , these process is not possible
    for i in range(M):
        if H[i] < G[i]:
            return -1

    explosions = 0

    for i in range(M-1):

        # this if stment, check the next num is greater than run , if it equals it skips
        if H[i] > G[i]:
            diff = H[i] - G[i]
            explosions += diff
            H[i] -= diff
            H[i+1] -= diff

    # We cant check the last value in the loop, so we seperately create this
    if H[-1] > G[-1]:
        diff = H[-1] - G[-1]
        explosions += diff
        H[-1] -= diff
    print(explosions)

# Example usage:
M = 3  # Number of mountains
H = [9, 10, 1]  # Heights of mountain range A
G = [1, 1, 1]  # Heights of mountain range B
min_explosion(M, H, G)