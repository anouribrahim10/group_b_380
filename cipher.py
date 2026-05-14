def encrypt(plaintext, key_sequence):
    """
    Encrypts the plaintext using a sequence of numeric shifts (e.g. [6, 20, 11]).
    Only alphabetic characters are shifted; spaces and punctuation remain as is.
    Preserves original capitalization.
    """
    ciphertext = []
    
    key_len = len(key_sequence)
    key_idx = 0
    
    for char in plaintext:
        if char.isalpha():
            # Determine base depending on case
            base = ord('A') if char.isupper() else ord('a')
            
            # Convert letter to 0-25 scale
            p = ord(char) - base
            # Subtract 1 since keys represent 1-based alphabet positions
            k_shift = key_sequence[key_idx % key_len] - 1
            
            # Forward shift and modulo 26
            c = (p + k_shift) % 26
            
            # Convert back to character
            ciphertext.append(chr(c + base))
            
            # Increment shift sequence index
            key_idx += 1
        else:
            # Add spaces and punctuation directly
            ciphertext.append(char)
            
    return "".join(ciphertext)

def decrypt(ciphertext, key_sequence):
    """
    Decrypts the ciphertext using a sequence of numeric shifts (e.g. [6, 20, 11]).
    Only alphabetic characters are shifted; spaces and punctuation remain as is.
    Preserves original capitalization.
    """
    plaintext = []
    key_len = len(key_sequence)
    key_idx = 0

    for char in ciphertext:
        if char.isalpha():
            # Determine base depending on case
            base = ord('A') if char.isupper() else ord('a')
            
            # Convert letter to 0-25 scale
            c = ord(char) - base
            # Subtract 1 since keys represent 1-based alphabet positions
            k_shift = key_sequence[key_idx % key_len] - 1
            
            # Reverse shift and modulo 26
            p = (c - k_shift) % 26
            
            # Convert back to character
            plaintext.append(chr(p + base))
            
            # Increment shift sequence index
            key_idx += 1
        else:
            # Add spaces and punctuation directly
            plaintext.append(char)

    return "".join(plaintext)
