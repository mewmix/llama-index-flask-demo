$(document).ready(function() {
  // Handle form submission
  $("#index-form").submit(function(event) {
    event.preventDefault();

    // Get form data
    var user_handles = $("#user-handles").val();
    var prompt_text = $("#prompt-text").val();

    // Send form data to server
    $.ajax({
      type: "POST",
      url: "/",
      data: {
        user_handles: user_handles,
        prompt_text: prompt_text
      },
      success: function(data) {
        // Display query results
        $("#results").html(data);
      }
    });
  });
});

