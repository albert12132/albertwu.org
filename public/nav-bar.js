$(document).ready(function(){
  $('#nav-bar').css('height', ($(window).height() - 100) + 'px');
  var navBarWidth = '270px';
  var navBarSpeed = 500;
  $('#nav-bar-hide').click(function(){
    if ($('#content').css('margin-left') === navBarWidth) {
      $('#content').animate({'margin-left':0}, navBarSpeed);
    } else {
      $('#content').animate({'margin-left':navBarWidth}, navBarSpeed);
    }
  });
});

$(window).resize(function(){
  $('#nav-bar').css('height', ($(window).height() - 100) + 'px');
});
