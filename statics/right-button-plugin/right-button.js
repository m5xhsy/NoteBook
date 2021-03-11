

function getImageDataURL(image) {
    // 创建画布
    const canvas = document.createElement('canvas');
    canvas.width = image.width;
    canvas.height = image.height;
    const ctx = canvas.getContext('2d');
    // 以图片为背景剪裁画布
    ctx.drawImage(image, 0, 0, image.width, image.height);
    // 获取图片后缀名
    const extension = image.src.substring(image.src.lastIndexOf('.') + 1).toLowerCase();
    // 某些图片 url 可能没有后缀名，默认是 png
    return canvas.toDataURL('image/' + extension, 1);
}


function downLoad(downloadName, url) {
    const tag = document.createElement('a');
    // 此属性的值就是下载时图片的名称，注意，名称中不能有半角点，否则下载时后缀名会错误
    tag.setAttribute('download', downloadName.replace(/\./g, '。'));

    const image = new Image();
    // 设置 image 的 url, 添加时间戳，防止浏览器缓存图片
    image.src = url + '?time=' + new Date().getTime();
    //重要，设置 crossOrigin 属性，否则图片跨域会报错
    image.setAttribute('crossOrigin', 'Anonymous');
    // 图片未加载完成时操作会报错
    image.onload = () => {
        tag.href = getImageDataURL(image);
        tag.click();
    };
}

function copy(text) {
    var inp = document.createElement('input'); // create input标签
    document.body.appendChild(inp) // 添加到body中
    inp.value = text// 给input设置value属性为需要copy的内容
    inp.select(); // 选中
    document.execCommand('copy', false); // copy已经选中的内容
    inp.remove(); // 删除掉这个dom
}

function select_options() {
    if (flag == 0) {
        window.location.reload()
    } else if (flag == 1) {
        downLoad("m5xhsy-" + new Date().getTime(), oElement.src)
    } else {
        copy(selectionText)
    }
}

var so = document.getElementById("So")
var flag = 0; //0刷新，1保存，2复制
var oElement;
var selectionText;
var pox=0;
var poy=0;
window.oncontextmenu = function (e) {
    selectionText = window.getSelection().toString();
    oElement = document.elementFromPoint(event.x, event.y);
    if (oElement.tagName == "IMG") {
        flag = 1;
        so.innerText = "🍌 保 存"
    } else if (selectionText) {
        so.innerText = "🍍 复 制"
        flag = 2;
    } else {
        so.innerText = "🍊 刷 新";
        flag = 0
    }

    console.log(oElement.tagName)
    //取消默认的浏览器自带右键
    e.preventDefault();
    var evt = window.event || arguments[0];
    var menu = document.getElementById('right_menu');
    // var container = document.getElementById('container');


    /*获取当前鼠标右键按下后的位置，据此定义菜单显示的位置*/
    var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    pox =  evt.clientX;
    poy = evt.clientY - 74+scrollTop;
    if (pox + menu.offsetWidth > document.documentElement.clientWidth) {
        // pox = document.documentElement.clientWidth - menu.offsetWidth - 3 //3是菜单栏阴影
        pox = pox-menu.offsetWidth
    }
    console.log(poy-scrollTop + menu.offsetHeight+ "----"+document.documentElement.clientHeight)
    if (poy-scrollTop + menu.offsetHeight> document.documentElement.clientHeight) {
        // poy = scrollTop+document.documentElement.clientHeight - menu.offsetHeight - 3 //3是菜单栏阴影
        poy = poy-menu.offsetHeight+74
    }
    console.log("x:"+evt.clientY)
    console.log("poy:"+poy)
    console.log("poy-scrollTop:"+(poy-scrollTop))
    if (poy-scrollTop  < 0) {
        poy = scrollTop-15
    }

    /*设置菜单可见*/
    menu.style.left = pox + "px";
    menu.style.top = poy + "px";
    menu.style.visibility = "visible";

}


window.onscroll = function () {
    document.getElementById('right_menu').style.visibility = 'hidden';
    var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
}

window.onclick = function (e) {
    //关闭右键菜单
    document.getElementById('right_menu').style.visibility = 'hidden';
    //用户触发click事件就可以关闭了，因为绑定在window上，按事件冒泡处理，不会影响菜单的功能
}