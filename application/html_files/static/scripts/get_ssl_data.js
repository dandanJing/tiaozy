var essence_pagenum;
var essence_change_enable;
$(document).ready(function(){
	essence_pagenum = 1;
    essence_change_enable = false;
    getEssence(essence_pagenum);
    getEnBooks();
    getMaPhBooks();
    $("#change-essence").click(function(){
        if (essence_change_enable) {
            getEssence(essence_pagenum);
        };
    });
});

function getEssence(pagenum){
    $.ajax({
        url:"/get-ssl-essence-books",
        type:"post",
        data:JSON.stringify({
            'pagenum':pagenum
        }),
        dataType:"json",
        contentType:'application/json;charset=UTF-8',
        success:function (data_json) {
            var book_list = data_json["book_list"];
            showBooks($("#ssl-essence"),book_list);
            if(data_json["continuationToken"]){
                essence_pagenum += 1;
            }else{
                essence_pagenum = 1;
            }
            essence_change_enable = true;
        },
        error:function (data) {
           toastr.error("获取数据失败");
           essence_change_enable = true;
           essence_pagenum = 1;
        },
    });
};

function getEnBooks(){
    $.ajax({
        url:"/get-ssl-en-books",
        type:"get",
        dataType:"json",
        contentType:'application/json;charset=UTF-8',
        success:function (data) {
            showBooks($("#ssl-en"),data);
        },
        error:function (data) {
           toastr.error("获取数据失败");
        },
    });
};

function getMaPhBooks(){
    $.ajax({
        url:"/get-ssl-maph-books",
        type:"get",
        dataType:"json",
        contentType:'application/json;charset=UTF-8',
        success:function (data) {
            showBooks($("#ssl-maph"),data);
        },
        error:function (data) {
           toastr.error("获取数据失败");
        },
    });
};

function showBooks(ths,data){
    var htmlInner = "<ul>";
    
    for(var i=0; i<data.length; i++){
        var item = data[i];
        htmlInner += "<li class=\"item\"><div class=\"item-pic\">";
        htmlInner += "<a href=\"/show_item_detail?id="+item['ItemId']+"\" target=\"_blank\">";
        htmlInner += "<img class=\"J_ItemPic\" src=\""+item['ImageUrl']+"\" title=\""+item['Title']+"\"></a>";
        htmlInner += "<span class=\"pic_action_box\"><a href=\"\"><img src=\"/static/images/buy_car_1.jpg\"></a>";
        htmlInner += "<a href=\"\"><img src=\"/static/images/upload_1.jpg\"></a></span></div>";
        htmlInner += "<p class=\"item-title\"><a href=\"\">"+item['Title']+"</a></p>";
        htmlInner += "<div class=\"price-block\"><p class=\"price\"><b>¥</b><em>"+item['Price']+"</em></p><p class=\"old_price\">";
        htmlInner += "<b>原价&nbsp;&nbsp;¥</b><em>"+item['OldPrice']+"</em></p></div></li>";                          
    }
    htmlInner += "</ul>";
    ths.html(htmlInner);
}