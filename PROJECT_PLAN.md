# Polyalphabetic Substitution Cipher Project

## 1. Project Overview & Algorithm Explanation

**What is this project asking for?**
The goal is to design and implement a program (using Python and the terminal) that can encrypt and decrypt secret messages using a **Polyalphabetic Caesar Cipher** (widely known as a Vigenère cipher).

**What is the algorithm we are building?**
- A standard **monoalphabetic cipher** (like a basic Caesar cipher) shifts every letter in a message by the exact same number of positions. For example, a shift of 3 turns every 'A' into 'D', every 'B' into 'E', etc.
- A **polyalphabetic cipher** is more secure because it uses a *sequence* of different monoalphabetic ciphers. Instead of one fixed shift for the whole message, the shift changes for every single letter, dictated by a secret **keyword**.

**How the algorithm works in practice:**
1. **The Alphabet as Numbers:** We treat letters as numbers from 0 to 25 (A=0, B=1, ... Z=25).
2. **The Keyword Phase:** You choose a secret keyword (e.g., `KEY`). You repeat that keyword until it matches the length of the message you want to encrypt.
   - *Message:*  `H E L L O W O R L D`
   - *Keyword:*  `K E Y K E K E Y K E`
3. **Encryption:** You add the numerical value of the message letter and the corresponding keyword letter together (wrapping around after Z).
4. **Decryption:** You take the encrypted letter and subtract the value of the keyword letter to get the original message back.

---

## 2. Step-by-Step Implementation Phases

Here is the breakdown of tasks to divide among the group to complete the project successfully.

### Phase 1: Project Setup & Ground Rules
- [ ] Initialize the Python project and agree on where code is stored (e.g., a shared GitHub repo, a shared folder, or Replit).
- [ ] Define the scope of characters: Agree on whether the program will handle only UPPERCASE letters, both cases, or ignore spaces/punctuation entirely. 
  - *Recommendation:* Convert all input to uppercase and preserve spaces/punctuation without encrypting them.

### Phase 2: Core Mathematics & Logic Formulation
- [ ] **Letter Translation:** Research and understand how to convert letters to numbers in Python using the `ord()` and `chr()` functions. Learn how modulo arithmetic (`% 26`) creates the wrap-around effect from Z to A.
- [ ] **Keyword Expansion:** Write a helper script or function that takes a keyword and repeats it to perfectly match the length of a given text.

### Phase 3: Encryption Implementation (Code)
- [ ] Create a file named `cipher.py`.
- [ ] Create the function `encrypt(plaintext, keyword)`.
- [ ] Inside the function, loop through each character in the `plaintext`:
  - If the character is a letter, calculate the forward shift using the corresponding letter from the expanded keyword.
  - If it is a space or punctuation, just add it to the final result exactly as it is.
- [ ] Return the finished encrypted string.

### Phase 4: Decryption Implementation (Code)
- [ ] In `cipher.py`, create the counterpart function `decrypt(ciphertext, keyword)`.
- [ ] Inside the function, loop through each character in the `ciphertext`:
  - If it's a letter, calculate the **reverse shift** using the keyword letter.
  - Handle the math to ensure subtracting doesn't cause errors if the result goes below zero.
- [ ] Return the original plaintext string.

### Phase 5: Terminal User Interface (CLI)
- [ ] Create a `main.py` file to handle all the terminal interactions.
- [ ] Build an interactive loop (e.g., using a `while True` loop) that displays a menu:
  1. Encrypt a message
  2. Decrypt a message
  3. Exit program
- [ ] Use Python's `input()` function to accept the user's choice, message, and secret keyword.
- [ ] Call the functions from `cipher.py` and neatly `print()` the results to the terminal.

### Phase 6: Edge Cases & Testing
- [ ] **Test Case 1:** Basic text. Encrypt "HELLO" with key "ABC". Decrypt the generated text to ensure it turns back into "HELLO".
- [ ] **Test Case 2:** Sentences with numbers and punctuation (e.g., "Meet me at 12:00 PM!"). Make sure the algorithm handles non-alphabet characters cleanly without crashing.
- [ ] **Test Case 3:** Edge cases: Empty messages, keywords longer than the message, or keywords containing numbers. Add safeguards to prompt the user if they input an invalid keyword.

---

## 3. How to Run the Project

Once the code is fully implemented, anyone can run your application locally using their terminal!

**Steps to run the application:**
1. Open your computer's terminal (or command prompt).
2. Use the `cd` command to navigate to the exact directory right where these files are saved:
   ```bash
   cd path/to/your/project
   ```
3. Run the main Python file to start the interactive interface:
   ```bash
   python main.py
   ```
4. Follow the interactive prompts displayed in the terminal to seamlessly encrypt and decrypt your inputs.
