# Jut.su auto skip script

This script help you with auto skip adds, intro and turn on the next series in site [jut.su](https://jut.su)

Now available only for this monitors:
* 1280x720
* 1920x1080
* 2560x1440


<hr>
At first, you need download and install Tesseract:

```
D:/Tesseract/tesseract.exe
```
[Link](https://tesseract-ocr.github.io/tessdoc/Home.html) (Choose your os)

Next you need clone this script:
```
git clone git@github.com:Splend1ed/Auto_jutsu.git

source venv/Scripts/activate
pip install -r requirements.txt
export PYTESSERACT_PATH=<path-to-tesseract.exe>
```
And run it:
```
python logic/main.py
```
If you want stop just open task manager and terminate it or press Ctrl + C in terminal

I will make a UI soon :)
