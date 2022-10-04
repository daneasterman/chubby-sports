$(".reveal_all").click(function () {
	const allPlayerFlex = $('.player_flex_wrapper');	
	
	allPlayerFlex.slideToggle("fast", function() {
		if ( allPlayerFlex.is(":visible") ) {
			$('.reveal_all').html("Hide All Leaders &uarr;")
		} else {
			$('.reveal_all').html("Show All Leaders &darr;")
		}
	});

});
	
$(".reveal_game_leaders").click(function () {
	const leaderButton = $(this);
	const gameFlex = $(this).parents(".game_flex");
	const playerFlex = $(gameFlex).next(".player_flex_wrapper");
	
	playerFlex.slideToggle("fast", function() {
		if ( playerFlex.is(":visible") ) {
			leaderButton.html("Hide Leaders &uarr;")
		} else {
			leaderButton.html("Show Leaders &darr;")
		}
	});

});	