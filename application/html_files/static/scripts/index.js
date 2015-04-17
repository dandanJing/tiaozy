var count;
$(document).ready(function(){
	var t = clickIndex =0;
	count=$("#slider-item li").length;
	$("#slider-item li:not(:first-child)").hide();
    $("#slide-index li").click(function(){
    	var i = $(this).text()-1;
    	clickIndex = i;
    	
    	if(i >= count)return;
    	$("#slider-item li").filter(":visible").fadeOut(300).parent().children().eq(i).fadeIn(600);
    	$(this).siblings().removeAttr("class");
        $(this).toggleClass("selected");
    });
    t = setInterval("showAuto()", 5000);
 	$("#slider-frame").hover(function(){
 		//alert("hover");
 		clearInterval(t)
 	}, function(){
 		t = setInterval("showAuto()", 5000);
 	});
    $(".item-pic").hover(function(){
        if($(this).children.length > 1){
            var temp = $(this).children().eq(1);
            temp.css({"display":"inline"});
        }
    },function(){
        if($(this).children.length > 1){
            var temp = $(this).children().eq(1);
            temp.css({"display":"none"});
        }
    });
});

function showAuto() {
 	clickIndex = clickIndex >=(count -1) ? 0 : ++clickIndex;
 	$("#slide-index li").eq(clickIndex).trigger('click');
 }
