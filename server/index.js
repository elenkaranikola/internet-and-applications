//document.addEventListener('DOMContentLoaded', function () {
//    fetch('http://localhost:3000/getAll')
//    .then(response => response.json())
//    .then(data => loadHTMLTable(data['data']))
//    
//});

function loadHTMLTable(data) {
    const table = document.querySelector('#table-body');

    if (data.length === 0) {
        table.innerHTML = "<tr><td class='no-data'>No Data</td></tr>";
        return;
    }

    let tableHtml = "";

    data.forEach(function ({title}) {
        tableHtml += "<tr>";
        tableHtml += `<td>${title}</td>`;
        tableHtml += "</tr>";
    });

    table.innerHTML = tableHtml;
}


document.querySelector('#update-btn').addEventListener('click', function(event) {
    fetch('http://localhost:3000/showAll')
    .then(response => response.json())
    .then(data => loadHTMLTableCountries(data['data']));
});

//document.querySelector('#update-btn').addEventListener('click', function(event) {
//    fetch('http://localhost:3000/showAll')
//    .then(response => response.json())
//    .then(data => {
//        if (data.success) {
//            location.reload();
//        }
//    })
//});



const showBtn = document.querySelector('#update-btn');

//showBtn.onclick = function() {
//    fetch('http://localhost:3000/showAll')
//    .then(response => response.json())
//    .then(data => loadHTMLTableCountries(data['data']));
//}

function loadHTMLTableCountries(data) {
    const table = document.querySelector('#countries-tbody');

    if (data.length === 0) {
        table.innerHTML = "<tr><td class='no-data' colspan='5'>No Data</td></tr>";
        return;
    }

    let tableHtml = "";

    data.forEach(function ({country, articles}) {
        tableHtml += "<tr>";
        tableHtml += `<td>${country}</td>`;
        tableHtml += `<td>${articles}</td>`;
        tableHtml += "</tr>";
    });

    table.innerHTML = tableHtml;

    let d = loadHTMLTable([]);
}

document.querySelector('table tbody').addEventListener('click', function(event) {
    if (event.target.className === "delete-row-btn") {
        deleteRowById(event.target.dataset.id);
    }
    if (event.target.className === "edit-row-btn") {
        handleEditRow(event.target.dataset.id);
    }
});


const searchBtn = document.querySelector('#search-btn');

searchBtn.onclick = function() {
    const searchValue = document.querySelector('#search-input').value;

    fetch('http://localhost:3000/search/' + searchValue)
    .then(response => response.json())
    .then(data => loadHTMLTable(data['data']));
}

//showBtn.onclick = function() {
//    //const searchValue = document.querySelector('#search-input').value;
//
//    fetch('http://localhost:3000/showAll')
//    .then(response => response.json())
//    .then(data => loadHTMLTable(data['data']));
//}


function deleteRowById(id) {
    fetch('http://localhost:3000/delete/' + id, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            location.reload();
        }
    });
}

function handleEditRow(id) {
    const updateSection = document.querySelector('#update-row');
    updateSection.hidden = false;
    document.querySelector('#update-name-input').dataset.id = id;
}

updateBtn.onclick = function() {
    const updateNameInput = document.querySelector('#update-name-input');


    console.log(updateNameInput);

    fetch('http://localhost:3000/update', {
        method: 'PATCH',
        headers: {
            'Content-type' : 'application/json'
        },
        body: JSON.stringify({
            id: updateNameInput.dataset.id,
            name: updateNameInput.value
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            location.reload();
        }
    })
}


const addBtn = document.querySelector('#add-name-btn');

addBtn.onclick = function () {
    const nameInput = document.querySelector('#name-input');
    const name = nameInput.value;
    nameInput.value = "";

    fetch('http://localhost:3000/insert', {
        headers: {
            'Content-type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({ name : name})
    })
    .then(response => response.json())
    .then(data => insertRowIntoTable(data['data']));
}

function insertRowIntoTable(data) {
    console.log(data);
    const table = document.querySelector('table tbody');
    const isTableData = table.querySelector('.no-data');

    let tableHtml = "<tr>";

    for (var key in data) {
        if (data.hasOwnProperty(key)) {
            if (key === 'dateAdded') {
                data[key] = new Date(data[key]).toLocaleString();
            }
            tableHtml += `<td>${data[key]}</td>`;
        }
    }

    tableHtml += `<td><button class="delete-row-btn" data-id=${data.id}>Delete</td>`;
    tableHtml += `<td><button class="edit-row-btn" data-id=${data.id}>Edit</td>`;

    tableHtml += "</tr>";

    if (isTableData) {
        table.innerHTML = tableHtml;
    } else {
        const newRow = table.insertRow();
        newRow.innerHTML = tableHtml;
    }
}

