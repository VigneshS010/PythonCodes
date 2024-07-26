# Palindrome
n = "madam"
def palindrome(n):
    return n == n[::-1]
print(palindrome(n))

# permutation

from itertools import permutations
def perm(n):
    sol = list(permutations(n))
    ans = []
    for i in sol:
        ans.append(''.join(i))
    print(ans)
perm(n)


# substring check

def substring(n, m):
    # for i in range(len(n)):
    #     print(n[i])
    #     if n[i] == m[0]:
    #         if n[i:i+len(n)] == m:
    #             print(n[i])
    #             return True
    # return False
    if m in n:
        return True
    else:
        return False

n = "madam"
m ="ada"
print(substring(n,m))


#Reverssing a string

def rev(n):
    sol = []
    for i in range(len(n)-1,-1,-1):
        sol.append(n[i])
    print(sol)

r = [1,2,3,4,5,99]
rev(r)


#K th largest element
def klarge(r,k):
    r.sort(reverse=True)
    print(r[k-1])


r = [1,1000,2,200,3,10,4,5]
klarge(r,3)


# Maximum Subarray Sum
def maxsub(a):
    sub = a[0]
    curr = 0
    # Iterate throught the list
    for i in a:
        # If it goes negativ set to 0
        if curr<0:
            curr = 0
        # adds new value until it become 0
        curr += i
        # it stores max of added numbers and old nums
        sub =  max(sub, curr)
    return sub

a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxsub(a))



# Longest Common SubSequence
def lcommonsub(n,m):
    lst= []
    for i in n:
        if i in m:
            lst.append(i)
    print(len(lst))

n = "abcdef"
m = "bdf"
lcommonsub(n,m)


# # Valid binary tree
# class TreeNode:
#     def __init__(self, left=None,  right=None, val=0):
#         self.val = val
#         self.left = left
#         self.right = right
#
# def is_valid(root):
#     def inorder(node):
#         if not node:
#             return True
#         if not


# merge all overlapping interval

def merge_interval(lst):
    f = []
    k = float('-inf')
    for i in range(1,len(lst)):
        if i == k:
            continue
        if lst[i-1][-1] > lst[i][0]:
            k = i+1
            s = []
            s.append(lst[i-1][0])
            s.append(lst[i][1])
            f.append(s)
        else:
            f.append(lst[i-1])
            if lst[i] == lst[-2]:
                f.append(lst[-1])
    print(f)

lst = [[1,3],[2,5],[7,9],[11,15]]
merge_interval(lst)