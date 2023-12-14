$(document).ready(function () {
    // This allow the toggling of the comment area to be displayed when is clicked
    $(".display-comment-btn").on("click", function () {
        let postId = $(this).data("post-id");
        $(".user-comment-area[data-post-id='" + postId + "']").toggle();
    });

    // This submits triggers the delete post modal 
    $(".delete-post-btn").on("click", function () {
        let postId = $(this).data("post-id");
        let postTitle = $(this).closest(".card").find(".post-title").text();
        console.log(postId)

        $("#delete-post-id-input").val(postId);
        $("#post-title").text(postTitle);

        let modalId = "#deletePostModal-" + postId;
        $(modalId).modal('show');
    });

    // triggers the delete post action
    $(".delete-post").on("click", function () {
        let deleteForm = $(this).closest("form");
        $(deleteForm).submit();
    });

    // This submits triggers the edit post modal 
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

    // triggers the edit post action
    $(".edit-post").on("click", function () {
        let editForm = $(this).closest("form");
        editForm.submit();
    });

    // opens the filter post modal when screens are small
    $("#filter-posts").on("click", function () {
        $("#filterModal").modal("show");
    });

    // opens the edit profile modal
    $("#edit-profile-btn").on("click", function () {
        $("#edit-profile-modal").modal("show");
    });

    // opens the delete profile modal confirmation
    $("#delete-profile-btn").on("click", function () {
        $("#edit-profile-modal").modal("hide");
        $("#delete-profile-modal").modal("show");
    });
});