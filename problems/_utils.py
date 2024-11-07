from _classes import ListNode, TreeNode


def print_dict(hash_map: dict) -> None:
    for key, value in hash_map.items():
        print(key, "->", value)


def print_matrix(matrix: list[list[int]]) -> None:
    sb = []
    for row in matrix:
        sb.append("  " + str(row))
    print("[\n" + "\n".join(sb) + "\n]")


def linked_list_to_list(head: ListNode | None) -> list[int]:
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


def list_to_linked_list(arr: list[int]) -> ListNode | None:
    sentinel = curr = ListNode()
    for val in arr:
        node = ListNode(val=val)
        curr.next = node
        curr = curr.next
    return sentinel.next


def print_linked_list(head: ListNode | None) -> None:
    arr = linked_list_to_list(head)
    print(" -> ".join([str(item) for item in arr]))


def tree_to_list(root: TreeNode | None) -> list[int]:
    pass
