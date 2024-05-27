const login = document.querySelector(".dd-button")
const navbar = document.querySelector(".custom-navbar")
const dropdown = document.querySelector('.dropdown')
const ddinput = document.querySelector('.dd-input')
const ddmenu = document.querySelector('.dd-menu')
const task_type = document.getElementById('id_task_type')
const task_eco = document.getElementById('id_task_eco')
const footer = document.querySelector('.footer')
const inputs = document.querySelectorAll('form.changeable input'); 





window.addEventListener("scroll", e => {
    // console.log(window.scrollY)
    if (window.scrollY > 10){
      login.classList.add("bgg-yellow")
      navbar.classList.add("added")
    }
    else {
      login.classList.remove("bgg-yellow")
      navbar.classList.remove("added")
    }
  });
//logic for the buttons in the signup page
  document.querySelectorAll('.cutoptionButton').forEach(button => {
    button.addEventListener('click', function() {
      document.querySelectorAll('.cutoptionButton').forEach(btn => btn.classList.remove('active'));
      this.classList.add('active'); 
      document.getElementById('custom_user_type').value = this.value; 
    });
  });


//needed some js logic to send the input via the task creation form
  document.querySelectorAll('.ittoptionButton').forEach(button => {
    if (task_type.value && button.value == task_type.value){
        button.classList.add('active');
    }
    button.addEventListener('click', function() {
      document.querySelectorAll('.ittoptionButton').forEach(btn => btn.classList.remove('active'));
      this.classList.add('active');
      document.getElementById('id_task_type').value = this.value; 
    });
  });


//this is another section of the task creation form
  document.querySelectorAll('.teoptionButton').forEach(button => {
    if (task_eco.value && button.value == task_eco.value){
      button.classList.add('active');
  }
    button.addEventListener('click', function() {
      document.querySelectorAll('.teoptionButton').forEach(btn => btn.classList.remove('active'));
      this.classList.add('active'); 
      document.getElementById('id_task_eco').value = this.value; 
    });
  });


if (inputs.length) {

//logic in the profile page to disable the send button if input hasnt changed
  document.addEventListener('DOMContentLoaded', () => { 
    var submitBtn = document.querySelector('button.btn[type="submit"]');

    let initialValues = {};
    submitBtn.disabled = true;

    inputs.forEach(input => {
        initialValues[input.name] = input.value;
        input.addEventListener('input', () => handleChange(input)); 
    });

    function handleChange(input) {
        const oldValue = initialValues[input.name];
        const newValue = input.value;

        if (newValue === oldValue) {
            submitBtn.disabled = true; 
            // console.log('disable');
        } else {
            submitBtn.disabled = false; 
            // console.log('enable');
        }
    }
});
}

//basic logic to close the dropdown menu when clicked outside
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.dropdown'))  {
      ddinput.checked = false;
    }
  });


  

