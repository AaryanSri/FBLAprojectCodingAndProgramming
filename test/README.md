# What is this project?
Hello! My name is Aaryan Srivastava, and this project is a submission for the
Coding + Programming Event in FBLA. This project is composed of multiple parts
which will be explained below, but there are also comments within the code itself
to help you understand it's purpose. Simply put, this project contains a
database (json file) in which I extract 5 questions on random and display them
on a server (think of it as a local website). I then allow the user to input his
or her answers, and then I generate a scoresheet containing all the information.

# My database
My database contains 50 questions, and is contained in the static folder, named
"database.json". There is also a backup file that I uploaded in the json folder in
.txt. This database has 50 questions, and essentially contains everything that my Website
will upload. This includes answer choices, the correct answer, the question itself, and
the question type. My program will extract information and load it onto the local server site.

# My Python-Code
I coded this using Python, meaning to run this program, you will need to install
python and python flask.


# My HTML-code
This code also uses html and css to display the code on your local server. All of
my html files can be found in the templates folder. Each html file has comments
which explain what each file does.
My CSS code is located in static > css.

# How to run this

First, install python. This can be done by going to python.org/downloads, and
download the latest version depending on which operating system you are using.
Now, you will need to install this code. On this github repository, there is a
download code option. Go ahead and download it wherever you like.

Now, open your command prompt. If you are on windows, first open your command prompt.
Now, navigate to the folder where the test.py file is at. After you do this,
you will now need to install Python flask. But you can do this in your command prompt.
Simply type in this command: "py -m venv env".
After a little bit, when your file comes back,
type this command: "env\Scripts\activate".
You should now see a (env) next to your cmd. Now type this command: "pip install flask".
After this, type in this command: "set FLASK_APP=test.py".

Now type this command: "flask run".

You should see something that says "Running on...". Copy that http address and paste it
into google chrome or whichever browser you would like to use. And voila! My code should be running!

If you want to look at my original code, then simply navigate to the files which I specified
above, and you are free to naviagte through my project! Enjoy!
