

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
    $(".upload-inner").children().removeClass("active");
    var active_index = -1;
    for(var i=1;i<$(".upload-inner").children().length;i++){
        var inputObj = $(".upload-inner").children().eq(i);
        if(inputObj.val()!=""){
            var imgobj = inputObj.get(0).files[0];
            var strsrc = getObjectURL(imgobj);
            if($("#images-ul").children().length < 5){
                appendImageChild(strsrc,i-1);
            }
            inputObj.css({"width":"1px","height":"1px","display":"inline"});
        }else if(active_index==-1){
            active_index = i;
        }
    }
    console.log("active_index:"+active_index);
    if(active_index>-1){
        setAsActiveInput(active_index);
    }
    
});

function setAsActiveInput(active_index){
    if(active_index< $(".upload-inner").children().length){
        var obj = $(".upload-inner").children().eq(active_index);
        obj.toggleClass("active");
        obj.css({"width":"90px","height":"90px","display":"inline"});
    }
}

function selectfile(ths,change_index){
    console.log(change_index);
    if(checkImgType(ths)){
        var imgobj = $(ths).get(0).files[0];
        var strsrc = getObjectURL(imgobj);
        if($("#images-ul").children().length < 5){
            appendImageChild(strsrc,change_index);
            $(ths).css({"width":"1px","height":"1px"});
            $(ths).removeClass("active");
            for(var i = 1;i<$(ths).parent().children().length;i++){
                var obj = $(ths).parent().children().eq(i);
                console.log("input "+i+"val: "+obj.val());
                if(obj.val()==""){
                    obj.toggleClass("active");
                    obj.css({"width":"90px","height":"90px","display":"inline"});
                    break;
                }
            }
        }else{
            toastr.error('最多上传5张图片');
            return;
        }
     }
}

function appendImageChild(strsrc,change_index){
    var innerHtml = "<li>";
    innerHtml += "<img src=\""+strsrc+"\"  class=\"display-image\" data-value=\""+change_index+"\">";
    innerHtml += "<img src=\"/static/images/delete.jpg\" class=\"delete-image\" onclick=\"deleteFile(this)\"></li>";
    var html_strat = $("#images-ul").html()+innerHtml;
    $("#images-ul").html(html_strat);
}

function  deleteFile(ths){
    if($(ths).parent().children().length >1){
        var input_index = $(ths).parent().children().eq(0).data('value');
        console.log("delete input : "+input_index);
        if($(".upload-inner").children().length > input_index+1){
            console.log($(".upload-inner").children().eq(input_index+1).val());
            $(".upload-inner").children().eq(input_index+1).val('');
            var i;
            for(i = 0; i< $(".upload-inner").children().length;i++){
                if($(".upload-inner").children().eq(i).hasClass("active")){
                    break;
                }
            }
            console.log('find active index:' + i);
            if(i==$(".upload-inner").children().length){
                $(".upload-inner").children().eq(input_index+1).toggleClass("active");
                $(".upload-inner").children().eq(input_index+1).css({"width":"90px","height":"90px","display":"inline"});
            }
            $(ths).parent().remove();
        }  
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