"""
Polyalphabetic Substitution Cipher — GUI
Group B (CS 380)



Run:
    python cipher_gui.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys

# -----------------------------------------------------------------------------
# 1. Try to import the team's cipher logic; fall back to a reference impl.
# -----------------------------------------------------------------------------
try:
    from cipher import encrypt as _team_encrypt, decrypt as _team_decrypt
    _USING_TEAM_LOGIC = True
except Exception:
    _team_encrypt = None
    _team_decrypt = None
    _USING_TEAM_LOGIC = False


def _ref_encrypt(plaintext: str, key_sequence: list) -> str:
    """Reference Vigenère encrypt. Letters get shifted, everything else passes through."""
    if not key_sequence:
        raise ValueError("Key sequence is empty.")
    out = []
    k = 0
    for ch in plaintext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = key_sequence[k % len(key_sequence)] % 26
            out.append(chr((ord(ch) - base + shift) % 26 + base))
            k += 1
        else:
            out.append(ch)
    return ''.join(out)


def _ref_decrypt(ciphertext: str, key_sequence: list) -> str:
    """Reference Vigenère decrypt."""
    if not key_sequence:
        raise ValueError("Key sequence is empty.")
    out = []
    k = 0
    for ch in ciphertext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = key_sequence[k % len(key_sequence)] % 26
            out.append(chr((ord(ch) - base - shift) % 26 + base))
            k += 1
        else:
            out.append(ch)
    return ''.join(out)


def do_encrypt(text, key_sequence):
    if _USING_TEAM_LOGIC and _team_encrypt:
        return _team_encrypt(text, key_sequence)
    return _ref_encrypt(text, key_sequence)


def do_decrypt(text, key_sequence):
    if _USING_TEAM_LOGIC and _team_decrypt:
        return _team_decrypt(text, key_sequence)
    return _ref_decrypt(text, key_sequence)


# -----------------------------------------------------------------------------
# 2. Helpers for the cipher-pattern -> shift-sequence transformation.
# -----------------------------------------------------------------------------
def parse_pattern(pattern: str) -> list:
    """'C1 C2 C2 C1'  ->  ['C1', 'C2', 'C2', 'C1']  (whitespace OR comma separated)"""
    if not pattern.strip():
        return []
    cleaned = pattern.replace(',', ' ')
    return [tok.strip() for tok in cleaned.split() if tok.strip()]


def parse_shifts(text: str) -> dict:
    """'C1=6, C2=20'  ->  {'C1': 6, 'C2': 20}"""
    mapping = {}
    if not text.strip():
        return mapping
    parts = text.replace(',', '\n').splitlines()
    for raw in parts:
        raw = raw.strip()
        if not raw:
            continue
        if '=' not in raw:
            raise ValueError(f"Bad shift entry '{raw}'. Use the form C1=6.")
        label, value = raw.split('=', 1)
        label = label.strip()
        value = value.strip()
        if not label:
            raise ValueError(f"Missing cipher label in '{raw}'.")
        try:
            mapping[label] = int(value)
        except ValueError:
            raise ValueError(f"Shift for '{label}' must be an integer (got '{value}').")
    return mapping


def build_key_sequence(pattern_tokens, shift_map):
    """Expand the pattern using the shift mapping into a list of integer shifts."""
    seq = []
    for tok in pattern_tokens:
        if tok not in shift_map:
            raise ValueError(f"No shift defined for cipher '{tok}'. Add it like {tok}=5.")
        seq.append(shift_map[tok])
    return seq


def aligned_shift_view(message: str, key_sequence: list) -> str:
    """Build a two-line visualization: letters of the message and the shift used for each."""
    if not key_sequence:
        return ""
    letters = []
    shifts = []
    k = 0
    for ch in message:
        if ch.isalpha():
            shift = key_sequence[k % len(key_sequence)]
            width = max(len(ch), len(str(shift)))
            letters.append(ch.center(width))
            shifts.append(str(shift).center(width))
            k += 1
        else:
            letters.append(ch)
            shifts.append(' ' * len(ch))
    return ''.join(letters) + '\n' + ''.join(shifts)


# -----------------------------------------------------------------------------
# 3. The GUI itself.
# -----------------------------------------------------------------------------
class CipherApp(tk.Tk):
    # Color palette — clean modern dark/light hybrid
    BG       = "#f5f6fa"
    CARD     = "#ffffff"
    ACCENT   = "#3b5bdb"
    ACCENT_D = "#2c46ad"
    TEXT     = "#1f2330"
    MUTED    = "#6b7280"
    OK       = "#2f9e44"
    ERR      = "#c92a2a"
    BORDER   = "#e2e4ec"

    def __init__(self):
        super().__init__()
        self.title("Polyalphabetic Cipher — Group B")
        self.geometry("980x680")
        self.minsize(860, 600)
        self.configure(bg=self.BG)

        self._build_styles()
        self._build_layout()
        self._set_status(
            f"Ready · using {'team cipher.py' if _USING_TEAM_LOGIC else 'built-in reference logic'}",
            ok=True,
        )

    # ---- styling ----
    def _build_styles(self):
        style = ttk.Style(self)
        # 'clam' is the most themable cross-platform ttk theme
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure("Card.TFrame", background=self.CARD)
        style.configure("Bg.TFrame", background=self.BG)
        style.configure("Title.TLabel", background=self.BG, foreground=self.TEXT,
                        font=("Segoe UI", 20, "bold"))
        style.configure("Subtitle.TLabel", background=self.BG, foreground=self.MUTED,
                        font=("Segoe UI", 10))
        style.configure("Section.TLabel", background=self.CARD, foreground=self.TEXT,
                        font=("Segoe UI", 11, "bold"))
        style.configure("Field.TLabel", background=self.CARD, foreground=self.MUTED,
                        font=("Segoe UI", 9))
        style.configure("Status.TLabel", background=self.BG, foreground=self.MUTED,
                        font=("Segoe UI", 9))

        style.configure("Primary.TButton",
                        background=self.ACCENT, foreground="white",
                        font=("Segoe UI", 10, "bold"),
                        padding=(18, 10), borderwidth=0, focusthickness=0)
        style.map("Primary.TButton",
                  background=[("active", self.ACCENT_D), ("pressed", self.ACCENT_D)])

        style.configure("Ghost.TButton",
                        background=self.CARD, foreground=self.TEXT,
                        font=("Segoe UI", 10),
                        padding=(14, 8), borderwidth=1, relief="solid")
        style.map("Ghost.TButton",
                  background=[("active", "#eef0f8")])

        style.configure("Mode.TRadiobutton",
                        background=self.CARD, foreground=self.TEXT,
                        font=("Segoe UI", 10), padding=4)

        style.configure("TEntry", fieldbackground="white", padding=6)

    # ---- layout ----
    def _build_layout(self):
        outer = ttk.Frame(self, style="Bg.TFrame", padding=18)
        outer.pack(fill="both", expand=True)

        # Header
        header = ttk.Frame(outer, style="Bg.TFrame")
        header.pack(fill="x", pady=(0, 14))
        ttk.Label(header, text="Polyalphabetic Substitution Cipher",
                  style="Title.TLabel").pack(anchor="w")
        ttk.Label(header,
                  text="Vigenère-style encryption — Group B · CS 380",
                  style="Subtitle.TLabel").pack(anchor="w", pady=(2, 0))

        # Main split: left = controls, right = io
        body = ttk.Frame(outer, style="Bg.TFrame")
        body.pack(fill="both", expand=True)
        body.columnconfigure(0, weight=0, minsize=320)
        body.columnconfigure(1, weight=1)
        body.rowconfigure(0, weight=1)

        # ----- LEFT CARD: configuration -----
        left = self._card(body)
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 12))

        ttk.Label(left, text="Configuration", style="Section.TLabel").pack(anchor="w", pady=(0, 10))

        # Mode toggle
        ttk.Label(left, text="Mode", style="Field.TLabel").pack(anchor="w")
        self.mode_var = tk.StringVar(value="encrypt")
        mode_box = tk.Frame(left, bg=self.CARD)
        mode_box.pack(fill="x", pady=(2, 14))
        ttk.Radiobutton(mode_box, text="Encrypt", value="encrypt",
                        variable=self.mode_var, style="Mode.TRadiobutton").pack(side="left")
        ttk.Radiobutton(mode_box, text="Decrypt", value="decrypt",
                        variable=self.mode_var, style="Mode.TRadiobutton").pack(side="left", padx=(16, 0))

        # Pattern
        ttk.Label(left, text="Cipher pattern  (e.g.  C1 C2 C2 C1)",
                  style="Field.TLabel").pack(anchor="w")
        self.pattern_var = tk.StringVar(value="C1 C2 C2 C1")
        ttk.Entry(left, textvariable=self.pattern_var).pack(fill="x", pady=(2, 14))

        # Shifts mapping
        ttk.Label(left, text="Shift values  (one per line, e.g.  C1=6)",
                  style="Field.TLabel").pack(anchor="w")
        self.shift_text = tk.Text(left, height=6, font=("Consolas", 10),
                                  relief="solid", borderwidth=1,
                                  highlightthickness=0, padx=8, pady=6)
        self.shift_text.insert("1.0", "C1=6\nC2=20")
        self.shift_text.pack(fill="x", pady=(2, 14))

        # Action buttons
        actions = tk.Frame(left, bg=self.CARD)
        actions.pack(fill="x", pady=(4, 0))
        ttk.Button(actions, text="Run", style="Primary.TButton",
                   command=self.on_run).pack(fill="x")
        ttk.Button(actions, text="Swap input ⇄ output", style="Ghost.TButton",
                   command=self.on_swap).pack(fill="x", pady=(8, 0))
        ttk.Button(actions, text="Clear all", style="Ghost.TButton",
                   command=self.on_clear).pack(fill="x", pady=(6, 0))

        # ----- RIGHT CARD: io -----
        right = self._card(body)
        right.grid(row=0, column=1, sticky="nsew")
        right.columnconfigure(0, weight=1)
        right.rowconfigure(1, weight=1)
        right.rowconfigure(3, weight=1)
        right.rowconfigure(5, weight=0)

        ttk.Label(right, text="Input message",
                  style="Section.TLabel").grid(row=0, column=0, sticky="w", pady=(0, 6))
        self.input_text = tk.Text(right, height=6, wrap="word",
                                  font=("Segoe UI", 11),
                                  relief="solid", borderwidth=1,
                                  highlightthickness=0, padx=10, pady=8)
        self.input_text.insert("1.0", "HELLO WORLD")
        self.input_text.grid(row=1, column=0, sticky="nsew", pady=(0, 12))

        ttk.Label(right, text="Output",
                  style="Section.TLabel").grid(row=2, column=0, sticky="w", pady=(4, 6))
        self.output_text = tk.Text(right, height=6, wrap="word",
                                   font=("Segoe UI", 11),
                                   relief="solid", borderwidth=1,
                                   highlightthickness=0, padx=10, pady=8,
                                   background="#fafbff")
        self.output_text.grid(row=3, column=0, sticky="nsew")

        # Output row buttons
        outbtns = tk.Frame(right, bg=self.CARD)
        outbtns.grid(row=4, column=0, sticky="ew", pady=(8, 0))
        ttk.Button(outbtns, text="Copy output", style="Ghost.TButton",
                   command=self.on_copy).pack(side="left")

        ttk.Label(right, text="Shift sequence",
                  style="Section.TLabel").grid(row=5, column=0, sticky="w", pady=(16, 6))
        self.shift_view = tk.Text(right, height=4, wrap="none",
                                  font=("Consolas", 11),
                                  relief="solid", borderwidth=1,
                                  highlightthickness=0, padx=10, pady=8,
                                  background="#fafbff")
        self.shift_view.grid(row=6, column=0, sticky="ew")

        # Status bar
        self.status_var = tk.StringVar(value="")
        self.status_lbl = ttk.Label(outer, textvariable=self.status_var,
                                    style="Status.TLabel")
        self.status_lbl.pack(anchor="w", pady=(12, 0))

    def _card(self, parent):
        """A white card with a 1px border. Use the returned frame directly for both
        layout (.grid/.pack on it) and as the parent for child widgets."""
        card = tk.Frame(parent, bg=self.CARD,
                        highlightbackground=self.BORDER, highlightthickness=1,
                        bd=0, padx=18, pady=18)
        return card

    # ---- actions ----
    def on_run(self):
        try:
            pattern_tokens = parse_pattern(self.pattern_var.get())
            if not pattern_tokens:
                raise ValueError("Cipher pattern is empty. Try something like 'C1 C2 C2 C1'.")
            shift_map = parse_shifts(self.shift_text.get("1.0", "end"))
            key_sequence = build_key_sequence(pattern_tokens, shift_map)
            message = self.input_text.get("1.0", "end-1c")

            if self.mode_var.get() == "encrypt":
                result = do_encrypt(message, key_sequence)
            else:
                result = do_decrypt(message, key_sequence)

            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", result)

            self.shift_view.delete("1.0", "end")
            self.shift_view.insert("1.0", aligned_shift_view(message, key_sequence))

            mode_word = "Encrypted" if self.mode_var.get() == "encrypt" else "Decrypted"
            self._set_status(f"{mode_word} {sum(1 for c in message if c.isalpha())} letters "
                             f"with pattern {' '.join(pattern_tokens)}.", ok=True)
        except Exception as e:
            self._set_status(f"Error: {e}", ok=False)
            messagebox.showerror("Cipher error", str(e))

    def on_swap(self):
        out = self.output_text.get("1.0", "end-1c")
        if not out.strip():
            self._set_status("Nothing in output to swap.", ok=False)
            return
        self.input_text.delete("1.0", "end")
        self.input_text.insert("1.0", out)
        self.output_text.delete("1.0", "end")
        # flip the mode so a follow-up Run reverses the operation
        self.mode_var.set("decrypt" if self.mode_var.get() == "encrypt" else "encrypt")
        self._set_status("Swapped. Mode flipped — click Run to round-trip.", ok=True)

    def on_clear(self):
        self.input_text.delete("1.0", "end")
        self.output_text.delete("1.0", "end")
        self.shift_view.delete("1.0", "end")
        self._set_status("Cleared.", ok=True)

    def on_copy(self):
        out = self.output_text.get("1.0", "end-1c")
        if not out:
            self._set_status("Nothing to copy.", ok=False)
            return
        self.clipboard_clear()
        self.clipboard_append(out)
        self._set_status("Output copied to clipboard.", ok=True)

    def _set_status(self, msg, ok=True):
        self.status_var.set(msg)
        self.status_lbl.configure(foreground=self.OK if ok else self.ERR)


if __name__ == "__main__":
    app = CipherApp()
    app.mainloop()
