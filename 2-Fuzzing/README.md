# 2. Fuzzing - TRUN Command

**Target:** Vulnserver (Windows XP SP3)  
**Attacker:** Kali Linux (VMware)  
**Tool Used:** Python socket script  
**Command Under Test:** `TRUN`

---

## 🐍 Script: `fuzz.py`

This script sends an increasingly large payload to the TRUN command to determine at what point the application crashes.

### 🔧 How it works:

- Starts with 100 "A"s
- Increments by 100 each loop
- Sends: `TRUN /.:/AAAA...`
- Waits 1 second between each try
- When Vulnserver crashes, it prints how many bytes caused the crash

---

### 🧪 Run it like this:

```bash
python3 fuzz.py
