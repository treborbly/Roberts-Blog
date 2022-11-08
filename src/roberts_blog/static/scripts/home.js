

let page_title = document.getElementById('h1-header');
let create_post_button = document.querySelector('.add-blog');
let blog_area = document.querySelectorAll(".content");


page_title.addEventListener('load', title_animation())

function title_animation() {
    let duration = null;
    let speed = 0;
    let resume = 10;
    let left = 0;
    let right = 0;

    duration = setInterval(frame, 5);
    function frame() {
        if (speed >= resume) {
            clearInterval(duration);
        }
        else {
            resume += 1;
            speed += 1;
            page_title.style.transform = "rotateX("+speed+"deg)";
        }
    }
}

create_post_button.addEventListener('mouseover', addBlogAnimation);
create_post_button.addEventListener('mouseout', addBlogAnimationReset);

function addBlogAnimation () {
    create_post_button.style.transform = "scale(1.2)";
    create_post_button.style.transition = "transform 250ms";
}
function addBlogAnimationReset () {
    create_post_button.style.transform = 'none';
}

for (let blog of blog_area) {
    blog.addEventListener('mouseover', BlogAreaAnimation);
    blog.addEventListener('mouseout', BlogAreaAnimationReset);

    function BlogAreaAnimation() {
        blog.style.transform = "scale(1.05)";
        blog.style.transition = "transform 250ms";
}

    function BlogAreaAnimationReset() {
        blog.style.transform = 'none';
}   
}




