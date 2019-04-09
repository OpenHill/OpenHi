// 重置布局
function rewhsize() {
    let $main = $("#main");
    let mainw = $main.width();
    let mainh = $main.height();
    let $topnav = $("#topnav");
    // 设置宽
    $topnav.width(mainw);
    $("#content").css("margin-top", $topnav.height() + 1);
    $("#content").height(mainh - $topnav.height());
}

window.onresize = function () {
    rewhsize();
};


//  select 加载
function loadSelect1() {
    $.ajax({
        type: "post",
        url: "/editor/api/classfiyfather",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(),
        dataType: "json",
        async: true,
        timeout: 10000,
        success: function (msg) {
            if (msg.code == 200) {
                Object.keys(msg.data).forEach(function (key) {
                    $("#exampleFormControlSelect1").append("<option value='" + msg.data[key].Id + "'>" + msg.data[key].Name + "</option>")
                });
            } else {
                toastr.error(msg.message);
            }
        },
        error: function (msg) {
            toastr.error(msg);
        }

    });
}


// 加载事件
$(function () {
    // 全局变量初始化
    var nowtabnum = 1; // 已存在的标签数量。
    var maxtabnum = 5; // 最多一次添加五个标签

    // 加载布局
    rewhsize();
    // 加载父级分类
    loadSelect1();

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
        let vals = $("#addtabtxtbox").val();
        // var tabalertObj = $("#tabalert"); //错误提示框

        if (nowtabnum == maxtabnum) {
            toastr.warning("最多添加" + maxtabnum + "个标签")
            return;
        }
        if (vals.length == 0) {
            toastr.warning("标签名不能为空");
            return;
        }
        var pattern = new RegExp("[`~!@#$^&*()=|{}':;',\\[\\].<>《》/?~！@#￥……&*（）\\-=+——|{}【】‘；：”“'。，、？]");
        if (pattern.test(vals)) {
            toastr.warning("包含特殊字符" + vals + "。");
            return;
        }
        if (vals.length >= 2 && isNaN(vals) && vals.length <= 16) {
            html = " <span class=\"tabcontent\">\n" +
                "<span class=\"label label-default posttab\">" + vals + "</span>\n" +
                "<span class=\"btn tabclearbtn\">×</span>\n" +
                "</span>";
            $("#tabbox").append(html);
            $("#addtabtxtbox").val("");
            nowtabnum++;

        } else {
            toastr.warning("不允许全是数字or少于两个字符");
            // return;
        }
    });

    $("#seeEditorBtn").click(function () {
        let t = quill.container.firstChild.innerHTML;
        $("#seeEditorBody").html(t);
    });

    $("#tabbox").on("click", "span.tabclearbtn", function () {
        $(this).parent().remove();
        nowtabnum--;
    });


    $("#exampleFormControlSelect1").change(function () {

        let value = $(this).val();
        if (value != 0) {
            $.ajax({
                type: "post",
                url: "/editor/api/classfiychildren",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify({"Id": value}),
                dataType: "json",
                async: true,
                timeout: 50000,
                success: function (msg) {
                    if (msg.code == 200) {
                        $("#exampleFormControlSelect2").empty();
                        Object.keys(msg.data).forEach(function (key) {
                            $("#exampleFormControlSelect2").append("<option value='" + msg.data[key].Id + "'>" + msg.data[key].Name + "</option>");
                        });
                    } else {
                        toastr.error(msg.message);
                    }
                },
                error: function (msg) {
                    toastr.error(msg);
                }

            });
        } else {
            $("#exampleFormControlSelect2").empty();
        }


    });


    $("#post_submit").click(function (event) {
        let postContent = quill.container.firstChild.innerHTML;
        let postTitle = $("#post-title").val().trim();
        let tabsObj = $(".posttab");
        let tags = "";
        for (let j = 0; tabsObj.length > j; j++
        ) {
            tags = tags + ":" + tabsObj[j].innerText
        }
        let classfiy = 0;

        // console.log($("#exampleFormControlSelect1").index());
        // console.log($("#exampleFormControlSelect2").val());
        if ($("#exampleFormControlSelect2").val()) {
            classfiy = $("#exampleFormControlSelect2").val();
        } else if ($("#exampleFormControlSelect1").val() != 0) {
            classfiy = $("#exampleFormControlSelect1").val();
        } else {
            toastr.warning("未选择分类！");
            return;
        }


        // $.ajax({
        //     type: "post",
        //     url: "/editor",
        //     contentType: "application/json; charset=utf-8",
        //     data: JSON.stringify({"Id": value}),
        //     dataType: "json",
        //     async: true,
        //     timeout: 50000,
        //     success: function (msg) {
        //         if (msg.code == 200) {
        //             $("#exampleFormControlSelect2").empty();
        //             Object.keys(msg.data).forEach(function (key) {
        //                 $("#exampleFormControlSelect2").append("<option value='" + msg.data[key].Id + "'>" + msg.data[key].Name + "</option>");
        //             });
        //         } else {
        //             toastr.error(msg.message);
        //         }
        //     },
        //     error: function (msg) {
        //         toastr.error(msg);
        //     }
        //
        // });


    });
    // key

});
