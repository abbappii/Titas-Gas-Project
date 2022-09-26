
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

// function showGasLineData(data) {
//     $('#gas_line_info').modal('toggle');
//     let tableBody = document.getElementById('gas_table_body');
//     let htmlData = '';
//     for (let dia_info of data) {
//         //console.log(dia_info)
//         htmlData += `<tr>
//                             <th scope="row">${dia_info.dia}</th>
//                             <td>${dia_info.depth}</td>
//                             <td>${dia_info.pressure}</td>
//                             <td>${dia_info.len}</td>
//                         </tr>`
//     };

//     tableBody.innerHTML = htmlData;
// }

