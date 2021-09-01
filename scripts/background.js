// Waits until the user clicks on the anime site in order to receive the data
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  var animeData = request;

  // Sends the information to our Python script
  $.ajax({
    type: 'POST',
    url: 'http://localhost:5000/anime_data',
    data: animeData,
    success: function(newData) {
      alert('Success');
    }
  })
  sendResponse({ message: "Background received message"});
})

chrome.webNavigation.onHistoryStateUpdated.addListener(function(details) {
  chrome.tabs.executeScript(null,{file:"/scripts/content.js"});
});