var myPostPage = 1;
var myPostType = 1;
$(document).ready(function(){
    var style = $("#selctType").html();
    console.log("selectStyle:"+style);
    // style = 3;
    tapLeftMenu(style,$(".left-menu ul").children().eq(style-1));
});

function tapLeftMenu(data,ths){
    if($(ths).hasClass("active")&& data<5){
        return;
    }else if(data < 5){
        $(ths).siblings().removeClass("active");
        $(ths).toggleClass("active");
    }else{
       $(ths).siblings().removeClass("active"); 
    }

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
        htmlInner += "<li onclick=\"selectMyPost(4,this)\">成功交易</li></ul></div></div>";                                 
        htmlInner += "<div class=\"post-content\" id=\"post-content\"></div>";                    
        $("#right-body-cont").html(htmlInner);
        myPostPage = 1;
        selectMyPost(1,"");
    }else if(data==3){
        $.ajax({
            url:"/get-my-ask-items",
            type:"post",
            data:JSON.stringify({
            }),
            dataType:"json",
            contentType:'application/json;charset=UTF-8',
            success:function (data) {
                showMyAskItem(data);
            },
            error:function (data) {
               toastr.error("获取数据失败");
            },
        });
    }else if(data==5 || data==6 || data==7){
        if($(ths).children().eq(0).hasClass('closed')){
            console.log("data:"+data+' closed');
            $(ths).children().eq(0).removeClass('closed');
            $(ths).children().eq(0).toggleClass('opened');
            $(ths).children().eq(1).css({"display":"block"});
        }else{
             console.log("data:"+data+' opened');
            $(ths).children().eq(0).removeClass('opened');
            $(ths).children().eq(0).toggleClass('closed');
            $(ths).children().eq(1).css({"display":"none"});
        }
    }
}

function tapLeftSmallMenu(data,ths){
}
///////////////////////////////我的资料//////////////////////////////////
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
            // alert(data);
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


///////////////////////////////我的发布//////////////////////////////////
function selectMyPost(data,ths){
    if($(ths).hasClass("active")){
        return;
    }
    if(ths!=""){
        myPostPage = 1;
    }
    $(ths).siblings().removeClass("active");
    $(ths).toggleClass("active");
    var typeStr = "all";
    myPostType = data;
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
        "getPage":myPostPage,
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

function showMyPosts(data){
    var result = data['result'];
    var pages = data['Pagenum'];
    var htmlInner = "";
    if(pages.length > 1){
        htmlInner += "<div class=\"nav-detail\"><ul><li onclick=\"changePostPage(-2,this)\">上一页</li>";
        for(var i =0; i <pages.length; i++){
            if(myPostPage == pages[i]){
                htmlInner += "<li class=\"active\" onclick=\"changePostPage("+pages[i]+",this)\">"+pages[i]+"</li>";
            }else{
                htmlInner += "<li onclick=\"changePostPage("+pages[i]+",this)\">"+pages[i]+"</li>";
            }    
        }     
        htmlInner +="<li onclick=\"changePostPage(-1,this)\">下一页</li></ul></div>";
    }
    //
    htmlInner +="<ul class=\"posts-ul\">";
    for(var i=0; i< result.length;i++){
        var item = result[i];
        htmlInner +="<li><div class=\"item-time\">"+item["PostTime"]+"</div>";
        htmlInner +="<div class=\"item-pic\"><a target=\"_blank\" href=\"/open_item?id="+item["ItemId"]+"\">";
        htmlInner +="<img class=\"J_ItemPic\" src=\""+item["ImageUrl"]+"\"></a></div>";
        htmlInner +="<div class=\"item-info\"><p><a>"+item['Title']+"</a></p>";
        htmlInner +="<div class=\"price-block\"><span class=\"price\"><b>¥</b><em>"+item["Price"]+"</em></span>";
        htmlInner +="<span class=\"old-price\">原价:"+item["OldPrice"]+"</span></div>";
        htmlInner +="<div class=\"bottom-info\"><span class=\"item-click\">浏览:"+item['ClickCount']+"</span>";
        htmlInner +="<span class=\"item-messages\">留言:"+item['MessageCount']+"</span></div></div>";
        htmlInner +="<div class=\"item-btn\"><span onclick=\"deleteItem(this,'"+item["ItemId"]+"')\">删除</span>";
        if(item['IsTradeSuccess']){
            htmlInner +="<span class=\"tradeSuccess\">交易完成</span></div></li>";
        }else{
           htmlInner +="<span><a href=\"/modify-my-item?itemid="+item['ItemId']+"\">修改</a></span>";
           htmlInner +="<span class=\"notTrade\" onclick=\"setTradeSuccess(this,'"+item["ItemId"]+"')\">交易成功</span></div></li>"; 
        }    
    }
    htmlInner += "</ul>";
    $("#post-content").html(htmlInner);
}

function changePostPage(data,ths){
    if($(ths).hasClass("active")){
        return;
    }

    var pagesnum = $(ths).siblings().length-1;
    if(data==-2 && myPostPage>1){
        myPostPage-=1;
    }else if(data==-1 && myPostPage < pagesnum){
        myPostPage+=1;
    }else if(data>=1){
        myPostPage = data;
    }else{
        return;
    }
    selectMyPost(myPostType,"");
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
                console.log("delete success");
                $(ths).parent().parent().remove();
            }else{
                 toastr.error("删除失败");
            }　   
    　　},
        error:function (data) {
            toastr.error("删除失败");
        },
    });
}

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

             } else{
                toastr.error("设置失败");
             }
    　　},
        error:function (data) {
            toastr.error("设置失败");
        },
    }); 
}
//////////////////////////////////////////我的求购///////////////////////////////////////////////////

