const LOADING_DIV = document.createElement('div');

LOADING_DIV.classList.add('spinner-border');
LOADING_DIV.setAttribute('role', 'status');

function loadItems(event) {
    const files = event.target.files;
    const list = document.getElementById('uploaded_pdf_list');
    list.innerHTML = '';
    for (var i = 0; i < files.length; i++) {
        const item = document.createElement('li');
        const div = document.createElement('div');
        const span = document.createElement('span');
        item.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'align-items-start');
        div.classList.add('ms-2', 'me-auto', 'fw-bold');
        span.classList.add('badge', 'rounded-pill');
        div.textContent = files[i].name;
        span.textContent = files[i].name.split('.').pop();
        if (span.textContent === 'pdf') {
            span.classList.add('text-bg-danger');
        } else {
            span.classList.add('text-bg-primary');
        }
        item.appendChild(div);
        item.appendChild(span);
        list.appendChild(item);
    }
}

function displayLoader(element){
    element.append(LOADING_DIV);
}
function removeLoader(element){
    element.removeChild(LOADING_DIV);
}