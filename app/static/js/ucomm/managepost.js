$(function () {
    $("#deletePostBtn").click(function () {
        if (confirm("是否删除?")) {
            $.ajax({
                url: '/useradmin/Api/delete',
                type: "DELETE",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify({
                        pid: $("#deletePostBtn").attr("data-pid")
                    }
                ),
                dataType: "json",
                async: true,
                timeout: 50000,
                success: function (msg) {
                    if (msg.code == 200) {
                        // 成功
                        window.location.href = window.location.href;
                    } else {
                        // 失败
                        toastr.error(msg.message);
                        // $("#login_submit").removeClass("disabled")
                    }
                },
                error: function (msg) {
                    // console.log(msg);
                    toastr.error(msg.message);
                }
            });
        }

    });
});