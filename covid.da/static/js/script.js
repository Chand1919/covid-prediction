// Wait for DOM to load
document.addEventListener("DOMContentLoaded", function () {
    const form = document.forms["predictionForm"];
    const submitBtn = document.getElementById("submitBtn");
    const loadingText = document.getElementById("loading");

    // ✅ Form validation
    function validateForm() {
        let age = form["age"].value;
        let gender = form["gender"].value;
        let vaccineType = form["vaccine_type"].value;
        let doses = form["doses"].value;
        let booster = form["booster"].value;
        let immuneScore = form["immune_score"].value;

        // Simple validation
        if (age === "" || gender === "" || vaccineType === "" ||
            doses === "" || booster === "" || immuneScore === "") {
            alert("⚠️ Please fill out all fields.");
            return false;
        }

        if (age < 1 || age > 120) {
            alert("⚠️ Please enter a valid age between 1 and 120.");
            return false;
        }

        return true; // Valid
    }

    // ✅ Show loading spinner
    function showLoading() {
        submitBtn.disabled = true; // Disable button
        loadingText.style.display = "block"; // Show loading text
    }

    // ✅ Hide loading after prediction
    function hideLoading() {
        submitBtn.disabled = false;
        loadingText.style.display = "none";
    }

    // On form submit
    form.addEventListener("submit", function (e) {
        if (!validateForm()) {
            e.preventDefault(); // Prevent form submission
            return false;
        }
        showLoading();
        // Let backend handle the request, spinner will show
    });
});
