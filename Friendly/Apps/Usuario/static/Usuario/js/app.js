$(document).ready(function(){
    validation = new Date()
    validation.setFullYear(validation.getFullYear() -15)
    format= `${validation.getFullYear()}-${(validation.getMonth()+1)}-${validation.getDate()}`
    console.log(format)
    $("#formulario").validate({
    errorClass:"is-invalid",
    rules:{
        nombre:{
            required:true
        },
        Apellido:{
            required:true
        },
        Email:{
            required: true,
            email:true
        },
        fnacimiento:{
            required:true,
            max:format
        }
    },
    messages:{
        nombre:{
            required:"Debe ingresar su nombre"
        },
        Apellido:{
            required:"Debe ingresar su apellido"
        },
        Email:{
            required: "Debe ingresar su correo",
            email: "Debe ingresar un correo valido"
        },
        fnacimiento:{
            required:"Debe ingresar su fecha de nacimiento",
            max:"Debes ser mayor de 15 años"
        }
    }


    })
})

$("#formulario").submit(function(){
    if($("#formulario").valid()){
        return true
    }else{
        Swal.fire({
            type: 'error',
            title: '¡¡¡ Se produjo un error !!!  ',
            text: 'Por favor verifique sus datos',
            
          })
    }
    return false
})