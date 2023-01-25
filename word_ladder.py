class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)
        starts = {beginWord}
        if endWord not in words:
            return 0
        level = 1
        
        def findNeighbors(currentNode, words):
            return_set = set()
            letter_list = list(currentNode)
            x = len(letter_list)
            for _ in range(x):
                disposable_list = copy.deepcopy(letter_list)
                for i in range(97, 123):
                    disposable_list[_] = chr(i)
                    if ''.join(disposable_list) in words:
                        return_set.add(''.join(disposable_list))
            return return_set

        while starts:
            level+=1
            return_set = set()
            for _ in starts:
                return_set.update(findNeighbors(_, words))
            new_nodes = set()
            for i in return_set:
                if i == endWord:
                    return level
                new_nodes.add(i)
                words.remove(i)
            starts = new_nodes
        return 0
