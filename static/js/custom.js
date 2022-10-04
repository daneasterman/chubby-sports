$(".reveal_all").click(function (ev) {
	const allPlayerFlex = $('.player_flex_wrapper');		
	
	if ( allPlayerFlex.is(":hidden") ) {
		ev.preventDefault();
		const hash = "#listings";
		$("html, body").animate({scrollTop: $(hash).offset().top,},
			1000, function () { window.location.hash = hash; });
	}
	
	allPlayerFlex.slideToggle("fast", function() {
		if ( allPlayerFlex.is(":visible") ) {
			$('.reveal_all').html("Hide All Leaders &uarr;");
			$('.reveal_specific').html("Hide Leaders &uarr;");
		} else {
			$('.reveal_all').html("Show All Leaders &darr;");
			$('.reveal_specific').html("Show Leaders &uarr;");
			
		}
	});
});
	
$(".reveal_specific").click(function () {
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
