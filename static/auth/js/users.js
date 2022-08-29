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

$('#users_info_pane').on('click', function (e) {
    e.preventDefault()
    let attrName = e.target.parentElement.getAttribute('id')
    const userId = e.target.parentElement.parentElement.parentElement.getAttribute('data-id');

    if (attrName === 'editProfileAdmin') {
        if (userId !== null) {
            //console.log(userId)
            // e.target.parentElement.setAttribute('href', `{% url 'geo_app:user_update_api' ${userId} %}`)
            // let url = `${hostAddress}/api/user_update/${userId}/`
            let url = `${hostAddress}/auth/admin_update_profile/${userId}/`
            window.open(url).focus();
            // $('#userUpdateModal').modal('toggle')
        }
    } else if (attrName === 'deleteProfileAdmin') {
        let text = "Are You sure you want to delete this User?";
        if (confirm(text) == true) {
            fetch(`/auth/api/user_update/${userId}/`, writeServer('DELETE', ''))
                .then(response => response.text())
                .then(data => {
                    //console.log('deleted')
                    usersList()
                });
        }}



    }
);

//fetch api data
function usersList() {
    fetch(`/auth/api/users_list/`)
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
                        <th scope="col">Phone</th>
                        <th scope="col">Edit Permission</th>
                        <th scope="col">Action</th>
                    </tr>
                </thead>`
    let profilePic, permissionIcon;
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

            if (user.is_superuser || user.is_staff) {
                permissionIcon = `<i class="fa fa-check-circle" aria-hidden="true" style="color: green"></i>`
            } else {
                permissionIcon = `<i class="fa fa-times-circle" style="color:red"></i>`
            }
            userTableBodyContent += `<tr id="visit-list-table">
                    <th scope="row" style="width: 50px">${ser++}</th>
                    <td class="text-left" >${profilePic} <span style="padding:5px 0">${user.full_name}</span>
                    </td>
                    <td>${user.email}</td>
                    <td>${user?.phone_number}</td>
                    <td>${permissionIcon}</td>
                    <td class="users_list_action text-center" data-id=${user.id}>
                        <div><a href=""  id="editProfileAdmin"><i class="fa fa-pencil-square-o" aria-hidden="true"></i></a></div>
                        <div><a href="" id="deleteProfileAdmin"><i class="fa fa-times-circle" aria-hidden="true"></i></a></div>                        
                    </td>
                </tr>`

        })
    }
    let userTableBody = `<tbody>${userTableBodyContent}</tbody>`;
    userList.innerHTML = `${userTableHead}${userTableBody}`
}

//edit user
filterUser.addEventListener('keyup', function () {
    //console.log(filterUser.value)
    fetch(`/auth/api/users_list/?search=${filterUser.value}`)
        .then((response) => response.json())
        .then(data => UserInformationList(data))
        .catch((error) => {
            console.error('Error:', error);
        });
})







