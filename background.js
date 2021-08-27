chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  alert(request);
  var animeData = request;

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