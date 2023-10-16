const professionSelect = document.getElementById('id_profession');
const formEl = document.querySelector('form')
const formButtonsWrapper = formEl.querySelector('div')

// const API_ENDPOINT = "http://127.0.0.1:8000"

// async function fetchData(endpoint) {
//     const url = API_ENDPOINT + endpoint;


//     const response = await fetch(url);

//     if (!response.ok) {

//         throw new Error(`HTTP error! Status: ${response.status}`);
//     }

//     const data = await response.json();

//     return data
// }

// const fetchExperience = async (professionId) => {
//     const endpoint = `/api/profession-to-experience/?profession=${professionId}`
//     const response = await fetchData(endpoint)
//     return response
// }

// const fetchQualification = async (professionId) => {
//     const endpoint = `/api/profession-to-qualification/?profession=${professionId}`
//     const response = await fetchData(endpoint)
//     return response
// }

// const createExpereinceInput = (data) => {
//     const existingQualificationChoice = document.getElementById('experience-select-wrapper')
//     if (existingQualificationChoice) { existingQualificationChoice.remove() }

//     const experienceType = data[0].experience.name + ":"
//     const experienceChoices = data.map(item => { return { id: item.experience.id, choice: item.experience.value } })

//     const pEl = document.createElement('p')
//     const labelEl = document.createElement('label')
//     const selectEl = document.createElement('select')
//     const optionEls = experienceChoices.map(choice => {
//         const optionEl = document.createElement('option')
//         optionEl.value = choice.id
//         optionEl.innerHTML = choice.choice

//         return optionEl
//     })

//     pEl.id = 'experience-select-wrapper'
//     selectEl.id = 'id_experience'
//     selectEl.setAttribute('name', 'experience')
//     labelEl.setAttribute('for', 'experience-select');
//     labelEl.innerHTML = experienceType
//     optionEls.forEach(optionEl => selectEl.append(optionEl))

//     pEl.append(labelEl)
//     pEl.append(selectEl)

//     formEl.insertBefore(pEl, formButtonsWrapper);
// }

// const createQualificationInput = (data) => {
//     const existingQualificationChoice = document.getElementById('qualification-select-wrapper')
//     if (existingQualificationChoice) { existingQualificationChoice.remove() }

//     const qualificationType = data[0].qualification.name + ":"
//     const qualificationChoices = data.map(item => { return { id: item.qualification.id, choice: item.qualification.value } })

//     const pEl = document.createElement('p')
//     const labelEl = document.createElement('label')
//     const selectEl = document.createElement('select')
//     const optionEls = qualificationChoices.map(choice => {
//         const optionEl = document.createElement('option')
//         optionEl.setAttribute('name', 'qualifictaion')
//         optionEl.value = choice.id
//         optionEl.innerHTML = choice.choice

//         return optionEl
//     })

//     pEl.id = "qualification-select-wrapper"
//     selectEl.id = 'id_qualification'
//     selectEl.setAttribute('name', 'qualification')
//     labelEl.setAttribute('for', 'qualification-select');
//     labelEl.innerHTML = qualificationType
//     optionEls.forEach(optionEl => selectEl.append(optionEl))

//     pEl.append(labelEl)
//     pEl.append(selectEl)

//     formEl.insertBefore(pEl, formButtonsWrapper);
// }

// professionSelect.addEventListener('change', (e) => {
//     const professionId = parseFloat(professionSelect.value)

//     if (isNaN(professionId)) { return }

//     fetchExperience(professionId).then(response => createExpereinceInput(response))
//     fetchQualification(professionId).then(response => createQualificationInput(response))
// })

// document.querySelector('form').querySelectorAll('p')[2].querySelector('label').innerHTML = 'Profesija'