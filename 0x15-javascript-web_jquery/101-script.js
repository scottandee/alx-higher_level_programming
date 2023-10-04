/* Script that adds, removes, and clears li elements */

window.onload = function () {
  $('DIV#add_item').click(() => {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(() => {
    $('li:last-child').remove();
  });
  $('DIV#clear_list').click(() => {
    $('UL.my_list').empty();
  });
};
