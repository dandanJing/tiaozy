

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

function selectfile(ths,change_index){

    if(checkImgType(ths)){
        var imgobj = $(ths).get(0).files[0];
        var strsrc = getObjectURL(imgobj);
        if(change_index < $("#images-ul").children().length){
            var liObj = $("#images-ul").children().eq(change_index);
            var imgObject = document.createElement('img');
            imgObject.src = strsrc;
            $(imgObject).val(change_index);
            liObj.children().eq(0).remove();
            $(imgObject).toggleClass("display-image");
            liObj.prepend(imgObject);
            $(liObj).css({"display":"inline"});
        }
        
        if(change_index+2 <6){
            $(ths).css({"width":"1px","height":"1px"});
            $(ths).parent().children().eq(change_index+2).toggleClass("active");
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