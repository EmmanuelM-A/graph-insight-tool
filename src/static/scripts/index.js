
document.getElementById("upload-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);

    const response = await fetch("/api/upload", {
        method: "POST",
        body: formData
    });

    const result = await response.json();

    console.log(result.message);
});