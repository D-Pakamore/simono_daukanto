const classFormWrapper = document.querySelector('.class-form-position-wrapper')
const classForm = classFormWrapper.querySelector('form')
const classSuccessMessage = document.getElementById('class-succes-message')

const yearlyHoursFormWrapper = document.querySelector('.yearly-hours-form-position-wrapper')
const yearlyHoursForm = yearlyHoursFormWrapper.querySelector('form')
const selectActivity = document.getElementById('id_activity');
const selectYearlyHours = document.getElementById('id_yearly_hours');

const yearlyHoursHidden = document.getElementById("id_yearly_hours_multiple");
const yearlyHoursHiddenOption = yearlyHoursHidden.querySelector("option");

const classListWrapper = document.getElementById("class-list-wrapper")
const activityListWrapper = document.getElementById("activity-list-wrapper")

const addClassToList = (value) => {
    const el = document.createElement('div')
    el.innerHTML = value

    classListWrapper.appendChild(el)
}

const addActivityToList = (value) => {
    const el = document.createElement('div')
    el.innerHTML = value

    activityListWrapper.appendChild(el)
}


const clearYearlyHoursSelect = () => {
    selectYearlyHours.innerHTML = '';
    const option = document.createElement('option');
    option.text = '---------';
    selectYearlyHours.appendChild(option);
}

const addYearlyHourToForm = () => {

    if (yearlyHoursHiddenOption.value.length != 0) {
        yearlyHoursHiddenOption.value = yearlyHoursHiddenOption.value + "," + selectYearlyHours.value
    } else {
        yearlyHoursHiddenOption.value = selectYearlyHours.value
    }

}

classForm.addEventListener('submit', (e) => {

    const selects = classForm.querySelectorAll('select')
    const input = document.getElementById('id_classes_count')

    const firstSelectText = selects[0].options[selects[0].selectedIndex].text
    const secondSelectText = selects[1].options[selects[1].selectedIndex].text

    addClassToList(firstSelectText + " " + secondSelectText + " - " + input.value)

    setTimeout(() => {
        selects.forEach(select => {
            select.value = "---------"
        })

        input.value = ""
    }, 100)
})

selectActivity.addEventListener('change', () => {
    const selectedActivity = selectActivity.value;

    if (selectedActivity.length === 0) {
        clearYearlyHoursSelect()
        return
    }

    fetch(`/workload/get_yearly_hours/?activity_id=${selectedActivity}`)
        .then(response => response.json())
        .then(data => {
            // Clear the current options in the yearly hours select
            selectYearlyHours.innerHTML = '';

            // Add new options based on the fetched data
            data.yearly_hours.forEach(yearlyHour => {
                const option = document.createElement('option');
                option.value = yearlyHour.id;
                option.text = yearlyHour.hours;
                selectYearlyHours.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
});

yearlyHoursForm.addEventListener('submit', (e) => {
    e.preventDefault();

    addYearlyHourToForm()
    addActivityToList(selectActivity.options[selectActivity.selectedIndex].text)
    clearYearlyHoursSelect()
    selectActivity.value = selectActivity.querySelectorAll('option')[0].value
})