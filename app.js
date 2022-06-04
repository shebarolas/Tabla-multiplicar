const {crearArchivo} = require("./helpers/multiplicacion");

crearArchivo(3).then(message => console.log(message)).catch(err => console.log(err));