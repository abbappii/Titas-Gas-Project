
function valvepitLineInfo(id){
    console.log("id is :",id.properties.pk);
    fetch(`/api/valvepit_api/${id.properties.pk}/`)

        .then((response) => response.json())
        .then(data => 
            {showValvepitInformation(data)
                console.log(data);})
        
        .catch((error) => {
            console.error('Error:', error);
        });
}


function showValvepitInformation(data) {
    $('#valvepit_info').modal('toggle');
    let tableBody = document.getElementById('valvepit_info_table_body');
    let htmlData = '';
    for (let id_info of data) {
        htmlData += `<tr>
                            <td>${id_info.id}</td>
                            <td>${id_info.depth}</td> 
                            <td>${id_info.pressure}</td>
                            <td>${id_info.valve_type}</td>
                            <td>${id_info.valvepit_s}</td>
                            
                        </tr>`
    };

    tableBody.innerHTML = htmlData;
}
