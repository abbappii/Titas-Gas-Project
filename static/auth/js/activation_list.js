const userList = document.getElementById('users_info_pane');
const editUser = document.getElementById('edit_user');
const filterUser = document.getElementById('filter_user');

const hostAddress = window.location.origin
usersList()
const writeServer = (action, data) => ({
    method: action,
    body: JSON.stringify(data),
    headers: {
        'X-CSRFToken': csrftoken,
        'Content-Type': 'application/json; charset=UTF-8'
    }
});


$('#users_info_pane').on('click', function (e) {
    e.preventDefault()
    const userId = e.target.parentElement.getAttribute('data-id')

    if (userId !== null) {
        //console.log(userId)
        // e.target.parentElement.setAttribute('href', `{% url 'geo_app:user_update_api' ${userId} %}`)
        // let url = `${hostAddress}/api/user_update/${userId}/`
        let url = `${hostAddress}/auth/admin_update_profile/${userId}/`
        window.open(url).focus();
        // $('#userUpdateModal').modal('toggle')
    }

});

let responseData, text;
$('#users_info_pane').on('click', function (e) {
        e.preventDefault()
        let attrName = e.target.parentElement.getAttribute('id')
        const userId = e.target.parentElement.parentElement.parentElement.getAttribute('data-id');

        if (attrName === 'activateAccount') {
            responseData = {
                "is_active": true
            }
            text = "Are You sure you want to Active this User?";
            if (confirm(text) == true) {
                fetch(`/auth/api/activation_request/${userId}/`, writeServer('PATCH', responseData))
                    .then(response => response.json())
                    .then(data => {
                        usersList()

                    }).catch((error) => {
                    console.error('Error:', error);
                });
            }
        } else if (attrName === 'declineRequest') {
            text = "Are You sure you want to decline this User?";
            responseData = {
                "is_active": false
            }
            if (confirm(text) == true) {
                fetch(`/auth/api/activation_request/${userId}/`, writeServer('PATCH', responseData))
                    .then(response => response.json())
                    .then(data => {
                        usersList()

                    }).catch((error) => {
                    console.error('Error:', error);
                });
            }
        }
        else if (attrName === 'suspendAccount') {
            text = "Are You sure you want to suspend this User?";
            responseData = {
                "is_suspended": true
            }
            if (confirm(text) == true) {
                fetch(`/auth/api/activation_request/${userId}/`, writeServer('PATCH', responseData))
                    .then(response => response.json())
                    .then(data => {
                        usersList()

                    }).catch((error) => {
                    console.error('Error:', error);
                });
            }
        }


    }
);

//fetch api data
function usersList() {
    fetch(`/auth/api/activation_request/`)
        .then((response) => response.json())
        .then(data => UserInformationList(data))
        .catch((error) => {
            console.error('Error:', error);
        });

}

//show api data in table
function UserInformationList(data) {
    let userTableBodyContent = '';

    let userTableHead = `<thead>
                    <tr>
                        <th scope="col">Id</th>
                        <th scope="col">Name</th>
                        <th scope="col">Email</th>
                        <th scope="col">Action</th>
                    </tr>
                </thead>`
    let profilePic;
    let ser = 1;

    if (data.length == 0) {
        userTableBodyContent += `<h3 class="text-danger text-center">No User found.</h3>`
    } else {


        data.forEach(user => {
            if (user.profile_pic === `${hostAddress}/media/default.jpg`) {
                profilePic = ''
            } else {
                profilePic = `<img src="${user?.profile_pic}" alt="" style="width: 50px; height: 50px; border-radius: 50%" className="mx-2">`
            }


            userTableBodyContent += `<tr id="visit-list-table">
                    <th scope="row" style="width: 50px"">${ser++}</th>
                    <td class="text-left" >${profilePic} <span style="padding:5px 0">${user.full_name}</span>
                    </td>
                    <td>${user.email}</td>
                    <td class="users_list_action text-center" data-id=${user.id}>
                        <div><a href=""  id="activateAccount"><i class="fa fa-check-circle" aria-hidden="true" style="color: #006b1b"></i></a></div>
                        <div><a href=""  id="declineRequest"><i class="fa fa-times-circle" aria-hidden="true" style="color: #990000"></i></a></div>
                        <div><a href="" id="suspendAccount"><i class="fa fa-ban" aria-hidden="true" style="color: red"></i></a></div>                        
                    </td>
                </tr>`

        })
    }
    let userTableBody = `<tbody>${userTableBodyContent}</tbody>`;
    userList.innerHTML = `${userTableHead}${userTableBody}`
}

//edit user
filterUser.addEventListener('keyup', function () {
    fetch(`/auth/api/activation_request/?search=${filterUser.value}`)
        .then((response) => response.json())
        .then(data => UserInformationList(data))
        .catch((error) => {
            console.error('Error:', error);
        });
})







