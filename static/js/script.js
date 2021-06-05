// Initialize Materialize features using jQuery
$(document).ready(function(){
    // Initialize mobile collapse with custom right side functionality
    $(".sidenav").sidenav({edge: "right"});
    // Initialize accordian collapsible functionality
    $(document).ready(function(){
      $('.collapsible').collapsible();
    });
  });