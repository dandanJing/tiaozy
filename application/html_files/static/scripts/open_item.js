var msgPageNum;
$(document).ready(function(){
	getAllPost();
    msgPageNum = 1;
	loadMessages(msgPageNum);
});

/////////////////////////////////load data///////////////////////////////////////////////
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

function loadMessages(pagenum){
	$.ajax({
        url:"/get-item-messages",
        type:"post",
        data:JSON.stringify({
        	'itemid':$("#itemid").html(),
            "pagenum":pagenum
        }),
        dataType:"json",
        contentType:'application/json;charset=UTF-8',
        success:function (data) {
        	showMessages(data);
        },
        error:function (data) {
           toastr.error("获取留言失败");
        },
    });
}

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

function showMessages(data){
    var htmlInner = "<ul>";
    
    for(var i=0; i<data.length; i++){
        var item = data[i];
        htmlInner += "<li><img src=\"/static/images/avatar.jpg\"> <div class=\"message-cont\">";
        htmlInner += item['Message']+"</div><div class=\"message-time\">"+item['PostTime']+"</div></li>";                       
    }
    htmlInner += "</ul>";
    $("#messages-display").html(htmlInner);
}

///////////////////////////////description action////////////////////////////////////////

function clickDetailBottom(index,ths){
    $(ths).siblings().removeClass("active");
    $(ths).toggleClass("active");
    if(index==0){
        $(".detail-content").css({"display":"block"});
        $(".message-box").css({"display":"none"});
    }else{
        $(".detail-content").css({"display":"none"});
        $(".message-box").css({"display":"block"});
    }
};

///////////////////////////////message action//////////////////////////////////////
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
                if($(".messages-display ul").children().length<8){
                    appendMessage(data);
                }      
            },
            error:function (data) {
               toastr.error("留言失败,请重试");
            },
        });
    }
}; 

function changePage(data,ths){
    var totalPage = $(ths).siblings().length-1;
    if(data==-1 && msgPageNum > 1){
        var rmstr = "#msg-page"+msgPageNum;
        msgPageNum -=1;
        loadMessages(msgPageNum);
        $(ths).siblings().removeClass("active");
        $(ths).siblings().eq(msgPageNum-1).toggleClass("active");
    }else if(data==1 && msgPageNum< totalPage){
        msgPageNum +=1;
        loadMessages(msgPageNum);
        $(ths).siblings().removeClass("active");
        $(ths).siblings().eq(msgPageNum).toggleClass("active");
    }
};

function tapPage(ths){
    if($(ths).hasClass("active")){
        return;
    }
    var totalPage = $(ths).siblings().length-1;
    var changePage = parseInt($(ths).html());
    if(changePage <= totalPage && changePage > 0){
        msgPageNum = changePage;
        loadMessages(msgPageNum);
        $(ths).siblings().removeClass("active");
        $(ths).toggleClass("active");
    }
}

function appendMessage(data){
    var htmlInner = $("#messages-display").html();
    for(var i=0; i<data.length; i++){
        var item = data[i];
        htmlInner += "<li><img src=\"/static/images/avatar.jpg\"> <div class=\"message-cont\">";
        htmlInner += item['Message']+"</div><div class=\"message-time\">"+item['PostTime']+"</div></li>";                       
    }
    $("#messages-display").html(htmlInner);
}

function textDidChange(){
    var remain = 200-$("#message-text").val().length;
    if(remain < 0){
        $(".send-textnum").html(remain+'/200');
    }else{
       $(".send-textnum").html(remain+'/200'); 
    }
};
/////////////////////////////////item action/////////////////////////////////////
function setTradeSuccess(ths,itemid){
   $.ajax({
    　　url : '/set-trade-success-by-itemid',
    　　data : JSON.stringify({
        "itemid":itemid,
        }),
       dataType:"json",
    　　type : "POST",
       contentType:'application/json;charset=UTF-8',
    　　success : function(data) {
             if(data['result']){
                var htmlInner = "<div class=\"trade-successed\">交易已完成</div>";
                 htmlInner +=  "<div class=\"delete-item\" onclick=\"deleteItem(this,itemid)\">删除</div>";
                $("#action-box").html(htmlInner);
             } else{
                toastr.error("设置失败");
             }
    　　},
        error:function (data) {
            toastr.error("设置失败");
        },
    }); 
}

function deleteItem(ths,itemid){
    $.ajax({
    　　url : '/delete-my-post-by-itemid',
    　　data : JSON.stringify({
        "itemid":itemid,
        }),
       dataType:"json",
    　　type : "POST",
       contentType:'application/json;charset=UTF-8',
    　　success : function(data) {
            if(data['result']){
               window.location.href = "/";
            }else{
                toastr.error("删除失败");
            }　   
    　　},
        error:function (data) {
            toastr.error("删除失败");
        },
    });
}