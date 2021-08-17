 op1 = "Piedra"
 op2 = "Papel"
 op3 = "Tijera"

 resultado = function(user, cpu){
    if(user != cpu){
        if(user === op1 && cpu === op3){
            console.log("el usuario GANO con "+ op1)
        }elif(user === op2 && cpu === op1){
            console.log( "el usuario GANO con " + op2)
        }elif(user === op3 && cpu === op2){
            console.log("el usuario GANO con " + op3)
        }else{
            console.log("La CPU Gano!!")
        }
    }elif(user === cpu){
        console.log("Empate")
    }
}