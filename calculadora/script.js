function calcular(n1,n2){

    n1 = parseFloat(document.getElementById("n1").value)
    n2 = parseFloat(document.getElementById("n2").value)
selector = document.getElementById("selector").value

switch(selector){
case '+':
    calculo = (n1 + n2)
    document.getElementById('resultado').innerHTML = `O resultado da soma é ${calculo}`
    break
case '-':
    calculo = (n1 - n2)
    document.getElementById('resultado').innerHTML = `O resultado da subtração é ${calculo}`
    break
case '*':
    calculo = (n1 * n2)
    document.getElementById('resultado').innerHTML = `O resultado da multiplicação é ${calculo}`
    break
case '/':
    calculo = Math.round((n1 / n2))
    if(Number.isNaN(calculo)){
    document.getElementById('resultado').innerHTML = `Fora dos reais`
    } else{
    document.getElementById('resultado').innerHTML = `O resultado da divisão é ${calculo}`

    break
        }
    }
 }