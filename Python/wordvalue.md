### Task:  

Create a program that calculates the "worth" of words based on Scrabble-like scoring rules and determines the highest-scoring word(s) from a list or a file.  

---

#### Requirements:  

1. **Scoring System**:  
   - Use the provided dictionary to assign point values to letters:  
     - Letters such as `e`, `a`, and `o` are worth 1 point.  
     - Rare letters such as `q` and `z` are worth 10 points.  
   - Calculate the score of a word by summing up the scores of its letters.  

2. **Input**:  
   - Read a list of words from a text file named `dictionary.txt`.  
   - Each word is on a new line, and all input words should be converted to lowercase.  

3. **Processing**:  
   - Implement the function `calculate_score(word)` to compute the score of a given word based on the scoring dictionary.  
   - Implement the function `worthOfList(word_list)` to:  
     - Calculate the score of each word in the list.  
     - Identify the highest score among the words.  
     - Return all words with the maximum score.  

4. **Output**:  
   - Use the function `betterPrinter(list)` to display the words with their scores:  
     - If there are fewer than 10 results, print each word with its score.  
     - If there are more than 10 results, print the number of results and the score of one of the words.  

---

#### Example Input (`dictionary.txt`):  
```
hi  
quiz  
bomb  
president  
zero  
one  
two  
three  
four  
five  
```

#### Example Output:  
If the words are processed, the output might be:  
```
quiz : 22  
```