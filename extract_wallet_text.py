# extract_wallet_text.py
# pip install bsddb3
import bsddb3, re, string, sys

year_re = re.compile(r'\b(19|20)\d{2}\b')
word_re = re.compile(r'[A-Za-ząęćłńóśżźĄĆĘŁŃÓŚŻŹ]{4,}')
email_re = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')

def to_text(b):
    return b.decode('utf-8', errors='replace')

def interesting(s):
    if year_re.search(s): return True
    if email_re.search(s): return True
    if word_re.search(s): return True
    printable = sum(1 for ch in s if ch in string.printable and not ch.isspace())
    if printable >= 5:
        hex_chars = set("0123456789abcdefABCDEF")
        hex_ratio = sum(1 for ch in s if ch in hex_chars) / max(1, len(s))
        if hex_ratio > 0.9:
            return False
        return True
    return False

def main(p):
    try:
        db = bsddb3.btopen(p, 'r')
    except Exception as e:
        print("Błąd otwarcia DB:", e); return
    found = False
    for k,v in db.items():
        ks = to_text(k); vs = to_text(v)
        if interesting(ks) or interesting(vs):
            found = True
            print("---- ENTRY ----")
            if interesting(ks): print("KEY  :", ks)
            else: print("KEY  : (binary)")
            if interesting(vs): print("VALUE:", vs)
            else: print("VALUE: (binary)")
    db.close()
    if not found:
        print("Nie znaleziono czytelnych etykiet/komentarzy.")
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 extract_wallet_text.py wallet_copy.dat")
    else:
        main(sys.argv[1])
