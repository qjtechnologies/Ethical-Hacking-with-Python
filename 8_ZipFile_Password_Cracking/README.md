# Compress and Decompress a ZipFile with Password

1.  Creating a Password Protected Zip File by compressing directory
```
zip --encrypt -r zipfile.zip myFolder/
```

2. Creating a Password Protected Zip File by compressing file
```
zip --encrypt zipfile.zip myfile1
```

3. Creating a Password Protected Zip File by compressing multiple files
```
zip --encrypt zipfile.zip myfile1 myfile2 myfile3
```

4. Decompress a Password Protected Zip File
```
unzip zipfile.zip
```
