$(document).ready(function(){
	$(".J_RadioBtn").click(function(){

        if(!$(this).hasClass("active")){
            $(this).siblings().removeClass("active");
            $(this).toggleClass("active");
            $("#feature").val($(this).val());
        }
    });
});

function checkImgType(ths){  
    if (ths.value == "") {  
         toastr.error("请上传图片");
        return false;  
    } else {  
        if (!/\.(gif|jpg|jpeg|png|GIF|JPG|PNG)$/.test(ths.value)) {  
            toastr.error('图片类型有误,图片类型必须是.gif,jpeg,jpg,png中的一种');      
            return false;  
        }  
    }  
    return true;  
}  

function selectfile(file){
    if(checkImgType($(this))){
        alert(1);
         // var p = $("#upload-file").value;
         // $(".upload-inner b").css({"background":p});
     }else{
     } 
}