var login = require("facebook-chat-api");
var translate = require('google-translate-api');
var temp_api;
login({email: "account", password: "password"}, function callback (err, api) {
  if(err) return console.error(err);
  api.listen(function callback(err, message) {
    console.log(message.threadID);
    //senderID for sender
    //threadID for group
    if(message.threadID == "1646490642302025" && message.senderID!= "100002104636722"){
      translate(message.body, {from: 'zh-tw', to: 'en'}).then(res => {
          if(res.from.language.iso != "en")
            api.sendMessage(res.text,message.threadID);
      }).catch(err => {
          console.error(err);
      });
    }
    // api.sendMessage(message.body,message.threadID);
  });
});
