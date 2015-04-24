$(document).ready(function(){
    var style = $("#selctType").html();
    tapLeftMenu(style,$(".left-menu ul").children().eq(style-1));
});

function tapLeftMenu(data,ths){
    if($(ths).hasClass("active")){
        return;
    }
    $(ths).siblings().removeClass("active");
    $(ths).toggleClass("active");
    if(data==1){
        $.ajax({
            url:"/get-my-personal-info",
            type:"post",
            data:JSON.stringify({
            }),
            dataType:"json",
            contentType:'application/json;charset=UTF-8',
            success:function (data) {
                showMyPersonalInfo(data);
            },
            error:function (data) {
               toastr.error("获取数据失败");
            },
        });
    }else if(data==2){
        var htmlInner="<div class=\"mypost-title\"><div class=\"post-title-nav\">";
        htmlInner += "<ul><li class=\"active\" onclick=\"selectMyPost(1,this)\">所有发布</li>";
        htmlInner += "<li onclick=\"selectMyPost(2,this)\">按时间排序</li>";
        htmlInner += "<li onclick=\"selectMyPost(3,this)\">按热度排序</li>";            
        htmlInner += "<li onclick=\"selectMyPost(4,this)\">成功交易</li>";                
        htmlInner += "</ul></div><div class=\"nav-detail\">";                    
        htmlInner += "<ul><li>上一页</li><li>1</li><li>2</li><li>下一页</li></ul></div></div>";                    
        htmlInner += "<div class=\"post-content\" id=\"post-content\">";                    
        $("#right-body-cont").html(htmlInner);
        selectMyPost(1,"")
    }
}

function showMyPosts(data){
    var htmlInner="<ul>";
    for(var i=0; i< data.length;i++){
        var item = data[i];
        htmlInner +="<li><div class=\"item-time\">"+item["PostTime"]+"</div>";
        htmlInner +="<div class=\"item-pic\"><a target=\"_blank\" href=\"/show_item_detail?id=\""+item["ItemId"]+"\">";
        htmlInner +="<img class=\"J_ItemPic\" src=\""+item["ImageUrl"]+"\"></a></div>";
        htmlInner +="<div class=\"item-info\"><p><a>"+item['Title']+"</a></p>";
        htmlInner +="<div class=\"price-block\"><span class=\"price\"><b>¥</b><em>"+item["Price"]+"</em></span>";
        htmlInner +="<span class=\"old-price\">原价:"+item["OldPrice"]+"</span></div>";
        htmlInner +="<div class=\"bottom-info\"><span class=\"item-click\">浏览:"+item['ClickCount']+"</span>";
        htmlInner +="<span class=\"item-messages\">留言:"+item['MessageCount']+"</span></div></div>";
        if(item['IsTradeSuccess']){
            htmlInner +="<div class=\"item-btn\"><span>删除</span></div></li>";
        }else{
            htmlInner +="<div class=\"item-btn\"><span>删除</span><span>修改</span><span>交易成功</span></div></li>";  
        }  
    }
    htmlInner += "</ul>";
    $("#post-content").html(htmlInner);
}

