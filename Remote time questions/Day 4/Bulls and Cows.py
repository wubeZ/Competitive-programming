class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        x = y = 0
        secret_list = list(secret)
        guess_list = list(guess)
        length = len(secret_list)
        for i in range(length):  
            if secret[i] == guess[i]:
                x += 1
                secret_list.remove(secret[i])
                guess_list.remove(guess[i])
        
        for j in guess_list:
            if j in secret_list:
                y += 1
                secret_list.remove(j)
                
        return str(x) + "A" + str(y) + "B"
        
