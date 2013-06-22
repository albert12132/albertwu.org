$('document').ready(function() {
  $('button').click(function() {
    var solution_id = $(this).attr('id')
    $('.' + solution_id).fadeToggle();
  });
});
