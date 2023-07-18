$("#toggle_menu").click(function(){
    var menueContent = $("#navbarSupportedContent");
    var menueContent1 = $("#navbarResponsive");
    if(menueContent.hasClass("show")){
        menueContent.removeClass("show");
        menueContent1.removeClass("show");
    }
    else{
        menueContent.addClass("show");
        menueContent1.addClass("show");
    }

})