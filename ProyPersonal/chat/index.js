const redline = require("readline");

const rl = redline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

function add(x1, x2) {
    return x1 + x2;
}

function substract(x1, x2) {
    return x1 - x2;
}

function multiply(x1, x2) {
    return x1 * x2;
}

function divide(x1, x2) {
    if (x2 === 0) {
        console.log("NO seas pendejo");
    } else {
        return x1 / x2;
    }
}

console.log("1. Suma");
console.log("2. Resta");
console.log("3. Multiplicacion");
console.log("4. Division");

rl.question("Elije una opcion: ", function (opcion) {
    opcion = parseInt(opcion);

    rl.question("Introduce el numero deseado: ", function (input1) {
        let x1 = parseFloat(input1);

        rl.question("introduce el segundo numero desesado:", function (input2) {
            let x2 = parseFloat(input2);

            if (opcion === 1) {
                console.log("Suma: ", add(x1, x2));
            } else if (opcion === 2) {
                console.log("Resta: ", substract(x1, x2));
            } else if (opcion === 3) {
                console.log("Multiplicacion: ", multiply(x1, x2));
            } else if (opcion === 4) {
                console.log("Division: ", divide(x1, x2));
            } else {
                console.log("Opcion no valida");
            }
            rl.close();
        });
    });
});

