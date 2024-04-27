import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://prod.app.vodex.ai")

    # Inject JavaScript code into the webpage
    script = """
function getXPathWithUniqueAttributes(element) {
    const attributes = ['id', 'name', 'class']; // Add more attributes as needed
    for (const attr of attributes) {
        const value = element.getAttribute(attr);
        if (value) {
            const text = element.textContent.trim();
            if (text) {
                return `//${element.tagName.toLowerCase()}[text()='${text}']`;
            }
            return `//${element.tagName.toLowerCase()}[@${attr}='${value}']`;
        }
    }

    // If no unique attributes found, include text content in XPath
    const text = element.textContent.trim();
    if (text) {
        return `//${element.tagName.toLowerCase()}[text()='${text}']`;
    }

    // If no unique attributes or text content found, fallback to position-based XPath
    return getXPath(element);
}

    function getSiblingIndex(element) {
        var parent = element.parentNode;
        if (!parent) return -1;
        var siblings = parent.children;
        for (var i = 0; i < siblings.length; i++) {
            if (siblings[i] === element) {
                return i;
            }
        }
        return -1;
    }

    document.addEventListener('click', function(event) {
        var xpath = getXPathWithUniqueAttributes(event.target);
        console.log('Clicked element XPath:', xpath);
    });
    """

    driver.execute_script(script)

    # Continuous monitoring for click events
    while True:
        time.sleep(1)  # Check every second for click events

if __name__ == '__main__':
    main()
































# import multiprocessing
# import threading
# from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import time


# def main():
#     # Set up Chrome options
#     chrome_options = Options()
#     chrome_options.add_experimental_option("detach", True)  # To run Chrome in headless mode

#     driver = webdriver.Chrome(options=chrome_options)
#     driver.maximize_window()
#     driver.get("https://prod.app.vodex.ai") 

    
#     while True:

#         script = """        
#     #                         

# let lastLoggedXPath = null;

# function getXPathWithUniqueAttributes(element) {
#     const attributes = ['id', 'name', 'class']; // Add more attributes as needed
#     for (const attr of attributes) {
#         const value = element.getAttribute(attr);
#         if (value) {
#             return `//${element.tagName.toLowerCase()}[@${attr}='${value}']`;
#         }
#     }
#     // If no unique attributes found, fallback to position-based XPath
#     return getXPath(element);
# }

# function getSiblingIndex(element) {
#     var parent = element.parentNode;
#     if (!parent) return -1;
#     var siblings = parent.children;
#     for (var i = 0; i < siblings.length; i++) {
#         if (siblings[i] === element) {
#             return i;
#         }
#     }
#     return -1;
# }

# document.addEventListener('click', function(event) {
#     var xpath = getXPathWithUniqueAttributes(event.target);
#     if (xpath !== lastLoggedXPath) {
#         console.log('Clicked element XPath:', xpath);
#         lastLoggedXPath = xpath;
#     }
# });

# """

#         vals = driver.execute_script(script)

# if __name__ == '__main__':
#     main()
    





# *?**********************************************************
# function sendXPathsToServer() {
#     $.ajax({
#         url: "/test",
#         type: "POST",
#         contentType: "application/json",
#         data: JSON.stringify(global_xpath_list),
#         success: function(response) {
#             console.log("XPaths sent successfully:", response);
#             // Clear the list after successful transmission (optional)
#             global_xpath_list = [];
#         },
#         error: function(jqXHR, textStatus, errorThrown) {
#             console.error("Error sending XPaths:", textStatus, errorThrown);
#         }
#     });
# }
# *****************************************************
#  let global_xpath_list = [];
    # let lastLoggedXPath = null;

    # function getXPath(element) {
    #   var xpath = '';
    #   for (; element && element.nodeType == 1; element = element.parentNode) {
    #     var id = getSiblingIndex(element) + 1;
    #     id = id > 1 ? '[' + id + ']' : '';
    #     xpath = '/' + element.tagName.toLowerCase() + id + xpath;
    #   }
    #   return xpath;
    # }

    # function getSiblingIndex(element) {
    #   var parent = element.parentNode;
    #   if (!parent) return -1;
    #   var siblings = parent.children;
    #   for (var i = 0; i < siblings.length; i++) {
    #     if (siblings[i] === element) {
    #       return i;
    #     }
    #   }
    #   return -1;
    # }

    # function sendXPathsToServer() {

    #     $.ajax({
    #       url: "/test",
    #       type: "POST",
    #       contentType: "application/json",
    #       data: JSON.stringify(global_xpath_list),
    #       success: function(response) {
    #         console.log("XPaths sent successfully:", response);
    #         // Clear the list after successful transmission (optional)
    #         global_xpath_list = [];
    #       },
    #       error: function(jqXHR, textStatus, errorThrown) {
    #         console.error("Error sending XPaths:", textStatus, errorThrown);
    #       }
    #     });
    #   }
    # ****************************************************************************************************************







































#     # *******************************************************************************************

# function getSiblingIndex(element) {
#     var parent = element.parentNode;
#     if (!parent) return -1;
#     var siblings = parent.children;
#     var index = 0;
#     for (var i = 0; i < siblings.length; i++) {
#         if (siblings[i].nodeType === 1) {
#             index++;
#             if (siblings[i] === element) {
#                 return index;
#             }
#         }
#     }
#     return -1;
# }

#     # **************************************************************************************************


#     function getXPath(element) {
#     if (!element || !element.ownerDocument) return ''; // Exit if element is null or not attached to a document
#     const document = element.ownerDocument;
#     const xpathSegments = [];
    
#     // Iterate through ancestors to build XPath
#     for (; element && element.nodeType === 1; element = element.parentNode) {
#         let segment = element.tagName.toLowerCase();
#         if (element.id) {
#             // Use ID if available
#             segment += '[@id="' + element.id + '"]';
#             xpathSegments.unshift(segment);
#             break; // Stop traversal if element has an ID
#         } else {
#             // Use position among siblings
#             let index = 1;
#             let sibling = element.previousSibling;
#             for (; sibling; sibling = sibling.previousSibling) {
#                 if (sibling.nodeType === 1 && sibling.tagName === element.tagName) {
#                     index++;
#                 }
#             }
#             segment += '[' + index + ']';
#         }
#         xpathSegments.unshift(segment);
#     }
    
#     // Combine segments to form the full XPath
#     return xpathSegments.length ? '/' + xpathSegments.join('/') : '';
# }

    
