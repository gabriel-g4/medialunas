// Agregar.html on /editar

// Changes select tags "tipo" and "masa_madre" by making the db 
// fetched option the default "selected" option for convenience sake 


function setSelected(selectId) {
    const element = document.getElementById(selectId);
    const eValue = element.getAttribute("value");
    const eChildren = element.children;


    for (let i = 0; i < eChildren.length; i++) {
        if (eChildren[i].getAttribute("value") == eValue) {

            eChildren[i].setAttribute("selected","selected")
            break;

        }
    }
}

setSelected("tipo");
setSelected("masa_madre");