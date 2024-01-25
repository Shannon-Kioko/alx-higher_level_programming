$.ajax({
    type: "get",
    url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
    dataType: "json",
    success: function (response) {
        $('div#character').text(response.name)
    }
});