function showMyAskItem(data){
    var htmlInner = "<div class=\"myask-title\"><div class=\"myask-title-nav\"><ul>";
    htmlInner +=  "<li class=\"active\" onclick=\"\">所有求购</li><li onclick=\"\">按时间排序</li>";              
    htmlInner +=  "<li onclick=\"\">按浏览次数排序</li><li onclick=\"\">回复次数排序</li><li onclick=\"\">成功交易</li></ul></div></div>";                        
    htmlInner +=  "<div class=\"myask-content\" id=\"myask-content\">";          
    htmlInner +=  "<table><tr class=\"table-title\"><td width=\"150\">标题</td><td width=\"50\">浏览</td>";
    htmlInner +=  "<td width=\"100\">最近编辑时间</td><td width=\"100\">发布时间</td>";                     
    htmlInner +=  "<td width=\"80\">联系人</td><td width=\"120\">联系方式</td>";                        
    htmlInner +=  "<td width=\"200\">详细描述</td><td width=\"150\" class=\"no-border\">操作</td></tr>";                       
   for(var i=0;i<data.length;i++){
        var item = data[i];
         htmlInner += "<tr><td width=\"150\">"+item["Title"]+"</td>";
         htmlInner += "<td width=\"50\">"+item["ClickCount"]+"</td>";
         htmlInner += "<td width=\"100\">"+item["LastEditTime"]+"</td>";
         htmlInner += "<td width=\"100\">"+item["PostTime"]+"</td>";
         htmlInner += "<td width=\"80\">"+item["ContactUserName"]+"</td>";
         htmlInner += "<td width=\"120\">"+item["ContactUserPhone"]+"</td>";
         htmlInner += "<td width=\"200\">"+item["Description"]+"</td>";
         htmlInner += "<td width=\"150\" class=\"no-border\">"+"<span class=\"delete-btn\" onclick=\"deleteMyAskItem(this,'"+item["ItemId"]+"')\">删除</span>";
         htmlInner += "<span class=\"modify-btn\"><a href=\"/ask-item/?itemid="+item["ItemId"]+"\">修改</a></span>"+"</td></tr>";
   }
   htmlInner += "</table></div>";
   $("#right-body-cont").html(htmlInner);
}

function deleteMyAskItem(ths,itemid){
    console.log("delete:"+itemid);
    $.ajax({
    　　url : '/delete-my-ask-by-itemid',
    　　data : JSON.stringify({
        "itemid":itemid,
        }),
       dataType:"json",
    　　type : "POST",
       contentType:'application/json;charset=UTF-8',
    　　success : function(data) {
             if(data['result']){
                $(ths).parent().parent().remove();
             } else{
                toastr.error("删除失败");
             }
    　　},
        error:function (data) {
            toastr.error("删除失败");
        },
    }); 
}

////////////////////////////////////////////////////////////////////////////////////////////