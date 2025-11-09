🧾 Wallet Text Extractor (Berkeley DB Inspector)

⚠️ Educational / Forensic Use Only
This script is intended for educational, debugging, or forensic analysis of your own wallet data files (e.g., wallet.dat from older Bitcoin Core versions).
It does not recover private keys or decrypt data — it only extracts readable text strings from a Berkeley DB database.

Never use it to inspect or analyze wallet files that you do not own or have permission to access.

📘 Overview

extract_wallet_text.py opens a Berkeley DB database file (commonly used in early Bitcoin Core wallets) and scans its contents for human-readable text such as:

Names or labels

E-mail addresses

Years or dates

Other words or strings that appear to be ASCII or UTF-8 text

It prints out any key/value entries that appear to contain text rather than binary or hexadecimal data.

⚙️ Features

Opens .dat files using bsddb3 (Berkeley DB Python bindings).

Detects printable strings that might include:

Years (1990–2099)

Emails

Words (4 or more letters, including Polish characters)

Ignores pure hexadecimal or binary data (e.g., cryptographic keys).

Displays potentially interesting entries in a human-readable format.

🧠 How It Works

Opens a Berkeley DB file using:

db = bsddb3.btopen(path, 'r')


Iterates through every key–value pair in the database.

Decodes the binary data (bytes) to text (UTF-8 with replacement on errors).

Uses simple heuristics (regex patterns) to detect:

readable words,

years like “2017” or “2021”,

email addresses,

or other printable text sequences.

Prints all entries that appear to contain human-readable text:

---- ENTRY ----
KEY  : label
VALUE: Main wallet account
---- ENTRY ----
KEY  : email
VALUE: satoshi@example.com

🧩 Regex Patterns Used
Pattern	Purpose
`\b(19	20)\d{2}\b`
[A-Za-ząęćłńóśżźĄĆĘŁŃÓŚŻŹ]{4,}	Detects readable words (4+ letters)
[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}	Detects email addresses

The script also filters out sequences that look like pure hexadecimal data (e.g. abcdef123456) to reduce noise.

▶️ Usage
Installation

You need the bsddb3 library:

pip install bsddb3

Running
python3 extract_wallet_text.py wallet_copy.dat


If you run it without arguments:

python3 extract_wallet_text.py


You’ll see:

Usage: python3 extract_wallet_text.py wallet_copy.dat

Example Output
---- ENTRY ----
KEY  : name
VALUE: My old BTC wallet
---- ENTRY ----
KEY  : email
VALUE: test@example.com
---- ENTRY ----
KEY  : label
VALUE: Backup 2015


If no readable strings are found:

Nie znaleziono czytelnych etykiet/komentarzy.
(No readable labels/comments found.)

⚠️ Limitations & Notes

This tool does not extract, decrypt, or expose private keys.

It only prints text strings that can be decoded from the Berkeley DB file.

It is not guaranteed to identify all meaningful data — results depend on file structure and encoding.

Works primarily with older wallet formats (wallet.dat from Bitcoin Core ≤ v0.15).

For analysis only — not a wallet recovery tool.

🧪 Example Use Cases

Inspecting your own backup wallet.dat file for readable metadata.

Understanding how early Bitcoin Core wallets stored information in Berkeley DB.

Digital forensics or research on legacy cryptocurrency software.

🪪 License & Ethics

MIT License — provided “as is,” without any warranty.
Use responsibly and only on wallet files that you legally own or have explicit permission to analyze.
Unauthorized inspection of others’ data may violate privacy laws and ethical standards.

BTC donation address: bc1q4nyq7kr4nwq6zw35pg0zl0k9jmdmtmadlfvqhr
