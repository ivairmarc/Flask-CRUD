function initPaginationAndSearch(tableId, searchInputId, searchButtonId, rowsPerPage = 5) {
    let currentPage = 1;
    let filteredRows = [];

    function displayTablePage(page) {
        const rows = filteredRows.length > 0 ? filteredRows : document.querySelectorAll(`#${tableId} tbody tr`);
        const totalRows = rows.length;
        const totalPages = Math.ceil(totalRows / rowsPerPage);

        // Ajusta a página atual se necessário
        if (page < 1) page = 1;
        if (page > totalPages) page = totalPages;

        // Esconde todas as linhas e exibe apenas as necessárias
        document.querySelectorAll(`#${tableId} tbody tr`).forEach(row => {
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
        const tableRows = document.querySelectorAll(`#${tableId} tbody tr`);
        filteredRows = [];

        tableRows.forEach(row => {
            const rowText = Array.from(row.cells).map(cell => cell.textContent.toLowerCase()).join(' ');
            if (rowText.includes(input)) {
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
        const tableRows = filteredRows.length > 0 ? filteredRows : document.querySelectorAll(`#${tableId} tbody tr`);
        const totalPages = Math.ceil(tableRows.length / rowsPerPage);
        if (currentPage < totalPages) {
            currentPage++;
            displayTablePage(currentPage);
        }
    });

    const searchInput = document.getElementById(searchInputId);
    document.getElementById(searchButtonId).addEventListener('click', () => {
        search(searchInput.value);
    });

    searchInput.addEventListener('keydown', (e) => {
        if (e.keyCode === 13) {  // Verifica se a tecla Enter foi pressionada
            search(e.target.value);
        }
    });

    // Inicializa a primeira página
    displayTablePage(currentPage);
}
