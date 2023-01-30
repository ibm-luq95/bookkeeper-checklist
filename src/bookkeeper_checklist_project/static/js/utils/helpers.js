"use strict";
import { DEBUG, FETCHURLNAMEURL, isDisabledCssClass } from "./constants.js";
import { getCookie } from "./cookie.js";
import { showToastNotification } from "./notifications.js";

const enableInputsOnLoad = (inputClassName) => {
  const allBkChLstInputs = document.querySelectorAll(`.${inputClassName}`);
  allBkChLstInputs.forEach((element) => {
    const isDisabled = element.dataset["isDisabled"];
    if (isDisabled !== "1") {
      element.disabled = false;
      element.classList.remove(isDisabledCssClass);
    }
  });
};
// fadeOut a dom element
const fadeOut = (el) => {
  el.style.opacity = 1;

  (function fade() {
    if ((el.style.opacity -= 0.1) < 0) {
      el.style.display = "none";
    } else {
      requestAnimationFrame(fade);
    }
  })();
};

// fadeIn a dom element
const fadeIn = (el, display) => {
  el.style.opacity = 0;
  el.style.display = display || "block";

  (function fade() {
    const val = parseFloat(el.style.opacity);
    if (!((val += 0.1) > 1)) {
      el.style.opacity = val;
      requestAnimationFrame(fade);
    }
  })();
};

/**
 * Capitalized the first letter of string
 * @param {string} text String will capitalized
 * @returns string
 */
const capitalizedFirstLetter = (text) => {
  const capitalized = text.charAt(0).toUpperCase() + text.slice(1);
  return capitalized;
};

/**
 * This function will send a request to backend server
 * @param {Object} options json object of all options of the request
 * @returns Promise
 */
const sendRequest = (options) => {
  return new Promise((resolve, reject) => {
    try {
      const url = options["url"];
      const controller = new AbortController(); // the AbortController
      const { signal } = controller;
      const headers = new Headers({
        "Content-Type":
          options["contentType"] ?? "application/json;charset=utf-8",
        // "Content-Type": `Content-Type: application/pdf`,
        // "Content-Type": "application/x-www-form-urlencoded",
        Accept: "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": options["token"]
          ? options["token"]
          : getCookie("csrftoken"),
        // "Content-Disposition": "attachment; filename=upload.jpg",
      });
      // const formData = Object.fromEntries(options["dataToSend"].entries());
      const fetchOptions = {
        method: options["method"],
        mode: "same-origin",
        credentials: "include",
        cache: "no-cache",
        body: JSON.stringify(options["dataToSend"]),
        // body: formData,
      };
      const request = new Request(url, {
        headers: headers,
        signal: signal,
      });
      const fetchObj = fetch(request, fetchOptions);
      fetchObj
        .then((response) => {
          if (!response.ok) {
            return response.text().then((text) => {
              reject(JSON.parse(text));
            });
          }
          resolve(response.json());
        })
        .catch((error) => {
          reject(error);
        });
    } catch (error) {
      reject(error);
    }
  });
};

/**
 * This function will send GET a request to backend server
 * @param {Object} options json object of all options of the request
 * @returns Promise
 */
const sendGetRequest = (options) => {
  return new Promise((resolve, reject) => {
    try {
      const url = options["url"];
      const controller = new AbortController(); // the AbortController
      const { signal } = controller;
      const headers = new Headers({
        "Content-Type":
          options["contentType"] ?? "application/json;charset=utf-8",
        // "Content-Type": `Content-Type: application/pdf`,
        // "Content-Type": "application/x-www-form-urlencoded",
        Accept: "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": options["token"]
          ? options["token"]
          : getCookie("csrftoken"),
        // "Content-Disposition": "attachment; filename=upload.jpg",
      });
      // const formData = Object.fromEntries(options["dataToSend"].entries());
      const fetchOptions = {
        method: "GET",
        mode: "same-origin",
        credentials: "include",
        cache: "no-cache",
        // body: JSON.stringify(options["dataToSend"]),
      };
      const request = new Request(url, {
        headers: headers,
        signal: signal,
      });
      const fetchObj = fetch(request, fetchOptions);
      fetchObj
        .then((response) => {
          if (!response.ok) {
            return response.text().then((text) => {
              reject(JSON.parse(text));
            });
          }
          resolve(response.json());
        })
        .catch((error) => {
          reject(error);
        });
    } catch (error) {
      reject(error);
    }
  });
};

/**
 * This object will send request api with uploaded file using XMLHTTPRequest
 */
