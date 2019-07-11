//显示当前天数
$(document).ready(function () {
    var time = new Date();
//         var day = ("0" + time.getDate()).slice(-2);
    var month = ("0" + (time.getMonth() + 1)).slice(-2);
    var today = time.getFullYear() + "-" + (month);
    $('#cwa-date_info').val(today);
});


//获取当前存入session的用户信息
function get_session() {
    var user = '';
      $.ajax({
            url: '/cwa/get_session',
            type: 'get',
            async: false,
            dataType: 'json',
            success: function (data) {
                console.log('1', data);
                users = [data.id, data.name];
                console.log('2', users);
                 user = data
            }
        });return user

}

var users = get_session();


$(function () {
    // 签到
    $('.cwa-btn1').click(function () {
        //判断是否 已经签到,如果已签到返回true,未签到返回false
        $.ajax({
            url: '/cwa/log_in?uid=' + users.id,
            type: 'get',
            async: true,
            dataType: 'json',
            success: function (data) {
                console.log(data);
                if (data === 1) {
                    alert('已签到,请不要重复签到');
                } else {
                    $.ajax({
                        url: '/cwa/log_in/',
                        type: 'post',
                        data: {'uid': users.id, 'name': users.name},
                        async: false,
                        dataType: 'json',
                        success: function (data) {
                            alert(data)
                        }
                    })
                }
            }
        });
    });

    // 签退
    $('.cwa-btn2').click(function () {
        //判断是否 已经签到,如果已签到返回true,未签到返回false
        $.ajax({
            url: '/cwa/log_back?uid=' + users.id,
            type: 'get',
            async: true,
            dataType: 'json',
            success: function (data) {
                console.log(data);
                if (data > 0) {
                    if(data === 1){
                        alert('已签退,请不要重复签退')
                    }else{
                        alert('请先签到!')}
                } else {
                    $.ajax({
                        url: '/cwa/log_back/',
                        type: 'post',
                        data: {'uid': users.id},
                        async: false,
                        dataType: 'json',
                        success: function (data) {
                            alert(data)
                        }
                    })
                }
            }
        });
    });
});

// 查询
$(function () {
    // 查询一个员工的信息
    $('.cwa-sub1').click(function () {
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
                        // " onclick=\"func('"+u+"')\"
                        var a = "<a href=\"/cwa/alter\?user=\'"+u+"'\">修改</a>";
                        html += '<td>' + u[0] + '</td>';
                        html += '<td>' + u[1] + '</td>';
                        html += '<td>' + u[2] + '</td>';
                        html += '<td>' + u[3] + '</td>';
                        html += '<td>' + u[4] + '</td>';
                        html += '<td>' + u[5] + '</td>';
                        html += '<td>' + a + '</td>';
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

    // 查询当天异常考勤的员工
    $('.cwa-sub2').click(function () {
        $.ajax({
            url: '/cwa/find_all/',
            type: 'post',
            async: false,
            dataType: 'json',
            success: function (data) {
                if(data){
                    // alert(data);
                    var users = data.split('|');
                    var html = '';
                    for (var i = 0; i < users.length; i++) {
                        html += '<tr>';
                        var u = users[i].split('_');
                        var a = "<a href=\"/cwa/alter\?user=\'"+u+"'\">修改</a>";
                        html += '<td>' + u[0] + '</td>';
                        html += '<td>' + u[1] + '</td>';
                        html += '<td>' + u[2] + '</td>';
                        html += '<td>' + u[3] + '</td>';
                        html += '<td>' + u[4] + '</td>';
                        html += '<td>' + u[5] + '</td>';
                        html += '<td>' + a + '</td>';
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


// 修改
$(function () {
    $('#cwa-change').click(function () {
        $.ajax({
            url: '/cwa/alter_server/',
            type: 'post',
            data:{
                'uid': $('#cwa-alter-td1').text(),
                'time': $('#cwa-alter-td2').text(),
                'select':$('#cwa-sel').val(),
                'msg':$('#cwa-msg').val()
            },
            async: true,
            dataType: 'json',
            success: function (data) {
                alert(data)
            }
        })
    })
});













