### Task:  

Create a program that processes the text from a file to find the longest substring of unique characters.  

#### Requirements:  
1. **Input**:  
   - Read text from a file named `raven.txt`.  
2. **Processing**:  
   - Convert all characters to lowercase for case insensitivity.  
   - Ignore punctuation, spaces, and special characters (e.g., `-` or `—`).  
   - Identify substrings where all characters are unique (no duplicates).  
   - If a duplicate character is found, store the current substring in a list and reset to start a new substring.  
3. **Output**:  
   - Find the longest substring(s) from the list of unique-character substrings.  
   - Print the longest substring(s) and their length.  

#### Example Output:  
If the content of `raven.txt` is:  
```
Once upon a midnight dreary, while I pondered, weak and weary.
```

The output might be:  
```
The longest substring(s) are: ['pondered']  
Length of the substring: 8  
```  
