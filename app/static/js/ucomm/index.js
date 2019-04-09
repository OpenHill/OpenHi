$(function () {
    window.onresize = function () {
        rewhsize();
    };

    // 设置宽高
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
        checkInputBox($(this), 7, 50);
    });
    $("#login_userpwd").change(function () {
        checkInputBox($(this), 6, 30);
    });

    // 登陆表单验证
    $("#login_submit").click(function (event) {
        event.preventDefault();
        var flag = isclass([$("#login_username"), $("#login_userpwd")], "has-success")
        if (flag) {
            // 发送 Ajax 请求
            $("#login_submit").addClass("disabled");
            $.ajax({
                type: "POST",
                url: "/login",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify({
                        username: $("#login_username").val(),
                        userpwd: $("#login_userpwd").val()
                    }
                ),
                dataType: "json",
                async: true,
                timeout: 50000,
                success: function (msg) {
                    if (msg.code == 200) {
                        // 成功
                        window.location.href = "/"
                    } else {
                        // 失败
                        toastr.error(msg.message);
                        $("#login_submit").removeClass("disabled")
                    }
                },
                error: function (msg) {
                    // console.log(msg);
                    toastr.error(msg.message);
                }

            });
        } else {

        }
    });


    // 注册
    $("#regnin_usernikename").change(function () {
        checkInputBox($(this), 1, 10);
    });
    $("#regnin_username").change(function () {
        checkInputBox($(this), 7, 50);
    });
    $("#regnin_userpwd").change(function () {
        checkInputBox($(this), 6, 30);
    });

    // 检查输入框
    function checkInputBox(inputobj, minlen, maxlen) {
        var lens = inputobj.val().length;
        if (lens >= minlen && lens <= maxlen) {
            // 失败
            inputobj.parent("div").removeClass("has-error").addClass("has-success")
        } else {
            // 成功
            inputobj.parent("div").removeClass("has-success").addClass("has-error")

        }

    }

    // 是否包含class
    function isclass(lis, classname) {
        var flag = false;
        for (var i = 0; i < lis.length; i++) {
            if (lis[i].parent("div").attr("class").indexOf(classname) == -1) {
                flag = true; // 不满足条件阻拦
            }
        }
        return !flag

    }


    // 注册表单验证
    $("#regnin_submit").click(function (event) {
        event.preventDefault();
        var flag = isclass([$("#regnin_usernikename"), $("#regnin_username"), $("#regnin_userpwd")], "has-success")
        if (flag) {
            $("#regnin_submit").addClass("disabled");
            // 发送 Ajax 请求
            $.ajax({
                type: "POST",
                url: "/regnin",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify({
                        usernikename: $("#regnin_usernikename").val(),
                        username: $("#regnin_username").val(),
                        userpwd: $("#regnin_userpwd").val()
                    }
                ),
                dataType: "json",
                async: true,
                timeout: 50000,
                success: function (msg) {
                    if (msg.code == 200) {
                        // 成功
                        window.location.href = "/"
                    } else {
                        // 失败s
                        // $("#regnin_alert").text(msg.message);
                        toastr.error(msg.message);
                        $("#regnin_submit").removeClass("disabled");
                    }
                },
                error: function (msg) {
                   toastr.error(msg);
                }
            });
        } else {

        }


    });


    rewhsize();
});