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
        console.log(postId);

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
        let postTags = $(this).closest(".card").find(".post-tags").text().trim();
        let postWorldArea = $(this).closest(".card").find(".post-area").text();
        let postCountry = $(this).closest(".card").find(".post-country").text();
        let postContent = $(this).closest(".card").find(".post-content").text().trim();

        $(".edit-post-title-input input").val(postTitle);
        $(".edit-post-country-input input").val(postCountry);
        $(".edit-post-content-input textarea").val(postContent);
        $(".edit-post-tags-input select").val(postTags);
        $(".edit-post-area-input select").val(postWorldArea);

        let modalId = "#editPostModal-" + postId;
        $(modalId).modal('show');
    });

    // opens the filter post modal when screens are small
    $("#filter-posts").on("click", function () {
        $("#filterModal").modal("show");
    });

    // opens the edit profile modal
    $("#edit-profile-btn").on("click", function () {
        let display_name = $(this).closest(".card").find(".display_name").text();
        let languages = $(this).closest(".card").find(".languages").text();
        let most_visited_area = $(this).closest(".card").find(".most_visited_area").text().trim();
        let countries_traveled = $(this).closest(".card").find(".countries_traveled").text();
        let user_description = $(this).closest(".card").find(".user_description").text().trim();

        $(".edit-profile-display_name-input input").val(display_name);
        $(".edit-profile-languages-input input").val(languages);
        $(".edit-profile-most_visited_area-input select").val(most_visited_area);
        $(".edit-profile-countries_traveled-input input").val(countries_traveled);
        $(".edit-profile-user_description-input textarea").val(user_description);

        $("#edit-profile-modal").modal("show");
    });

    // opens the delete profile modal confirmation
    $("#delete-profile-btn").on("click", function () {
        $("#edit-profile-modal").modal("hide");
        $("#delete-profile-modal").modal("show");
    });
});