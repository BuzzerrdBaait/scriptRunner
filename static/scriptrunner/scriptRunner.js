function pythonSignals(functionID,...rest){

let signal=''

let numArgs=0

let arg1 = rest[0]

let arg2= rest[1]

let arg3= rest[2]

let arg4= rest[3]



if(functionID == 'newFunction'){

    arg1=document.getElementById('functionName').value

    numArgs= document.getElementById('numArgs').value

    signal= `function=${functionID}&functionName=${arg1}&numArgs=${numArgs}`

}

//_.-._{functionName}_.-._

//_.-._deleteFunction_.-._
else if(functionID == 'deleteFunction') {

        arg1 = document.getElementById('deleteFunction_arg1').value;
    
        signal = `function=deleteFunction&arg1=${arg1}`;}
//_.-._deleteFunction_.-._








fetch(scriptRunnerURL,{

    method: 'POST',
    headers:{

        'Content-Type': 'application/x-www-form-urlencoded',
        'X-CSRFToken' : csrfToken,
    },

    body: signal
})
.then (response => response.text())
.then(output => {

    if(functionID=='newFunction'){
        document.getElementById(`${functionID}`).innerText=output;
    }

    else{
        document.getElementById(`${functionID}_output`).innerText=output;
    }


})
.catch(error => console.error('Error',error));

}
