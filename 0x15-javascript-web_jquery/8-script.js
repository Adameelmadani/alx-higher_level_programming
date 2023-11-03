$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  dataType: 'json',
  success: function(data){
    const size = data.results.length;
    for (var i = 0; i < size; i ++) {
      $("UL#list_movies").append($("<li></li>").text(data.results[i].title));
    }
  }
})