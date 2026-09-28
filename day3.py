
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Map each value to its index in inorder
        inorder_index = {value: i for i, value in enumerate(inorder)}

        # Pointer for the current root in preorder
        preorder_index = 0

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_index

            # No elements in this subtree
            if left > right:
                return None

            # Preorder gives us the root
            root_value = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_value)

            # Find the root position in inorder
            mid = inorder_index[root_value]

            # Build left and right subtrees
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)
