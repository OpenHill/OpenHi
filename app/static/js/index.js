$(function () {
    rewhsize();
    window.onresize = function () {
        rewhsize();
    }

    function rewhsize() {
        var $main = $("#main");
        var mainw = $main.width();
        var mainh = $main.height();
        var $leftobj = $("#one");
        var $rightobj = $("#two");
        var $topnav = $("#topnav");
        // 设置宽
        if ($leftobj.css("display") == "block") {
            $leftobj.width(mainw / 12 * 3);
            $rightobj.width(mainw / 12 * 9);
            $rightobj.css("margin-left", $leftobj.width());
        } else {
            $leftobj.width(0);
            $rightobj.css("margin-left", "0px");
            $rightobj.width(mainw);
        }
        $topnav.width(mainw);
        $leftobj.css("margin-top", $topnav.height() + 1);
        $rightobj.css("margin-top", $topnav.height() + 1);
        $leftobj.height(mainh - $topnav.height());
        $rightobj.height(mainh - $topnav.height());
    }

    // 登陆
    $("#login_username").change(function () {
        var len = $(this).val().length;
        if (len >= 7 && len <= 50) {
            // 失败
            $(this).parent("div").removeClass("has-error").addClass("has-success")
        } else {
            // 成功
            $(this).parent("div").removeClass("has-success").addClass("has-error")

        }
    });
    $("#login_userpwd").change(function () {
        var len = $(this).val().length;
        if (len >= 6 && len <= 20) {
            // 失败
            $(this).parent("div").removeClass("has-error").addClass("has-success")
        } else {
            // 成功
            $(this).parent("div").removeClass("has-success").addClass("has-error")

        }
    });
    // 登陆表单验证
    $("#login_submit").click(function (event) {
        var ifflag = false; //默认不阻拦
        var datalis = $("[data-form-flag='Login']");
        // console.log(ifflag);
        for (var i = 0; i < datalis.length; i++) {
             console.log($(datalis[i]).attr("class"));
            if ($(datalis[i]).attr("class").indexOf("has-success") == -1) {
                ifflag = true; // 不满足条件阻拦
            }
        }
        if (ifflag) {
            event.preventDefault();
        }
    });


    // 注册
    $("#regnin_usernikename").change(function () {
        var len = $(this).val().length;
        if (len >= 1 && len <= 10) {
            // 失败
            $(this).parent("div").removeClass("has-error").addClass("has-success")
        } else {
            // 成功
            $(this).parent("div").removeClass("has-success").addClass("has-error")

        }
    });
    $("#regnin_username").change(function () {
        var len = $(this).val().length;
        if (len >= 7 && len <= 50) {
            // 失败
            $(this).parent("div").removeClass("has-error").addClass("has-success")
        } else {
            // 成功
            $(this).parent("div").removeClass("has-success").addClass("has-error")

        }
    });
    $("#regnin_userpwd").change(function () {
        var len = $(this).val().length;
        if (len >= 6 && len <= 30) {
            // 失败
            $(this).parent("div").removeClass("has-error").addClass("has-success")
        } else {
            // 成功
            $(this).parent("div").removeClass("has-success").addClass("has-error")

        }
    });

    // 登陆表单验证
    $("#regnin_submit").click(function (event) {
        var ifflag = false; //默认不阻拦
        var datalis = $("[data-form-flag='Regnin']");
        // console.log(ifflag);
        for (var i = 0; i < datalis.length; i++) {
             console.log($(datalis[i]).attr("class"));
            if ($(datalis[i]).attr("class").indexOf("has-success") == -1) {
                ifflag = true; // 不满足条件阻拦
            }
        }
        if (ifflag) {
            event.preventDefault();
        }
    });
});