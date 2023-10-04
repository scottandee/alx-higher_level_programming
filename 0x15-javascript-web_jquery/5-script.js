/* Append to unordered list on click */
const item = '<li>Item</li>';
const list = $('UL.my_list');
const addItem = $('DIV#add_item');

addItem.click(() => {
  list.append(item);
});
