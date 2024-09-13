// Basic JS file for handling interactive elements on the page

// Function to handle bulk file uploads
document.addEventListener("DOMContentLoaded", function () {
  const uploadForm = document.getElementById("bulk-upload-form");

  if (uploadForm) {
    uploadForm.addEventListener("submit", function (event) {
      event.preventDefault(); // Prevent default form submission
      const formData = new FormData(uploadForm);

      fetch(uploadForm.action, {
        method: "POST",
        body: formData,
        headers: {
          "X-CSRFToken": getCSRFToken(), // Handle CSRF token
        },
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.message) {
            document.getElementById(
              "upload-status"
            ).innerHTML = `<div class="alert alert-success">${data.message}</div>`;
          } else {
            document.getElementById(
              "upload-status"
            ).innerHTML = `<div class="alert alert-danger">Upload failed.</div>`;
          }
        })
        .catch((error) => console.error("Error:", error));
    });
  }
});

// Function to get the CSRF token from the page's cookies
function getCSRFToken() {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, 10) === "csrftoken=") {
        cookieValue = decodeURIComponent(cookie.substring(10));
        break;
      }
    }
  }
  return cookieValue;
}
