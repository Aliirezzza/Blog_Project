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



//  ajax icon like and dislike
$(document).ready(function () {
    var $LikeLink = $('#post_like')
    var $DisLikelink = $('#post_dislike')

// icon like
    $LikeLink.click(function (e) {
        e.preventDefault();
        alert("برای پسندیدن مطلب به 'ادامه مطلب 'بروید ");
    })
// icon dislike
    $DisLikelink.click(function (e) {
        e.preventDefault();
        alert("برای نپسندیدن مطلب به 'ادامه مطلب 'بروید ");
    })
})


