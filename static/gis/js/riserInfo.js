//Riser information

function RiserInformation(feature) {
    var id = feature.properties.pk;
    fetch(`/api/riser/${id}/`)
        .then((response) => response.json())
        .then(data => showRiserData(data, feature))
        .catch((error) => {
            console.error('Error:', error);
        });
}


function showRiserData(data ,feature) {
    console.log('data:',data);
    let coOrdinates = feature.geometry.coordinates[0][1]+','+feature.geometry.coordinates[0][0]
    $('#riser_info').modal('toggle');
    let tableContent = document.getElementById('riser_info_table');
    let htmlData = '';
    data = data[0];
    let temp = 1;
    htmlData += `<p class="text-center py-3 px-4">Coordinates: <a href="http://maps.google.com?q=${coOrdinates}" target="_blank">${coOrdinates}</a></p>
                    <table class="table">
                        <thead >
                           <tr class="text-center">
                            <th scope="col">ID</th>
                            <th scope="col">Customer Id</th>
                            <th scope="col">Customer Name</th>
                            <th scope="col">Status</th>
                            <th scope="col">Burner Type</th>
                            <th scope="col">Burner No</th>
                        </tr>
                        </thead>
                        </thead>
                        <tbody class="text-center">
                        ${new Array(40)}

                        ${data.customerid?
                            `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customerid}</td>
                            <td>${data.customer_1}</td>
                            <td>${data.status_1}</td>
                            <td>${data.burner_typ}</td>
                            <td>${data.burner_no_field}</td>
                        </tr>`
                            : ''}
                        ${data.customer_2?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_2}</td>
                            <td>${data.customer_3}</td>
                            <td>${data.status_2}</td>
                            <td>${data.burner_t_1}</td>
                            <td>${data.burner_no1}</td>
                        </tr>`
                        : ''}
                        ${data.customer_4?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_4}</td>
                            <td>${data.customer_5}</td>
                            <td>${data.status_3}</td>
                            <td>${data.burner_t_2}</td>
                            <td>${data.burner_n_1}</td>
                        </tr>`
                        : ''}
                        ${data.customer_6?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_6}</td>
                            <td>${data.customer_7}</td>
                            <td>${data.status_4}</td>
                            <td>${data.burner_t_3}</td>
                            <td>${data.burner_n_2}</td>
                        </tr>`
                        : ''}
                        ${data.customer_8?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_8}</td>
                            <td>${data.customer_9}</td>
                            <td>${data.status_5}</td>
                            <td>${data.burner_t_4}</td>
                            <td>${data.burner_n_3}</td>
                        </tr>`
                        : ''}s
                        ${data.custome_10?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.custome_10}</td>
                            <td>${data.custome_11}</td>
                            <td>${data.status_6}</td>
                            <td>${data.burner_t_5}</td>
                            <td>${data.burner_n_4}</td>
                        </tr>`
                        : ''}
                        ${data.custome_12?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.custome_12}</td>
                            <td>${data.custome_13}</td>
                            <td>${data.status_7}</td>
                            <td>${data.burner_t_6}</td>
                            <td>${data.burner_n_5}</td>
                        </tr>`
                        : ''}
                        ${data.custome_14?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.custome_14}</td>
                            <td>${data.custome_15}</td>
                            <td>${data.status_8}</td>
                            <td>${data.burner_t_7}</td>
                            <td>${data.burner_n_6}</td>
                        </tr>`
                        : ''}
                        ${data.custome_16?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.custome_16}</td>
                            <td>${data.custome_17}</td>
                            <td>${data.status}</td>
                            <td>${data.burner_t_8}</td>
                            <td>${data.burner_n_7}</td>
                        </tr>`

                        : ''}
                        ${data.custome_18?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.custome_18}</td>
                            <td>${data.custome_19}</td>
                            <td>${data.status_10}</td>
                            <td>${data.burner_t_9}</td>
                            <td>${data.burner_n_8}</td>
                        </tr>`
                        : ''}

                        ${data.customer_id_20?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_20}</td>
                            <td>${data.customer_name_20}</td>
                            <td>${data.status_20}</td>
                            <td>${data.burner_type_20}</td>
                            <td>${data.burner_no_field_20}</td>
                        </tr>`
                        : ''}

                        ${data.customer_id_21?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_21}</td>
                            <td>${data.customer_name_21}</td>
                            <td>${data.status_21}</td>
                            <td>${data.burner_type_21}</td>
                            <td>${data.burner_no_field_21}</td>
                        </tr>`
    
                        : ''}
                        ${data.customer_id_22?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_22}</td>
                            <td>${data.customer_name_22}</td>
                            <td>${data.status_22}</td>
                            <td>${data.burner_type_22}</td>
                            <td>${data.burner_no_field_22}</td>
                        </tr>`

                        : ''}
                        ${data.customer_id_23?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_23}</td>
                            <td>${data.customer_name_23}</td>
                            <td>${data.status_23}</td>
                            <td>${data.burner_type_23}</td>
                            <td>${data.burner_no_field_23}</td>
                        </tr>`

                        : ''}

                        ${data.customer_id_24?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_24}</td>
                            <td>${data.customer_name_24}</td>
                            <td>${data.status_24}</td>
                            <td>${data.burner_type_24}</td>
                            <td>${data.burner_no_field_24}</td>
                        </tr>`

                        : ''}

                        ${data.customer_id_25?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_25}</td>
                            <td>${data.customer_name_25}</td>
                            <td>${data.status_25}</td>
                            <td>${data.burner_type_25}</td>
                            <td>${data.burner_no_field_25}</td>
                        </tr>`
                        : ''}

                        ${data.customer_id_26?
                            `<tr class="text-center">
                                <td>${temp++}</td>
                                <td>${data.customer_id_26}</td>
                                <td>${data.customer_name_26}</td>
                                <td>${data.status_26}</td>
                                <td>${data.burner_type_26}</td>
                                <td>${data.burner_no_field_26}</td>
                        </tr>`
                        : ''}

                        ${data.customer_id_27?
                            `<tr class="text-center">
                                <td>${temp++}</td>
                                <td>${data.customer_id_27}</td>
                                <td>${data.customer_name_27}</td>
                                <td>${data.status_27}</td>
                                <td>${data.burner_type_27}</td>
                                <td>${data.burner_no_field_27}</td>
                        </tr>`
                        : ''}

                        ${data.customer_id_28?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_28}</td>
                            <td>${data.customer_name_28}</td>
                            <td>${data.status_28}</td>
                            <td>${data.burner_type_28}</td>
                            <td>${data.burner_no_field_28}</td>
                        </tr>`

                        : ''}

                        ${data.customer_id_29?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_29}</td>
                            <td>${data.customer_name_29}</td>
                            <td>${data.status_29}</td>
                            <td>${data.burner_type_29}</td>
                            <td>${data.burner_no_field_29}</td>
                        </tr>`

                        : ''}

                        ${data.customer_id_30?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_30}</td>
                            <td>${data.customer_name_30}</td>
                            <td>${data.status_30}</td>
                            <td>${data.burner_type_30}</td>
                            <td>${data.burner_no_field_30}</td>
                        </tr>`

                        : ''}

                        ${data.customer_id_31?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_31}</td>
                            <td>${data.customer_name_31}</td>
                            <td>${data.status_31}</td>
                            <td>${data.burner_type_31}</td>
                            <td>${data.burner_no_field_31}</td>
                        </tr>`

                        : ''}

                        ${data.customer_id_32?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_32}</td>
                            <td>${data.customer_name_32}</td>
                            <td>${data.status_32}</td>
                            <td>${data.burner_type_32}</td>
                            <td>${data.burner_no_field_32}</td>
                        </tr>`

                        : ''}

                        ${data.customer_id_33?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_33}</td>
                            <td>${data.customer_name_33}</td>
                            <td>${data.status_33}</td>
                            <td>${data.burner_type_33}</td>
                            <td>${data.burner_no_field_33}</td>
                        </tr>`

                        : ''}

                        ${data.customer_id_34?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_34}</td>
                            <td>${data.customer_name_34}</td>
                            <td>${data.status_34}</td>
                            <td>${data.burner_type_34}</td>
                            <td>${data.burner_no_field_34}</td>
                        </tr>`

                        : ''}

                        ${data.customer_id_35?
                        `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_35}</td>
                            <td>${data.customer_name_35}</td>
                            <td>${data.status_35}</td>
                            <td>${data.burner_type_35}</td>
                            <td>${data.burner_no_field_35}</td>
                        </tr>`

                        : ''}

                        ${data.customer_id_36?
                            `<tr class="text-center">
                                <td>${temp++}</td>
                                <td>${data.customer_id_36}</td>
                                <td>${data.customer_name_36}</td>
                                <td>${data.status_36}</td>
                                <td>${data.burner_type_36}</td>
                                <td>${data.burner_no_field_36}</td>
                            </tr>`

                            : ''}

                            ${data.customer_id_37?
                            `<tr class="text-center">
                                <td>${temp++}</td>
                                <td>${data.customer_id_37}</td>
                                <td>${data.customer_name_37}</td>
                                <td>${data.status_37}</td>
                                <td>${data.burner_type_37}</td>
                                <td>${data.burner_no_field_37}</td>
                            </tr>`
    
                            : ''}

                            ${data.customer_id_38?
                            `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_38}</td>
                            <td>${data.customer_name_38}</td>
                            <td>${data.status_38}</td>
                            <td>${data.burner_type_38}</td>
                            <td>${data.burner_no_field_38}</td>
                            </tr>`

                            : ''}

                            ${data.customer_id_39?
                            `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_39}</td>
                            <td>${data.customer_name_39}</td>
                            <td>${data.status_39}</td>
                            <td>${data.burner_type_39}</td>
                            <td>${data.burner_no_field_39 = models.FloatField(blank=True, null=True)
                            }</td>
                            </tr>`

                            : ''}

                            ${data.customer_id_40?
                            `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_40}</td>
                            <td>${data.customer_name_40 = models.CharField(max_length=100, blank=True, null=True)
                            }</td>
                            <td>${data.status_40}</td>
                            <td>${data.burner_type_40}</td>
                            <td>${data.burner_no_field_40}</td>
                            </tr>`

                            : ''}

                            ${data.customer_id_41?
                            `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_41}</td>
                            <td>${data.customer_name_41 = models.CharField(max_length=100, blank=True, null=True)
                            }</td>
                            <td>${data.status_41}</td>
                            <td>${data.burner_type_41}</td>
                            <td>${data.burner_no_field_41}</td>
                            </tr>`

                            : ''}

                            ${data.customer_id_42?
                            `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_42}</td>
                            <td>${data.customer_name_42 = models.CharField(max_length=100, blank=True, null=True)
                            }</td>
                            <td>${data.status_42}</td>
                            <td>${data.burner_type_42}</td>
                            <td>${data.burner_no_field_42}</td>
                            </tr>`

                            : ''}

                            ${data.customer_id_43?
                            `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_43}</td>
                            <td>${data.customer_name_43 = models.CharField(max_length=100, blank=True, null=True)
                            }</td>
                            <td>${data.status_43}</td>
                            <td>${data.burner_type_43}</td>
                            <td>${data.burner_no_field_43}</td>
                            </tr>`

                            : ''}

                            ${data.customer_id_44?
                            `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_44}</td>
                            <td>${data.customer_name_44 = models.CharField(max_length=100, blank=True, null=True)
                            }</td>
                            <td>${data.status_44}</td>
                            <td>${data.burner_type_44}</td>
                            <td>${data.burner_no_field_44}</td>
                            </tr>`

                            : ''}

                            ${data.customer_id_45?
                            `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_45}</td>
                            <td>${data.customer_name_45 = models.CharField(max_length=100, blank=True, null=True)
                            }</td>
                            <td>${data.status_45}</td>
                            <td>${data.burner_type_45}</td>
                            <td>${data.burner_no_field_45}</td>
                            </tr>`

                            : ''}

                            ${data.customer_id_46?
                            `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_46}</td>
                            <td>${data.customer_name_46 = models.CharField(max_length=100, blank=True, null=True)
                            }</td>
                            <td>${data.status_46}</td>
                            <td>${data.burner_type_46}</td>
                            <td>${data.burner_no_field_46 = models.FloatField(blank=True, null=True)
                            }</td>
                            </tr>`

                            : ''}

                            ${data.customer_id_47?
                            `<tr class="text-center">
                            <td>${temp++}</td>
                            <td>${data.customer_id_47}</td>
                            <td>${data.customer_name_47 = models.CharField(max_length=100, blank=True, null=True)
                            }</td>
                            <td>${data.status_47}</td>
                            <td>${data.burner_type_47}</td>
                            <td>${data.burner_no_field_47 = models.FloatField(blank=True, null=True)
                            }</td>
                            </tr>`

                            : ''}

                            ${data.customer_id_48?
                            `<tr class="text-center">
                                <td>${temp++}</td>
                                <td>${data.customer_id_48}</td>
                                <td>${data.customer_name_48 = models.CharField(max_length=100, blank=True, null=True)
                                }</td>
                                <td>${data.status_48}</td>
                                <td>${data.burner_type_48}</td>
                                <td>${data.burner_no_field_48 = models.FloatField(blank=True, null=True)
                                }</td>
                            </tr>`

                            : ''}

                            ${data.customer_id_49?
                            `<tr class="text-center">
                                <td>${temp++}</td>
                                <td>${data.customer_id_49}</td>
                                <td>${data.customer_name_49 = models.CharField(max_length=100, blank=True, null=True)
                                }</td>
                                <td>${data.status_49}</td>
                                <td>${data.burner_type_49}</td>
                                <td>${data.burner_no_field_49 = models.FloatField(blank=True, null=True)
                                }</td>
                            </tr>`

                            : ''}

                            ${data.customer_id_50?
                            `<tr class="text-center">
                                <td>${temp++}</td>
                                <td>${data.customer_id_50}</td>
                                <td>${data.customer_name_50 = models.CharField(max_length=100, blank=True, null=True)
                                }</td>
                                <td>${data.status_50}</td>
                                <td>${data.burner_type_50}</td>
                                <td>${data.burner_no_field_50 = models.FloatField(blank=True, null=True)
                                }</td>
                            </tr>`

                            : ''}

                            ${data.customer_id_51?
                            `<tr class="text-center">
                                <td>${temp++}</td>
                                <td>${data.customer_id_51}</td>
                                <td>${data.customer_name_51 = models.CharField(max_length=100, blank=True, null=True)
                                }</td>
                                <td>${data.status_51}</td>
                                <td>${data.burner_type_51}</td>
                                <td>${data.burner_no_field_51 = models.FloatField(blank=True, null=True)
                                }</td>
                            </tr>`

                            : ''}

                            ${data.customer_id_52?
                            `<tr class="text-center">
                                <td>${temp++}</td>
                                <td>${data.customer_id_52}</td>
                                <td>${data.customer_name_52 = models.CharField(max_length=100, blank=True, null=True)
                                }</td>
                                <td>${data.status_52}</td>
                                <td>${data.burner_type_52}</td>
                                <td>${data.burner_no_field_52 = models.FloatField(blank=True, null=True)
                                }</td>
                            </tr>`

                            : ''}

                            ${data.customer_id_53?
                            `<tr class="text-center">
                                <td>${temp++}</td>
                                <td>${data.customer_id_53}</td>
                                <td>${data.customer_name_53 = models.CharField(max_length=100, blank=True, null=True)
                                }</td>
                                <td>${data.status_53}</td>
                                <td>${data.burner_type_53}</td>
                                <td>${data.burner_no_field_53 = models.FloatField(blank=True, null=True)
                                }</td>
                            </tr>`

                            : ''}

                            ${data.customer_id_54?
                            `<tr class="text-center">
                                <td>${temp++}</td>
                                <td>${data.customer_id_54}</td>
                                <td>${data.customer_name_54 = models.CharField(max_length=100, blank=True, null=True)
                                }</td>
                                <td>${data.status_54}</td>
                                <td>${data.burner_type_54}</td>
                                <td>${data.burner_no_field_54 = models.FloatField(blank=True, null=True)
                                }</td>
                            </tr>`

                            : ''}

                            ${data.customer_id_55?
                            `<tr class="text-center">
                                <td>${temp++}</td>
                                <td>${data.customer_id_55}</td>
                                <td>${data.customer_name_55 = models.CharField(max_length=100, blank=True, null=True)
                                }</td>
                                <td>${data.status_55}</td>
                                <td>${data.burner_type_55}</td>
                                <td>${data.burner_no_field_55 = models.FloatField(blank=True, null=True)
                                }</td>
                            </tr>`
    
                            : ''}

                            ${data.customer_id_56?
                            `<tr class="text-center">
                                <td>${temp++}</td>
                                <td>${data.customer_id_56}</td>
                                <td>${data.customer_name_56 = models.CharField(max_length=100, blank=True, null=True)
                                }</td>
                                <td>${data.status_56}</td>
                                <td>${data.burner_type_56}</td>
                                <td>${data.burner_no_field_56 = models.FloatField(blank=True, null=True)
                                }</td>
                            </tr>`
    
                            : ''}

                            ${data.customer_id_57?
                            `<tr class="text-center">
                                <td>${temp++}</td>
                                <td>${data.customer_id_57}</td>
                                <td>${data.customer_name_57 = models.CharField(max_length=100, blank=True, null=True)
                                }</td>
                                <td>${data.status_57}</td>
                                <td>${data.burner_type_57}</td>
                                <td>${data.burner_no_field_57 = models.FloatField(blank=True, null=True)
                                }</td>
                            </tr>`
    
                            : ''}

                            ${data.customer_id_58?
                            `<tr class="text-center">
                                <td>${temp++}</td>
                                <td>${data.customer_id_58}</td>
                                <td>${data.customer_name_58 = models.CharField(max_length=100, blank=True, null=True)
                                }</td>
                                <td>${data.status_58}</td>
                                <td>${data.burner_type_58}</td>
                                <td>${data.burner_no_field_58 = models.FloatField(blank=True, null=True)
                                }</td>
                            </tr>`
    
                            : ''}

                            ${data.customer_id_59?
                            `<tr class="text-center">
                                <td>${temp++}</td>
                                <td>${data.customer_id_59}</td>
                                <td>${data.customer_name_59 = models.CharField(max_length=100, blank=True, null=True)
                                }</td>
                                <td>${data.status_59}</td>
                                <td>${data.burner_type_59}</td>
                                <td>${data.burner_no_field_59 = models.FloatField(blank=True, null=True)
                                }</td>
                            </tr>`
    
                            : ''}

                            ${data.customer_id_60?
                            `<tr class="text-center">
                                <td>${temp++}</td>
                                <td>${data.customer_id_60}</td>
                                <td>${data.customer_name_60 = models.CharField(max_length=100, blank=True, null=True)
                                }</td>
                                <td>${data.status_60}</td>
                                <td>${data.burner_type_60}</td>
                                <td>${data.burner_no_field_60 = models.FloatField(blank=True, null=True)
                                }</td>
                            </tr>`
    
                            : ''}

                                                                                                                                                                        

                        

                         </tbody>
                    </table>`


 

    tableContent.innerHTML = htmlData;
}

