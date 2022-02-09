$(document).ready(function(){
    $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function(){
      const name = data.name;
      $('div'.text(name);
  })
})
