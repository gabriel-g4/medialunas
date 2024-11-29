// index

// Adds a click event to each main table's row to go to its
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
// I used an event on the keyup of the bar, then that bar value is stored
// and later compared to each row value, accesing it by its index
// The select tag and its options must have the same order
// as the table columns. (not the same values)
// If the table in its accessed cell includes the search bar's value
// shows the row, else changes its style.display to none.

const searchBar = document.getElementById("search-bar");
const mainTable = document.getElementById("main-table");
const rows = mainTable.rows;
const length = rows.length;

searchBar.addEventListener('keyup', (e) => {
  const barValue = searchBar.value.toLowerCase();
  const selectedFilter = document.getElementById("selected-filter");
  const filterIndex = selectedFilter.selectedIndex - 1 
  // There is an extra value at the start of the select tag, so I need to 
  // extract 1 to match the table's columns' length;
  

  if (selectedFilter.value != "-"){

    for (let i = 1; i < length; i++) {
      
      let col = rows[i].cells;
      
      if (!col[filterIndex].innerHTML.toLowerCase().includes(barValue)) {
        mainTable.rows[i].style.display = "none";
      } else {
        mainTable.rows[i].style.display = "table-row";
      }

    }
  } else {

    // In this side of the bifurcation, the selected value is "-"
    // That means a general search in all rows and columns.

    for (let i = 1; i < length; i++) {

      let col = rows[i].cells;
      
      for (let j = 0; j < col.length; j++)  {
        
        if (col[j].innerHTML.toLowerCase().includes(barValue)){
          mainTable.rows[i].style.display = "table-row";
          break;
        }

        mainTable.rows[i].style.display = "none";

      } 
    }
  }
})