const GasPipePane = document.getElementById('gas_line_btn');
const GasDiaPane = document.getElementById('gas_line_dia_info');
const InfoPane = document.getElementById('information_pane');
const mapPane = document.getElementById('map');

//set left position


GasPipePane.addEventListener('click', function (e) {
    DisplayFunction();

    if ($('#information_pane').hasClass('display-none')) {
        $('.gas-line-legend').css({
            'left': '15px'
        })
    } else {
        $('.gas-line-legend').css({
            'left': '20vw'
        })
    }

})

// `<tr>
//     <th scope="row">2"</th>
//     <td>12'</td>
//     <td>2.3Km</td>
//     <td>150PSI</td>
// </tr>`

//set information pane visibility
function DisplayFunction() {
    if (InfoPane.classList.contains('display-none')) {
        InfoPane.classList.remove('display-none');
        InfoPane.style.width = '20%'
        mapPane.style.width = '80%';
    } else {
        InfoPane.classList.add('display-none');
        mapPane.style.width = '100%';
    }
    fetch(`/api/pipe_line_info/`)
        .then((response) => response.json())
        .then(data => displayDia(data))
        .catch((error) => {
            console.error('Error:', error);
        });

}

function displayDia(data) {
    let xVal = data['x_val'];
    let yVal = data['y_val'];
    var html = '';
    for (let dia_info of data['gas_line_dia_info']) {
        html += `<tr data-id="${dia_info['dia']}">
                    <th scope="row" >${dia_info['dia']}</th>
                    <td>${dia_info.count}</td>
                    <td>${dia_info.total} M</td>
                </tr>`
    }
    ;

    GasDiaPane.innerHTML = html
    barChart(xVal, yVal)
}





