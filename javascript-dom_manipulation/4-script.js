document.addEventListener('DOMContentLoaded', () => {
  const addButton = document.getElementById('add_item');
  const myList = document.querySelector('ul.my_list');

  addButton.addEventListener('click', () => {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    myList.appendChild(newItem);
  });
});