$(function(){
    $("button#send").click(function(){
        $.ajax({
            type: 'GET',
            url: 'comments/',
            data: {'comment_text': $("input#comment").val(),
                'lobby_pk': '{{ lobby.pk }}'
                },
            success: function(data){
                $("ul#comment_holder").append("<li>" + data.comment + "</li>");
            }
        });
    });
});