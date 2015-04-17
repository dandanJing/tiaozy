$(document).ready(function(){
    // alert($("#username").val());
    checkNameLabel();
    $("#username").focus(function(){
        $("#name-ph").css({"display":"none"});
    });
    $("#username").blur(function(){
        checkNameLabel();
    });
    $(".placeholder").click(function(){
        $("#username").focus();
    });
});

function checkNameLabel(){
    if ($("#username").val().length > 0) {
        $("#name-ph").css({"display":"none"});
    }else{
        $("#name-ph").css({"display":"block"});
    }
}