function showMyPersonalInfo(data){
    var std_str = "";
    var other_str = "";
    var avatar_str = "\"/static/images/avatar.png\"";
    if(data.IsStudent){
       std_str = "checked" ;
    }else{
       other_str = "checked" ;
    }
    if(data.AvatarUrl.length > 0){
        avatar_str = data.AvatarUrl;
    }
    var htmlInner="<div><span class=\"label-title\">用户名:</span><strong>"+data.Username+"</strong></div>";
    htmlInner +="<form id=\"my-info-form\" method=\"post\" enctype=\"multipart/form-data\" action=\"/change-my-info\">";
    htmlInner +="<div class=\"avatar-box\"><span class=\"label-title\">我的头像:</span>";
    htmlInner +="<div class=\"my-avatar\"><img id=\"avatar-img\" src="+avatar_str+"></div>";
    htmlInner +="<div class=\"change-avatar\">修改头像<input type=\"file\" id=\"avatar-input\" name=\"file\" onchange=\"selectAvatar(this)\"></input>";
    htmlInner +="<div class=\"label-desc\">图片格式:GIF,JPG,JPEG,PNG,最佳尺寸100*100像素</div></div></div>";   
    htmlInner +="<div class=\"input-box\"><span class=\"label-title\">手机:</span>";       
    htmlInner +="<input type=\"text\" id=\"phone-input\" name=\"phone\" value=\""+data.Mobilephone+"\"></input></div>";       
    htmlInner +="<div class=\"input-box\"><span class=\"label-title\">邮箱:</span><input type=\"text\" id=\"email-input\" name=\"email\" value=\""+data.Email+"\"></input></div>";      
    htmlInner +="<div class=\"input-box\"><span class=\"label-title\">QQ:</span><input type=\"text\" id=\"qq-input\" name=\"qq\" value=\""+data.QQ+"\"></input></div>";            
    htmlInner +="<div class=\"input-box\"><span class=\"label-title\">身份:</span>";            
    htmlInner +="<input id=\"status1\" class=\"status-radio\" type=\"radio\" name=\"is-student\" value=\"1\" "+std_str+"><span class=\"span-title\">学生</span></input>";         
    htmlInner +="<input id=\"status2\" class=\"status-radio\" type=\"radio\" name=\"is-student\" value=\"0\" "+other_str+"><span class=\"span-title\">其他</span></input></div>";  
    htmlInner +="<div class=\"type-title\">补充资料</div><div class=\"input-box\"><span class=\"label-title\">真实姓名:</span>";         
    htmlInner +="<input type=\"text\" id=\"truename-input\" name=\"realname\" value=\""+data.RealName+"\"></input></div>";    
    htmlInner +="<label id=\"btn\" class=\"btn\">";       
    htmlInner +="<input id=\"submit_btn\" class=\"btns\" type=\"button\" style=\"width:110px;height:34px;\" checked=\"checked\"";       
    htmlInner +="value=\"提交修改\" onclick=\"submitForm()\"></input></label></form>";   
    $("#right-body-cont").html(htmlInner);
}

function selectAvatar(ths){
    if(checkImgType(ths)){
        var imgobj = $('#avatar-input').get(0).files[0];
        var strsrc = getObjectURL(imgobj);
        var imgObject = document.createElement('img');
        imgObject.src = strsrc;
        $(".my-avatar").html(imgObject);
    }else{
        $("#avatar-input").val("");
    }
}

function submitForm(){
    $.ajaxFileUpload({
        url:'/upload-my-avatar',
        secureuri:false,
        fileElementId:"avatar-input",
        dataType:"text",
        success:function(data) {
            alert(data);
        },
        error:function (data) {
            toastr.error("上传图片失败");
        },
    });
    $.ajax({
    　　url : '/change-my-info',
    　　data : $('#my-info-form').serialize(),
    　　type : "POST",
    　　success : function(data) {
    　　　　if(data['errors']){
            var error_str = "";
            var errors = data['errors'];
             for(var i=0; i< errors.length;i++){
                toastr.error(errors[i]);
             }
             
           }else{
            toastr.success("修改数据成功！");
           }
    　　},
        error:function (data) {
            toastr.error("修改数据失败");
        },
    });
}

function selectMyPost(data,ths){
    if($(ths).hasClass("active")){
        return;
    }
    $(ths).siblings().removeClass("active");
    $(ths).toggleClass("active");
    var typeStr = "all";
    switch(data){
        case 1:typeStr = "all";break;
        case 2:typeStr = "time";break;
        case 3:typeStr = "click";break;
        case 4:typeStr = "success";break;
        default:
        typeStr = "all";
    }
    $.ajax({
    　　url : '/get-my-posts-by-type',
    　　data : JSON.stringify({
        "type":typeStr,
        }),
       dataType:"json",
    　　type : "POST",
       contentType:'application/json;charset=UTF-8',
    　　success : function(data) {
    　　　　showMyPosts(data);
    　　},
        error:function (data) {
            toastr.error("获取数据失败");
        },
    });
}