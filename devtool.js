// Async function to fetch and hash file using SHA-256
async function fetchAndHash(url) {
    const response = await fetch(url);
    const buffer = await response.arrayBuffer();
    const hashBuffer = await crypto.subtle.digest('SHA-256', buffer);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    return hashHex;
}

// function to append SHA256 hash to URL
function appendHashToURL(filename, hash) {
    const baseUrl = "https://urlscan.io/search/#";
    const fullUrl = `${baseUrl}${hash}`; // Changed to template literal with backticks
    console.log(`${filename}: ${fullUrl}`); // Changed to template literal with backticks
    return fullUrl;
}

// get all network requests from the Network panel
const performanceEntries = performance.getEntriesByType('resource');
const fileHashes = {};

// Process each request
for (const entry of performanceEntries) {
    const url = entry.name;
    const fileName = url.split('/').pop();
    
    fetchAndHash(url).then(hash => {
        fileHashes[fileName] = hash;
        const fullUrl = appendHashToURL(fileName, hash);
    }).catch(error => {
        console.error(`Error hashing ${fileName}: ${error}`); // Changed to template literal with backticks
    });
}