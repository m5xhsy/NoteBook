入口函数
    方法一
        $(document).ready(function(                                  //不用等待图片资源加载完就可以调用
        ));
    方法二
        $(function(){
        });


事件
    $('#id').click(function(){})                                //点击事件
























1.获取事件源
    $('#id')
2.事件
    $('#id').click(function(){
        $('#id').css('color','red')
        $('.class').css({
            'background-color':'#fff'           //或者'backgroundColor':'red'
            width:300                           //width:'300px'
        })
    })