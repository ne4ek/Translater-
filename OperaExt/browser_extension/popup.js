document.getElementById("sendButton").addEventListener("click", () => {
    chrome.runtime.sendMessage("run");
});


