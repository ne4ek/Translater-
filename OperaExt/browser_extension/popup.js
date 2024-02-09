chrome.runtime.sendMessage("iconClick")


chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message[0] === "selectionText") {
        let originalText = document.querySelector("#originalText")
        response = message[1]
        originalText.value = response
    }
})


document.getElementById("sendBut").addEventListener("click", () => {
    chrome.runtime.sendMessage("run");
});






