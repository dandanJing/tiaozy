
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