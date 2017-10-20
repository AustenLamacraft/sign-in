$(function() {
    $('button').click(function() {
        $.ajax({
            url: '/signUp',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
								// document.location.replace(response.redirect);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
