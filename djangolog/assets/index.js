
button = document.getElementById('submit')
url = document.getElementById('url')
code = document.getElementById('code')
result = document.getElementById('result')
errors = document.getElementById('errors')
const shortenerForm = document.getElementById('shortener-form')


async function shortenURL(e) {
    e.preventDefault()
    urlToShorten = url.value
    customCode = code.value
    // if(customCode == '') {
    //     customCode = 'Not applicable'
    // }
    console.log(`URL: ${urlToShorten}\nCode: ${customCode}`);

    let shortenedURL = ':)'

    let requestURL = "http://localhost:5000/api/custom"
    let requestBody = {
        longUrl: urlToShorten,
        urlCode: customCode
    }
    if(customCode == '') {
        requestURL = "http://localhost:5000/api/short"
        requestBody = {
            longUrl: urlToShorten
        }
    }
    console.log(customCode)
    // Make an API call to the URL shortening service and get the json and display the shortened URL or errors(if any)
    // await fetch("https://shortt-ly.herokuapp.com/api/short", {
    await fetch(requestURL, {
        method: 'POST',
        body: JSON.stringify(requestBody),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    }).then(response => response.json())
      .then(json => {
            console.log(json)
            if(json.hasOwnProperty('errors')) {
                let displayText = `Error: ${json.errors.message}`
                result.innerHTML = ''
                errors.innerHTML = displayText
            }
            else {
                shortenedURL = json.shortUrl;
                let displayText = 'Your shortened URL is : ' + shortenedURL
                errors.innerHTML = ''
                result.innerHTML = displayText
            }
      })
      .catch(err => console.log(err));
}

shortenerForm.addEventListener('submit', shortenURL)