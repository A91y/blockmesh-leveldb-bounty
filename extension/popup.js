document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('set').addEventListener('click', setValue);
    document.getElementById('get').addEventListener('click', getValue);
  });
  
  function setValue() {
    chrome.storage.sync.set({ key: "hello world" }, () => {
      if (chrome.runtime.lastError) {
        document.getElementById('status').textContent = `Error: ${chrome.runtime.lastError.message}`;
      } else {
        document.getElementById('status').textContent = "Value is set to 'hello world'";
      }
    });
  }
  
  function getValue() {
    chrome.storage.sync.get('key', (result) => {
      if (chrome.runtime.lastError) {
        document.getElementById('status').textContent = `Error: ${chrome.runtime.lastError.message}`;
      } else {
        document.getElementById('status').textContent = `Stored value: ${result.key}`;
      }
    });
  }
  