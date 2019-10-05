# Unix Password Cracking using Dictionary Attacks

### Open a Unix File Password Shadow File
```
cat /etc/shadow
```

### John the Ripper
1. Cracking all Unix Account passwords
```
john /etc/shadow
```

2. Viewing all Cracked Passwords
```
john --show /etc/shadow
```

