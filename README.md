# Number-Finder
Save time finding Numbers or emails in text.

## What does it do?
Have you ever had to run through pages upon pages oif a document trying to find all of the phone numbers or emails within in it to put into a list? Or just wished you had an easy way of collecting the information from a slab of text? 
Well that is exactly what this script will do.
It will take the text and scan through it and search for every phone number or email that matches the criteria. This is due to a series of regular expressions that help it figure out what is actually a phone number so it doesn't get mixed up with something like a date!

## Usage
So as mentioned this script utilises Regular Expressions, it also utilises a module named 'Pyperclip'. This allows a script to take something from your clipboard and work with it, or in a simialr fashion, work on something and then put it onto your clipboard ready to be pasted.
What you will do is: 
1. copy the text you want searched
2. Run the script
3. In a notepad (or where ever you would like the information) paste the information

**Done!**

Now you have a list of all the phone numbers or emails from within that copied text.
Keep in mind, since I am in Australia, this does only work for _Australian_ Numbers. The email portion will work as long as the emails follow the normal naming conventions.

## Installation
You can find the documentation for Pyperclip [here.](https://pyperclip.readthedocs.io/en/latest/)

Can be installed with the following:
```bash
pip install pyperclip
```
