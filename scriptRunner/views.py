from django.shortcuts import HttpResponse,render

from django.conf import settings

from .functions import *

import subprocess

import os

example_nums=[]

post_args=[]


# Links to free government apis.
# https://catalog.data.gov/dataset?q=-aapi+api+OR++res_format%3Aapi
#https://data.wa.gov/Consumer-Protection/Data-Breach-Notifications-Affecting-Washington-Res/sb4j-ca4h/about_data

def scriptRunner(request):

    #optional SAML integration 

    # https://github.com/SAML-Toolkits/python-saml/tree/master/demo-django
    #           OR
    # https://github.com/grafana/django-saml2-auth

    FUNCTIONS_TXT=os.path.join(settings.BASE_DIR,'static','scriptrunner','functions.txt')



    if request.method == 'POST':

        post_args=[]
        
        #_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.
        # Pulling out the arguments from the post's body
        #_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.
        for item in request.POST:
            post_args.append(request.POST.get(item))

        print(post_args)   
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

        # DO NOT DELETE ! ! ! >>->>>

        #<<<deleteFunction>>>
        elif action == 'deleteFunction':
            
             result=deleteFunction(arg1,)
       #<<<deleteFunction>>>



        else:
            result="Null call"

        #_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.
        # Return the output with HttpResponse
        # _.-._.-._.-._.-._.-._.-._.-._.-._.-._.-. 
        # 
        # 
  
        return HttpResponse(result)

    
    dataForPage={

        'test': "test"

      #  'functions':functions
    }
    
    return render(request, 'scriptRunner.html', dataForPage)

