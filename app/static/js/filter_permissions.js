function search(query) {
  const input = query.toLowerCase();
  const tableRows = document.querySelectorAll('#datatable tbody tr');

  tableRows.forEach(row => {
    const module = row.cells[0].textContent.toLowerCase();
    const permission = row.cells[1].textContent.toLowerCase();
    const name = row.cells[2].textContent.toLowerCase();

    const searchPhrase = input.split(' in:');
    const searchValue = searchPhrase[0].trim();
    let columnsToSearch = ['module', 'permission', 'name'];

    if (searchPhrase.length > 1) {
      columnsToSearch = searchPhrase[1].split(',').map(c => c.trim());
    }

    let match = false;
    if (columnsToSearch.includes('module') && module.includes(searchValue)) {
      match = true;
    }
    if (columnsToSearch.includes('permission') && permission.includes(searchValue)) {
      match = true;
    }
    if (columnsToSearch.includes('name') && name.includes(searchValue)) {
      match = true;
    }

    if (match) {
      row.style.display = '';
    } else {
      row.style.display = 'none';
    }
  });
}

const advancedSearchInput = document.getElementById('advanced-search-input');
document.getElementById('advanced-search-button').addEventListener('click', (e) => {
  search(advancedSearchInput.value);
});

advancedSearchInput.addEventListener('keydown', (e) => {
  if (e.keyCode === 13) {
    search(e.target.value);
  }
});