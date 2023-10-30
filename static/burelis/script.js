kidsUl = document.querySelector('.dropdown-menu')
ulInput = kidsUl.querySelector('input')
liEls = kidsUl.querySelectorAll('li')

ulInput.addEventListener('input', (e) => {
    const value = ulInput.value.toLowerCase()

    liEls.forEach(li => {
        const liText = li.querySelector('a').innerHTML.toLowerCase()

        if (liText.search(value) != -1) {
            li.style.display = 'block'
        } else {
            li.style.display = 'none'
        }
    })
})