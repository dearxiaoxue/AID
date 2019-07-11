/**
 * Created by tarena on 19-6-18.
 */


$(function () {
    // 查询一个员工的信息
    $('.cwa-user-sub1').click(function () {
        $.ajax({
            url: '/cwa/find_one/',
            type: 'post',
            data: {
                'uid': $(".cwa-id").val(),
                'date': $('.cwa-date').val(),
                'day': $('.cwa-day').val()
            },
            async: false,
            dataType: 'json',
            success: function (data) {
                if(data){
                    var users = data.split('|');
                    var html = '';
                    for (var i = 0; i < users.length; i++) {
                        html += '<tr>';
                        var u = users[i].split('_');
                        html += '<td>' + u[0] + '</td>';
                        html += '<td>' + u[1] + '</td>';
                        html += '<td>' + u[2] + '</td>';
                        html += '<td>' + u[3] + '</td>';
                        html += '<td>' + u[4] + '</td>';
                        html += '<td>' + u[5] + '</td>';
                        html += '</tr>';
                    }
                    $("#cwa-show").html(html)
                }else{
                    alert('暂无考勤信息');
                    $("#cwa-show").html('')
                }
                // alert(data);
            }
        })
    });

    // 查询所有异常考勤
    $('.cwa-user-sub2').click(function () {
        $.ajax({
            url: '/cwa/find_user_all/',
            type: 'post',
            async: false,
            dataType: 'json',
            success: function (data) {
                if(data){
                    var users = data.split('|');
                    var html = '';
                    for (var i = 0; i < users.length; i++) {
                        html += '<tr>';
                        var u = users[i].split('_');
                        html += '<td>' + u[0] + '</td>';
                        html += '<td>' + u[1] + '</td>';
                        html += '<td>' + u[2] + '</td>';
                        html += '<td>' + u[3] + '</td>';
                        html += '<td>' + u[4] + '</td>';
                        html += '<td>' + u[5] + '</td>';
                        html += '</tr>';
                    }
                    $("#cwa-show").html(html)
                }else{
                    alert('暂无考勤异常');
                    $("#cwa-show").html('')
                }
            }
        })
    });

});
