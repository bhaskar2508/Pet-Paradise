var crsr = document.querySelector("#cursor")
var blur = document.querySelector("#cursor-blur")

document.addEventListener("mousemove",function(dets){
    crsr.style.left = dets.x+"px"
    crsr.style.top = dets.y+"px"
    blur.style.left = dets.x- 150+"px"
    blur.style.top = dets.y+"px"
})


gsap.to("menu",{
    backgroundColor : "#000",
    height:"80px",
    duration : 0.5,
    scrollTrigger:{
        trigger:"menu",
        scroller:'body',
        // markers:true
        start:"top -10%",
        end:" top -11%",
        scrub:1

    }
})

gsap.to("collection-container",{
    backgroundColor :"#000",
    scrollTrigger:{
        trigger:"collection-container",
        scroller:'body',
        // markers:true
        start:"top -25%",
        end:"top -70%",
        scrub:2
    }
})


document.addEventListener('DOMContentLoaded', () => {
    let cartCount = 0;

    function addToCart() {
        cartCount++;
        document.getElementById('cart-count').textContent = cartCount;
    }

    const addToCartButtons = document.querySelectorAll('.btn-add-to-cart');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', addToCart);
    });
});

