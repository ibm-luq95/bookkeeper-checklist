"use strict";

import { isDisabledCssClass } from "./constants.js";
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
        "Content-Type": options["contentType"] ?? "application/json;charset=utf-8",
        // "Content-Type": `Content-Type: application/pdf`,
        // "Content-Type": "application/x-www-form-urlencoded",
        Accept: "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": options["token"] ? options["token"] : getCookie("csrftoken"),
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
  constructor(url, formDataObject, csrfToken, requestMethod, isDebugging = false) {
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
          this.ajaxObject.upload.addEventListener("progress", this.uploadProgressHandler, false);
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
          false,
        );
        this.ajaxObject.send(this.formData);
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
  abortHandler(event) {
    this.ajaxObject.abort();
    showToastNotification("Abort uploading!", "danger");
  }
}

export { enableInputsOnLoad, sendRequest, fadeIn, fadeOut, UploadFileRequest };
