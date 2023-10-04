/* Update header text */
const text = 'New Header!!!';
const update = $('DIV#update_header');

update.click(() => {
  $('header').text(text);
});
