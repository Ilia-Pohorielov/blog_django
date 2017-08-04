$(document).ready(function () {
   var menu = $('.left-sidebar .first-level li:not(.second-level li)');
    menu.on('click',function () {
        $(this).addClass('active');
        $(this).siblings().removeClass('active')
    });
});
