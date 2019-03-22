$(function () {
    rewhsize();
    window.onresize = function () {
        rewhsize();
    }

    function rewhsize() {
        console.log("我被加载了");
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

    // form表单验证//
    // $("#loginform").bootstrapValidator({
    //     excluded: [':disabled', ':hidden', ':not(:visible)'],
    //     // live: 'disabled',
    //     submitButtons: '#login_submit',
    //     feedbackIcons: {//根据验证结果显示的各种图标
    //         valid: 'glyphicon glyphicon-ok',
    //         invalid: 'glyphicon glyphicon-remove',
    //         validating: 'glyphicon glyphicon-refresh'
    //     },
    //     fields: {
    //         username: {
    //             validators: {
    //                 notEmpty: {//检测非空,radio也可用
    //                     message: '文本框必须输入'
    //                 }, stringLength: {//检测长度
    //                     min: 6,
    //                     max: 30,
    //                     message: '长度必须在6-30之间'
    //                 }
    //             }
    //         }
    //     }
    // });
    //
    // $("#login_submit").click(function () {//非submit按钮点击后进行验证，如果是submit则无需此句直接验证
    //     $("#loginform").bootstrapValidator('validate');//提交验证
    //     if ($("#loginform").data('bootstrapValidator').isValid()) {//获取验证结果，如果成功，执行下面代码
    //         alert("yes");//验证成功后的操作，如ajax
    //     }
    // });

    // submit 状态
    // var submitflag = false;
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
        if (len >= 6 && len <= 30) {
            // 失败
            $(this).parent("div").removeClass("has-error").addClass("has-success")
        } else {
            // 成功
            $(this).parent("div").removeClass("has-success").addClass("has-error")

        }
    });
    // 登陆表单验证
    $("#login_submit").submit(function(){
        var ifflag = document.getElementsByClassName("has-error");
        if (ifflag.length == 0) {
            return true;
        } else {
            return false;
        }
    });

});