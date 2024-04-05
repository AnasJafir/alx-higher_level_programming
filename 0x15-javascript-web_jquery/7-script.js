/* global $ */
$(document).ready(function () {
  $('#fetch_character').click(function () {
    $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
      $('#character').append(data.name);
    });
  });
});
