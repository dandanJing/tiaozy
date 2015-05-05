var groupIndex = 1;
$(document).ready(function(){
    selectItem($("#itemType").html());
});

function selectGroup(index,ths){
    if(index<=_lists.length){
        var listValue = _lists[index-1];
        var htmlCon = "<ul>";
        for(var i=0; i< listValue.length;i++){
            htmlCon = htmlCon +"<li><a href=\"modify_item_type/?type="+(100*index+i)+"\">"+listValue[i]+"</a></li>"
        }
        htmlCon = htmlCon +"</ul>";
        $("#list-inner").html(htmlCon);

        $(ths).siblings().removeAttr("class");
        $(ths).toggleClass("active");
    }
}

function selectItem(typeIndex){
    groupIndex = parseInt(typeIndex)/100;
    var smallIndex = parseInt(typeIndex)%100;

    if(groupIndex<=_lists.length){
        var listValue = _lists[groupIndex-1];
        var htmlCon = "<ul class=\"small-ul\">";
        var classStr = "";
        for(var i=0; i< listValue.length;i++){
            classStr = "";
            if(i==smallIndex){
                classStr = "class=\"active\"";
            }
            htmlCon = htmlCon +"<li " + classStr+"><a href=\"modify_item_type/?type="+(100*groupIndex+i)+"\">"+listValue[i]+"</a></li>"
        }
        htmlCon = htmlCon +"</ul>";
        $("#list-inner").html(htmlCon);
    }
    if(groupIndex<=$(".type-ul").children().length){
        console.log(smallIndex);
        $(".type-ul").children().removeAttr("class");
        $(".type-ul").children().eq(groupIndex-1).toggleClass("active");
    }
}