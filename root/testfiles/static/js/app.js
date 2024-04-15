var login = document.querySelector(".dd-button")
var navbar = document.querySelector(".custom-navbar")
var dropdown = document.querySelector('.dropdown')
ddinput = document.querySelector('.dd-input')
hamburger_input = document.querySelector('.hamburger-input')
ddmenu = document.querySelector('.dd-menu')
ddinput = document.querySelector('.dd-input')
var task_type = document.getElementById('id_task_type')
var task_eco = document.getElementById('id_task_eco')
var footer = document.querySelector('.footer')
var inputs = document.querySelectorAll('form.changeable input'); 





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

  document.querySelectorAll('.cutoptionButton').forEach(button => {
    button.addEventListener('click', function() {
      document.querySelectorAll('.cutoptionButton').forEach(btn => btn.classList.remove('active'));
      this.classList.add('active'); // Highlight the selected button
      document.getElementById('custom_user_type').value = this.value; // Store selected value
    });
  });



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



  document.querySelectorAll('.teoptionButton').forEach(button => {
    if (task_eco.value && button.value == task_eco.value){
      button.classList.add('active');
  }
    button.addEventListener('click', function() {
      document.querySelectorAll('.teoptionButton').forEach(btn => btn.classList.remove('active'));
      this.classList.add('active'); // Highlight the selected button
      document.getElementById('id_task_eco').value = this.value; // Store selected value
    });
  });


if (inputs.length) {


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


  document.addEventListener('click', (e) => {
    if (!e.target.closest('.dropdown'))  {
      ddinput.checked = false;
    }
  });

  document.addEventListener('click', (e) => {
    if (!e.target.closest('.hamburger'))  {
      hamburger_input.checked = false;
    }
  });
  

