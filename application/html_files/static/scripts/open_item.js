$(document).ready(function(){
	getAllPost();
});

function getAllPost(data,ths){
	$(ths).siblings().removeClass("active");
	$(ths).toggleClass("active");
	var dic = {};
	dic['username'] = $("#username").html();
	if (data == 1){
		dic['is_trade_success'] = true;
	}
	$.ajax({
        url:"/get-user-all-posts",
        type:"post",
        data:JSON.stringify(dic),
        dataType:"json",
        contentType:'application/json;charset=UTF-8',
        success:function (data) {
        	showBooks(data);
        },
        error:function (data) {
           toastr.error("获取数据失败");
        },
    });
};

function showBooks(data){
    var htmlInner = "<ul>";
    
    for(var i=0; i<data.length; i++){
        var item = data[i];
        htmlInner += "<li><div class=\"item-pic\">";
        htmlInner += "<a target=\"_blank\" href=\"/open_item?id="+item['ItemId']+"\">";
        htmlInner += "<img class=\"J_ItemPic\" src=\""+item['ImageUrl']+"\" title=\""+item['Title']+"\"></a></div>";
        htmlInner += "<div class=\"item-info\"><p><a href=\"/open_item?id="+item['ItemId']+"\">"+item['Title']+"</a></p>";
        htmlInner += "<p class=\"price-block\"><span class=\"price\"><b>¥</b><em>"+item['Price']+"</em></span></p></div></li>";                         
    }
    htmlInner += "</ul>";
    $("#to-display").html(htmlInner);
}