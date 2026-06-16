function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function setText(id, value) {
    const element = document.getElementById(id);
    if (element) {
        element.textContent = value || "";
    }
}

function showPreview(data) {
    const previewPanel = document.getElementById("previewPanel");
    const previewImage = document.getElementById("previewImage");
    const imagePlaceholder = document.getElementById("imagePlaceholder");
    const hashtagContainer = document.getElementById("previewHashtags");

    previewPanel.classList.add("active");

    setText("previewTopic", data.topic || "Generated Post");
    setText("previewPlatform", `Platform: ${data.platform || "General"}`);
    setText("previewTone", `Tone: ${data.tone || "Professional"}`);
    setText("previewProvider", `Provider: ${data.provider || "demo"}`);
    setText("previewCaption", data.caption || "");
    setText("previewImagePrompt", data.image_prompt || "No image prompt returned.");

    if (data.image_url) {
        previewImage.src = data.image_url;
        previewImage.hidden = false;
        imagePlaceholder.hidden = true;
    } else {
        previewImage.hidden = true;
        imagePlaceholder.hidden = false;
    }

    hashtagContainer.innerHTML = "";
    const hashtags = data.hashtags || [];
    hashtags.forEach((tag) => {
        const span = document.createElement("span");
        span.textContent = tag;
        hashtagContainer.appendChild(span);
    });
}

function setupCopyButton() {
    const copyBtn = document.getElementById("copyBtn");
    if (!copyBtn) return;

    copyBtn.addEventListener("click", async () => {
        const caption = document.getElementById("previewCaption")?.textContent || "";
        const hashtags = Array.from(document.querySelectorAll("#previewHashtags span"))
            .map((item) => item.textContent)
            .join(" ");
        const text = `${caption}\n\n${hashtags}`.trim();

        try {
            await navigator.clipboard.writeText(text);
            copyBtn.textContent = "Copied!";
            setTimeout(() => {
                copyBtn.textContent = "Copy Caption";
            }, 1500);
        } catch (error) {
            alert("Copy failed. You can manually select and copy the caption.");
        }
    });
}

document.addEventListener("DOMContentLoaded", () => {
    setupCopyButton();

    const form = document.getElementById("postForm");
    const generateBtn = document.getElementById("generateBtn");
    const statusText = document.getElementById("statusText");

    if (!form) return;

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const formData = new FormData(form);
        generateBtn.disabled = true;
        generateBtn.textContent = "Generating...";
        statusText.textContent = "AI agents are creating your post preview...";

        try {
            const response = await fetch(form.action, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                },
                body: formData,
            });

            const data = await response.json();
            if (!response.ok || !data.success) {
                throw new Error("Generation failed. Please check your input or API keys.");
            }

            showPreview(data);
            statusText.textContent = "Post generated successfully.";
        } catch (error) {
            statusText.textContent = error.message;
        } finally {
            generateBtn.disabled = false;
            generateBtn.textContent = "Generate Post";
        }
    });
});
