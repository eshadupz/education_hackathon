const button = document.getElementById('but2');

button.addEventListener('click', () => {
  fetch('/results')
    .then(response => response.json())
    .then(data => console.log(data));
});