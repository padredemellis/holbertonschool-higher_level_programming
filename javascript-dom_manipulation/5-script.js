document.addEventListener('DOMContentLoaded', () => {
  const updateButton = document.getElementById('update_header');
  const header = document.querySelector('header');

  updateButton.addEventListener('click', () => {
    header.textContent = 'New Header!!!';
  });
});