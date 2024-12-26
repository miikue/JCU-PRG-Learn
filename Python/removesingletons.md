### Task: Filter Non-Unique Elements from a List

#### Objective:
Write a program to filter out all unique elements (elements that appear only once) from a list of integers.

---

#### Requirements:
1. **Input:**
   - A predefined list of integers. Example:
     ```python
     pool = [2, 5, 3, 6, 2, 5, 7, 3]
     ```

2. **Output:**
   - A list containing only non-unique elements. Example output for the above input:
     ```python
     [2, 5, 3, 2, 5, 3]
     ```

3. **Implementation:**
   - Use a single function to solve the task.  
   - Avoid modifying the list while iterating over it.

---

#### Input/Output Example:
Input:  
```python
pool = [1, 2, 2, 3, 4, 4, 5]
```

Output:  
```python
[2, 2, 4, 4]
```