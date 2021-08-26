$(document).ready(function () {
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
        placeholder: "انتخاب برچسب(ها)..."
    });
});