$(document).ready(function() {
  $('h1, h2, h3, h4, h5, h6').addClass('anchor');
});

$(document).ready(function(){
  $('#nav-bar').css('height', ($(window).height() - 100) + 'px');
  var navBarWidth = '270px';
  var navBarSpeed = 500;
  $('#nav-bar-toggle').click(function(){
    if ($('#content').css('margin-left') === navBarWidth) {
      $('#content').animate({'margin-left':0}, navBarSpeed);
      $('#nav-bar-toggle-icon').text('>');
    } else {
      $('#content').animate({'margin-left':navBarWidth}, navBarSpeed);
      $('#nav-bar-toggle-icon').text('<');
    }
  });
});

$(window).resize(function(){
  $('#nav-bar').css('height', ($(window).height() - 100) + 'px');
});
