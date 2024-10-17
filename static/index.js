// index

/* <script>
        document.addEventListener('DOMContentLoaded', function() {
          const rows = document.querySelectorAll('tr[data-url]');
          rows.forEach(row => {
            row.addEventListener('click', function() {
              window.location.href = this.getAttribute('data-url');
            });
          });
        });
    </script> 
*/

const tableRows = document.querySelectorAll(".main-row");

tableRows.forEach(tr => {
  tr.addEventListener("click", ()=> {
    window.location.href = tr.getAttribute("data-url");
  })
});

