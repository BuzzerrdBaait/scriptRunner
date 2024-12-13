import os
from django.conf import settings

def insert_text(file_path, search_string,text):

    with open(file_path,'r') as file:

        content= file.readlines()

    keywordFoundIndex=[]

    for index, line in enumerate(content):

        if search_string in line:

            keywordFoundIndex.append(index)

    if keywordFoundIndex:

        last_occurence_of_keyword= keywordFoundIndex[-1]

        content.insert(last_occurence_of_keyword+1,text+'\n')

    with open(file_path,'w') as file:

        file.writelines(content)

    print("\nUpdated document\n")

def deleteLines(filePath,delimiter):
    deleteLine = False
    with open(filePath, "r") as file:
        content = file.readlines()

    with open(filePath, "w") as file:
        for line in content:
            if deleteLine and delimiter in line:
                deleteLine = False
                continue

            if delimiter in line and not deleteLine:
                deleteLine = True
                continue  

            if not deleteLine:
                file.write(line)


def newFunction(functionName,numArgs):
    #https://www.redhat.com/en/blog/use-python-subprocess-bash
    #subprocess.run([f'cd..','python manage.py startapp {appName}'])

    JAVASCRIPT_PATH=os.path.join(settings.BASE_DIR,'static','scriptrunner','scriptRunner.js')

    HTML_PATH=os.path.join(settings.BASE_DIR,'templates','scriptRunner','scriptRunner.html')

    VIEWS_PATH=os.path.join(settings.BASE_DIR,'scriptRunner','views.py')

    FUNCTIONS_PATH=os.path.join(settings.BASE_DIR,'scriptRunner','functions.py')

    FUNCTIONS_TXT=os.path.join(settings.BASE_DIR,'static','scriptrunner','functions.txt')


    JSdelimeter=f"//_.-._{functionName}_.-._"

    HTMLdelimeter=f"<!--{functionName}_-->"

    VIEWSdelimeter=f"#<<<{functionName}>>>"

    FUNCTIONdelimeter=f"#<<<{functionName}>>>"

    print( "Triggered newFunction\n"
          f"Function Name  : {functionName}\n"
          f"Number of args :{numArgs}\n"
          f"JS file path   :{JAVASCRIPT_PATH}\n"
          f"HTML file path :{HTML_PATH}\n")
    
#      S T A R T    J A V A S C R I P T    
    jsFunctionValidation = f"""
{JSdelimeter}
else if(functionID == '{functionName}') {{
"""

    for i in range(int(numArgs)):
        jsFunctionValidation += """
        arg{x} = document.getElementById('{functionName}_arg{x}').value;
    """.format(functionName=functionName, x=i+1)

    # Start the signal assignment (no newline after the backtick)
    jsFunctionValidation += f"""
        signal = `function={functionName}"""

    # Now add the arguments in a single line
    args = "".join([f"&arg{x}=${{arg{x}}}" for x in range(1, int(numArgs) + 1)])
    jsFunctionValidation += args + f"`;}}\n{JSdelimeter}"  # Keep the signal and arguments on the same line

    insert_text(JAVASCRIPT_PATH,'_.-._',jsFunctionValidation)

#   E N D    J A V A S C R I P T 

#_.-._.-._.-._.-._.-._.-._.-._.-.

# S T A R T   H T M L

    htmlInsertion = f"""
{HTMLdelimeter}
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
{HTMLdelimeter}
"""

    # Insert the HTML into the HTML file
    insert_text(HTML_PATH, '_-->', htmlInsertion)

# E N D    H T M L

# S T A R T   V I E W S

    viewsInsertion=f"""
        {VIEWSdelimeter}
        elif action == '{functionName}':
            """
    result = f"{functionName}("

    x=1

    for i in range(int(numArgs)):
        result+=f"arg{x},"
        x+=1

    viewsInsertion+="\n             result="+result+f")\n       {VIEWSdelimeter}"

    insert_text(VIEWS_PATH,">>>",viewsInsertion)

# E N D     V I E W S

# S T A R T   F U N C T I O N

    x=1  
    functionInsertion = f"""
{FUNCTIONdelimeter}
def {functionName}(
"""
    args = "".join([f"arg{x}," for x in range(1, int(numArgs) + 1)])
    functionInsertion=functionInsertion[:-1]
    functionInsertion += args + "):\n"
    x+=1
    # Now add the function body
    functionInsertion += f"""
        print('yay!')
        return "yay!"

{FUNCTIONdelimeter}
"""
    
    # Now insert the new function into the functions.py file
    insert_text(FUNCTIONS_PATH, ">>>", functionInsertion)
    
    try:
        # appending to functions.txt
        with open(FUNCTIONS_TXT,'a') as file:
            file.write(functionName+"\n")

    except:

        print("unable to insert into functions.txt")

    return "Function successfully created"



# DO NOT DELETE ! ! ! >>-->>>

#<<<deleteFunction>>>
def deleteFunction(functionName,):
    
    JAVASCRIPT_PATH=os.path.join(settings.BASE_DIR,'static','scriptrunner','scriptRunner.js')

    HTML_PATH=os.path.join(settings.BASE_DIR,'templates','scriptRunner','scriptRunner.html')

    VIEWS_PATH=os.path.join(settings.BASE_DIR,'scriptRunner','views.py')

    FUNCTIONS_PATH=os.path.join(settings.BASE_DIR,'scriptRunner','functions.py')
    
    FUNCTIONS_TXT=os.path.join(settings.BASE_DIR,'static','scriptrunner','functions.txt')

    JSdelimeter=f"//_.-._{functionName}_.-._"

    HTMLdelimeter=f"<!--{functionName}_-->"

    VIEWSdelimeter=f"#<<<{functionName}>>>"

    FUNCTIONdelimeter=f"#<<<{functionName}>>>"

    try:
        deleteLines(JAVASCRIPT_PATH,JSdelimeter)

    except:
        deletedLinesComplete=f"Failed to delete {functionName} in Javascript file."

    deleteLines(HTML_PATH,HTMLdelimeter)

    deleteLines(VIEWS_PATH,VIEWSdelimeter)

    deleteLines(FUNCTIONS_PATH,FUNCTIONdelimeter)

    # We have to handle functions.txt different because we are looking for a keyword to remove.
    with open(FUNCTIONS_TXT,'r') as file:

        text=file.readlines()

    with open(FUNCTIONS_TXT,'w') as file:

        for line in text:

            if functionName not in line:
                file.write(line)


    deletedLinesComplete=f"Deleted {functionName}"

    return deletedLinesComplete

#<<<deleteFunction>>>







































