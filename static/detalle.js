
// detalle
/* <a href="/eliminar/{{ medialuna['id'] }}" class="btn btn-danger btn-lg" onclick="return confirm('Eliminar?');">Eliminar</a> */

const btnDelete = document.getElementById("btn-delete");

btnDelete.addEventListener("click", (e)=>{
  e.preventDefault();
  if (confirm("Desea eliminar entrada?"))
  {
    window.location.href = btnDelete.getAttribute("href");
  }
});