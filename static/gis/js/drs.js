
function drsInfo(feature){
    var id = feature.properties.pk
    // console.log("id is :",id.properties.pk);
    fetch(`/api/drs_api/${id}/`)

        .then((response) => response.json())
        .then(data => 
            {showDrsInformation(data)
                console.log(data);})
        
        .catch((error) => {
            console.error('Error:', error);
        });
}


function showDrsInformation(data) {
    $('#drs_info').modal('toggle');
    let tableBody = document.getElementById('drs_info_table_body');
    let htmlData = '';
    for (let id_info of data) {
        htmlData += `<tr>
                            <td>${id_info.id}</td>
                            <td>${id_info.name}</td> 
                            
                        </tr>`
    };

    tableBody.innerHTML = htmlData;
}
