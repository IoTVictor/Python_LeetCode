# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def postTrasval(root):
            dp = [0, 0]
            if not root:
                return dp
            left = postTrasval(root.left)
            right = postTrasval(root.right)

            dp[0] = max(left[0], left[1]) + max(right[0], right[1])
            dp[1] = root.val + left[0] + right[0]

            return dp

        dp = postTrasval(root)
        return max(dp[0], dp[1])

if __name__ == '__main__':

    T = TreeNode(3)
    T.left = TreeNode(2)
    T.right = TreeNode(3)
    T.left.right = TreeNode(3)
    T.right.right = TreeNode(1)


    s = Solution()
    print(s.rob(T))

