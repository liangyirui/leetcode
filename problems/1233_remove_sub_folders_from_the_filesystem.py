"""
https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/

Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.

If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j] must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".

The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.

For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.
"""

class TrieNode:
    def __init__(self) -> None:
        self.is_end = False
        self.children = {}
        
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        
def remove_subfolders(folder: list[str]) -> list[str]:
    trie = Trie()
    for path in folder:
        node = trie.root
        folders = path.split("/")
        for f in folders:
            if f == "":
                continue
            if f not in node.children:
                node.children[f] = TrieNode()
            node = node.children[f]
        node.is_end = True
        
    result = []
    for path in folder:
        node = Trie.root
        folders = path.split("/")
        is_subfolder = False
        for i, f in enumerate(folders):
            if f == "":
                continue
            next_node = node.children[f]
            if next_node.is_end and i != len(folders) - 1:
                is_subfolder = True
                break
            node = next_node
        if not is_subfolder:
            result.append(path)
	
    return result