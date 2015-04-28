$(document).ready(function(){
    var active_img_index = 0; 
    setActiveImage(active_img_index);
    $("#small-imgs li").click(function(){
        setActiveImage($("#small-imgs li").index(this));
    });
    $(".show_num").click(function(){
        var username = $(".seller").html();
        $.ajax({
        url:"/get-user-for-username",
        type:"post",
        dataType:"json",
        data:JSON.stringify({
            'username':username
        }),
        contentType:'application/json;charset=UTF-8',
        success:function (data) {
            $(".seller-phone").html(data['phone']);
        },
        error:function (data) {
           alert(error);
        },
    });
        $(".seller-phone p").html("1");
    });
});

function setActiveImage(tag){
    //alert($("#small-imgs").children().length)
    $("#small-imgs").children().removeAttr("class");
    $("#small-imgs").children().eq(tag).toggleClass("active");
    $("#show-img").children().eq(0).html($("#small-imgs").children().eq(tag).html());
}