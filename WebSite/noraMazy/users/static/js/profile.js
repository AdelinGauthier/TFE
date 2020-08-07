$(document).ready(function() {

  function toggleSidebar() {
    $(".button").toggleClass("active");
    $("main").toggleClass("move-to-left");
    $(".sidebar-item").toggleClass("active");
  }

  $(".button").on("click tap", function() {
    toggleSidebar();
  });

  $(document).keyup(function(e) {
    if (e.keyCode === 27) {
      toggleSidebar();
    }
  });
});


(function($) {
  $('div li a').click(function() {
    $(this).addClass('active').siblings('a').removeClass('active');
    $('section:nth-of-type('+$(this).data('rel')+')').stop().show(1).siblings('section').stop().hide(1);
  });
})(jQuery);


function test() {
  var x = document.getElementById("compteCache");
    x.style.display = "none";
}