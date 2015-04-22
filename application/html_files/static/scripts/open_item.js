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

function clickDetailBottom(index,ths){
    $(ths).siblings().removeClass("active");
    $(ths).toggleClass("active");
    if(index==0){
        $(".detail-content").css({"display":"block"});
        $("#message-box").css({"display":"none"});
    }else{
        $(".detail-content").css({"display":"none"});
        $("#message-box").css({"display":"block"});
    }
};

function textDidChange(){
    var remain = 200-$("#message-text").val().length;
    if(remain < 0){
        $(".send-textnum").html(remain+'/200');
    }else{
       $(".send-textnum").html(remain+'/200'); 
    }
};

function sendMessage(){
    var text = $("#message-text").val();
    if(text.length <=0){
        toastr.error("留言不能为空");
    }else if(text.length > 200){
        toastr.error("留言长度不能多于200个字");
    }else{
        $.ajax({
            url:"/post-item-message",
            type:"post",
            data:JSON.stringify({
                "message":text,
                "itemid":$("#itemid").html()
            }),
            dataType:"json",
            contentType:'application/json;charset=UTF-8',
            success:function (data) {
                $("#message-text").val("");
            },
            error:function (data) {
               toastr.error("留言失败,请重试");
            },
        });
    }
}; 