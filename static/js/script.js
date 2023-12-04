// document.addEventListener("DOMContentLoaded", function () {

//     let buttons = document.getElementsByTagName('button');
//     let commentArea = document.getElementById("user-comment-area");

//     let editProfileBtn = document.getElementById("edit-profile-btn");
//     let editProfilePopup = document.getElementById("edit-profile-popup");

//     editProfileBtn.addEventListener("click", function() {
//         editProfilePopup.classList.add()
        
//     });

    // for (let button of buttons) {
    //     button.addEventListener('click', function () {
    //         if (this.getAttribute('data-type') === 'display-comment') {
    //             commentArea.classList.remove("comment-hide");
    //         } else if (this.getAttribute('data-type') === 'edit-profile') {

    //         }
    //     });
    // }
// });

// $('#deletePostModal').on('show.bs.modal', function (event) {
//     var button = $(event.relatedTarget);
//     var postId = button.data('post-id');
//     var postTitle = button.data('post-title');

//     var modal = $(this);
//     modal.find('#postTitlePlaceholder').text(postTitle);
//     modal.find('form').attr('action', '{% url "delete_post" post_id=0 %}'.replace('0', postId));
// });