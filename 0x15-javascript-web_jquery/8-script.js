$.ajax({
  type: 'get',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  dataType: 'json',
  success: function (response) {
    console.log(response.results);
    const movies = response.results;
    $.each(movies, function (i, movie) {
      $('ul#list_movies').append(`<li>${movie.title}</li>`);
    });
  }
});