class UploadFileRequest {
  /**
   * Constructor which will init url and form data to the object
   * @param {string} url the url endpoint
   * @param {FormData} formDataObject FormData object which contains all data to upload
   * @param {string} csrfToken django csrf token
   * @param {string} requestMethod request type, default POST
   * @param {boolean} isDebugging logging output
   */
  constructor(
    url,
    formDataObject,
    csrfToken,
    requestMethod,
    isDebugging = false
  ) {
    this.url = url;
    this.formData = formDataObject;
    this.csrfToken = csrfToken;
    this.requestMethod = requestMethod ?? "POST";
    this.ajaxObject = new XMLHttpRequest();
    this.isDebugging = isDebugging;
  }

  /**
   * This method will set the header for the request
   */
  setHeaders() {
    try {
      if (this.csrfToken == "") {
        throw new Error("CSRF Token Required!");
      }
      // this.ajaxObject.setRequestHeader("Content-Type", "multipart/form-data");
      // this.ajaxObject.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
      this.ajaxObject.setRequestHeader("X-Requested-With", "XMLHttpRequest");
      this.ajaxObject.setRequestHeader("Accept", "application/json");
      this.ajaxObject.setRequestHeader("Cache-Control", "no-cache");
      // this.ajaxObject.setRequestHeader("Access-Control-Allow-Origin", "*");
      this.ajaxObject.setRequestHeader("X-CSRFToken", this.csrfToken);
      // console.log(this.csrfToken);
      this.ajaxObject.withCredentials = true;
      // this.ajaxObject.timeout = 60;
      this.ajaxObject.responseType = "json";
    } catch (error) {
      console.error(error);
      showToastNotification(error, "danger");
    }
  }
  /**
   * This method will send the request
   * @returns Promise
   */
  sendRequest() {
    return new Promise((resolve, reject) => {
      try {
        // set upload progress handler

        if (this.isDebugging === true) {
          // this.ajaxObject.addEventListener("progress", this.uploadProgressHandler, false);
          this.ajaxObject.upload.addEventListener(
            "progress",
            this.uploadProgressHandler,
            false
          );
          // set upload error handler
        }

        // open the connection
        this.ajaxObject.open(this.requestMethod, this.url, true);

        // call setHeader method
        this.setHeaders();

        // this.ajaxObject.addEventListener("error", this.errorHandler, false);
        this.ajaxObject.addEventListener("error", this.errorHandler, false);
        // set upload abort handler
        // this.ajaxObject.addEventListener("abort", this.abortHandler, false);
        this.ajaxObject.addEventListener("abort", this.abortHandler, false);

        // set upload complete handler
        this.ajaxObject.addEventListener(
          "load",
          (event) => {
            console.warn("Load event!");
            console.log(event);
          },
          false
        );
        this.ajaxObject.send(this.formData);
        // eslint-disable-next-line no-unused-vars
        this.ajaxObject.addEventListener("readystatechange", (event) => {
          if (this.ajaxObject.readyState === 4) {
            const response = this.ajaxObject.response;
            if (this.ok() === true) {
              resolve(response["msg"]);
            } else {
              console.error(this.ajaxObject.response);
              reject(response["user_error_msg"]);
            }
          }
        });
      } catch (error) {
        console.error(error);
        showToastNotification(error, "danger");
        reject(error);
      }
    });
  }
  /**
   * This check if the response is ok
   * @returns bool
   */
  ok() {
    // console.log(this.ajaxObject.status);
    if (this.ajaxObject.status >= 200 && this.ajaxObject.status < 400) {
      return true;
    } else {
      return false;
    }
  }
  uploadProgressHandler(event) {
    const percent = (event.loaded / event.total) * 100;
    console.log(Math.round(percent) + "%");
  }

  errorHandler(event) {
    showToastNotification("Error while uploading!", "danger");
    console.error(event);
  }
  // eslint-disable-next-line no-unused-vars
  abortHandler(event) {
    this.ajaxObject.abort();
    showToastNotification("Abort uploading!", "danger");
  }
}

/**
 * Order or sort json object items
 * @param {Object} unorderedObject Un ordered object
 * @returns Object
 */
const orderObjectItems = (unorderedObject) => {
  const orderedObject = Object.keys(unorderedObject)
    .sort()
    .reduce((obj, key) => {
      obj[key] = unorderedObject[key];
      return obj;
    }, {});
  return orderedObject;
};

/**
 * This will serialize form inputs
 * @typedef param
 * @param {Object} param - this is object param
 * @param {HTMLFormElement} param.formElement The form element
 * @param {Array} param.excludedFields Array of excluded fields
 * @param {boolean} param.isOrdered Order the returned object
 * @returns {Object} json object of all inputs
 */
