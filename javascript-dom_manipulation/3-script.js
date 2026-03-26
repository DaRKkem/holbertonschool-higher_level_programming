document.querySelector('#toggle_header').addEventListener('click', function () {
  const header = document.querySelector('header');
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
    // OR header.classList.replace('red', 'green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
    // OR header.classList.replace('green', 'red');
  }
});
