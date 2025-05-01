function toggleDetails(button) {
    const detailsRow = button.closest('tr').nextElementSibling;
    if (detailsRow.style.display === 'table-row') {
        detailsRow.style.display = 'none';
        button.textContent = 'Ver más';
    } else {
        detailsRow.style.display = 'table-row';
        button.textContent = 'Ocultar';
    }
}
