$(document).ready(function () {

    $('#smartwizard').smartWizard({
        selected: 0,
        theme: 'arrows',
        autoAdjustHeight: true,
        transitionEffect: 'fade',
        showStepURLhash: false,

    });

    $.ajax({
        type: "Get",
        url: "/api/categories",
        success: function (resp) {
            for (let cat of resp.categories) {
                $('#select-category').append(`<option>${cat.id}</option>`)
            }
        }
    });

    $.ajax({
        type: "Get",
        url: "/api/tags",
        success: function (resp) {
            for (let cat of resp.tags) {
                $('#select-tags').append(`<option>${cat.name}</option>`)
            }
        }
    });

    $('#select-tags').select2({
        tags: true,
        placeholder: "انتخاب برچسب(های) دلخواه"
    });

});

// $('#SUBMIT').click(function(e){
//   e.preventDefault();
//   $('#register_form').submit();
// })


