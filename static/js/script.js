// Initialize Materialize features using jQuery
$(document).ready(function(){
    // Initialize mobile collapse with custom right side functionality
    $(".sidenav").sidenav({edge: "right"});
    // Initialize accordian collapsible functionality
    $('.collapsible').collapsible();
    // Initialize tooltip functionality
    $('.tooltipped').tooltip();
    // Initialize add recipe category selection functionality
    $('select').formSelect();
    // Initialize carousel functionality
    $('.carousel').carousel();
  });