
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        freq = {}
        
        for i in range(len(order)):
            freq[order[i]] = i
      
        for curr in range(len(words) - 1):
            curr_word = words[curr]
            next_word = words[curr + 1]
            
            for j in range(min(len(curr_word), len(next_word))):
                
                if freq[curr_word[j]] > freq[next_word[j]]:
                    return False
                
                if freq[curr_word[j]] < freq[next_word[j]]:
                    break
            
            else:
                if len(curr_word) > len(next_word):
                    return False

        return True



        