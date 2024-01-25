$(document).ready(() => {
  const languageCode = $('input#language_code').val();
  $('input#btn_translate').on('click', () => {
    $.ajax({
      type: 'get',
      url: `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`,
      dataType: 'json',
      success: function (response) {
        console.log(response);
        $('div#hello').text(response.hello);
      }
    });
  });
});
