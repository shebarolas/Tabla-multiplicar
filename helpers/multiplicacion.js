const fs = require('fs');

const crearArchivo = async(base = 5) =>{
    try{
        let texto = "";
        for (let i = 1; i <= 10; i++) {
            texto += `${base} x ${i} = ${base * i}\n`;
        }
    
        fs.writeFile(`./out/tabla${base}.txt`, texto, (err)=>{
            if(err){
                throw err;
            }
        });

            return "Archivo creado con Extio"
    }catch(err){
        return "Error al crear Archivo";
    }
}

module.exports = {crearArchivo};

