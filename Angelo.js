function newFunction(marca, modelo, anio){
    var marca = marca || 'Toyota';
    var modelo = modelo || 'Coralla';
    var anio = anio || '2015';
    console.log(marca, modelo, anio);
}

// es6

function newFunction2(marca = 'Toyota', modelo = 'Corolla', anio = '2015'){
    console.log(marca, modelo, anio);
};

