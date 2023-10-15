"""
*****
*   *
*   *
*   *
*****
"""

def draw_pattern(n):
    for row in range(n):
        for col in range(n):
            if row in (0, n-1):
                print("*", end=" ")
            else:
                if col in (0, n-1):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

        print()


if __name__=='__main__':
    draw_pattern(5)