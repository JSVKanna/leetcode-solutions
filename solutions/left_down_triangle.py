"""
*****
****
***
**
*
"""

def draw_pattern(n):
    for row in range(n+1):
        for col in range(n-row):
            print("*", end=" ")
        print()


if __name__=="__main__":
    draw_pattern(5)