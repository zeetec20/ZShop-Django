var wrap_form = document.getElementById('wrap_form')

if (wrap_form.getAttribute('mode') == 'login') {
    wrap_form.scrollTo(0, wrap_form.scrollHeight)
} else if (wrap_form.getAttribute('mode') == 'register') {
    wrap_form.scrollTo(0, 0)
}

document.getElementById('button_login').addEventListener('click', (event) => {
    wrap_form.scrollTo(0, wrap_form.scrollHeight)
})

document.getElementById('button_register').addEventListener('click', (event) => {
    wrap_form.scrollTo(0, 0)
})