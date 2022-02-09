$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, status) {
    data.results.forEach(obj => {
      $('UL#list_movies').append('<li>' + obj.title + '</li>');
    });
  });
});
