$(document).ready(function(){

  // index.html

  $('.login-show')
  .click(function(){
    $('.signin__login').show(300,'swing');
    $('.signin__button').hide();
  });	

  $('.signin')
  .click(function(event){
    if(event.target == this) {
      $('.signin__login').hide();
      $('.signin__button').show(300, 'swing');
    }
  });

  // manual.html

  $('.table-show')
  .click(function(){
    $('.table-container').show();
  });

  $('.table-close')
  .click(function(){
    $('.table-container').hide();
  });	
  
  $('.table-container')
  .click(function(event){
    if(event.target == this) {
      $('.table-container').hide();
    }
  });

  $('.popup-show')
  .click(function(){
    $('.popup-container').show();
  });	

  $('.popup-close')
  .click(function(){
    $('.popup-container').hide();
  });	

  $('.popup-container')
  .click(function(event){
    if(event.target == this) {
      $(this).hide();
    }
  });
});