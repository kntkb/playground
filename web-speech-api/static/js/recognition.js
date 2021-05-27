// https://qiita.com/m-shimao/items/e340efac71f709c43a4e

var recognition = new webkitSpeechRecognition();
  recognition.onresult = function(event) {
  if (event.results.length > 0) {
    q.value = event.results[0][0].transcript;
  }
}