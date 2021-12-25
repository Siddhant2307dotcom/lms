  $(window).scroll(function(){
    $('nav').toggleClass('scrolled',$(this).scrollTop()>100);
  });
console.log("HW")
// $.('.navbar a').on('click',function(e){
//   console.log(this.hash)
// })
