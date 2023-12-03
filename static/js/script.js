document.addEventListener("DOMContentLoaded", function () {

    let buttons = document.getElementsByTagName('button');
    let commentArea = document.getElementById("user-comment-area");

    for (let button of buttons) {
        button.addEventListener('click', function () {
            if (this.getAttribute('data-type') === 'display-comment') {
                commentArea.classList.remove("comment-hide");
            } else if (this.getAttribute('data-type') === 'edit-profile') {

            }
        });
    }
});