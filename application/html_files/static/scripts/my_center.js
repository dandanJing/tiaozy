

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
        $.ajax({
            url:"/get-my-posts",
            type:"post",
            data:JSON.stringify({
                'pagenum':1
            }),
            dataType:"json",
            contentType:'application/json;charset=UTF-8',
            success:function (data) {
                showMyPosts(data);
            },
            error:function (data) {
               toastr.error("获取数据失败");
            },
        });
    }
}

function showMyPosts(data){
    $("#right-body-cont").html(data.length);
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
    　　data : $('#my-info-form').serialize()+"&fileInput="+$("input[name='file']").val(),
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
