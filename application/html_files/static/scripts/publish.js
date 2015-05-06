
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