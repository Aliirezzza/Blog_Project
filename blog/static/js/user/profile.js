
$(".deletebtn").click(function (){
        if (confirm("از حذف مقاله مطمعن هستید؟")) {
            $.ajax(
                type: "Post",
                url: "{{ url_for('blog.post_delete', post_id=post._id ) }}"

            alert("مقاله شما حذف شد.");;
  }
    })