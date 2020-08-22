var curValue = 0.0;

function addtotext(value){
    document.getElementById("calcEntry").value += value;
}
function addtoOverall(value){
    document.getElementById("overallEquation").value += value;
}

function calculate(value){
    perfromBasic();
    addtoOverall(getCalc());
    addtoOverall(value);
    if (value == "="){
        addtoOverall(curValue);
    }
    Clear();
}

function perfromBasic(){
    last = document.getElementById("overallEquation").value;
    last = last[last.length-1];
    switch (last){
        case "+": curValue += getCalc(); break;
        case undefined: curValue += getCalc(); break;
        case "-": curValue -= getCalc(); break;
        case "*": curValue *= getCalc(); break;
        case "/": curValue /= getCalc(); break;
        default: 
            curValue = getCalc();
            document.getElementById("overallEquation").value = "";
            break;
    }
}

function setCalc(val){
    document.getElementById("calcEntry").value = val;
}

function getCalc(){
    num = document.getElementById("calcEntry").value;
    if (num == "" && document.getElementById("overallEquation").value == ""){
        return 0;
    }
    else if (num == ""){
        return "";
    }
    return parseFloat(num, 10);
}

function Clear(){
    document.getElementById("calcEntry").value="";
}

function ClearAll(){
    document.getElementById("overallEquation").value = "";
    Clear();
    curValue = 0.0;
}