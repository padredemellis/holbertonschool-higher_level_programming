#!/usr/bin/node
const updateHeaderRed = document.querySelector('#red_header');
updateHeaderRed.addEventListener('click', function () {
  const headerElement = document.querySelector('header');
  headerElement.classList.add('red');
});
