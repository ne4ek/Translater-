//Tools

function changeButtonColor(button) {
    button.classList.add("buttonClickAnimation")
    setTimeout(() => {
        button.classList.remove("buttonClickAnimation")
    }, 500)

    button.classList.add("button")
}

let originalText = document.getElementById("originalText")
let translatedText = document.getElementById("translatedText")


//add selection word at textarea
chrome.runtime.sendMessage(["iconClick", null])

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message[0] === "selectionText") {
        response = message[1]
        originalText.value = response
    }
})


//send data
let sendButton = document.getElementById("sendBut")
sendButton.addEventListener("click", () => {
    changeButtonColor(sendButton)

    if (originalText.value) {
        chrome.runtime.sendMessage(["sendWord", originalText.value]);
    }
});

//translate data
let translateButton = document.getElementById("translateBut")
translateButton.addEventListener("click", () => {
    changeButtonColor(translateButton)

    chrome.runtime.sendMessage(["translateWord", originalText.value])
    chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
        let translatedWord = message["translatedWord"]
        if (translatedWord) {
            console.log(translatedWord)
            translatedText.value = translatedWord
        } else {
            translatedText.value = "ERROR"
        }
    })
})


//delete data
let deleteButton = document.getElementById("deleteBut")
deleteButton.addEventListener("click", () => {
    changeButtonColor(deleteButton)

    if (originalText.value) {
        chrome.runtime.sendMessage(["deleteWord", originalText.value])
    }
})


//delete last word
let deleteLastButton = document.getElementById("deleteLastBut")
deleteLastButton.addEventListener("click", () => {
    changeButtonColor(deleteLastButton)
    chrome.runtime.sendMessage(["deleteLastWord", null])
})




