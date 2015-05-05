var groupIndex = 100;
$(document).ready(function(){
    console.log("itemType:"+$("#itemType").html());
    selectItemType($("#itemType").html());
});

function selectGroup(index,ths){
    var itemid = $("#itemid").html();
    console.log(itemid);

    if(index<=_lists.length){
        var listValue = _lists[index-1];
        var htmlCon = "<ul>";
        for(var i=0; i< listValue.length;i++){
            htmlCon = htmlCon +"<li><a href=\"/modify-item-type/?type="+(100*index+i)+"&itemid="+itemid+"\">"+listValue[i]+"</a></li>"
        }
        htmlCon = htmlCon +"</ul>";
        $("#list-inner").html(htmlCon);

        $(ths).siblings().removeAttr("class");
        $(ths).toggleClass("active");
    }
}

function selectItemType(typeIndex){
    groupIndex = parseInt(parseInt(typeIndex)/100);
    var smallIndex = parseInt(typeIndex)%100;
    var itemid = $("#itemid").html();
    console.log("itemid:"+itemid);
    if(groupIndex<=_lists.length){
        console.log("groupIndex:"+groupIndex);
        var listValue = _lists[groupIndex-1];
        var htmlCon = "<ul class=\"small-ul\">";
        var classStr = "";
        for(var i=0; i< listValue.length;i++){
            classStr = "";
            if(i==smallIndex){
                classStr = "class=\"active\"";
            }
            htmlCon = htmlCon +"<li " + classStr+"><a href=\"/modify-item-type/?type="+(100*groupIndex+i)+"&itemid="+itemid+"\">"+listValue[i]+"</a></li>"
        }
        htmlCon = htmlCon +"</ul>";
        $("#list-inner").html(htmlCon);
    }
    if(groupIndex<=$(".type-ul").children().length){
        console.log("smallIndex:"+smallIndex);
        $(".type-ul").children().removeAttr("class");
        $(".type-ul").children().eq(groupIndex-1).toggleClass("active");
    }
}