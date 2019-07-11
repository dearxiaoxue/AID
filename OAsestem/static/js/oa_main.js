    $(function () {
    //加载事件
        var collection = $(".flag");
        $.each(collection, function () {
            $(this).addClass("start");
        });
    });
    //单击事件
    function dj(dom) {
        var collection = $(".flag");
        $.each(collection, function () {
            $(this).removeClass("end");
            $(this).addClass("start");
        });
        $(dom).removeClass("start");
        $(dom).addClass("end");
    }
