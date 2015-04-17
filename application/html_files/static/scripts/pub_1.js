$(document).ready(function(){
	$(".J_RadioBtn").click(function(){

        if(!$(this).hasClass("active")){
            $(this).siblings().removeClass("active");
            $(this).toggleClass("active");
            $("#feature").val($(this).val());
        }
    });
});

