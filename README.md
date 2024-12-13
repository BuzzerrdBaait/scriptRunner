Welcome to ScriptRunner

This is an experimental library that allows the easy integration of python widgets into your web app. 

Here are a couple screen shots:

Here is the scriptRunner application main page.

![image](https://github.com/user-attachments/assets/92aa6c75-0f54-41a3-954a-23823eb5bb16)

I choose to create a function called anyFunction with 3 arguments.

![image](https://github.com/user-attachments/assets/05152d89-cbad-4e19-b343-1b702a83afbf)

I refresh my page manually for now because I intend to implement the LLM here in the future. 

I guess Ill make another widget called multiplyNumbers while I am at it.

![image](https://github.com/user-attachments/assets/6264867c-51af-4df5-b9df-783dcb122a5d)

I test the widgets, if yay comes back you are good. Otherwise you will get a huge html string returned.

If in trouble at this point, here is how you can fix it:
I have found that restarting my server helps, and closing the files (scriptRunner.html, scriptRunner.js,views.py,functions.py). Also, depending on your browser setttings, you may have to clear the browser cache. It is a weird bug because after I do the previously mentioned steps, I don't have to do them again, and I can keep making more widgets without problems. I would love input here if anyone has some ideas.

So now all I have to do is open functions.py and edit the function's template however I like.
I turn this:
![image](https://github.com/user-attachments/assets/1c669971-9a94-4ad4-9f4c-3a08fb53db58)
To this:
![image](https://github.com/user-attachments/assets/718a00d7-daa5-42f5-bb0e-428e8fef3089)

And in my app I get this:

![image](https://github.com/user-attachments/assets/fc9ada9e-de3e-466a-bf0e-c35701550608)


Getting started:

cloning or downloading the zip file, unzip the file and open cmd line.

cd into the folder containing manage.py
use:
>>> py manage.py runserver
to launch the server
![image](https://github.com/user-attachments/assets/7169d0a3-0b4d-4215-888c-b5007852819b)
hold control+click http://127.0.0.1:8000/

this takes you to the main page.

![image](https://github.com/user-attachments/assets/2b7e8f1d-3cc8-48a6-994a-ad2eeacc82ce)

follow the link and that will take you to the app. 

Want to contribute?
I plan to add documentation to the main page. If anyone wants to help with that I would be grateful.
Also, I would be open to someone making this look better. I like building things and designing is not my forte.
Any interest give me motivation!

