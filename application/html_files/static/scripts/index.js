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

    showOnSelling();
    var selling_time = setInterval("showOnSelling()", 15000);
});

function showAuto() {
 	clickIndex = clickIndex >=(count -1) ? 0 : ++clickIndex;
 	$("#slide-index li").eq(clickIndex).trigger('click');
 }

function showOnSelling(){
    $.ajax({
        url:"/get-on-selling",
        type:"get",
        dataType:"json",
        contentType:'application/json;charset=UTF-8',
        success:function (data) {
            var htmlInner = "<ul>";
            for(var i=0; i<data.length; i++){
                var item = data[i];
                htmlInner += "<li class=\"item\"><div class=\"item-pic\"><a href=\"/\" target=\"_blank\">";
                htmlInner += "<img src=\""+item['ImageUrl']+"\" title=\""+item['Title']+"\"></a></div>";
                htmlInner += "<div class=\"info\"><h5>"+item['Title']+"</h5>";
                htmlInner += "<p class=\"desc\">"+"<a href=\"/\">"+item['Description']+"</a></p>"
                htmlInner += "<div class=\"price-block\"><p class=\"price\"><b>¥</b><em>"+item['Price']+"</em></p></div></li>";
            }
            htmlInner += "</ul>";
            $("#on-selling-box").html(htmlInner);
        },
        error:function (data) {
            
        },
    });
}