# image-to-ascii
## Project Description
image-to-ascii is a fully open-source project which converts an image into an ascii art image. </br>
## How to Install image-to-ascii ?
Here are few steps you have to complete to install and run image-to-ascii

**Step 0 :** Open your favorite terminal

**Step 1 :** Clone the repository

```
$ git clone https://github.com/Arkeon34/image-to-ascii
```

**Step 2 :** Create a python virtual environment

```
$ cd image-to-ascii
$ python -m venv venv-name
```

**Step 3:** Run the virtual environment
```
# Windows PowerShell
$ venv-name\Scripts\activate.ps1

# Linux terminal (bash)
$ source venv-name/bin/activate
```

**Step 4:** Install the dependencies
```
$ pip install -r requirements.txt
```
Now you are ready to go !

## How to convert my image ?
The project is quite simple at the moment. </br>
To convert your image into ascii art, you just need to put your image in the 'images' directory. </br>
Then, in your terminal run this command :
```
$ python module_core/main.py -in image-to-ascii/images/[IMAGE-NAME] -out result/text.txt
```

## Final result!
![demo_ascii](https://user-images.githubusercontent.com/94650900/153655210-e679c88e-d633-4608-9004-8f9365944744.png)
![demo-image](https://user-images.githubusercontent.com/94650900/153655291-c71a0337-37a2-4bf3-a940-8706a572377c.png)
