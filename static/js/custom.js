$(document).ready(function(){
	
	$(".dropdown_cta").click(function () {
		const gameFlex = $(this).parents(".game_flex");
		const playerFlex = $(gameFlex).next(".player_flex_wrapper")
		$(playerFlex).slideToggle("fast", function() {});
	});

});