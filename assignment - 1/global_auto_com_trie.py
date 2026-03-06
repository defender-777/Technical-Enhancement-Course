from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.freq = defaultdict(int)
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.freq[word] += 1
        node.is_end = True

    def autocomplete(self, prefix):
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        # sort suggestions by frequency
        suggestions = sorted(node.freq.items(), key=lambda x: -x[1])
        return [word for word, _ in suggestions[:5]]


if __name__ == "__main__":
    trie = Trie()

    words = ["apple", "app", "application", "apt", "ape", "apply"]
    for w in words:
        trie.insert(w)

    print(trie.autocomplete("ap"))