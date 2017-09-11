# Proxy Checker
Simple proxy checker powered by **Python**
## Usage
**You need to have a text document with proxies. Then you must execute the script**
```SHELL
./check.py
```
**And then type your proxy text document. After the script filters the good and bad proxies, and by the way, adds the good proxies into text document, named `good.txt`**
## Problems with `colorama`?
Maybe you'll have this error while exec the script
```SHELL
Traceback (most recent call last):
  File "./check.py", line 4, in <module>
    from colorama import Fore
ImportError: No module named colorama
```
### How to fix it?
**You must install the `colorama` module, you can even do it by typing in your terminal next:**
```SHELL
sudo pip install colorama
```
### WARNING
*If you didn't install , pip, do it now, coz without this, you'll never fix your problem, and 'll never install modules for* **Python** 
```SHELL
sudo apt install python-pip
```
