# Python_Chatbot
Python Chatbot Project
Project Showcase Entry [1000 words]

For this project, I was assigned to create a chatbot using Python. I worked with a group of five
other students to complete this project. We wanted to create a chatbot based around sports
where the user can talk to the chatbot about sports. Our devised plan in order to create this
chatbot was to each create our own separate chatbot and then combine them all together as
one whole chatbot about sports. So, we each decided to pick a sport to theme our own separate
chatbots to work on. The sports include Football, Rugby, Cricket, Boxing and Basketball which I
chose. This ultimately would lead to our main chatbot to be based around five different sports.

My contribution to this project was to create my own mini chatbot about Basketball, in particular,
NBA. My idea was to create an NBA chatbot that would let the user actually chat to the chatbot
about basketball by using lists. With this method, I could program my chatbot to get the user to
enter a question such as “what is your favourite team?” and then the chatbot would check if the
user’s input matched anything in the list using selection and then respond back to the user with
a random team picked out of a database.

In addition, I had also created a database using SQLite 3 and DB Browser For SQLite which is a
software that allowed me to keep track of my database. I had implemented a database because
it allowed the user to talk more about the sport to the chatbot such as asking about “who is the
tallest player?” in which the chatbot would respond by querying the database and finding the
tallest player. I already knew how to use an SQL Database alongside with Python because I had
previous programming experience during my A-Levels since my A-Level Computer Science
Project was based around the use of databases which is a skill that helped me extend the
functionality of this chatbot project. Also, my Software Design module also aided towards my
chatbot because it had taught me more about SQL in which I could use newly learnt commands
on top of my known knowledge as well design the database better with normalisation.

Furthermore, after finishing implementing a database to my chatbot I had realised that I could
extend and improve my program even more by integrating an API. An API is an Application
Programming Interface which would allow importing the package onto my program for use. I
found an NBA API that can search and gather data from a website that contained NBA
statistics. As I read the documentation for this API package, I learnt how to use this API as well
as to structure and format my code using other packages like ‘pprint’ so that the program prints
it clearly for the user because the API collects raw data which are numbers in lists and
dictionaries. The documentation did not include full code solutions on how to use the API so I
had to test for myself by integrating the functions of the package with the programming
knowledge I already knew.

Finally, I wanted to make my program more interactive with the user by making the program
actually speak to the user as well as print the text on the screen. In order to do this, I had to
research how to do this. I was lucky enough to find a package and line of code that solved my
problem. I then put this into my program and created it as a general function (say()) which takes
in a string as a function input and turns it into speech and prints the text. This changed most of
the code so that instead of print I call this function so that the chatbot can actually speak.

In conclusion, I feel that this chatbot project has improved me a lot as a programmer which then
helps me towards my Programming and Algorithms module because it allowed me to practise
new skills learnt from that module and transfer them towards this project. In addition, I was also
able to practise techniques learnt from my Software Design module towards this project
because I had to work in a team of five which meant we implemented the use of Scrum
Techniques. For example, every week during our ALL lab sessions, we would share our
progress with each other to make sure we were all on track to finish before the project deadline
as well as help each other on code if needed. Even for myself, I used other scrum methods
such having my own Kanban board to keep track of the work I needed to do for towards my
contribution to the project.

Furthermore, during this project, I also learnt how to use PyCharm CE which is a free Integrated
Development Environment for Python. I used this software instead of the normal Python IDE
because it allowed me to track all the files I created for my project as well as having a terminal
for me to test my python code. During my project, I had to set up my own Virtual Environment
within PyCharm so that I could install packages on my computer without any risks and so that
some of my teams code would be compatible with my system since we found that some pieces
of code would work for someone's system but will not for mine. Therefore, to solve this problem,
a Virtual Environment was needed so that their code could work on my system when we
merged all our contributed work together as one. PyCharm also helped me write better code by
highlighting typo errors which I can amend and write better quality code.

Finally, PyCharm also had a git integration in it which allowed us as a team to create a git
repository so that we can keep track of file changes and version control our code so that any
accidental changes can be reverted back. Use of GitHub benefited me as towards this project
because it allowed us to clone the repository to PyCharm where we can access each other's
files to see everyone’s contribution to the project and see if there are any similar solutions of
code we need to solve our own code problems without having to do lots of research.

References
Text to speech code:
https://stackoverflow.com/questions/22139394/python-text-to-speech-with-that-can-read-variables-contents

NBA api Documentation:
https://sportsreference.readthedocs.io/en/latest/nba.html
