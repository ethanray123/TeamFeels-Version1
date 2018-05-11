$(function(){
    $(".thumbnail").click(function() {
        var img = $(this).attr("src");

        $('#live img').fadeOut(400, function(){
            $('#live img').attr('src', img);
        }).fadeIn(400);
    });
});
