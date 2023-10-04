/* Fetch character name from a url */
$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  success: (data) => {
    $('DIV#character').text(data.name);
  }
});
