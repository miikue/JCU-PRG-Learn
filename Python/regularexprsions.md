### Task:  

Create a program that demonstrates the use of regular expressions for pattern matching with various types of input.  

#### Requirements:  
1. **Functionality**:  
   - Implement a function `testPattern(pattern, test_string)` that uses Python's `re.match()` method to determine if the `test_string` matches the `pattern`.  
   - Print `Přijat` (Accepted) if the string matches, and `Nepřijat` (Rejected) otherwise.  

2. **Patterns to Test**:  
   - **Custom Pattern**: Matches strings with zero or more `a`, followed by `bc` repeated one or more times, and ending with a character in the range `0-5` or `a-z`. Example: `"aaaaaabccccf"`.  
   - **Phone Number**: Matches Czech-style phone numbers in the format `123 456 789`.  
   - **Email Address**: Matches email addresses containing alphanumeric characters, a single `@`, and a domain with a `.`. Example: `"nejakyEmail@email.cz"`.  
   - **Date**: Matches dates in the format `DD/MM/YYYY`, where:  
     - `DD` is `01-31`  
     - `MM` is `01-12`  
     - `YYYY` is a 4-digit year.  
     Example: `"31/12/2020"`.  
   - **MAC Address**: Matches MAC addresses in the format `XX:XX:XX:XX:XX:XX`, where `XX` consists of two hexadecimal characters (0-9, A-F, a-f). Example: `"01:23:45:67:89:AB"`.  

3. **Output**:  
   For each test case, print whether the string was accepted or rejected.  

#### Example Output:  
```
Přijat  
Přijat  
Přijat  
Přijat  
Přijat  
```  