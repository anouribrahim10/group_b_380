# Polyalphabetic Cipher - Team Delegation Guide

This guide explicitly details exactly what each of the 4 group members needs to do to successfully build this project from scratch. It defines functions, file names, and expectations so everyone can work independently.

---

## 🧑‍💻 Person 1: Math & Encryption Lead

**Your Goal:** Write the mathematical logic that shifts text forward.
**Where you work:** `cipher.py`

**Your Tasks:**
1. **Create the file:** Create `cipher.py`.
2. **Write the Function Design:** Define a function like this: `def encrypt(plaintext, key_sequence):`
   - `plaintext` will be a string (e.g., `"HELLO"`).
   - `key_sequence` will be a list of numbers (e.g., `[6, 20, 20, 6, 20]`).
3. **Handle Uppercase:** Convert the entire `plaintext` string to uppercase immediately so you don't have to worry about lowercase letters.
4. **Build the Loop:** Use a `for` loop to look at every character in the string.
   - If the character is a letter (`char.isalpha()`), use Python's `ord()` function to convert it to a number from 0-25.
   - Add the corresponding shift number from the `key_sequence` list.
   - Use modulo 26 (`% 26`) on the result to ensure it doesn't go past 'Z'. (e.g., 'Z' shifted by 1 wraps back to 'A').
   - Convert the number back to a character using `chr()`.
5. **Handle Punctuation:** If the character is a space, comma, or number (not `.isalpha()`), do not shift it. Just pass it through as-is, and **do not** advance to the next number in your `key_sequence`.
6. **Return Result:** Return the final concatenated string.

---

## 🕵️‍♂️ Person 2: Decryption Specialist

**Your Goal:** Write the logic to reverse Person 1's math and decipher text.
**Where you work:** `cipher.py` (Work below Person 1's code)

**Your Tasks:**
1. **Write the Function Design:** Define a function exactly like Person 1 did: `def decrypt(ciphertext, key_sequence):`
2. **Reverse the Math:** Replicate Person 1's logic of looping through the letters and converting them to 0-25 numbers, but instead of adding the `key_sequence` shift, you **subtract** it.
   - *Example:* If the cipher letter is 'A' (0) and the shift is 6, you do `(0 - 6) % 26`. Python is smart and knows that `% 26` of a negative number wraps backwards to 'U' (20).
3. **Coordinate:** Speak with Person 1 to ensure that your functions both accept the exact same variables and output the exact same type of string. You both need to process spaces and punctuation exactly the same way.

---

## 🖥️ Person 3: The Interface & Integration Developer

**Your Goal:** Build the terminal interface and handle user text input.
**Where you work:** `main.py`

**Your Tasks:**
1. **Create the File:** Create `main.py`.
2. **Import the Math:** At the very top, write `from cipher import encrypt, decrypt`.
3. **Build the Main Menu:** Use a `while True` loop to continuously print a menu asking the user if they want to: `1. Encrypt`, `2. Decrypt`, or `3. Exit`.
4. **Handle The Cipher Sequence UI:** This is your hardest task. When a user picks Encrypt or Decrypt:
   - Ask for their text message.
   - Ask for their cipher sequence: `"Enter sequence (e.g. C1 C2 C2 C1 C3): "`.
   - Parse their input string, figure out how many unique values they typed (e.g., C1, C2, and C3).
   - Use a `for` loop to ask the user to assign a shift number to each unique value `"Enter key number for C1: "`.
   - Take those definitions and map them across their original sequence to build a flat list of integers (e.g., `[6, 20, 20, 6, 11]`).
5. **Execute:** Pass the user's message and that final list of integers into Person 1 or 2's functions and `print()` the result beautifully.

---

## 🧪 Person 4: Quality Assurance & Project Manager

**Your Goal:** Attempt to break the program, fix errors, and handle submissions.
**Where you work:** Across all files, testing locally.

**Your Tasks:**
1. **Version Control Setup:** Set up the GitHub repository (if using one) or ensure all files are grouped together properly. 
2. **Test Edge Cases (Bug Hunting):**
   - Run the script and type completely random characters when it asks for the Sequence array (e.g. enter letters when it wants shift numbers). If it crashes, work with Person 3 to add `try/except` blocks so it gracefully prints `"Invalid input, try again."`
   - Test empty messages. What happens if the user hits "Enter" without typing any text?
   - Ensure you can successfully encrypt the statement `"We encrypt at 11:59 PM!"` and get it perfectly back verbatim when deciphering it.
3. **Documentation:** Keep the project's README or `PROJECT_PLAN.md` up to date with the team's progress. Ensure code is commented. 
4. **Presentation:** Take point on generating the final zip file or GitHub link for your professor, confirming everything exactly matches the grading rubric.
