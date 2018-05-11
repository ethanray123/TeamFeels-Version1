$(function(){
    // cached the elements
    var $results_holder = $("#search_result");
    var $search_bar = $("#search");

    // clears the ul element with id "search_result" when input element
    // with id "search" is out of focus
    $(document).click(function(e) {
        if($(e.target).parents('#search_result').length == 0){
            $('body ul#search_result').empty();
            $('body input#search').val('');
        }
    });

    // performs ajax when keyup and focus event happens
    $search_bar.on("keyup focus ", function(){
        $.ajax({
            type: 'GET',
            url: 'stream/search_result/',
            data: {'search_text': $search_bar.val()},
            success: function(results){
            // appends all the search results in the the ul element
            // with id "search_result"
            // "results" is the json response from the server
                console.log(results);
                $results_holder.empty();
                $.each(results.streamers, function(i, streamer){
                    $results_holder.append("<li><a href=\""+ streamer.url + "\">" + streamer.user__username + "</a><span class='type'>streamer</span></li>");
                });
                $.each(results.lobbies, function(i, lobby){
                    $results_holder.append("<li><a href=\"" + lobby.url + "\">" + lobby.lobbyname + "</a><span class='type'>lobby</span></li>");
                });
                $.each(results.streams, function(i, stream){
                    $results_holder.append("<li>" + stream.title + "<span class='type'>stream</span></li>");
                });
            }
        });
    });
});