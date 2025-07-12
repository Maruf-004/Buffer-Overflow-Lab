# 1. Spiking - TRUN Command

**Target:** Vulnserver (Windows XP SP3)  
**Attacker:** Kali Linux (VMware)  
**Tool Used:** Spike (`generic_send_tcp`)  
**Command Under Test:** `TRUN`

---

## 🔧 Script: `test.spk`

```c
s_readline();
s_string("TRUN");
s_string_variable("0");
