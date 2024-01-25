$.ajax({
  type: 'get',
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  success: (response) => {
    $('div#hello').text(response.hello);
  }
});
