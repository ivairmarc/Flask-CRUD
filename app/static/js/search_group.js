
function filterGroups() {
    const search = document.getElementById('group-search').value.toLowerCase();
    const options = document.querySelectorAll('#group-list option');
    options.forEach(option => {
        if (option.text.toLowerCase().includes(search)) {
            option.style.display = 'block';
        } else {
            option.style.display = 'none';
        }
    });
}
