

$(document).ready(function(){
	$(".J_RadioBtn").click(function(){
        if(!$(this).hasClass("active")){
            $(this).siblings().removeClass("active");
            $(this).toggleClass("active");
            $("#feature").val($(this).val());
        }
    });
    $(".upload-inner").hover(function(){
    });
});

function checkImgType(ths){  
    if (ths.value == "") {  
         toastr.error("请上传图片");
        return false;  
    } else {  
        if (!/\.(gif|jpg|jpeg|png|GIF|JPG|PNG)$/.test(ths.value)) {  
            toastr.error('图片类型有误,图片类型必须是.gif,jpeg,jpg,png中的一种');   
            ths.value = "" ; 
            return false;  
        }  
    }  
    return true;  
}  

function getObjectURL(file) {
    var url = null ; 
    if (window.createObjectURL!=undefined) { // basic
        url = window.createObjectURL(file) ;
    } else if (window.URL!=undefined) { // mozilla(firefox)
        url = window.URL.createObjectURL(file) ;
    } else if (window.webkitURL!=undefined) { // webkit or chrome
        url = window.webkitURL.createObjectURL(file) ;
    }
    return url ;
}

function selectfile(ths){
   
    if($("#J_UploadPic img").length >= 6){
        toastr.error('最多上传5张图片'); 
        return;
    }

    if(checkImgType(ths)){

        var imgobj = $('#upload-file').get(0).files[0];
        var strsrc = getObjectURL(imgobj);
        var divObj = document.getElementById("J_UploadPic");
        var imgObject = document.createElement('img');
        imgObject.src = strsrc;
        $(imgObject).css({"width":"100px","height":"100px","top":"0px","margin-left":"10px"});
        divObj.appendChild(imgObject);
        var _newfile   = ths.cloneNode();
        _newfile.name  = "upfile[]";
        $(_newfile).css({"width":"1px","height":"1px"}),
        // _newfile.css({"display":"none"});
        // _newfile.disabled = true;
        divObj.appendChild(_newfile);
        var delObj = document.createElement('img');
        delObj.src = "/static/images/delete.jpg";
        $(delObj).css({"width":"20px","height":"20px","top":"0px","margin-left":"-20px","position":"absolute","z-index":"3"});
        divObj.appendChild(delObj);
        $(delObj).click(function(){
            var chObjs = $(this).parent().children();
            var index = $(".upload img").index(this);
            if(index == -1){
                return;
            }
            var rmIndex = 3*(index/2);
            var len = chObjs.length;
            if(rmIndex < len){
                for(var i=0;i<3;i++){
                    chObjs.eq(rmIndex).remove();
                    rmIndex = rmIndex-1;
                }
            }   
        });
     }
}

function submit_form(){
    if($("#title").val().length <= 0){
         toastr.error('请输入标题'); 
         return;
    }
    if($("#price").val().length <= 0){
         toastr.error('请输入价格'); 
         return;
    }
    if($("#original-price").val().length <= 0){
         toastr.error('请输入原价'); 
         return;
    }
    if($("#J_UploadPic img").length<= 1){
        toastr.error('请上传图片'); 
        return;
    }
    $("#publishForm").submit();
}

