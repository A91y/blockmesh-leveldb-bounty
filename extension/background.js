chrome.runtime.onInstalled.addListener(() => {
    console.log("Extension installed");
    
    chrome.storage.local.set({ key: "hello world" }, () => {
      if (chrome.runtime.lastError) {
        console.error("Error setting value:", chrome.runtime.lastError);
      } else {
        console.log("Value is set to 'hello world'");
        
        // Verify the value is set correctly
        chrome.storage.local.get('key', (result) => {
          console.log("Stored value:", result.key);
        });
      }
    });
  });
  