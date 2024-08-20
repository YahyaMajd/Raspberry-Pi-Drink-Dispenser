let D = document.getElementById("Dispense4");
D.addEventListener("click", function()
{
    console.log(1+2)
    sendSignal("click", "TRUE");
})

function Dispense(){
    const dispense = {"RUM_COKE" : "true"}
    const disp_str = JSON.stringify(dispense);
    return disp_str;
}

function sendSignal(){
    fetch('http://localhost:5000',{
        method : 'POST',
        headers :{
            'Content-type' : 'application/json'
        },
        body : JSON.stringify(Dispense())
    }).then(res => {
        return res.json()
    }).then(
        data => console.log(data)).catch(error => console.log("ERROR"))
}