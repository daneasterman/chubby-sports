$(".reveal_all").click(function (ev) {
	const allPlayerFlex = $('.player_wrapper');	
	 // If any player/leader divs are hidden:
	if ( allPlayerFlex.is(":hidden") ) {	
			smoothScrollDown(ev)
			allPlayerFlex.slideDown("fast", function() {});
			$('.reveal_specific').html("Hide Leaders &uarr;");				
		 } else {
			smoothScrollDown(ev)
		 }
});

function smoothScrollDown(ev) {
	ev.preventDefault();
	const hash = "#listings";
	$("html, body").animate({scrollTop: $(hash).offset().top,},
		1000, );
}
	
$(".reveal_specific").click(function () {
	const leaderButton = $(this);
	const gameFlex = $(this).parents(".game_flex");
	const specificPlayerFlex = $(gameFlex).next(".player_wrapper");

	if ( specificPlayerFlex.is(":hidden") ) {
		specificPlayerFlex.slideDown("fast", function() {});				
		leaderButton.html("Hide Leaders &uarr;")
	} else {
		specificPlayerFlex.slideUp("fast", function() {});
		leaderButton.html("Show Leaders &darr;")
	}
});

// Soccer version for "Show Scorers" instead of "Show Leaders" button:
$(".reveal_scorer").click(function () {
	const leaderButton = $(this);
	const gameFlex = $(this).parents(".soccer_flex");
	const specificPlayerFlex = $(gameFlex).next(".player_wrapper");

	if ( specificPlayerFlex.is(":hidden") ) {
		specificPlayerFlex.slideDown("fast", function() {});				
		leaderButton.html("Hide Scorers &uarr;")
	} else {
		specificPlayerFlex.slideUp("fast", function() {});
		leaderButton.html("Show Scorers &darr;")
	}
});
