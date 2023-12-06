$(document).ready(function () {
    // This allow the toggling of the comment area to be displayed when is clicked
    $(".display-comment-btn").on("click", function () {
        let postId = $(this).data("post-id");
        $(".user-comment-area[data-post-id='" + postId + "']").toggle();
    });


    $(".delete-post-btn").on("click", function () {
        let postId = $(this).data("post-id");
        let postTitle = $(this).closest(".card").find(".post-title").text();

        $("#delete-post-id-input").val(postId);
        $("#post-title").text(postTitle);

        let modalId = "#deletePostModal-" + postId;
        $(modalId).modal('show');
    });

    $(".delete-post").on("click", function () {
        $(".delete-post-form").submit();
    });

    $(".edit-post-btn").on("click", function () {
        let postId = $(this).data("post-id");
        let postTitle = $(this).closest(".card").find(".post-title").text();

        $("#edit-post-id-input").val(postId);

        let modalId = "#editPostModal-" + postId;
        $(modalId).modal('show');
    });

    $(".edit-post").on("click", function () {
        $(".edit-post-form").submit(function () {

        });
    });
});