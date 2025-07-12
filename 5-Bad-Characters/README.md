# 5. Finding Bad Characters

**Goal:** Identify which byte values are "bad" (alter or break shellcode)

---

## 🔧 How it works:

- Send all bytes from `\x01` to `\xff` after EIP
- Observe them in memory (Dump window) in Immunity Debugger
- Look for broken or missing sequences

---

## 📦 Payload:

- 2003 "A"s
- 4 "B"s (EIP placeholder)
- 10 "C"s
- Full bad character list

---

## 🧪 Run:

```bash
python3 badchars.py
🔍 In Immunity Debugger:
Right-click → Follow ESP in Dump

Should look like:

Copy
Edit
01 02 03 04 05 06 07 08 09 0A ...
Look for broken bytes (e.g., missing 0A)

Record bad characters (e.g., \x00\x0a\x0d)
