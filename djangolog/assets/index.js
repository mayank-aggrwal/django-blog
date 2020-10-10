
button = document.getElementById('submit')
url = document.getElementById('url')
code = document.getElementById('code')
result = document.getElementById('result')
errors = document.getElementById('errors')
const shortenerForm = document.getElementById('shortener-form')


function shortenURL(e) {
    e.preventDefault()
    urlToShorten = url.value
    customCode = code.value
    if(customCode == '') {
        customCode = 'Not applicable'
    }
    console.log(`URL: ${urlToShorten}\nCode: ${customCode}`)

    // Make an API call to the URL shortening service and get the json and display the shortened URL or errors(if any)
    shortenedURL = ':)'
    const displayText = 'Your shortened URL is : ' + shortenedURL
    result.innerHTML = displayText
}


shortenerForm.addEventListener('submit', shortenURL)