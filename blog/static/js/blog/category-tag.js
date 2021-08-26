$(document).ready(function () {

    $.ajax({
        type: "Get",
        url: "/api/tags",
        success: function (resp) {
            console.log(resp);
            for (let tag of resp.tags) {
                $('#body-tags').append(`<button id="button-tag"><a href="http://127.0.0.1:5000/tag-posts/${tag.name}/">${tag.name}</a></button>`)
            }
        }
    });


    $.ajax({
        type: "Get",
        url: "/api/categories",
        success: function (resp) {
            $('#cat-column').jstree({
                'core': {
                    "themes": {
                        "variant": "large"
                    },
                    'data': resp.categories
                },
                "types": {
                    "default": {
                        "icon": false
                    },
                },
                "plugins":
                    ["wholerow", "types", "ui", "themes", "html_data"]
            })
        },
    })

    $('#cat-column').bind("select_node.jstree", function (e, data) {
        let id = data.node.id;
        window.location.href = `http://127.0.0.1:5000/category-posts/${id}/`;
    });
});