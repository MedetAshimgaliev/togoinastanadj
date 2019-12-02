$('#first').mouseenter(function(){
     $('#second').show(); 
});
$('#first').mouseleave(function(){
     $('#second').hide(); 
});
$('#one').mouseenter(function(){
     $('#two').show(); 
});
$('#one').mouseleave(function(){
     $('#two').hide(); 
});
$('#odin').mouseenter(function(){
     $('#dwa').show(); 
});
$('#odin').mouseleave(function(){
     $('#two').hide(); 
});
// $("#first").on({
//     mouseenter: function () {
//         $("#second").fadeIn();
//     },
//     mouseleave: function () {
//         var $target = $("#second");

//         //delay the fade out to see whether the mouse is moved to the second button
//         var timer = setTimeout(function () {
//             $target.stop(true, true).fadeOut();
//         }, 200);
//         $target.data('hoverTimer', timer);
//     }
// });
// $("#second").on({
//     mouseenter: function () {
//         //if mouse is moved inside then clear the timer so that it will not get hidden
//         clearTimeout($(this).data('hoverTimer'));
//         $(this).stop(true, true).fadeIn();
//     },
//     mouseleave: function () {
//         $(this).stop(true, true).fadeOut();
//     }
// });