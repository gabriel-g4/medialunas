
// detalle

// Gives the delete button a click event with a confirmation
// and redirects.


const btnDelete = document.getElementById("btn-delete");

btnDelete.addEventListener("click", (e)=>{
  e.preventDefault();
  if (confirm("Desea eliminar entrada?"))
  {
    window.location.href = btnDelete.getAttribute("href");
  }
});