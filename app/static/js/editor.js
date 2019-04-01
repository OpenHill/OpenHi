$(function () {
    // 全局变量初始化
    var nowtabnum = 1; // 已存在的标签数量。
    var maxtabnum = 5; // 最多一次添加五个标签

    // 界面初始化
    // 加载布局
    rewhsize();
    window.onresize = function () {
        rewhsize();
    }

    function rewhsize() {
        var $main = $("#main");
        var mainw = $main.width();
        var mainh = $main.height();
        var $topnav = $("#topnav");
        // 设置宽
        $topnav.width(mainw);
        $("#content").css("margin-top", $topnav.height() + 1);
        $("#content").height(mainh - $topnav.height());
    }

    // 加载编辑器
    var quill = new Quill('#editor-container', {
        modules: {
            formula: true,
            syntax: true,
            toolbar: '#toolbar-container'
        },
        placeholder: '文本不得少于20个字',
        theme: 'snow'
    });

    //标签系统
    $("#addtabbtn").click(function () {
        var vals = $("#addtabtxtbox").val();
        var tabalertObj = $("#tabalert"); //错误提示框

        if (nowtabnum == maxtabnum) {
            tabalertObj.text("最多添加" + maxtabnum + "个标签");
            return;
        }
        if (vals.length == 0) {
            tabalertObj.text("标签名不能为空");
            return;
        }
        var pattern = new RegExp("[`~!@#$^&*()=|{}':;',\\[\\].<>《》/?~！@#￥……&*（）\\-=+——|{}【】‘；：”“'。，、？]");
        if (pattern.test(vals)) {
            tabalertObj.text("包含特殊字符" + vals + "。");
            return;
        }
        if (vals.length >= 2 && isNaN(vals) && vals.length <= 16) {
            html = " <span class=\"tabcontent\">\n" +
                "<span class=\"label label-default\">" + vals + "</span>\n" +
                "<span class=\"btn tabclearbtn\">×</span>\n" +
                "</span>";
            $("#tabbox").append(html);
            $("#addtabtxtbox").val("");
            nowtabnum++;

        } else {
            tabalertObj.text("不允许全是数字or少于两个字符");
            return;
        }

        console.log();
    });

    $("#tabbox").on("click", "span.tabclearbtn", function () {
        $(this).parent().remove();
        nowtabnum--;
    });


    $("#post_submit").click(function (event) {
        let t = quill.container.firstChild.innerHTML;
        $("#editor_text").val(t);
        // event.preventDefault();
    });


});
