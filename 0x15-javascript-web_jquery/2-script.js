$("div").on( "click", "button", function( event ) {
  $(event.delegateTarget ).css( "color", "red");
});
