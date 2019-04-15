$(function () {
    $("#showcontent").html($("#showcontent").text());

    var i = document.getElementsByClassName("comment_content");
    for (var c = 0; i.length >= c; c++) {
        $(i[c]).html($(i[c]).text());
    }


    var nexttext;
    var commenteditor = new Quill("#editor", {
        modules: {
            syntax: true,
            toolbar: [
                [{header: [2, 3, false]}],
                ['bold', 'italic', 'underline'],
                ['link', 'code-block'],
                [{'color': []}]
            ]
        },
        placeholder: '评价一下哦，(文明，素质，么么哒)',
        theme: 'snow'
    });
    commenteditor.on('text-change', function (delta, oldDelta, source) {

        if (commenteditor.getLength() >= 250) {
            commenteditor.setText(nexttext);
            toastr.warning("最多1000字！")
        } else {
            nexttext = commenteditor.getContents().ops[0].insert;
        }
    });


    $(".comment_comment").on("click", function () {
        let commentlevel = $(this).attr("data-v");
        let showalObj = $("#showal");
        if (commentlevel == 1) {
            // 一级目录的回复
            showalObj.attr("data-cid", $(this).attr("data-cid")); // 回复的话题
            showalObj.attr("data-upcid", $(this).attr("data-cid")); // 回复的最大话题
            $("#showrelyname").text($(this).attr("data-name")); //
        } else {
            // 二级目录的回复
            showalObj.attr("data-cid", $(this).attr("data-cid")); // 回复的话题
            let fatherCidObj = $(this).parents(".commentItemBody")[1];
            let childrenAObj = $(fatherCidObj).children()[1];
            showalObj.attr("data-upcid", $(childrenAObj).children().attr("data-cid")); // 回复的最大话题
            $("#showrelyname").text($(this).attr("data-name")); //
        }
    });

    $("#comment_submit").click(function () {
        let showalObj = $("#showal");
        let content = commenteditor.container.firstChild.innerHTML;
        let name = $("#commenttitle").val().trim();
        if (name < 4 || name > 10) {
            toastr.warning("昵称最少4个字符,最多10个字符");
            return;
        }
        if (commenteditor.getLength() < 6 || commenteditor.getLength() > 250) {
            toastr.warning("评论最少6个字符,最多250个字符");
            return;
        }
        $.ajax({
            type: "POST",
            url: "/post/comment",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify({

                    Name: name,
                    Uid: showalObj.attr("data-uid"), // 回复谁
                    Cid: showalObj.attr("data-cid"), // 回复的话题
                    Upcid: showalObj.attr("data-upcid"), // 回复的最大话题
                    Pid: $("#commentshow").attr("data-pid"), //
                    Content: content,

                }
            ),
            dataType: "json",
            async: true,
            timeout: 50000,
            success: function (msg) {
                console.log(msg);
                if (msg.code == 200) {
                    // 成功
                    window.location.reload();
                } else {
                    // 失败
                    toastr.error(msg.message);
                    // $("#comment_submit").removeClass("disabled")
                }
            },
            error: function (msg) {
                // console.log(msg);
                toastr.error(msg.message);
            }

        })
    });


});