// alert("Here is background");var serverhost = 'http://127.0.0.1:8000';
// Example POST method implementation:
async function postData(url = '', data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      mode: 'cors', // no-cors, *cors, same-origin
    //   cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    //   credentials: 'same-origin', // include, *same-origin, omit
      headers: {
        'Content-Type': 'application/json'
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
    //   redirect: 'follow', // manual, *follow, error
    //   referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
      body:JSON.stringify(data) // body data type must match "Content-Type" header
    });
    // alert("Response from server is :" +response);
    return await response.json(); // parses JSON response into native JavaScript objects
  }

  
	chrome.runtime.onMessage.addListener(
		(message, sender, sendResponse)=> {
			var url = "http://127.0.0.1:8000/img";
			console.log(url);
            // var data = {
            //     "Yo":"Man",
            //     "Hello":"Bro",
            //     "request":JSON.stringify(message),
            //     "keys":JSON.stringify(message.keys)
            // };
            // const response = postData(url,message);
            fetch(url, {
                method: 'POST', // *GET, POST, PUT, DELETE, etc.
                mode: 'cors', // no-cors, *cors, same-origin
              //   cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
              //   credentials: 'same-origin', // include, *same-origin, omit
                headers: {
                  'Content-Type': 'application/json'
                  // 'Content-Type': 'application/x-www-form-urlencoded',
                },
              //   redirect: 'follow', // manual, *follow, error
              //   referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
                body:JSON.stringify(message) // body data type must match "Content-Type" header
              })
            .then(response=>response.json())
            .then(response=>sendResponse(
                response
            ));
            // sendResponse(
            //     {"content":response}
            // );

			return true;  // Will respond asynchronously.
		  
	});
