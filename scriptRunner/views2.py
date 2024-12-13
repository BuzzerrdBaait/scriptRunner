from django.shortcuts import HttpResponse,render

from django.conf import settings

from .functions import *

import subprocess

import os

example_nums=[]

post_args=[]


def newFunction(functionName,numArgs):
    #https://www.redhat.com/en/blog/use-python-subprocess-bash
    #subprocess.run([f'cd..','python manage.py startapp {appName}'])

    JAVASCRIPT_PATH=os.path.join(settings.BASE_DIR,'static','scriptrunner','scriptRunnerEX.js')

    HTML_PATH=os.path.join(settings.BASE_DIR,'templates','scriptRunner','scriptRunner.html')

    VIEWS_PATH=os.path.join(settings.BASE_DIR,'scriptRunner','views.py')

    FUNCTIONS_PATH=os.path.join(settings.BASE_DIR,'scriptRunner','functions.py')

    print( "Triggered newFunction\n"
          f"Function Name  : {functionName}\n"
          f"Number of args :{numArgs}\n"
          f"JS file path   :{JAVASCRIPT_PATH}\n"
          f"HTML file path :{HTML_PATH}\n")
    
#      S T A R T    J A V A S C R I P T    
    jsFunctionValidation = """
else if(functionID == '{functionName}') {{
""".format(functionName=functionName)

    for i in range(int(numArgs)):
        jsFunctionValidation += """
    arg{x} = document.getElementById('{functionName}_arg{x}');
    """.format(functionName=functionName, x=i+1)

    # Start the signal assignment (no newline after the backtick)
    jsFunctionValidation += """
    signal = `function=${{functionID}}"""

    # Now add the arguments in a single line
    args = "".join([f"&arg{x}=${{arg{x}}}" for x in range(1, int(numArgs) + 1)])
    jsFunctionValidation += args + "`;\n}"  # Keep the signal and arguments on the same line

    insert_text(JAVASCRIPT_PATH,'//_.-._.-._',jsFunctionValidation)

#   E N D    J A V A S C R I P T 

#_.-._.-._.-._.-._.-._.-._.-._.-.

# S T A R T   H T M L

    htmlInsertion = f"""
<div class="container">
    <input type="text" id="{functionName}_arg1" placeholder="">
"""

    # Add input fields for the rest of the arguments
    for i in range(2, int(numArgs) + 1):
        htmlInsertion += f'    <input type="text" id="{functionName}_arg{i}" placeholder="">\n'

    # Add the button to call the function
    htmlInsertion += f"""
    <button onclick="pythonSignals('{functionName}')">{functionName}</button>

    <div class="outputTab">
        <p2 id="{functionName}_output" text="{functionName} output"></p2>
    </div>
</div>
<!-- New function -->
"""

    # Insert the HTML into the HTML file
    insert_text(HTML_PATH, '<!-- New function -->', htmlInsertion)

# E N D    H T M L

# S T A R T   V I E W S

    viewsInsertion=f"""
        elif action == '{functionName}':
            """
    result = f"{functionName}("

    x=1

    for i in range(int(numArgs)):
        result+=f"arg{x}"
        x+=1

    viewsInsertion+="\n             "+result+")\n#I <3 programming, point fucking blank!"

    insert_text(VIEWS_PATH,"#I <3 programming, point fucking blank!",viewsInsertion)

# E N D     V I E W S

# S T A R T   F U N C T I O N

    x=1  
    functionInsertion = f"""
def {functionName}(
"""
    args = "".join([f"arg{x}='arg{x}'," for x in range(1, int(numArgs) + 1)])
    functionInsertion=functionInsertion[:-1]
    functionInsertion += args + "):\n"
    x+=1
    # Now add the function body, with proper indentation
    functionInsertion += """
        arguments = []
        for var, value in locals().items():
            args = f'{var}: {value}'
            arguments.append(args)
        return arguments
"""
    
    print("FUNCTION INSERTION:\n" + functionInsertion)

    # Now insert the new function into the functions.py file
    insert_text(FUNCTIONS_PATH, "print('newfunction')", functionInsertion)

    return "Function successfully created"


    




# Here is a large catalog of APIs that could be implemented into any website.
# https://catalog.data.gov/dataset?q=-aapi+api+OR++res_format%3Aapi
#https://data.wa.gov/Consumer-Protection/Data-Breach-Notifications-Affecting-Washington-Res/sb4j-ca4h/about_data

def scriptRunner(request):

    #optional SAML integration 

    # https://github.com/SAML-Toolkits/python-saml/tree/master/demo-django
    #           OR
    # https://github.com/grafana/django-saml2-auth

    if request.method == 'POST':

        post_args=[]


        #_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.
        # Pulling out the arguments from the post's body
        #_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.
        for item in request.POST:
            post_args.append(request.POST.get(item))


        #_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.
        # Extracting our arguments from post_args
        #_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.
        try:
            action=post_args[0]
        except:
            print("action not found")
        try:
            arg1=post_args[1]
        except:
            print("arg1 not found")
        try:
            arg2=post_args[2]
        except:
            print("args2 not found")
        try:
            arg3=post_args[3]
        except:
            print("args 3 not found.")
        try:
            arg4=post_args[4]
        except:
            print("args 4 not found.")

            
        #_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.
        # Checking arg1 to determine what python function to run.
        #_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.
        if action == 'newFunction':

            functionName=arg1

            numArgs=arg2

            result = newFunction(functionName,numArgs)

        #I <3 programming, point fucking blank!


        else:
            result="Null call"


        #_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.
        # Return the output with HttpResponse
        # _.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.    
            
        return HttpResponse(result)
    
    return render(request, 'scriptRunner.html')

