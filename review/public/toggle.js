$('document').ready(function() {
  $('button').click(function() {
    var solution_id = $(this).attr('id');
    $('div.' + solution_id).slideToggle(600);

    var shown = $('span.' + solution_id).hasClass('hidden');
    if (shown) {
      $('span.blank' + solution_id).toggle();
      $('span.' + solution_id).fadeToggle(600);
    } else {
      $('span.' + solution_id).toggle();
      $('span.blank' + solution_id).fadeToggle(600);
    }
    $('span.' + solution_id).toggleClass('hidden');
  });
});
