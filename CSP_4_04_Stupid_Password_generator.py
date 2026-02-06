"""
Problem: Stupid Password Generator
Write a program that enters two integers n and l and generates, in alphabetical order, all possible "stupid” passwords" that consist of the following 5 characters:

Character 1: a digit from 1 to n.
Character 2: a digit from 1 to n.
Character 3: a small letter from the first l letters of the Latin alphabet.
Character 4: a small letter from the first l letters of the Latin alphabet.
Character 5: a digit from 1 to n, greater than the first 2 digits.
Input Data
The input is read as arguments and consists of two integers: n and l within the range [1 … 9].Screenshot 2025-10-07 at 10.53.33 AM.png

Output Data
Return a list of all "stupid" passwords in alphabetical order.
"""

def stupidPassword(n: int, l: int):
    passwords = []
    for char1 in range(1, n + 1):
        for char2 in range(1, n + 1):
            for char3_val in range(ord('a'), ord('a') + l):
                char3=chr(char3_val)
                for char4_val in range(ord('a'), ord('a') + l):
                    char4 = chr(char4_val)
                    for char5 in range(1, n + 1):
                        if char5 > char1 and char5 > char2:
                            password = f"{char1}{char2}{char3}{char4}{char5}"
                            passwords.append(password)
    print(passwords)
    return passwords


