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
        let postTags = $(this).closest(".card").find(".post-tags").text();
        let postWorldArea = $(this).closest(".card").find(".post-area").text();
        let postCountry = $(this).closest(".card").find(".post-country").text();
        let postContent = $(this).closest(".card").find(".post-content").text();

        $("#edit-post-id-input").val(postId);
        $("#edit-post-country-input").val(postCountry);
        $("#edit-post-content-input").val(postContent);
        $("#edit-post-tags-input").val(postTags).trigger('change');
        $("#edit-post-area-input").val(postWorldArea).trigger('change');

        let modalId = "#editPostModal-" + postId;
        $(modalId).modal('show');
    });

    $(".edit-post").on("click", function () {
        $(".edit-post-form").submit();
    });
});