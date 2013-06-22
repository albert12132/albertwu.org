$('document').ready(function() {
  $('button').click(function() {
    var solution_id = $(this).attr('id')
    $('div.' + solution_id).slideToggle(600);
    $('span.blank' + solution_id).toggle();
    $('span.' + solution_id).fadeToggle(600);
  });
});
