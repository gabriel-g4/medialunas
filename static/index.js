// index

// Adds a click event to each main table row to go to its
// detalle's url.

const tableRows = document.querySelectorAll(".main-row");

tableRows.forEach(tr => {
  tr.addEventListener("click", ()=> {
    window.location.href = tr.getAttribute("data-url");
  })
});

// DYNAMIC SEARCH BAR

// My approach to this problem was to get the main table, and
// operate on its rows and cells.
// I used an event on the keyup of the bar, then that value is stored
// and later compared to each row value, accesing it by its index
// The select tag and its options must have the same order
// as the table columns. (not the same values)
// If the table in its accessed cell includes the search bar value
// shows the row, else changes its style.display to none.

const searchBar = document.getElementById("search-bar");
const mainTable = document.getElementById("main-table");
const rows = mainTable.rows;
const length = rows.length;

searchBar.addEventListener('keyup', (e) => {
  const barValue = searchBar.value.toLowerCase();
  const selectedFilter = document.getElementById("selected-filter");
  const filterIndex = selectedFilter.selectedIndex;
  
  for (let i = 1; i < length; i++) {
    let col = rows[i].cells;
    
    if (!col[filterIndex].innerHTML.toLowerCase().includes(barValue)) {
      mainTable.rows[i].style.display = "none";
    } else {
      mainTable.rows[i].style.display = "table-row";
    }
  }
})