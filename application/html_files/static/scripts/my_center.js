

function tapLeftMenu(data,ths){
    if(data==2){
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