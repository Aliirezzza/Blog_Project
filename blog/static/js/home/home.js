$(document).ready(function() {

    $('#NavbarUl > li')
        .click(function(e) {
            $('#NavbarUl > li')
                .removeClass('active');
            $(this).addClass('active');
        });
});

$(function() {
    $(".like").click(function() {
        var input = $(this).find('.qty1');
        input.val(parseInt(input.val()) + 1);
    });

    $(".dislike").click(function() {
        var input = $(this).find('.qty2');
        input.val(input.val() - 1);
    });
});
