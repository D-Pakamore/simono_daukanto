const dropDownButton = document.getElementById('dropdownMenuLink');
const buttonIcon = dropDownButton.querySelector('img');


dropDownButton.addEventListener('click', () => {
    const currentDeg = Number(buttonIcon.style.rotate.replace('deg', ''))
    const rotate = currentDeg ? '0deg' : '180deg'
    
    buttonIcon.style.rotate = rotate
})