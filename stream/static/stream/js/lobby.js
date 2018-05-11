$(function(){
    $(".stuff").click(function() {
        var img = $(this).find(".thumbnail").attr("src");
        var user = $(this).find("#streamer").text()
        var title = $(this).find("#title").text()
        

        $('#live img').fadeOut(400, function(){
            $('#live img').attr('src', img);
        }).fadeIn(400);


        $('#live h5').fadeOut(400, function(){
            $("#live h5").html(title + " - " + user);
        }).fadeIn(400);

    });
});