const formInputSerializer = ({
  formElement,
  excludedFields = [],
  isOrdered = false,
}) => {
  const serializedObject = {};
  Array.from(formElement.elements).forEach((element) => {
    // check if the element.name in excludedFields
    if (excludedFields.includes(element.name) === false) {
      // check if the element name not empty string
      if (element.name !== "") {
        serializedObject[element.name] =
          element.type === "checkbox" ? element.checked : element.value;
      }
    }
  });
  return isOrdered === true
    ? orderObjectItems(serializedObject)
    : serializedObject;
};

/**
 * This function will set html form elements with values
 * @param {HTMLFormElement} formElement Form element which will set the values
 * @param {Object} objectOfValues Object of values to set
 */
const setFormInputValues = (formElement, objectOfValues) => {
  // check the type of formElement is HTMLFormElement
  if (formElement.constructor.name !== "HTMLFormElement") {
    throw new Error("The element to set values not form element!!");
  }
  for (const name in objectOfValues) {
    try {
      if (Object.hasOwnProperty.call(objectOfValues, name)) {
        const element = objectOfValues[name];
        formElement.elements[name].value = element;
      }
    } catch (error) {
      if (error instanceof TypeError) {
        // in case the input or element not exists
        if (DEBUG === true) {
          console.warn(
            `The element ${name} not exists in the form ${formElement.id}`
          );
        }
      }
    }
  }
};

/**
 * Fetch the url path by url name
 * @param {string} urlName URL name to fetch url
 */
const fetchUrlPathByName = async (urlName) => {
  try {
    const controller = new AbortController(); // the AbortController
    const { signal } = controller;
    const headers = new Headers({
      "Content-Type": "application/json;charset=utf-8",
      Accept: "application/json",
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": getCookie("csrftoken"),
    });
    const fetchOptions = {
      method: "POST",
      mode: "same-origin",
      credentials: "include",
      cache: "no-cache",
      body: JSON.stringify({ urlName: urlName }),
    };
    const request = new Request(FETCHURLNAMEURL, {
      headers: headers,
      signal: signal,
    });
    const response = await fetch(request, fetchOptions);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error(error);
  }
};

/**
 * Debugging print only if DEBUG is enabled, development only
 * @param {string} text Message to print
 * @param {string} consoleType Console log type
 */
const debuggingPrint = (text, consoleType = "log") => {
  if (DEBUG === true) {
    switch (consoleType) {
      case "log":
        console.log(text);
        break;
      case "warn":
        console.warn(text);
        break;
      case "info":
        console.info(text);
        break;
      case "error":
        console.error(text);
        break;
      case "dir":
        console.dir(text);
        break;
      case "table":
        console.table(text);
        break;

      default:
        break;
    }
  }
};

/**
 * Check if the checkbox single or multiple elements
 * @param {HTMLInputElement|RadioNodeList} htmlElement Element to check
 * @returns string
 */
const checkIfInputSingleOrList = (htmlElement) => {
  // RadioNodeList, HTMLInputElement
  if (htmlElement.getConstructorName() === "RadioNodeList") {
    // in case multiple inputs
    return "multiple";
  } else if (htmlElement.getConstructorName() === "HTMLInputElement") {
    // in case single input
    return "single";
  }
};

/**
 * Copy text to clipboard using native javascript api with toast notifications
 * @typedef param
 * @param {Object} param - this is object param
 * @param {string} param.textWillCopy Text will copy to clipboard
 * @param {string} param.label Label which will appear in notification
 * @param {boolean} param.isNotify If true will display notification message after copy
 * @param {string} param.notificationMsg Custom notification message not the default
 * @param {string} param.notificationType Notification type
 */
const addTxtToClipboardWithNotification = ({
  textWillCopy,
  label,
  isNotify = true,
  notificationMsg = null,
  notificationType = "success",
}) => {
  navigator.clipboard.writeText(textWillCopy);
  if (isNotify === true) {
    const msg = notificationMsg
      ? capitalizedFirstLetter(notificationMsg)
      : capitalizedFirstLetter(`${label} copied successfully!`);
    showToastNotification(msg, notificationType);
  }
};

export {
  capitalizedFirstLetter,
  enableInputsOnLoad,
  sendRequest,
  fadeIn,
  fadeOut,
  UploadFileRequest,
  sendGetRequest,
  formInputSerializer,
  setFormInputValues,
  fetchUrlPathByName,
  debuggingPrint,
  checkIfInputSingleOrList,
  orderObjectItems,
  addTxtToClipboardWithNotification,
};
