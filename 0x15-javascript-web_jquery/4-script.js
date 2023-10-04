/*  */
const toggle = $('DIV#toggle_header');
toggle.click(() => {
  $('header').toggleClass('red green');
});
