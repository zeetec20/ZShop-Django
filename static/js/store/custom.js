$(document).ready(function () {
    let button_logout = document.getElementById('button_logout')

    button_logout.addEventListener('click', (elm) => {
        let id_modal = document.getElementById('button_logout').getAttribute('modal')
        $(id_modal).modal('show')
    })
})