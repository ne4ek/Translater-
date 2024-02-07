document.getElementById("convertButton").addEventListener("click", () => {
    chrome.runtime.sendMessage("run");
});


