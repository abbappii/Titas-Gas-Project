const gasLine = document.getElementById('gas_line_dia_info');

gasLine.addEventListener('click', function (e) {
    let lineDia = e.target.parentNode.getAttribute('data-id');

    fetch(`/api/pipe_line_filter/?search=${lineDia}`)
        .then((response) => response.json())
        .then(data => showGasLineData(data))
        .catch((error) => {
            console.error('Error:', error);
        });
});

function pipeLineInfo(id){
    fetch(`/api/pipe_line_info/${id}/`)
        .then((response) => response.json())
        .then(data => showPipeLineInformation(data))
        .catch((error) => {
            console.error('Error:', error);
        });
}


function showGasLineData(data) {
    $('#gas_line_info').modal('toggle');
    let tableBody = document.getElementById('gas_table_body');
    let htmlData = '';
    for (let dia_info of data) {
        //console.log(dia_info)
        htmlData += `<tr>
                            <th scope="row">${dia_info.dia}</th>
                            <td>${dia_info.depth}</td>
                            <td>${dia_info.pressure}</td>
                            <td>${dia_info.len}</td>
                        </tr>`
    };

    tableBody.innerHTML = htmlData;
}


function showPipeLineInformation(data) {
    $('#pipeline_info').modal('toggle');
    let tableBody = document.getElementById('line_info_table_body');
    let htmlData = '';
    for (let dia_info of data) {
        htmlData += `<tr>
                            <th scope="row">${dia_info.dia}</th>
                            <td>${dia_info.depth}</td>
                            <td>${dia_info.pressure}</td>
                            <td>${dia_info.len}</td>
                        </tr>`
    };

    tableBody.innerHTML = htmlData;
}


