$(document).ready(function() {

  // Using validation to check for the presence of an input
  $( "#contact-form" ).submit(function( event ) {
      event.preventDefault();
      // If .required's value's length is zero
      if ( $( "#email" ).val().length === 0 || $( "#full_name" ).val().length === 0 || $("#note").val().length === 0) {
          // Prevent the form from submitting
          event.preventDefault();
          if ( $( "#error" ).length ) {
              // Error message aleady shown - do nothing
          } else {
            $( "<p id='error'  style='color:red;'>" ).text("Fill in all the fields and try again!").appendTo( ".mdl-card__supporting-text" );

          }
      } else {

          // Run $.ajax() here
          var email = $( "#email" ).val();
          var full_name = $( "#full_name" ).val();
          var note = $( "#note" ).val();
          var csrftoken = getCookie('csrftoken');
            console.log("run ajax here:  " + email + " " + note +  " " + full_name, " token: " + csrftoken);
          // Using the core $.ajax() method
          $.ajax({

              // The URL for the request
              url: "/contact/",

              // The data to send (will be converted to a query string)
              data: {
                  'email': email,
                  'full_name': full_name,
                  'note': note,
                  "csrfmiddlewaretoken": csrftoken,
              },

              // Whether this is a POST or GET request
              type: "POST",

              // The type of data we expect back
              dataType : "json",
          })
            // Code to run if the request succeeds (is done);
            // The response is passed to the function
            .done(function( json ) {
               $( "<p style='color:green;'>" ).text( json.message ).appendTo( ".mdl-card__supporting-text" );
              //  $( "<div class=\"content\">").html( json.html ).appendTo( "body" );
                $( "#contact-form" ).toggle( "slow", function() {
                    // Animation complete.
                  });
                $('#error').toggle();
                console.log(json.message);
            })
            // Code to run if the request fails; the raw request and
            // status codes are passed to the function
            .fail(function( xhr, status, errorThrown ) {

              $( "<p id='error' style='color:red;'>" ).text( json.message ).appendTo( ".mdl-card__supporting-text" );
              console.log( "Error: " + errorThrown );
              console.log( "Status: " + status );
              console.dir( xhr );
            })
            // Code to run regardless of success or failure;
            .always(function( xhr, status ) {
              console.log( "The request is complete!" );
            });
      }
  });

  function getCookie(name)
  {
      var cookieValue = null;
      if (document.cookie && document.cookie != '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
              var cookie = jQuery.trim(cookies[i]);
              // Does this cookie string begin with the name we want?

              if (cookie.substring(0, name.length + 1) == (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }

  $.ajaxSetup({
       beforeSend: function(xhr, settings) {
           if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
               // Only send the token to relative URLs i.e. locally.
               xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
           }
       }
  });

});
