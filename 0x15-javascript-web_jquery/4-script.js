$('div#toggle_header').on('click', () => {
  if ($('header').hasClass('red')) {
    $('header').removeClass('red').addClass('green');
  } else if ($('header').hasClass('green')) {
    $('header').removeClass('green').addClass('red');
  }
});
