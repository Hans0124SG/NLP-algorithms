import numpy as np

def minimalEditDistance(word1, word2):
    char1 = [i for i in word1]
    char2 = [i for i in word2]
    
    x = len(char1)
    y = len(char2)
    
    matrix = np.zeros((x, y))
    matrix[0] = [i for i in range(y)]
    matrix[:,0] = [i for i in range(x)]
    
    for i in range(x-1):
        for j in range(y-1):
            down = matrix[i+1][j]+1
            right = matrix[i][j+1]+1
            diag = matrix[i][j] + (0 if char1[i+1] == char2[j+1] else 2)
            
            action = min(down, right, diag)
            
            matrix[i+1][j+1] = action
    
    print(matrix)
    
    action_list = []
    aligned_char1 = []
    aligned_char2 = []
    x -= 1
    y -= 1
    last_value = matrix[x][y]
    
    while x + y != 0:
        down = matrix[x][y] - matrix[x-1][y] if x > 0 else -1
        right = matrix[x][y] - matrix[x][y-1] if y > 0 else -1
        diag = matrix[x][y] - matrix[x-1][y-1] if x + y > 1 else -1
        viable_action = [act for act in [down, right, diag] if act >= 0]
        action = max(viable_action)
        if action == diag:
            if matrix[x][y] == matrix[x-1][y-1]:
                action_list.append(' ')
            else:
                action_list.append('s')
            aligned_char1.append(char1[x])
            aligned_char2.append(char2[y])
            y -= 1
            x -= 1
        elif action == right:
            action_list.append('i')
            aligned_char1.append("*")
            aligned_char2.append(char2[y])
            y -= 1
        elif action == down:
            action_list.append('d')
            aligned_char1.append(char1[x])
            aligned_char2.append("*")
            x -= 1
            
    print(aligned_char1[::-1])
    print(aligned_char2[::-1])
    print(action_list[::-1])
   
word1 = '#intention'
word2 = '#execution'

minimalEditDistance(word1, word2)
