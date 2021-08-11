$(document).ready(function(){

$('#smartwizard').smartWizard({
selected: 0,
theme: 'arrows',
autoAdjustHeight:true,
transitionEffect:'fade',
showStepURLhash: false,

});

});

$('#SUBMIT').click(function(e){
  e.preventDefault();
  $('#register_form').submit();
})
