"""
*
**
* *
*  *
*   *
******
"""

def draw_pattern(n):
    for row in range(n+1):
        for col in range(row):
            if row in (0, n) or col in (0, row-1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


if __name__=="__main__":
    draw_pattern(5)