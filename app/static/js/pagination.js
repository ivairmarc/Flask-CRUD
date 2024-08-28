let currentPage = 1;
const rowsPerPage = 3;
let filteredRows = [];
function displayTablePage(page) {
  const rows = filteredRows.length > 0 ? filteredRows : document.querySelectorAll('#table-body tr');
  const totalRows = rows.length;
  const totalPages = Math.ceil(totalRows / rowsPerPage);
  // Ajusta a página atual se necessário
  if (page < 1) page = 1;
  if (page > totalPages) page = totalPages;
  // Esconde todas as linhas e exibe apenas as necessárias
  document.querySelectorAll('#table-body tr').forEach(row => {
    row.style.display = 'none';
  });
  for (let i = (page - 1) * rowsPerPage; i < (page * rowsPerPage) && i < totalRows; i++) {
    rows[i].style.display = '';
  }
  // Atualiza o número da página
  document.getElementById('page-number').textContent = `Página ${page} de ${totalPages}`;
  // Desabilita botões de navegação se estiver no início ou no fim
  document.getElementById('prev-page').disabled = page === 1;
  document.getElementById('next-page').disabled = page === totalPages;
}
function search(query) {
  const input = query.toLowerCase();
  const tableRows = document.querySelectorAll('#table-body tr');
  filteredRows = [];
  tableRows.forEach(row => {
    const module = row.cells[0].textContent.toLowerCase();
    const permission = row.cells[1].textContent.toLowerCase();
    const name = row.cells[2].textContent.toLowerCase();

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
      filteredRows.push(row);
    }
  });
  // Recalcula a paginação após a pesquisa
  currentPage = 1;
  displayTablePage(currentPage);
}
document.getElementById('prev-page').addEventListener('click', () => {
  if (currentPage > 1) {
    currentPage--;
    displayTablePage(currentPage);
  }
});
document.getElementById('next-page').addEventListener('click', () => {
  const tableRows = filteredRows.length > 0 ? filteredRows : document.querySelectorAll('#table-body tr');
  const totalPages = Math.ceil(tableRows.length / rowsPerPage);
  if (currentPage < totalPages) {
    currentPage++;
    displayTablePage(currentPage);
  }
});
const advancedSearchInput = document.getElementById('advanced-search-input');
document.getElementById('advanced-search-button').addEventListener('click', () => {
  search(advancedSearchInput.value);
});
advancedSearchInput.addEventListener('keydown', (e) => {
  if (e.keyCode === 13) {
    search(e.target.value);
  }
});
// Inicializa a primeira página
displayTablePage(currentPage);