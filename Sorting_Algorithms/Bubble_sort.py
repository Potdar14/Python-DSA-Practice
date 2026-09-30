'''
Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order. 
After each pass, the largest unsorted element moves to the end.

Example
original array --> [5  2  8  1]

[5  2  8  1]
5 > 2 → swap      ## 1st iteration
2  5  8  1

5 < 8 → no swap      
2  5  8  1

8 > 1 → swap     
2  5  1  8

[2  5  1  8]
2 > 5 → no swap     
2  5  1  8

5 > 1 → swap     
2  1  5  8

1 >  → swap     
2  5  1  8
'''
