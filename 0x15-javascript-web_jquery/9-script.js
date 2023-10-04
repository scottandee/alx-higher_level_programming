/* fetch a url and display value of hello */
$.ajax({
  type: 'GET',
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  success: (data) => {
    $('DIV#hello').html('<h1>' + data.hello + '</h1>');
  }
});
