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
            ths.value = "" ; 
            return false;  
        }  
    }  
    return true;  
}  

function selectfile(file){
     if(checkImgType(file)){
        // var filePath = file.value;
        // alert(filePath);
        // var fileSystem = new ActiveXObject("Scripting.FileSystemObject");
        // var file = fileSystem.GetFile(filePath);
        // var fileSize = file.Size;
        // alert(fileSize);
        // $(".upload-inner b").css({"background":file});
        var file = $('#upload-file').get(0).files[0];
        if(file) {
            $(".upload-inner b").css({"background":file});
        }else{
            alert(0);
        }
     }else{

     }
    // if($('#upload-file').files) {

    //     // Support: nsIDOMFile, nsIDOMFileList
    //     alert('1');
    //     alert('value: ' + document.getElementById('my-file').value);

    //     alert('files.length: ' + document.getElementById('my-file').files.length);

    //     alert('fileName: ' + document.getElementById('my-file').files.item(0).fileName);

    //     alert('fileSize: ' + document.getElementById('my-file').files.item(0).fileSize);

    //     alert('dataurl: ' + document.getElementById('my-file').files.item(0).getAsDataURL());

    //     alert('data: ' + document.getElementById('my-file').files.item(0).getAsBinary());

    //     alert('datatext: ' + document.getElementById('my-file').files.item(0).getAsText("utf-8"));

    // }else{
    //     alert('error');
    // }
    // if(checkImgType($(this))){
    //     alert(1);
    //      // var p = $("#upload-file").value;
    //      // $(".upload-inner b").css({"background":p});
    //  }else{
    //  } 
}