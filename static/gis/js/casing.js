// //Riser information

// function RiserInformation(feature) {
//     var id = feature.properties.pk;
//     fetch(`/api/riser/${id}/`)
//         .then((response) => response.json())
//         .then(data => showRiserData(data, feature))
//         .catch((error) => {
//             console.error('Error:', error);
//         });
// }


// function showRiserData(data ,feature) {
//     let coOrdinates = feature.geometry.coordinates[0][1]+','+feature.geometry.coordinates[0][0]
//     $('#riser_info').modal('toggle');
//     let tableContent = document.getElementById('riser_info_table');
//     let htmlData = '';
//     data = data[0];
//     let temp = 1;
//     htmlData += `<p class="text-center py-3 px-4">Coordinates: <a href="http://maps.google.com?q=${coOrdinates}" target="_blank">${coOrdinates}</a></p>
//                     <table class="table">
//                         <thead >
//                            <tr class="text-center">
//                             <th scope="col">ID</th>
//                             <th scope="col">Customer Id</th>
//                             <th scope="col">Customer Name</th>
//                             <th scope="col">Status</th>
//                             <th scope="col">Burner Type</th>
//                             <th scope="col">Burner No</th>
//                         </tr>
//                         </thead>
//                         </thead>
//                         <tbody class="text-center">
//                         ${data.customerid?
//                             `<tr class="text-center">
//                             <td>${temp++}</td>
//                             <td>${data.customerid}</td>
//                             <td>${data.customer_1}</td>
//                             <td>${data.status_1}</td>
//                             <td>${data.burner_typ}</td>
//                             <td>${data.burner_no_field}</td>
//                         </tr>`
//                             : ''}
//                         ${data.customer_2?
//                         `<tr class="text-center">
//                             <td>${temp++}</td>
//                             <td>${data.customer_2}</td>
//                             <td>${data.customer_3}</td>
//                             <td>${data.status_2}</td>
//                             <td>${data.burner_t_1}</td>
//                             <td>${data.burner_no1}</td>
//                         </tr>`
//                         : ''}
//                         ${data.customer_4?
//                         `<tr class="text-center">
//                             <td>${temp++}</td>
//                             <td>${data.customer_4}</td>
//                             <td>${data.customer_5}</td>
//                             <td>${data.status_3}</td>
//                             <td>${data.burner_t_2}</td>
//                             <td>${data.burner_n_1}</td>
//                         </tr>`
//                         : ''}
//                         ${data.customer_6?
//                         `<tr class="text-center">
//                             <td>${temp++}</td>
//                             <td>${data.customer_6}</td>
//                             <td>${data.customer_7}</td>
//                             <td>${data.status_4}</td>
//                             <td>${data.burner_t_3}</td>
//                             <td>${data.burner_n_2}</td>
//                         </tr>`
//                         : ''}
//                         ${data.customer_8?
//                         `<tr class="text-center">
//                             <td>${temp++}</td>
//                             <td>${data.customer_8}</td>
//                             <td>${data.customer_9}</td>
//                             <td>${data.status_5}</td>
//                             <td>${data.burner_t_4}</td>
//                             <td>${data.burner_n_3}</td>
//                         </tr>`
//                         : ''}
//                         ${data.customer_8?
//                         `<tr class="text-center">
//                             <td>${temp++}</td>
//                             <td>${data.customer_8}</td>
//                             <td>${data.custome_11}</td>
//                             <td>${data.status_6}</td>
//                             <td>${data.burner_t_5}</td>
//                             <td>${data.burner_n_4}</td>
//                         </tr>`
//                         : ''}
//                         ${data.custome_12?
//                         `<tr class="text-center">
//                             <td>${temp++}</td>
//                             <td>${data.custome_12}</td>
//                             <td>${data.custome_13}</td>
//                             <td>${data.status_7}</td>
//                             <td>${data.burner_t_6}</td>
//                             <td>${data.burner_n_5}</td>
//                         </tr>`
//                         : ''}
//                         ${data.custome_14?
//                         `<tr class="text-center">
//                             <td>${temp++}</td>
//                             <td>${data.custome_14}</td>
//                             <td>${data.custome_15}</td>
//                             <td>${data.status_8}</td>
//                             <td>${data.burner_t_7}</td>
//                             <td>${data.burner_n_6}</td>
//                         </tr>`
//                         : ''}
//                         ${data.custome_16?
//                         `<tr class="text-center">
//                             <td>${temp++}</td>
//                             <td>${data.custome_16}</td>
//                             <td>${data.custome_17}</td>
//                             <td>${data.status}</td>
//                             <td>${data.burner_t_8}</td>
//                             <td>${data.burner_n_7}</td>
//                         </tr>`
//                         : ''}
//                         ${data.custome_16?
//                         `<tr class="text-center">
//                             <td>${temp++}</td>
//                             <td>${data.custome_18}</td>
//                             <td>${data.custome_19}</td>
//                             <td>${data.status_10}</td>
//                             <td>${data.burner_t_9}</td>
//                             <td>${data.burner_n_8}</td>
//                         </tr>`
//                         : ''}
//                          </tbody>
//                     </table>`


//     tableContent.innerHTML = htmlData;
// }


