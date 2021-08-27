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

// //  ajax icon like and dislike
// $(document).ready(function () {
//     var $LikeLink = $('#post_like')
//     var $DisLikelink = $('#post_dislike')
//
// // icon like
//     $LikeLink.click(function (e) {
//         e.preventDefault();
//         alert("برای پسندیدن مطلب به 'ادامه مطلب 'بروید ");
//     })
// // icon dislike
//     $DisLikelink.click(function (e) {
//         e.preventDefault();
//         alert("برای نپسندیدن مطلب به 'ادامه مطلب 'بروید ");
//     })
// })

function like(post_id){
        console.log(post_id)

    var $LikeCounter = $(`#like_counter_${post_id}`)
    var $DislkeCounter = $(`#dislike_counter_${post_id}`)
    var $svgLike = $(`#like-${post_id}`)
    var $svgDislike = $(`#dislike-${post_id}`)
    $.ajax({

            url: 'api/like/'+post_id,
            type: "GET",
            data: {
                like: post_id,
            },
            success: function (resp) {
                if (resp['status'] == 1) {
                    $LikeCounter.html(parseInt($LikeCounter.html()) + 1);
                    $svgLike.css('color', 'red')
                } else if (resp['status'] == 2) {
                    $LikeCounter.html(parseInt($LikeCounter.html()) + 1);
                    $svgLike.css('color', 'red')
                    $DislkeCounter.html(parseInt($DislkeCounter.html()) - 1);
                    $svgDislike.css('color', '#99abb4')
                } else if (resp['status'] == 3) {
                    $LikeCounter.html(parseInt($LikeCounter.html()) - 1)
                    $svgLike.css('color', '#99abb4')
                }
            },
            error: function (xhr, ajaxOptions, thrownError) {
                console.log(xhr)
                $('#alert .modal-body').html('we have server error')
                $('#alert').modal('show')
            }
        })
}
function dislike(post_id){
    var $LikeCounter = $(`#like_counter_${post_id}`)
    var $DislkeCounter = $(`#dislike_counter_${post_id}`)
    var $svgLike = $(`#like-${post_id}`)
    var $svgDislike = $(`#dislike-${post_id}`)
    $.ajax({
            url: 'api/dislike/'+post_id,
            type: "GET",
            data: {
                dislike: post_id,
            },
            success: function (resp) {
                if (resp['status'] == 1) {
                    $DislkeCounter.html(parseInt($DislkeCounter.html()) + 1);
                    $svgDislike.css('color', 'red')
                } else if (resp['status'] == 2) {
                    $DislkeCounter.html(parseInt($DislkeCounter.html()) + 1);
                    $svgDislike.css('color', 'red')
                    $LikeCounter.html(parseInt($LikeCounter.html()) - 1);
                    $svgLike.css('color', '#99abb4')
                } else if (resp['status'] == 3) {
                    $DislkeCounter.html(parseInt($DislkeCounter.html()) - 1)
                    $svgDislike.css('color', '#99abb4')
                }
            },
            error: function (xhr, ajaxOptions, thrownError) {
                console.log(xhr)
                $('#alert .modal-body').html('we have server error')
                $('#alert').modal('show')
            }
        })
}
