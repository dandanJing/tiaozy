var _lists = [["英语","数物","计算机","电子","其他"],["面膜","水","乳","其他"],["电脑","相机","显示器","其他"],
["山地车","电动车", "普通单车", "死飞", "其他"],
["网球", "羽毛球", "足球", "篮球", "其他"],
["衣服", "外套", "其他"],
["沐浴露", "洗发水", "其他"],
["首饰",  "其他"],
["箱包","其他"] ];
$(document).ready(function(){
    selectGroup(1);
});

function selectGroup(index,ths){
    if(index<=_lists.length){
        var listValue = _lists[index-1];
        var htmlCon = "<ul>";
        for(var i=0; i< listValue.length;i++){
            htmlCon = htmlCon +"<li><a href=\"pub/?type="+(100*index+i)+"\">"+listValue[i]+"</a></li>"
        }
        htmlCon = htmlCon +"</ul>";
        $("#list-inner").html(htmlCon);

        $(ths).siblings().removeAttr("class");
        $(ths).toggleClass("active");
    }
}